"""Rebuild all native card faces, then impose one A4 duplex PDF.

Illustration bytes and all mechanics are retained. Text, quiet reading panels
and proper names are the publication revision. No raster editing is performed.
"""
from card_layout import *
import fitz,shutil
from reportlab import rl_config
from reportlab.lib.pagesizes import A4
from collections import Counter
rl_config.useA85=0
TMP=R.parent/'tmp/publication_20260909';ART=R.parent/'artifacts/publication_20260909'
ART.mkdir(exist_ok=True,parents=True)
def dump(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def save(d,p):
    d.xref_set_key(d.pdf_catalog(),'ViewerPreferences','<</PrintScaling /None /Duplex /DuplexFlipLongEdge>>')
    d.save(p,garbage=4,deflate=True);d.close()
def marks(c,b):
    x,y,w,h=b.x0,A4[1]-b.y1,b.width,b.height;c.setStrokeColor(INK);c.setLineWidth(.3)
    for xx in [x,x+w]:
        c.line(xx,y-4.75*mm,xx,y-3.25*mm);c.line(xx,y+h+3.25*mm,xx,y+h+4.75*mm)
    for yy in [y,y+h]:
        c.line(x-4.75*mm,yy,x-3.25*mm,yy);c.line(x+w+3.25*mm,yy,x+w+4.75*mm,yy)
def build():
    annotations=json.loads((P/'qa/illustrated_design_20260908/art_annotations.json').read_text())
    c=canvas.Canvas(str(TMP/'fronts.pdf'),invariant=1,pageCompression=1);measurements=[]
    for r in records:
        w,h=dimensions(r);c.setPageSize((w+6*mm,h+6*mm))
        # Uniform off-trim stock color avoids the previous stretched edge stripes.
        measurements.append(draw_front(c,r,3*mm,3*mm,annotation=annotations[r['id']],bleed=True));c.showPage()
    c.save();fd=fitz.open(TMP/'fronts.pdf');save(fd,TMP/'fronts_clean.pdf')
    fd=fitz.open(TMP/'fronts_clean.pdf')
    old=json.loads((P/'qa/print_preparation_20260909/imposition_manifest.json').read_text())
    jobs=old['placements'];c=canvas.Canvas(str(TMP/'sheets.pdf'),pagesize=A4,invariant=1,pageCompression=1)
    for i in range(46):
        c.setFillColor(INK);c.setFont('FWBody',7.2)
        c.drawString(12*mm,12*mm,f'FOULWAKE · {i//2+1:02d} · '+('ÖN'if i%2==0 else'ARKA'))
        c.drawRightString(198*mm,12*mm,'A4 · %100 · Uzun kenardan çift taraflı')
        for j in jobs:
            if j['page']==i:marks(c,fitz.Rect(j['bbox']))
        c.showPage()
    c.save();d=fitz.open(TMP/'sheets.pdf');idx={r['id']:i for i,r in enumerate(records)}
    paths={b:P/('print_island_20260909/pdf/BACK_ISLAND.pdf'if b=='BACK_ISLAND' else 'visual/illustrated_design_20260908/pdf/'+b+'.pdf')for b in set(BACK_ID.values())}
    backs={b:fitz.open(p)for b,p in paths.items()}
    for j in jobs:
        src=fd if j['side']=='front'else backs[j['back']];pg=idx[j['id']]if j['side']=='front'else 0
        d[j['page']].show_pdf_page(fitz.Rect(j['bbox'])+(-3*mm,-3*mm,3*mm,3*mm),src,pg,rotate=j['rotation'])
    d.set_metadata({'title':'FOULWAKE — 121 Kart — A4 Çift Taraflı','author':'FOULWAKE','subject':'121 ön ve 121 arka · 23 yaprak · %100 gerçek boyut · uzun kenar'})
    target=OUT/'pdf/FOULWAKE_KARTLAR_A4_CIFT_TARAFLI_v2.7.pdf';save(d,target);shutil.copy2(target,ART/target.name)
    dump(QA/'cards_manifest.json',{'task_id':'FOULWAKE-PUBLICATION-REDESIGN-001','pages':46,'sheets':23,'cards':121,'trim_sizes_mm':[[70,120],[63.5,88.9],[70,70]],'bleed_mm':3,'duplex':'LONG_EDGE','font_family':'Alegreya','fronts':measurements,'placements':jobs,'shared_backs':{b:{'path':str(p.relative_to(R)),'sha256':sha(p),'instances':Counter(BACK_ID.values())[b]}for b,p in paths.items()},'pdf':{'path':str(target.relative_to(R)),'sha256':sha(target),'bytes':target.stat().st_size},'status':'BUILT / AWAITING_REVIEW'})
    print({'pages':46,'fronts':121,'bytes':target.stat().st_size})
if __name__=='__main__':build()
