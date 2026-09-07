"""Extend the verified print geometry with selected full-deck artwork.

Retained pilot sources are read in place. New artwork has priority only inside
this task's directory. Canonical text and the binding captain crop are reused.
"""
from pathlib import Path
from collections import Counter
from io import BytesIO
import importlib.util,json,hashlib,sys,math
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
from reportlab.lib.pagesizes import A4
from pypdf import PdfReader,PdfWriter
R=Path(__file__).resolve().parents[4]
P=R/'working/v2.7'
OUT=P/'visual/full_deck_20260907';PDF=OUT/'pdf';PDF.mkdir(parents=True,exist_ok=True)
spec=importlib.util.spec_from_file_location('pilot_layout',P/'qa/recheck_visual/build_print.py')
layout=importlib.util.module_from_spec(spec);spec.loader.exec_module(layout)
class Sources:
 def __truediv__(self,name):
  new=OUT/'assets'/name
  return new if new.exists() else P/'visual/recheck_20260907/assets'/name
layout.ASSETS=Sources();layout.PDF=PDF;layout.OUT=OUT;layout.QA=P/'qa/full_deck_art'
QA=layout.QA;ROOT=R
ARTIFACTS=R.parent/'artifacts/full_deck_20260907'
records=layout.records;INDEX=layout.INDEX;BACKS=layout.BACKS;CAPTAIN=layout.CAPTAIN
dimensions=layout.dimensions;back_id=layout.back_id;metadata=layout.metadata
boxtext=layout.boxtext;page_frame=layout.page_frame
fitted_image=layout.fitted_image

def front(c,r,x,y,scale=1,record=True):
 # Preserve canonical type sizes. Square maps have a tighter metadata gap,
 # reserving a real illustration area even for the longest island effect.
 w,h=dimensions(r);c.saveState();c.translate(x,y);c.scale(scale,scale)
 c.setFillColor(layout.PAPER);c.rect(-3*mm,-3*mm,w+6*mm,h+6*mm,fill=1,stroke=0)
 c.setStrokeColor(layout.INK);c.setLineWidth(.7);c.roundRect(mm,mm,w-2*mm,h-2*mm,2*mm,fill=0)
 left=4.5*mm;cw=w-9*mm;top=h-4.5*mm
 th=boxtext(c,r.get('name',r.get('title')),left,top,cw,14 if h>110*mm else 11.2,'Title');top-=th+1.5*mm
 mh=boxtext(c,metadata(r),left,top,cw,7.6,'Strong',layout.MUTED)
 top-=mh+(1.5 if r['collection']=='maps'else 2.5)*mm
 effect=layout.para(r['effect'],8.6,'Body',11.1)
 flavor=layout.para(r['flavor'],8,'Flavor',10.2,color=layout.MUTED)
 _,eh=effect.wrap(cw,10000);_,fh=flavor.wrap(cw,10000)
 copy_top=9*mm+eh+fh+3.5*mm;art_h=top-copy_top-3.5*mm
 if art_h<9*mm:raise ValueError(('Artwork has no readable room',r['id'],art_h/mm))
 art=layout.ASSETS/(r['id']+'.png')
 if r['id']=='SET-KP-01':dpi=fitted_image(c,CAPTAIN,left,copy_top+3.5*mm,cw,art_h,source_rect=(22,180,874,1093))
 else:dpi=fitted_image(c,art,left,copy_top+3.5*mm,cw,art_h)
 effect.drawOn(c,left,copy_top-eh);rule_y=copy_top-eh-1.7*mm
 c.setStrokeColor(layout.LINE);c.setLineWidth(.4);c.line(left,rule_y,w-left,rule_y)
 flavor.drawOn(c,left,rule_y-1.8*mm-fh)
 c.setFont('Body',6.6);c.setFillColor(layout.MUTED);c.drawString(left,4.5*mm,r['id'])
 if r['collection']=='powers'and r.get('returns_to_power_deck')is False:
  c.drawRightString(w-left,4.5*mm,'Kullanım sonrası oyun dışı')
 c.restoreState()
 if record:layout.PLACEMENTS.append({'id':r['id'],'trim_mm':[w/mm,h/mm],'bleed_mm':3,'safe_mm':4.5,
  'effect_pt':8.6,'flavor_pt':8,'illustration':True,'effective_art_dpi':round(dpi,2),'art_height_mm':round(art_h/mm,3),
  'copy_sha256':hashlib.sha256(json.dumps({k:r.get(k)for k in ['name','title','effect','flavor']},ensure_ascii=False,sort_keys=True).encode()).hexdigest(),
  'exact_fields':{k:r[k]for k in ['name','title','role','group','time','side','category','family','section_label','effect','flavor']if k in r},'back':back_id(r)})
def back(c,bid,x,y,w,h,bleed=True):
 pad=3*mm if bleed else 0;x-=pad;y-=pad;w+=2*pad;h+=2*pad
 path=layout.ASSETS/(bid+'.png')
 c.saveState();c.translate(x,y)
 for rot in (0,180):
  c.saveState()
  if rot:c.translate(w,h);c.rotate(180)
  clip=c.beginPath();clip.rect(0,h/2,w,h/2);c.clipPath(clip,stroke=0)
  layout.fitted_image(c,path,0,0,w,h,contain=False)
  c.restoreState()
 c.restoreState()
layout.back=back
def lighthouse():
 p=PDF/'BACK_LIGHTHOUSE.pdf'
 c=canvas.Canvas(str(p),pagesize=(76*mm,76*mm),invariant=1,pageCompression=1)
 c.setTitle('FOULWAKE - Fener ortak arka yüz - yandan görünüm')
 back(c,'BACK_LIGHTHOUSE',3*mm,3*mm,70*mm,70*mm);c.showPage();c.save()
 print(json.dumps({'file':str(p.relative_to(R)),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}))

def copy_geometry():
 """Measure every canonical card before expensive full-deck rendering."""
 results=[]
 for r in records:
  w,h=dimensions(r);cw=w-9*mm
  title=r.get('name',r.get('title'));size=14 if h>110*mm else 11.2
  _,th=layout.para(title,size,'Title').wrap(cw,10000)
  _,mh=layout.para(metadata(r),7.6,'Strong').wrap(cw,10000)
  _,eh=layout.para(r['effect'],8.6,'Body',11.1).wrap(cw,10000)
  _,fh=layout.para(r['flavor'],8,'Flavor',10.2).wrap(cw,10000)
  art_h=h-4.5*mm-th-1.5*mm-mh-(1.5 if r['collection']=='maps'else 2.5)*mm-(9*mm+eh+fh+3.5*mm)-3.5*mm
  results.append({'id':r['id'],'art_height_mm':round(art_h/mm,3)})
 if any(x['art_height_mm']<9 for x in results):
  raise ValueError([x for x in results if x['art_height_mm']<9])
 return results

def instructions(c):
 page_frame(c,2,'BASKIDAN ÖNCE')
 paragraphs=[
  'Bu destenin 121 kartının tamamı resimlidir. Güncel kart metinleri, yedi ortak arka yüz ve yandan görünen yeni fener bu dosyada birlikte yer alır.',
  'A4 kâğıt, gerçek boyut / %100 ölçek; sayfaya sığdır kapalı. İlk iki sayfa kullanım notudur. Kart yaprakları 3. sayfadan başlar: her ön sayfayı hemen izleyen sayfa onun arkasıdır. Uzun kenardan çift taraflı baskı kullanın; arka sütunlar buna göre aynalanmıştır.',
  'Bölümlere ayrılmış PDF’lerde de ilk iki sayfa kullanım notudur. Her bölüm kendi içinde tam ön–arka çiftleri içerir. Bölümleri ayrı ayrı yazdırın; tek sayfaları birbirine karıştırmayın.',
  'Önce bir ön–arka çiftini deneyin. Kesmeden önce hizayı ışığa tutarak kontrol edin. Gizli kartlarda opak karton veya aynı opak kılıflar kullanın.',
  'Kesim çizgileri arasından kesin. Renkli taşma alanı kart boyuna eklenmez. Karakter ve yardımcılar 70×120 mm; Güç/Erzak ve Sadakat 63,5×88,9 mm; Harita 70×70 mm.',
  'Tayfa ve Hain kartları tek ortak arka yüzü kullanır. Deniz ve Kayalık kartlarında da aynı ortak arka yüz vardır. Kart kimliği ve sayfa bilgileri arka yüzün kesim alanı dışında kalır.',
  'Bu dosya çalışma baskısıdır. Fiziksel çift taraflı baskı, opaklık ve insanlarla masa denemesi henüz yapılmadı.'
 ]
 y=263*mm
 for t in paragraphs:y-=boxtext(c,t,20*mm,y,170*mm,10.5)+5*mm
 c.setStrokeColor(layout.INK);c.setLineWidth(.8);c.line(20*mm,33*mm,120*mm,33*mm)
 boxtext(c,'Ölçek kontrolü: bu çizgi 100 mm olmalı.',20*mm,29*mm,170*mm,9)

def build_cards():
 missing=[r['id']for r in records if r['id']!='SET-KP-01'and not(layout.ASSETS/(r['id']+'.png')).exists()]
 if missing:raise ValueError({'missing_fronts':missing})
 path=ARTIFACTS/'FOULWAKE_121_KART_TAM_RESIMLI_v2.7.pdf'
 c=canvas.Canvas(str(path),pagesize=A4,invariant=1,pageCompression=1)
 c.setTitle('FOULWAKE - 121 Resimli Kart');c.setAuthor('FOULWAKE / CHIEF_EDITOR')
 layout.cover(c,'121 resimli kart','Bütün deste · Yedi ortak arka yüz\nA4 · %100 ölçek · uzun kenardan çift taraflı baskı');c.showPage()
 instructions(c);c.showPage();number=3
 groups=[([r for r in records if dimensions(r)[1]==120*mm],2,2),
         ([r for r in records if r['collection']in ('powers','provisions','loyalties')],2,3),
         ([r for r in records if r['collection']=='maps'],2,3)]
 for rs,ncol,nrow in groups:
  w,h=dimensions(rs[0]);gap_y=9*mm if 80*mm<h<100*mm else 12*mm
  pitchw=w+12*mm;pitchh=h+gap_y
  startx=(A4[0]-(ncol*w+(ncol-1)*12*mm))/2
  starty=(A4[1]-(nrow*h+(nrow-1)*gap_y))/2
  for start in range(0,len(rs),ncol*nrow):
   batch=rs[start:start+ncol*nrow]
   for side in ('front','back'):
    c.saveState();c.translate(10*mm,135*mm);c.rotate(90)
    c.setFont('Body',7);c.setFillColor(layout.MUTED)
    c.drawString(0,0,f'FOULWAKE · {"ÖN" if side=="front" else "ARKA"} · {number}');c.restoreState()
    for i,r in enumerate(batch):
     col=i%ncol;row=i//ncol;x=startx+col*pitchw;y=starty+(nrow-1-row)*pitchh
     if side=='back':x=A4[0]-x-w;back(c,back_id(r),x,y,w,h)
     else:
      front(c,r,x,y)
      layout.PAGE_RECORDS.append({'id':r['id'],'page_1based':number,'bbox_pt':[x,A4[1]-y-h,x+w,A4[1]-y]})
     layout.crop_marks(c,x,y,w,h)
    c.showPage();number+=1
 c.save();assert number-1==48
 return path

def build_review():
 path=ARTIFACTS/'FOULWAKE_121_GORSEL_INCELEME_v2.7.pdf'
 c=canvas.Canvas(str(path),pagesize=A4,invariant=1,pageCompression=1)
 c.setTitle('FOULWAKE - Bütün Deste Görsel İnceleme')
 layout.cover(c,'Bütün deste · Görsel inceleme','121 ayrı ön yüz · Yedi ortak arka yüz\nKart metinleri ve gerçek ölçüler baskı dosyasındadır.');c.showPage()
 number=2
 for start in range(0,len(records),6):
  page_frame(c,number,'ÖN YÜZLER / '+str(start+1)+'–'+str(min(start+6,len(records))))
  for i,r in enumerate(records[start:start+6]):
   x=(17+(i%2)*92)*mm;y=(192-(i//2)*84)*mm
   path_art=CAPTAIN if r['id']=='SET-KP-01'else layout.ASSETS/(r['id']+'.png')
   fitted_image(c,path_art,x,y,84*mm,68*mm,source_rect=(22,180,874,1093)if r['id']=='SET-KP-01'else None)
   boxtext(c,r['id']+' · '+r.get('name',r.get('title')),x,y-2*mm,84*mm,8.6,'Strong')
  c.showPage();number+=1
 page_frame(c,number,'YEDİ ORTAK ARKA YÜZ')
 counts=Counter(back_id(r)for r in records)
 for i,bid in enumerate(BACKS):
  r=next(r for r in records if back_id(r)==bid);w,h=dimensions(r)
  s=min(37*mm/w,64*mm/h);x=(18+(i%4)*45)*mm;y=(181-(i//4)*96)*mm
  back(c,bid,x,y,w*s,h*s,False)
  boxtext(c,bid.replace('BACK_','')+' · '+str(counts[bid]),x,y-4*mm,39*mm,7.4,'Strong')
 boxtext(c,'Tayfa/Hain ve Deniz/Kayalık kendi aileleri içinde aynı masterı kullanır. Fenerin yeni yandan görünümü dört fener kartında ortaktır. Bu sayfalardaki etiketler kart arkasında yer almaz.',18*mm,46*mm,174*mm,10)
 c.showPage();number+=1;page_frame(c,number,'ORTAK DENİZDE FENER')
 for row in range(5):
  for col in range(5):
   bid='BACK_LIGHTHOUSE'if(row,col)==(2,3)else'BACK_ISLAND'if(row,col)==(1,1)else'BACK_SEA_ROCK'
   back(c,bid,(20+col*34)*mm,(73+row*34)*mm,34*mm,34*mm,False)
 boxtext(c,'Bu 5×5 düzen yalnız görsel komşuluğu gösterir. Oyun kurulumu örneği değildir. Aynı operatörün görsel ve teknik kontrolü tamamlandığında raporlanır; bağımsız sanat kabulü ve fiziksel baskı yerine geçmez.',20*mm,59*mm,170*mm,10)
 c.showPage();c.save();return path

def split_pdf(path,prefix,pairs=False,limit=10_800_000):
 """Keep complete duplex pairs and existing image streams in each volume."""
 reader=PdfReader(path);intro=[0,1]if pairs else[0]
 units=[list(range(i,min(i+(2 if pairs else 1),len(reader.pages))))for i in range(len(intro),len(reader.pages),2 if pairs else 1)]
 def encode(indices):
  writer=PdfWriter()
  for i in indices:writer.add_page(reader.pages[i])
  writer.add_metadata({'/Title':'FOULWAKE / '+prefix,'/Author':'FOULWAKE / CHIEF_EDITOR'})
  stream=BytesIO();writer.write(stream);return stream.getvalue()
 result=[];chosen=[];last=None
 def save(indices,data):
  dest=PDF/f'{prefix}_{len(result)+1:02d}.pdf';dest.write_bytes(data)
  result.append({'file':str(dest.relative_to(R)),'master_pages_1based':[i+1 for i in indices],
                 'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()})
 for unit in units:
  data=encode(intro+chosen+unit)
  if len(data)>limit and chosen:
   save(intro+chosen,last);chosen=[];data=encode(intro+unit)
  if len(data)>limit:raise ValueError(('Single complete unit exceeds transport budget',unit,len(data)))
  chosen+=unit;last=data
 if chosen:save(intro+chosen,last)
 return result

def build_all():
 ARTIFACTS.mkdir(parents=True,exist_ok=True);geometry=copy_geometry()
 layout.PLACEMENTS.clear();layout.PAGE_RECORDS.clear()
 cards=build_cards();review=build_review();lighthouse()
 volumes=split_pdf(cards,'FOULWAKE_KARTLAR',pairs=True)+split_pdf(review,'FOULWAKE_GORSEL')
 manifest={'task_id':'FOULWAKE-FULL-DECK-ART-001','status':'GENERATED_AWAITING_RENDER_INSPECTION',
 'cards':layout.PLACEMENTS,'card_pdf_positions':layout.PAGE_RECORDS,'copy_geometry':geometry,
 'back_counts':dict(Counter(back_id(r)for r in records)),'volumes':volumes,
 'compiled_masters':{p.name:{'pages':len(PdfReader(p).pages),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}for p in (cards,review)},
 'repository_pdfs':{p.name:hashlib.sha256(p.read_bytes()).hexdigest()for p in PDF.glob('*.pdf')}}
 (QA/'render_manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
 print(json.dumps({'cards':len(layout.PLACEMENTS),'illustrated_fronts':sum(x['illustration']for x in layout.PLACEMENTS),'volumes':len(volumes),'compiled_masters':manifest['compiled_masters']}))

if __name__=='__main__':
 if '--lighthouse' in sys.argv:lighthouse()
 elif '--preflight' in sys.argv:
  geometry=copy_geometry();print(json.dumps({'cards':len(geometry),'smallest_art_spaces':sorted(geometry,key=lambda x:x['art_height_mm'])[:8]}))
 else:build_all()
