"""FOULWAKE A4 publication: native text, source-linked panels and diagrams."""
from pathlib import Path
from html import escape
from io import BytesIO
from functools import lru_cache
import json,re,hashlib,shutil,math
import fitz
from PIL import Image as PILImage
from reportlab import rl_config
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import BaseDocTemplate,Frame,PageTemplate,Paragraph,Spacer,PageBreak,CondPageBreak,KeepTogether,Table,LongTable,TableStyle,Flowable,Image
from reportlab.platypus.tableofcontents import TableOfContents
R=Path(__file__).resolve().parents[4];P=R/'working/v2.7';Q=Path(__file__).resolve().parent;O=P/'publication_20260909';A=O/'assets';T=R.parent/'tmp/publication_20260909';ART=R.parent/'artifacts/publication_20260909'
rl_config.useA85=0;rl_config.invariant=1
for n,s in [('Body','Regular'),('Bold','Bold'),('Title','Black'),('Italic','Italic')]:pdfmetrics.registerFont(TTFont(n,str(O/'fonts'/f'Alegreya-{s}.ttf')))
pdfmetrics.registerFontFamily('Body',normal='Body',bold='Bold',italic='Italic',boldItalic='Bold')
INK=colors.CMYKColor(0,0,0,1);NAVY=colors.HexColor('#29434B');OCHRE=colors.HexColor('#A47A43');PAPER=colors.HexColor('#F8F1E3');PANEL=colors.HexColor('#EFE2C9');PALE=colors.HexColor('#E8EEEA');WIDTH=170*mm
UNITS=[];DIAGRAMS=[]
def rich(s):
 s=escape(str(s)).replace('\n','<br/>');s=re.sub(r'`([^`]+)`',r'\1',s);s=re.sub(r'\*\*([^*]+)\*\*',r'<b>\1</b>',s);return re.sub(r'(?<!\*)\*([^*]+)\*(?!\*)',r'<i>\1</i>',s)
def p(s,size=11.2,font='Body',after=7,**kw):
 return Paragraph(rich(s),ParagraphStyle('p',fontName=font,fontSize=size,leading=size*1.31,textColor=INK,spaceAfter=after,splitLongWords=False,allowWidows=0,allowOrphans=0,**kw))
def plain(c,s,x,y,w,size=10,font='Body',**kw):
 a=p(s,size,font,0,**kw);_,h=a.wrap(w,10000);a.drawOn(c,x,y-h);return h
def rule(c,x,y,w):
 c.setStrokeColor(OCHRE);c.setLineWidth(.45);c.line(x,y,x+w,y)
def rose(c,x,y,r):
 c.saveState();c.translate(x,y);c.setStrokeColor(OCHRE);c.setLineWidth(.4);c.circle(0,0,r,stroke=1,fill=0);c.circle(0,0,r*.8,stroke=1,fill=0)
 for n in range(8):
  c.saveState();c.rotate(n*45);path=c.beginPath();path.moveTo(0,r*1.22);path.lineTo(r*.13,0);path.lineTo(0,-r*.23);path.close();c.setFillColor(OCHRE if n%2 else NAVY);c.drawPath(path,fill=1,stroke=0);c.restoreState()
 c.restoreState()
class Ribbon(Flowable):
 def __init__(self,title,number):super().__init__();self.title=title;self.toc_title=title;self.toc_number=number;self.width=WIDTH;self.height=19*mm;self.keepWithNext=True
 def draw(self):
  c=self.canv;c.setFillColor(PANEL);c.setStrokeColor(OCHRE);c.setLineWidth(.5)
  path=c.beginPath();path.moveTo(0,2*mm);path.lineTo(2*mm,8*mm);path.lineTo(0,15*mm);path.lineTo(WIDTH,15*mm);path.lineTo(WIDTH-2*mm,8*mm);path.lineTo(WIDTH,2*mm);path.close();c.drawPath(path,fill=1,stroke=1)
  plain(c,self.title,5*mm,13.7*mm,WIDTH-10*mm,18,'Title')
class Illustration(Flowable):
 def __init__(self,name,caption,side='left'):super().__init__();self.name=name;self.caption=caption;self.width=WIDTH;self.height=62*mm
 def draw(self):
  c=self.canv;path=A/(self.name+'.png');im=PILImage.open(path);w=78*mm;h=w*im.height/im.width
  c.drawImage(ImageReader(str(path)),0,5*mm,w,h,mask='auto');plain(c,self.caption,86*mm,49*mm,80*mm,12,'Italic');rule(c,86*mm,8*mm,65*mm)
  DIAGRAMS.append({'type':'illustration','name':self.name,'page':c.getPageNumber(),'width_mm':78,'effective_dpi':im.width/(78/25.4)})
class Horizon(Flowable):
 def __init__(self):super().__init__();self.width=WIDTH;self.height=61*mm
 def draw(self):
  c=self.canv;c.setFillColor(PALE);c.roundRect(0,0,WIDTH,58*mm,2*mm,fill=1,stroke=0)
  x=53*mm;sz=14*mm
  for row in range(3):
   for col in range(5):
    xx=x+col*sz;yy=(2-row)*sz+11*mm;active=(row<2 and col in [1,2,3]);c.setFillColor(colors.HexColor('#C5D6D3')if active else colors.HexColor('#F6F5EC'));c.setStrokeColor(NAVY);c.setLineWidth(.4);c.rect(xx,yy,sz-1*mm,sz-1*mm,fill=1,stroke=1)
    if row==2 and col==2:
     path=c.beginPath();path.moveTo(xx+3*mm,yy+3*mm);path.lineTo(xx+10*mm,yy+3*mm);path.lineTo(xx+6.5*mm,yy+10*mm);path.close();c.setFillColor(NAVY);c.drawPath(path,fill=1,stroke=0)
  for text,yy in [('UZAK UFUK',50),('YAKIN UFUK',36),('GEMİ',22)]:plain(c,text,5*mm,yy*mm,43*mm,10,'Bold')
  plain(c,'İki Ufuk da aynı üç sütuna bakar. Sınır ve yasal yol koşulları ayrıca uygulanır.',5*mm,8.5*mm,160*mm,9.3)
  DIAGRAMS.append({'type':'horizon','page':c.getPageNumber(),'source':'§6.2'})
class MapSetup(Flowable):
 def __init__(self):super().__init__();self.width=WIDTH;self.height=109*mm
 def draw(self):
  c=self.canv;size=15*mm;x=12*mm;y=19*mm
  island={(1,1),(3,3)};light={(1,4),(3,0)}
  for row in range(5):
   for col in range(5):
    kind='Ada'if(row,col)in island else'Fener'if(row,col)in light else'Deniz'
    xx=x+col*size;yy=y+row*size;c.setFillColor(PANEL if kind=='Ada'else PALE if kind=='Fener'else NAVY);c.setStrokeColor(PAPER);c.setLineWidth(.8);c.rect(xx,yy,size-.7*mm,size-.7*mm,fill=1,stroke=1)
    c.drawImage(map_back_thumbnail(kind),xx,yy,size-.7*mm,size-.7*mm)
  col=2;cx=x+col*size;plain(c,'PORT AVANTA',x-5*mm,14*mm,85*mm,9,'Bold',alignment=1);plain(c,'SANTA VEDA',x-5*mm,106*mm,85*mm,9,'Bold',alignment=1)
  c.setStrokeColor(OCHRE);c.setLineWidth(1.8);c.rect(cx,y+4*size,size-.7*mm,size-.7*mm,stroke=1,fill=0)
  c.line(cx+7*mm,y-1*mm,cx+7*mm,y-4*mm);c.line(cx+7*mm,y+5*size,cx+7*mm,y+5*size+3*mm)
  plain(c,'5 × 5 / HIZLI OYUN',99*mm,99*mm,70*mm,12,'Bold')
  plain(c,'6–10 oyuncu: 15 Deniz, 6 Kayalık, 2 Ada, 2 Fener.\n\n21 koyu kare aynı Deniz/Kayalık arkasını gösterir. İki tür burada ayırt edilmez.\n\nÇerçeveli üst kare Hedef Limandır. Varış kartı dışarıda hizalanır; fazladan kare eklemez.',99*mm,89*mm,69*mm,10.4)
  plain(c,'Bu şema yalnız dışarıdan görünen düzeni gösterir; gizli olayları §2.3 ile denetle.',4*mm,6*mm,163*mm,9.3)
  DIAGRAMS.append({'type':'map_setup','page':c.getPageNumber(),'visible_categories':[21,2,2],'source':'§2.2–2.3; no hidden events asserted'})
@lru_cache(maxsize=3)
def map_back_thumbnail(kind):
 # Reproduce the actual shared card back in an explanatory PDF diagram.
 # Render only the card trim, excluding the existing off-trim bleed.
 path=P/('print_island_20260909/pdf/BACK_ISLAND.pdf' if kind=='Ada' else 'visual/illustrated_design_20260908/pdf/'+('BACK_LIGHTHOUSE' if kind=='Fener' else 'BACK_SEA_ROCK')+'.pdf')
 with fitz.open(path) as d:
  pix=d[0].get_pixmap(dpi=180,clip=d[0].rect+(3*mm,3*mm,-3*mm,-3*mm),alpha=False)
  return ImageReader(BytesIO(pix.tobytes('png')))
def box(label,lines,color=PANEL):
 content=[p(label,10,'Bold',5)]+[p(s,11.2,after=6)for s in lines]
 table=Table([[content]],colWidths=[WIDTH],hAlign='LEFT')
 table.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,-1),color),('BOX',(0,0),(-1,-1),.4,OCHRE),('LEFTPADDING',(0,0),(-1,-1),10),('RIGHTPADDING',(0,0),(-1,-1),10),('TOPPADDING',(0,0),(-1,-1),9),('BOTTOMPADDING',(0,0),(-1,-1),5)]));return KeepTogether([table,Spacer(1,9)])
def page_frame(c,doc):
 if doc.page==1:
  # Full-page native cover. The original illustration is displayed whole at
  # 88 mm / >300 ppi, avoiding an untruthful 300-dpi claim for a stretched image.
  c.setFillColor(PANEL);c.rect(0,0,*A4,fill=1,stroke=0)
  c.setStrokeColor(NAVY);c.setLineWidth(1.1);c.rect(10*mm,10*mm,190*mm,277*mm,fill=0,stroke=1)
  c.setLineWidth(.35);c.rect(12*mm,12*mm,186*mm,273*mm,fill=0,stroke=1)
  for x,y in [(20,20),(190,20),(20,277),(190,277)]:rose(c,x*mm,y*mm,3.7*mm)
  c.setFillColor(NAVY);c.setFont('Title',58);c.drawCentredString(105*mm,241*mm,'FOULWAKE')
  rule(c,30*mm,228*mm,150*mm)
  im=PILImage.open(A/'COVER.png');w=88*mm;h=w*im.height/im.width;x=(A4[0]-w)/2;y=78*mm
  c.setFillColor(NAVY);c.rect(x-2*mm,y-2*mm,w+4*mm,h+4*mm,fill=1,stroke=0);c.drawImage(ImageReader(str(A/'COVER.png')),x,y,w,h)
  # Quiet radiating nautical lines give the entire sheet a deliberate cover.
  c.setStrokeColor(OCHRE);c.setLineWidth(.35)
  for yy in [95,118,141,164,187]:
   c.line(23*mm,yy*mm,51*mm,(yy+7)*mm);c.line(159*mm,(yy+7)*mm,187*mm,yy*mm)
  rose(c,105*mm,43*mm,13*mm)
  return
 c.setFillColor(PAPER);c.rect(0,0,*A4,fill=1,stroke=0)
 # Light, warm margin bands retain the printed-paper character without noise under type.
 c.setFillColor(PANEL);c.rect(0,0,6*mm,A4[1],fill=1,stroke=0);c.rect(204*mm,0,6*mm,A4[1],fill=1,stroke=0)
 x=(22 if doc.page%2 else 18)*mm
 c.setFillColor(NAVY);c.setFont('Bold',8.5);c.drawString(x,284*mm,'FOULWAKE');c.drawRightString(x+WIDTH,284*mm,'SEFER DEFTERİ');rule(c,x,280*mm,WIDTH)
 c.setFont('Body',8.5);c.drawString(x,13*mm,str(doc.page));c.drawRightString(x+WIDTH,13*mm,'v2.7');rose(c,A4[0]/2,14*mm,1.6*mm)
class Book(BaseDocTemplate):
 def __init__(self,path):
  super().__init__(str(path),pagesize=A4,title='FOULWAKE',author='FOULWAKE');self.chapters=[]
  self.addPageTemplates([PageTemplate(id=n,frames=[Frame(x*mm,23*mm,WIDTH,251*mm,leftPadding=0,rightPadding=0,topPadding=0,bottomPadding=0)],onPage=page_frame)for n,x in [('odd',22),('even',18)]])
 def handle_pageBegin(self):self.pageTemplate=self.pageTemplates[self.page%2];super().handle_pageBegin()
 def afterFlowable(self,f):
  if hasattr(f,'toc_title'):
   key='section'+str(f.toc_number);self.canv.bookmarkPage(key);self.canv.addOutlineEntry(f.toc_title,key,0,False);self.notify('TOCEntry',(0,f.toc_title,self.page,key));self.chapters.append({'title':f.toc_title,'page':self.page})
def parse():
 lines=(P/'FOULWAKE_KURAL_KITABI_v2.7.md').read_text().splitlines();lines=lines[next(i for i,s in enumerate(lines)if s.startswith('## 1.')):];f=[];i=0;sec=0
 while i<len(lines):
  s=lines[i].strip()
  if not s or s=='---':i+=1;continue
  if s.startswith('## '):
   sec+=1;title=s[3:];f.append(PageBreak()if sec in [2,3,4,13,14,15,16,17,18] else CondPageBreak(64*mm) if sec>1 else Spacer(1,0));f.append(Ribbon(title,sec));UNITS.append(title);i+=1;continue
  if s.startswith('### '):
   title=s[4:];f.append(CondPageBreak(37*mm));f.append(p(title,13.4,'Bold',8,spaceBefore=8,keepWithNext=True));UNITS.append(title)
   if title.startswith('6.2'):f.append(Horizon())
   if title.startswith('3.1'):f.append(Illustration('PORT_AVANTA','Yük hazır. İmza eksik.\nPort Avanta’da her hareketin bir kâğıdı var.'))
   if title=='Gusto\'nun boş kamarası':f.append(Illustration('GUSTO_CABIN','Eşyaları yerinde. Kaptan değil.\nBu ayrıntılar bir suçluyu göstermez.'))
   i+=1;continue
  if s.startswith('**OKU') and (s.endswith('**')):
   label=s.strip('*').replace(' - ',' · ');i+=1;paras=[]
   while i<len(lines):
    z=lines[i].strip()
    if z.startswith(('#','**YAP','**OKU','|','- '))or re.match(r'^\d+\. ',z):break
    if z:
     buf=[z];i+=1
     while i<len(lines)and lines[i].strip()and not lines[i].startswith(('#','**YAP','**OKU')):buf.append(lines[i].strip());i+=1
     txt=' '.join(buf);paras.append(txt);UNITS.append(txt)
    else:i+=1
   f.append(box(label,paras));continue
  if s.startswith('|'):
   rows=[]
   while i<len(lines)and lines[i].strip().startswith('|'):
    cells=[v.strip()for v in lines[i].strip().strip('|').split('|')]
    if not all(re.fullmatch(r'[:\- ]+',v)for v in cells):rows.append(cells);UNITS.extend(cells)
    i+=1
   n=len(rows[0]);weights={2:[.32,.68],3:[.28,.18,.54],4:[.22,.25,.29,.24],5:[.11,.19,.245,.19,.265]}.get(n,[1/n]*n)
   if sec==1:weights=[.16,.39,.45]
   if sec==13:weights=[.28,.08,.64]
   if sec in (14,15):weights=[.29,.19,.52]
   data=[[p(z,10.2 if sec not in (13,14,15) else 9.8,'Bold'if j==0 else'Body',0)for z in row]for j,row in enumerate(rows)]
   table=LongTable(data,colWidths=[WIDTH*v for v in weights],repeatRows=1,hAlign='LEFT')
   table.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),PANEL),('ROWBACKGROUNDS',(0,1),(-1,-1),[colors.HexColor('#FDF9EF'),colors.HexColor('#EDF0E9')]),('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),7),('RIGHTPADDING',(0,0),(-1,-1),7),('TOPPADDING',(0,0),(-1,-1),4.5),('BOTTOMPADDING',(0,0),(-1,-1),4.5),('LINEBELOW',(0,0),(-1,0),.7,OCHRE)]));f.extend([table,Spacer(1,8)])
   if sec==14:table.setStyle(TableStyle([('TOPPADDING',(0,0),(-1,-1),3),('BOTTOMPADDING',(0,0),(-1,-1),3)]))
   if sec==2 and n==5:f.append(MapSetup())
   continue
  if s.startswith('- ')or re.match(r'^\d+\. ',s):
   t='• '+s[2:]if s.startswith('- ')else s;UNITS.append(t);f.append(p(t,11.2,after=6,leftIndent=10,firstLineIndent=-10));i+=1;continue
  buf=[s];i+=1
  while i<len(lines)and lines[i].strip()and not lines[i].startswith(('#','|','- ','**OKU','**YAP'))and not re.match(r'^\d+\. ',lines[i]):buf.append(lines[i].strip());i+=1
  t=' '.join(buf);UNITS.append(t)
  if t.startswith('**YAP:**'):f.append(box('YAP',[t[len('**YAP:**'):].strip()],PALE))
  elif t.startswith('**Örnek:**'):f.append(box('ÖRNEK',[t[len('**Örnek:**'):].strip()],PALE))
  else:f.append(p(t))
 return f
def build():
 doc=Book(T/'book_native.pdf');toc=TableOfContents();toc.levelStyles=[ParagraphStyle('toc',fontName='Body',fontSize=10.2,leading=13.6,textColor=INK,spaceBefore=2)]
 flows=[Spacer(1,240*mm),PageBreak(),p('Kitabı kullanırken',24,'Title',12),p('6–15 oyuncu ve 1 tarafsız Moderatör.\nGizli sadakat, ortak gemi, birlikte seçilen rota.',11.5,after=10),p('Önce §2 ile haritayı hazırla; masada §3 ile başla. Sefer sırasında §4 açık kalsın. §13–16 başvuru tablolarıdır; §17 isteğe bağlı hikâyedir. Bütün kitabı oyunculara okuma.',11.2,after=12),toc,Spacer(1,12),box('OKU / YAP',['OKU kutularını seslendir. YAP kutularındaki adımları uygula. Tat metni atmosferdir; yeni bir kural veya gizli ipucu değildir.'],PALE),PageBreak()]+parse()
 doc.multiBuild(flows);d=fitz.open(T/'book_native.pdf')
 # Final printable reverse is useful, with a short index and print settings.
 final=T/'colophon.pdf';c=canvas.Canvas(str(final),pagesize=A4,invariant=1);class_stub=type('Page',(),{'page':len(d)+1});page_frame(c,class_stub)
 plain(c,'Sık karışan üç ayrım',22*mm,269*mm,WIDTH,22,'Title');y=249*mm
 for title,body in [('Bakmak / açmak / girmek','Gizli bakış kartı kapalı tutar. Kamusal açma kartı açık tutar. Olay, ilk gerçek girişte çözülür (§6.4).'),('Karakter / Sadakat / makam','Karakter gemideki işindir. Sadakat takımındır. Kaptanlık değişebilen makamdır; bu üçü birbirini belirlemez (§1, §3, §5).'),('Varış / teslim','Hedef Limana giriş, son kontrolü başlatır. Gövde ve İskorbüt kontrolünden sonra Liman Gecesi oynanır; zafer şafakta belirlenir (§4.4, §12).')]:
  y-=plain(c,title,22*mm,y,WIDTH,13,'Bold')+3*mm;y-=plain(c,body,22*mm,y,WIDTH,11.5)+10*mm
 rule(c,22*mm,113*mm,WIDTH);plain(c,'Baskı',22*mm,106*mm,WIDTH,15,'Bold');plain(c,'A4 · Gerçek boyut / %100 · Uzun kenardan çift taraflı.\nKart PDF’sinde her ön sayfayı doğru arka sayfa izler. Sayfaya sığdırma kapalı olmalı. İlk yaprağı kesmeden önce iki yüzün kesim çizgilerini ışığa tutarak kontrol et.',22*mm,95*mm,WIDTH,11.2)
 plain(c,'9 Eylül 2026 · v2.7\nYazı ailesi: Alegreya — Juan Pablo del Peral / Huerta Tipográfica.\nDijital üretim kontrolü fiziksel yazıcı kalibrasyonunun yerine geçmez.',22*mm,42*mm,WIDTH,9.3)
 c.showPage();c.save()
 if len(d)%2:d.insert_pdf(fitz.open(final))
 else:
  # Keep the useful colophon even when parity already matches, paired with notes.
  d.insert_pdf(fitz.open(final));n=d.new_page(width=A4[0],height=A4[1]);notes=T/'notes.pdf';c=canvas.Canvas(str(notes),pagesize=A4,invariant=1);class_stub.page=len(d);page_frame(c,class_stub);plain(c,'Sefer notları',18*mm,268*mm,WIDTH,22,'Title')
  for y in range(45,249,12):rule(c,18*mm,y*mm,WIDTH)
  c.showPage();c.save();n.show_pdf_page(n.rect,fitz.open(notes),0)
 d.set_metadata({'title':'FOULWAKE — Kural Kitabı','author':'FOULWAKE','subject':'1721 · Port Avanta · Santa Veda · Kraliçe Tesella · Malum'})
 d.xref_set_key(d.pdf_catalog(),'ViewerPreferences','<</PrintScaling /None /Duplex /DuplexFlipLongEdge>>')
 target=O/'pdf/FOULWAKE_KURAL_KITABI_A4_v2.7.pdf';d.save(target,garbage=4,deflate=True);count=len(d);d.close();shutil.copy2(target,ART/target.name)
 (Q/'book_manifest.json').write_text(json.dumps({'pages':count,'source':str((P/'FOULWAKE_KURAL_KITABI_v2.7.md').relative_to(R)),'source_sha256':hashlib.sha256((P/'FOULWAKE_KURAL_KITABI_v2.7.md').read_bytes()).hexdigest(),'units':UNITS,'chapters':doc.chapters[-18:],'diagrams':DIAGRAMS,'cover_text':'FOULWAKE','cover_art_width_mm':88,'cover_art_ppi':1054/(88/25.4),'font_family':'Alegreya','body_pt':11.2,'table_pt_min':9.8,'inner_margin_mm':22,'outer_margin_mm':18,'sha256':hashlib.sha256(target.read_bytes()).hexdigest(),'status':'BUILT / AWAITING_REVIEW'},ensure_ascii=False,indent=2)+'\n')
 print({'book_pages':count,'bytes':target.stat().st_size})
if __name__=='__main__':build()
