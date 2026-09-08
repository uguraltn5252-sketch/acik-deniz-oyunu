"""One complete-card master drives both the duplex print and review PDFs."""
from pathlib import Path
from io import BytesIO
from collections import Counter
import json,hashlib,shutil,math
import fitz
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab import rl_config
from pypdf import PdfReader,PdfWriter
from card_layout import R,P,QA,OUT,INDEX,records,dimensions,BACK_ID,INK,PAPER,para,draw_front

rl_config.useA85=0
PDF=OUT/'pdf'
ARTIFACTS=R.parent/'artifacts/illustrated_design_20260908'
BASELINE=R.parent/'redesign_baseline_20260908/FOULWAKE_121_KART_TAM_RESIMLI_v2.7.pdf'
BACKS=['BACK_CHARACTER','BACK_POWER','BACK_LOYALTY','BACK_SEA_ROCK','BACK_ISLAND','BACK_LIGHTHOUSE','BACK_SUPPORT']
POSITIONS=[]

def save_master(doc,target):
    temporary=target.with_name(target.stem+'.pending.pdf')
    expected=len(doc)
    doc.save(temporary,garbage=4,deflate=True)
    doc.close()
    with fitz.open(temporary)as check:
        assert len(check)==expected and temporary.stat().st_size>0
    temporary.replace(target)

def text(c,s,x,y,w,size=10,font='FWBody',align=0):
    p=para(s,size,font,align=align);_,h=p.wrap(w,10000);p.drawOn(c,x,y-h);return h

def frame(c,n,label):
    c.setFillColor(INK);c.setFont('FWBold',10);c.drawString(16*mm,284*mm,label)
    c.setFont('FWBody',8);c.drawString(16*mm,10*mm,'FOULWAKE · v2.7 · 8 Eylül 2026 · Çalışma destesi');c.drawRightString(194*mm,10*mm,str(n))

def crop_marks(c,x,y,w,h):
    c.saveState();c.setStrokeColor(INK);c.setLineWidth(.35)
    for xx in [x,x+w]:
        c.line(xx,y-5.5*mm,xx,y-3.5*mm);c.line(xx,y+h+3.5*mm,xx,y+h+5.5*mm)
    for yy in [y,y+h]:
        c.line(x-5.5*mm,yy,x-3.5*mm,yy);c.line(x+w+3.5*mm,yy,x+w+5.5*mm,yy)
    c.restoreState()

def make_back_masters():
    PDF.mkdir(parents=True,exist_ok=True)
    retained=QA/'retained_backs.json'
    if retained.exists():
        evidence=json.loads(retained.read_text())
        if len(evidence)==7 and all((PDF/(x['id']+'.pdf')).is_file() and hashlib.sha256((PDF/(x['id']+'.pdf')).read_bytes()).hexdigest()==x['sha256'] for x in evidence):
            return  # Rebuild from the committed, verified masters without an old scratch PDF.
    source=fitz.open(BASELINE)
    old=json.loads((P/'qa/whole_game_polish_20260908/render_manifest.json').read_text())
    positions={x['id']:x for x in old['card_pdf_positions']}
    evidence=[]
    for bid in BACKS:
        target=PDF/(bid+'.pdf')
        if bid=='BACK_LIGHTHOUSE':
            original=P/'visual/polish_20260908/pdf/BACK_LIGHTHOUSE.pdf';shutil.copy2(original,target)
            evidence.append({'id':bid,'method':'BYTE_IDENTICAL_RETAINED_SINGLE_UPRIGHT_MASTER','source':str(original.relative_to(R)),'sha256':hashlib.sha256(target.read_bytes()).hexdigest()});continue
        r=next(r for r in records if BACK_ID[r['id']]==bid);w,h=dimensions(r);pos=positions[r['id']]
        x0,y0,x1,y1=pos['bbox_pt'];left=A4[0]-x1
        clip=fitz.Rect(left-3*mm,y0-3*mm,left+w+3*mm,y1+3*mm)
        doc=fitz.open();page=doc.new_page(width=w+6*mm,height=h+6*mm)
        page.show_pdf_page(page.rect,source,pos['page_1based'],clip=clip)
        doc.save(target,garbage=4,deflate=True);doc.close()
        evidence.append({'id':bid,'method':'RETAINED_NATIVE_PDF_ART / NO_REDRAW','source_pdf_sha256':'8cb0bccce33210fb3ca1957e6d93b03e020bf88d28ebb9e817b8dfd0d5342ab0','source_back_page_1based':pos['page_1based']+1,'clip_pt':list(clip),'sha256':hashlib.sha256(target.read_bytes()).hexdigest()})
    (QA/'retained_backs.json').write_text(json.dumps(evidence,ensure_ascii=False,indent=2)+'\n')

def front_master():
    ann=json.loads((QA/'art_annotations.json').read_text())
    assert set(INDEX)==set(ann),'All 121 art boundaries must be measured and reviewed'
    p=ARTIFACTS/'fronts_master.pdf';c=canvas.Canvas(str(p),invariant=1,pageCompression=1)
    placements=[]
    for r in records:
        c.setPageSize(dimensions(r));placements.append(draw_front(c,r,0,0,annotation=ann[r['id']],bleed=False));c.showPage()
    c.save();return p,placements

def cover(c,subtitle,description):
    c.setFillColor(PAPER);c.rect(0,0,*A4,fill=1,stroke=0)
    c.setFillColor(INK);c.setFont('FWBold',35);c.drawCentredString(A4[0]/2,247*mm,'FOULWAKE')
    text(c,subtitle,25*mm,225*mm,160*mm,22,'FWBold',1)
    text(c,description,30*mm,195*mm,150*mm,12,'FWBody',1)
    text(c,'121 özgün kart ön yüzü\nYedi ortak arka yüz\nGüncel kurallar ve kart metinleri',35*mm,158*mm,140*mm,13,'FWBody',1)
    text(c,'Tuzlu kâğıt · Canlı mürekkep · Kuru mizah',30*mm,95*mm,150*mm,12,'FWItalic',1)
    text(c,'8 Eylül 2026 · v2.7 çalışma destesi',30*mm,35*mm,150*mm,10,'FWBody',1)

def instructions(c):
    frame(c,2,'BASKI NOTLARI')
    ps=[
      'A4 kâğıt, gerçek boyut / %100 ölçek. Sayfaya sığdır seçeneğini kapatın. İlk iki sayfa kullanım notudur; kartlar 3. sayfadan başlar.',
      'Her ön sayfanın hemen arkasından eşleşen arka sayfa gelir. Uzun kenardan çift taraflı baskı için arka sütunlar aynalanmıştır. Bölümlere ayrılmış PDF’ler de kendi içinde tam ön–arka çiftleri taşır.',
      'Önce tek bir ön–arka çiftini deneyin. Kesmeden önce hizayı kontrol edin; gizli kartlarda aynı opak kılıflar veya uygun opak karton kullanın.',
      'Kesim çizgileri arasından kesin. Taşma alanı 3 mm’dir ve kart boyuna eklenmez. Karakter ve yardımcılar 70×120 mm; Güç/Erzak ve Sadakat 63,5×88,9 mm; Harita 70×70 mm.',
      'Tayfa ile Hain aynı Sadakat arkasını; Açık Deniz ile Kayalık aynı deniz arkasını paylaşır. Dört fener kartının arkasında aynı tek, dik kule vardır.',
      'Kartlar kaynak metinlerle ve ekranda kontrol edilmiş çalışma baskılarıdır. Fiziksel baskı, kesim, kılıf opaklığı ve insanlarla masa denemesi bu dosyanın üretimi sırasında yapılmadı.'
    ]
    y=265*mm
    for p in ps:y-=text(c,p,19*mm,y,172*mm,11)+7*mm
    c.setStrokeColor(INK);c.line(20*mm,38*mm,120*mm,38*mm)
    text(c,'Ölçek kontrolü: bu çizgi 100 mm olmalı.',20*mm,34*mm,170*mm,10)

def rect(x,y,w,h):return fitz.Rect(x,A4[1]-y-h,x+w,A4[1]-y)

def build_print(fronts):
    blank=ARTIFACTS/'print_background.pdf';c=canvas.Canvas(str(blank),pagesize=A4,invariant=1,pageCompression=1)
    cover(c,'121 resimli kart','Bütün deste · A4 · Çift taraflı çalışma baskısı');c.showPage();instructions(c);c.showPage()
    n=3;jobs=[]
    groups=[([r for r in records if dimensions(r)[1]>110*mm],2,2),([r for r in records if r['collection']in ('powers','provisions','loyalties')],2,3),([r for r in records if r['collection']=='maps'],2,3)]
    for group,ncol,nrow in groups:
        w,h=dimensions(group[0]);gx=12*mm;gy=9*mm if 80*mm<h<100*mm else 12*mm
        sx=(A4[0]-(2*w+gx))/2;sy=(A4[1]-(nrow*h+(nrow-1)*gy))/2
        for offset in range(0,len(group),ncol*nrow):
            batch=group[offset:offset+ncol*nrow]
            for side in ['front','back']:
                c.saveState();c.translate(10*mm,130*mm);c.rotate(90);c.setFillColor(INK);c.setFont('FWBody',7);c.drawString(0,0,f'FOULWAKE · {side.upper()} · {n}');c.restoreState()
                for j,r in enumerate(batch):
                    x=sx+(j%2)*(w+gx);y=sy+(nrow-1-j//2)*(h+gy)
                    if side=='back':x=A4[0]-x-w
                    else:c.setFillColor(PAPER);c.rect(x-3*mm,y-3*mm,w+6*mm,h+6*mm,fill=1,stroke=0)
                    crop_marks(c,x,y,w,h)
                    box=rect(x,y,w,h);jobs.append({'page':n-1,'side':side,'id':r['id'],'bbox':list(box)})
                c.showPage();n+=1
    c.save();assert n-1==48
    doc=fitz.open(blank);source=fitz.open(fronts);backdocs={b:fitz.open(PDF/(b+'.pdf'))for b in BACKS};idx={r['id']:i for i,r in enumerate(records)}
    for job in jobs:
        page=doc[job['page']];box=fitz.Rect(job['bbox'])
        if job['side']=='front':page.show_pdf_page(box,source,idx[job['id']])
        else:
            box=box+(-3*mm,-3*mm,3*mm,3*mm);page.show_pdf_page(box,backdocs[BACK_ID[job['id']]],0)
    target=ARTIFACTS/'FOULWAKE_121_KART_TAM_RESIMLI_v2.7.pdf'
    doc.set_metadata({'title':'FOULWAKE · 121 özgün resimli kart · 8 Eylül 2026','author':'FOULWAKE / CHIEF_EDITOR'})
    save_master(doc,target)
    return target,jobs

def build_review(fronts):
    blank=ARTIFACTS/'review_background.pdf';c=canvas.Canvas(str(blank),pagesize=A4,invariant=1,pageCompression=1)
    cover(c,'Kartların tamamı','121 kart · Çizim, başlık ve kurallar birlikte');c.showPage();n=2;jobs=[];backjobs=[]
    groups=[([r for r in records if dimensions(r)[1]>110*mm],1),([r for r in records if r['collection']in ('powers','provisions','loyalties')],1.18),([r for r in records if r['collection']=='maps'],1.18)]
    for group,scale in groups:
        w,h=dimensions(group[0]);w*=scale;h*=scale;gap=12*mm;sx=(A4[0]-2*w-gap)/2;sy=(A4[1]-2*h-gap)/2
        for offset in range(0,len(group),4):
            frame(c,n,'TAM KART İNCELEMESİ')
            for j,r in enumerate(group[offset:offset+4]):
                x=sx+(j%2)*(w+gap);y=sy+(1-j//2)*(h+gap);jobs.append({'page':n-1,'id':r['id'],'bbox':list(rect(x,y,w,h))})
            c.showPage();n+=1
    frame(c,n,'YEDİ ORTAK ARKA YÜZ')
    counts=Counter(BACK_ID.values())
    for i,bid in enumerate(BACKS):
        r=next(r for r in records if BACK_ID[r['id']]==bid);w,h=dimensions(r);s=min(37*mm/w,64*mm/h);w*=s;h*=s;x=(18+(i%4)*45)*mm;y=(181-(i//4)*94)*mm
        backjobs.append({'page':n-1,'id':bid,'bbox':list(rect(x,y,w,h))})
        text(c,bid.replace('BACK_','')+' · '+str(counts[bid]),x,y-3*mm,39*mm,7.5,'FWBold')
    text(c,'Ortak arkalar korunmuştur. Kart kimlikleri arka yüzlerde yer almaz. Fenerin beğenilen tek kuleli resmi değiştirilmemiştir.',18*mm,53*mm,174*mm,11)
    c.showPage();n+=1;frame(c,n,'ORTAK DENİZDE TEK FENER')
    for row in range(5):
        for col in range(5):
            bid='BACK_LIGHTHOUSE'if(row,col)==(2,3)else'BACK_ISLAND'if(row,col)==(1,1)else'BACK_SEA_ROCK'
            backjobs.append({'page':n-1,'id':bid,'bbox':list(rect((20+34*col)*mm,(73+34*row)*mm,34*mm,34*mm))})
    text(c,'Bu 5×5 düzen görsel komşuluğu gösterir; oyun kurulumu örneği değildir. Kart ve PDF kontrolleri aynı operatörce yapılmıştır. Estetik değerlendirme proje sahibine aittir.',20*mm,59*mm,170*mm,11)
    c.showPage();c.save()
    doc=fitz.open(blank);source=fitz.open(fronts);idx={r['id']:i for i,r in enumerate(records)};backdocs={b:fitz.open(PDF/(b+'.pdf'))for b in BACKS}
    for j in jobs:doc[j['page']].show_pdf_page(fitz.Rect(j['bbox']),source,idx[j['id']])
    for j in backjobs:
        src=backdocs[j['id']];clip=src[0].rect+(3*mm,3*mm,-3*mm,-3*mm)
        doc[j['page']].show_pdf_page(fitz.Rect(j['bbox']),src,0,clip=clip)
    target=ARTIFACTS/'FOULWAKE_121_GORSEL_INCELEME_v2.7.pdf'
    doc.set_metadata({'title':'FOULWAKE · 121 tamamlanmış kartın incelemesi','author':'FOULWAKE / CHIEF_EDITOR'});save_master(doc,target)
    return target,jobs

def split_pdf(path,prefix,pairs=False,limit=10_800_000):
    reader=PdfReader(path);intro=[0,1]if pairs else[0];step=2 if pairs else 1
    units=[list(range(i,min(i+step,len(reader.pages))))for i in range(len(intro),len(reader.pages),step)]
    def encode(indices):
        writer=PdfWriter()
        for i in indices:writer.add_page(reader.pages[i])
        stream=BytesIO();writer.write(stream);return stream.getvalue()
    result=[];chosen=[];last=None
    def save(indices,data):
        dest=PDF/f'{prefix}_{len(result)+1:02}.pdf';dest.write_bytes(data);result.append({'path':str(dest.relative_to(R)),'pages_1based':[i+1 for i in indices],'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()})
    for unit in units:
        data=encode(intro+chosen+unit)
        if len(data)>limit and chosen:save(intro+chosen,last);chosen=[];data=encode(intro+unit)
        if len(data)>limit:raise ValueError(('Transport limit for one complete page unit',unit,len(data)))
        chosen+=unit;last=data
    if chosen:save(intro+chosen,last)
    return result

def main():
    ARTIFACTS.mkdir(parents=True,exist_ok=True);PDF.mkdir(parents=True,exist_ok=True)
    make_back_masters();fronts,placements=front_master();printed,pp=build_print(fronts);review,rp=build_review(fronts)
    volumes=split_pdf(printed,'FOULWAKE_KARTLAR',True)+split_pdf(review,'FOULWAKE_INCELEME')
    manifest={'task_id':'FOULWAKE-ILLUSTRATED-DESIGN-002','status':'AWAITING_FINAL_PDF_INSPECTION','fronts':placements,'print_positions':pp,'review_positions':rp,'back_counts':dict(Counter(BACK_ID.values())),'volumes':volumes,'masters':{p.name:{'path':str(p),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'bytes':p.stat().st_size,'pages':len(fitz.open(p))}for p in [printed,review]}}
    (QA/'render_manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n');print(json.dumps(manifest['masters']))

if __name__=='__main__':main()
