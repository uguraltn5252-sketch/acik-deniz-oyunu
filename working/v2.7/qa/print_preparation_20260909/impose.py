"""121 exact native fronts, reflected A4 sheet slots and opposed quarter-turns."""
from common import *
from reportlab.pdfgen import canvas
from collections import Counter
import argparse

def marks(c,x,y,w,h):
    c.setStrokeColor(INK);c.setLineWidth(.3)
    for xx in [x,x+w]:
        c.line(xx,y-4.75*mm,xx,y-3.25*mm);c.line(xx,y+h+3.25*mm,xx,y+h+4.75*mm)
    for yy in [y,y+h]:
        c.line(x-4.75*mm,yy,x-3.25*mm,yy);c.line(x+w+3.25*mm,yy,x+w+4.75*mm,yy)

def front_masters(source_path):
    expected='04167b8290e9b7efdb211af2a236735eb50001357351a835acd60512e6e517dd'
    assert sha(source_path)==expected,'Source PDF differs from reviewed 8 September delivery'
    old=fitz.open(source_path);manifest=json.loads((P/'qa/illustrated_design_20260908/render_manifest.json').read_text())
    pos={x['id']:x for x in manifest['print_positions']if x['side']=='front'}
    trim=fitz.open();bleed=fitz.open();padding=3*mm;strip=.12*mm
    for r in records:
        w,h=dims(r);j=pos[r['id']];clip=fitz.Rect(j['bbox']);p=trim.new_page(width=w,height=h)
        p.show_pdf_page(p.rect,old,j['page'],clip=clip)
        p=bleed.new_page(width=w+2*padding,height=h+2*padding)
        # Extend only the outermost paper/ink beyond trim. The entire original
        # card remains native and unchanged inside trim; no image resampling.
        xs=[(0,padding,clip.x0,clip.x0+strip),(padding,padding+w,clip.x0,clip.x1),(padding+w,w+2*padding,clip.x1-strip,clip.x1)]
        ys=[(0,padding,clip.y0,clip.y0+strip),(padding,padding+h,clip.y0,clip.y1),(padding+h,h+2*padding,clip.y1-strip,clip.y1)]
        for yi,(y0,y1,sy0,sy1)in enumerate(ys):
            for xi,(x0,x1,sx0,sx1)in enumerate(xs):
                if xi==1 and yi==1:continue
                p.show_pdf_page(fitz.Rect(x0,y0,x1,y1),old,j['page'],clip=fitz.Rect(sx0,sy0,sx1,sy1),keep_proportion=False)
        p.show_pdf_page(fitz.Rect(padding,padding,w+padding,h+padding),old,j['page'],clip=clip)
    a=TMP/'fronts_trim.pdf';b=TMP/'fronts_bleed.pdf';save_pdf(trim,a,False);save_pdf(bleed,b,False)
    dump(QA/'front_source.json',{'source_pdf_sha256':expected,'source_commit':'0f65aa817bd0d8e6c06a97274648d9c6363a25bf','method':'Native PDF card extraction; only off-trim 3 mm paper/ink edge continuation','front_count':121})
    return a,b

def island_master(image_path):
    w=76*mm;raw=fitz.open();p=raw.new_page(width=w,height=w);p.insert_image(p.rect,filename=str(image_path))
    d=fitz.open();p=d.new_page(width=w,height=w)
    # Match the pre-existing direction-neutral back convention. Opposed native
    # half-page placements form ONE connected central island, not two motifs.
    half=fitz.Rect(0,0,w,w/2);p.show_pdf_page(half,raw,0,clip=half)
    p.show_pdf_page(fitz.Rect(0,w/2,w,w),raw,0,clip=half,rotate=180)
    path=PDF/'BACK_ISLAND.pdf';save_pdf(d,path,False)
    with fitz.open(path)as rendered:rendered[0].get_pixmap(matrix=fitz.Matrix(1024/w,1024/w)).save(TMP/'new_island_master.png')
    return path

def jobs():
    groups=[([r for r in records if dims(r)[1]>110*mm],2,0,12),([r for r in records if r['collection']in ('powers','provisions','loyalties')],3,90,8),([r for r in records if r['collection']=='maps'],3,0,12)]
    result=[];sheet=0
    for group,rows,rotation,gapx in groups:
        ow,oh=dims(group[0]);w,h=(oh,ow)if rotation else(ow,oh);gx=gapx*mm;gy=12*mm
        sx=(A4[0]-2*w-gx)/2;sy=(A4[1]-rows*h-(rows-1)*gy)/2
        for offset in range(0,len(group),2*rows):
            sheet+=1
            for i,r in enumerate(group[offset:offset+2*rows]):
                x=sx+(i%2)*(w+gx);y=sy+(rows-1-i//2)*(h+gy)
                for side in ['front','back']:
                    xx=x if side=='front' else A4[0]-x-w
                    result.append({'sheet':sheet,'page':2*(sheet-1)+(side=='back'),'side':side,'id':r['id'],'back':BACK[r['id']],'bbox':list(rect(xx,y,w,h)),'rotation':rotation if side=='front'else(-rotation)%360,'native_mm':[ow/mm,oh/mm]})
    assert sheet==23 and len(result)==242
    return result

def build(source_path,image_path):
    trim,front=front_masters(source_path);island_master(image_path)
    placements=jobs();background=TMP/'sheets_background.pdf';c=canvas.Canvas(str(background),pagesize=A4,invariant=1,pageCompression=1)
    for n in range(46):
        c.setFillColor(INK);c.setFont('Body',7)
        c.drawString(12*mm,12*mm,f'FOULWAKE | Yaprak {n//2+1:02d} | '+('ÖN'if n%2==0 else'ARKA'))
        c.drawRightString(198*mm,12*mm,'A4 | %100 | Uzun kenar | v2.7 / 09.09.2026')
        for j in [x for x in placements if x['page']==n]:
            b=fitz.Rect(j['bbox']);marks(c,b.x0,A4[1]-b.y1,b.width,b.height)
        c.showPage()
    c.save();d=fitz.open(background);fd=fitz.open(front)
    backs={bid:fitz.open(PDF/'BACK_ISLAND.pdf'if bid=='BACK_ISLAND'else BACK_ROOT/(bid+'.pdf'))for bid in set(BACK.values())}
    idx={r['id']:i for i,r in enumerate(records)}
    for j in placements:
        src=fd if j['side']=='front'else backs[j['back']];page=idx[j['id']]if j['side']=='front'else 0
        box=fitz.Rect(j['bbox'])+(-3*mm,-3*mm,3*mm,3*mm)
        d[j['page']].show_pdf_page(box,src,page,rotate=j['rotation'])
    path=ART/'FOULWAKE_KARTLAR_A4_CIFT_TARAFLI_v2.7.pdf';save_pdf(d,path)
    d=fitz.open(path);parts=[]
    for i in range(23):
        part=fitz.open();part.insert_pdf(d,from_page=2*i,to_page=2*i+1);p=PDF/f'KARTLAR_A4_{i+1:02d}.pdf';save_pdf(part,p)
        assert p.stat().st_size<20_000_000
        parts.append({'path':str(p.relative_to(R)),'pages':[2*i+1,2*i+2],'sha256':sha(p),'bytes':p.stat().st_size})
    m={'task_id':'FOULWAKE-A4-PRINT-001','status':'AWAITING_VERIFICATION','a4_mm':[210,297],'flip':'LONG_EDGE','scale':1,'bleed_mm':3,'trim_sizes_mm':[[70,120],[63.5,88.9],[70,70]],'fronts':121,'backs':121,'sheets':23,'pages':46,'back_counts':dict(Counter(BACK.values())),'placements':placements,'parts':parts,'master':{'path':str(path),'sha256':sha(path),'bytes':path.stat().st_size},'retained_back_sha256':{b:sha(BACK_ROOT/(b+'.pdf'))for b in backs if b!='BACK_ISLAND'},'island_sha256':sha(PDF/'BACK_ISLAND.pdf')}
    dump(QA/'imposition_manifest.json',m);print(json.dumps(m['master']))

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--source',required=True);p.add_argument('--island',required=True);a=p.parse_args();build(Path(a.source),Path(a.island))
