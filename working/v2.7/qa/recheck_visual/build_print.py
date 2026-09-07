"""Canonical UTF-8 -> vector type / image placement -> reproducible working PDFs.

Illustrations are generated assets, not programmatic substitutes. PDF clipping
and half-turn placement implement print geometry without repainting source art.
"""
from pathlib import Path
from collections import Counter
from html import escape
import hashlib,json,re,math
from functools import lru_cache
from io import BytesIO
from PIL import Image as RasterImage
from reportlab import rl_config
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (SimpleDocTemplate,Paragraph,Spacer,PageBreak,
    LongTable,TableStyle,Image,Flowable,CondPageBreak,KeepTogether)
from reportlab.platypus.tableofcontents import TableOfContents
from reportlab.lib.utils import ImageReader

rl_config.invariant=1
rl_config.useA85=0  # Binary PDF streams avoid a redundant 25% transport expansion.
ROOT=Path(__file__).resolve().parents[4]
P=ROOT/'working/v2.7'
OUT=P/'visual/recheck_20260907'
ASSETS=OUT/'assets'
PDF=OUT/'pdf'
QA=P/'qa/recheck_visual'
PDF.mkdir(parents=True,exist_ok=True)
INK=colors.HexColor('#192C37');PAPER=colors.HexColor('#F2E6CD')
RUST=colors.HexColor('#925132');MUTED=colors.HexColor('#5A6261')
LINE=colors.HexColor('#BCB29D');WHITE=colors.HexColor('#FCF9F1')
for name,file in [('Body','DejaVuSans.ttf'),('Strong','DejaVuSans-Bold.ttf'),
                  ('Book','DejaVuSerif.ttf'),('Title','DejaVuSerif-Bold.ttf'),
                  ('Flavor','DejaVuSerif-Italic.ttf')]:
    font_path=Path('/usr/share/fonts/truetype/dejavu')/file
    if not font_path.exists():
        from matplotlib import get_data_path
        font_path=Path(get_data_path())/'fonts/ttf'/file
    pdfmetrics.registerFont(TTFont(name,str(font_path)))
pdfmetrics.registerFontFamily('Body',normal='Body',bold='Strong',italic='Body',boldItalic='Strong')
pdfmetrics.registerFontFamily('Book',normal='Book',bold='Title',italic='Flavor',boldItalic='Title')

cards=json.loads((P/'FOULWAKE_CARD_TEXTS_v2.7.json').read_text())
records=[]
for group in ['characters','powers','provisions','loyalties','maps','utilities']:
    for r in cards[group]:records.append({**r,'collection':group})
records += [{**r,'collection':'override'} for r in json.loads((P/'FOULWAKE_OWNER_CARD_TEXT_OVERRIDES_v2.7.json').read_text())['records']]
INDEX={r['id']:r for r in records}
BRIEFS=json.loads((P/'visual/art_direction/FOULWAKE_121_ART_BRIEF_MANIFEST_v2.7.json').read_text())
BRIEF={r['card_identity']['id']:r for r in BRIEFS['records']}
PILOTS=[r['card_identity']['id']for r in BRIEFS['records']if r['card_identity']['pilot_selected']]
BACKS=['BACK_CHARACTER','BACK_POWER','BACK_LOYALTY','BACK_SEA_ROCK','BACK_ISLAND','BACK_LIGHTHOUSE','BACK_SUPPORT']
CAPTAIN=P/'visual/references/FOULWAKE_KAPTAN_ART_LANGUAGE_REFERENCE_v2.7.jpg'
PLACEMENTS=[];PAGE_RECORDS=[]


def clean(s):
    return str(s)


def rich(s):
    s=escape(clean(s))
    s=re.sub(r'`([^`]+)`',r'\1',s)
    s=re.sub(r'\*\*([^*]+)\*\*',r'<b>\1</b>',s)
    s=re.sub(r'(?<!\*)\*([^*]+)\*(?!\*)',r'<i>\1</i>',s)
    return s


def para(text,size=10,font='Body',leading=None,color=INK,after=0,**kw):
    return Paragraph(rich(text),ParagraphStyle('p',fontName=font,fontSize=size,
        leading=leading or size*1.32,textColor=color,spaceAfter=after,**kw))


def boxtext(c,text,x,y,w,size=10,font='Body',color=INK,leading=None):
    q=para(text,size,font,leading,color);_,h=q.wrap(w,10000);q.drawOn(c,x,y-h);return h


@lru_cache(maxsize=24)
def print_image(path):
    # PDF delivery encoding only: keep the original PNG unchanged and retain
    # every source pixel. No resize, repaint, colour grading or art alteration.
    if str(path).lower().endswith('.jpg'):return ImageReader(str(path))
    stream=BytesIO()
    with RasterImage.open(path) as source:
        source.convert('RGB').save(stream,format='JPEG',quality=80,subsampling=0,optimize=True)
    stream.seek(0)
    return ImageReader(stream)


def fitted_image(c,path,x,y,w,h,contain=True,source_rect=None):
    im=print_image(str(path));iw,ih=im.getSize()
    if source_rect:
        sx,sy,ex,ey=source_rect;sw,sh=ex-sx,ey-sy
        scale=min(w/sw,h/sh);dx=x+(w-sw*scale)/2;dy=y+(h-sh*scale)/2
        c.saveState();clip=c.beginPath();clip.rect(dx,dy,sw*scale,sh*scale);c.clipPath(clip,stroke=0)
        c.drawImage(im,dx-sx*scale,dy-(ih-ey)*scale,iw*scale,ih*scale,mask='auto');c.restoreState()
        return min(iw/(iw*scale/72),ih/(ih*scale/72))
    scale=(min if contain else max)(w/iw,h/ih)
    c.saveState();clip=c.beginPath();clip.rect(x,y,w,h);c.clipPath(clip,stroke=0)
    c.drawImage(im,x+(w-iw*scale)/2,y+(h-ih*scale)/2,iw*scale,ih*scale,mask='auto');c.restoreState()
    return 72/scale


def dimensions(r):
    if r['collection']=='maps':return 70*mm,70*mm
    if r['collection']in ('characters','utilities','override'):return 70*mm,120*mm
    return 63.5*mm,88.9*mm


def back_id(r):return BRIEF[r['id']]['card_identity']['back_binary']


def metadata(r):
    k=r['collection']
    if k=='characters':return f"{r['role']} · Etki {r['impact']} · {r['use_mode']}"
    if k=='powers':return f"{r['group']} · {r['time']}"
    if k=='provisions':return 'Başlangıçta aç · Gerçek Güç değildir'
    if k=='loyalties':return f"{r['side']} · Sadakat · Gizli tut"
    if k=='maps':return f"{r['category']} · {r['family']}"
    if k=='override':return r['section_label']
    return 'Seferin eşiği'


def front(c,r,x,y,scale=1,record=True):
    w,h=dimensions(r);c.saveState();c.translate(x,y);c.scale(scale,scale)
    c.setFillColor(PAPER);c.rect(-3*mm,-3*mm,w+6*mm,h+6*mm,fill=1,stroke=0)
    c.setStrokeColor(INK);c.setLineWidth(.7);c.roundRect(1*mm,1*mm,w-2*mm,h-2*mm,2*mm,fill=0)
    left=4.5*mm;cw=w-9*mm;top=h-4.5*mm
    title_size=14 if h>110*mm else 11.2
    title=r.get('name',r.get('title'))
    th=boxtext(c,title,left,top,cw,title_size,'Title');top-=th+1.5*mm
    mh=boxtext(c,metadata(r),left,top,cw,7.6,'Strong',MUTED);top-=mh+2.5*mm
    effect=para(r['effect'],8.6,'Body',11.1)
    flavor=para(r['flavor'],8,'Flavor',10.2,color=MUTED)
    _,eh=effect.wrap(cw,10000);_,fh=flavor.wrap(cw,10000)
    text_bottom=9*mm
    copy_top=text_bottom+eh+fh+3.5*mm
    art_h=top-copy_top-3.5*mm
    art=ASSETS/(r['id']+'.png')
    is_illustrated=art.exists()or r['id']=='SET-KP-01'
    dpi=None
    if is_illustrated:
        if art_h<9*mm:raise ValueError(('Artwork has no readable room',r['id'],art_h/mm))
        if r['id']=='SET-KP-01':dpi=fitted_image(c,CAPTAIN,left,copy_top+3.5*mm,cw,art_h,source_rect=(22,180,874,1093))
        else:dpi=fitted_image(c,art,left,copy_top+3.5*mm,cw,art_h)
    else:
        # A legible text prototype, not a fake illustration or reused picture.
        copy_top=min(top-5*mm,copy_top+max(0,art_h)*.55)
        c.setStrokeColor(LINE);c.setLineWidth(.45);c.line(left,top-1*mm,w-left,top-1*mm)
    if copy_top>top+1e-6:raise ValueError(('Copy overflow',r['id']))
    effect.drawOn(c,left,copy_top-eh)
    rule_y=copy_top-eh-1.7*mm
    c.setStrokeColor(LINE);c.setLineWidth(.4);c.line(left,rule_y,w-left,rule_y)
    flavor.drawOn(c,left,rule_y-1.8*mm-fh)
    c.setFont('Body',6.6);c.setFillColor(MUTED);c.drawString(left,4.5*mm,r['id'])
    if r['collection']=='powers' and r.get('returns_to_power_deck') is False:
        c.drawRightString(w-left,4.5*mm,'Kullanım sonrası oyun dışı')
    c.restoreState()
    if record:PLACEMENTS.append({'id':r['id'],'trim_mm':[w/mm,h/mm],'bleed_mm':3,'safe_mm':4.5,
        'effect_pt':8.6,'flavor_pt':8,'illustration':is_illustrated,'effective_art_dpi':round(dpi,2)if dpi else None,
        'copy_sha256':hashlib.sha256(json.dumps({k:r.get(k)for k in ['name','title','effect','flavor']},ensure_ascii=False,sort_keys=True).encode()).hexdigest(),
        'exact_fields':{k:r[k]for k in ['name','title','role','group','time','side','category','family','section_label','effect','flavor']if k in r},
        'back':back_id(r)})


def back(c,bid,x,y,w,h,bleed=True):
    pad=3*mm if bleed else 0
    x-=pad;y-=pad;w+=pad*2;h+=pad*2
    path=ASSETS/(bid+'.png')
    if not path.exists():raise FileNotFoundError(path)
    c.saveState();c.translate(x,y)
    # One generated upper half is placed twice at exact half-turn: PDF geometry,
    # not a second image variant or independent family texture.
    for rot in (0,180):
        c.saveState()
        if rot:c.translate(w,h);c.rotate(180)
        clip=c.beginPath();clip.rect(0,h/2,w,h/2);c.clipPath(clip,stroke=0)
        if bid=='BACK_LIGHTHOUSE':
            # Align the roof hub to the half-turn axis; original PNG intact.
            fitted_image(c,path,0,0,w,h,source_rect=(0,24,1254,1278))
        else:fitted_image(c,path,0,0,w,h,contain=False)
        c.restoreState()
    c.restoreState()


def crop_marks(c,x,y,w,h):
    c.setStrokeColor(MUTED);c.setLineWidth(.3)
    for xx in (x,x+w):
        for yy,dy in ((y,-1),(y+h,1)):c.line(xx,yy+3.5*mm*dy,xx,yy+5.5*mm*dy)
    for yy in (y,y+h):
        for xx,dx in ((x,-1),(x+w,1)):c.line(xx+3.5*mm*dx,yy,xx+5.5*mm*dx,yy)


def page_frame(c,number,title='FOULWAKE / KURU PAY'):
    W,H=A4;c.setFillColor(INK);c.setFont('Strong',8);c.drawString(18*mm,H-13*mm,title)
    c.setStrokeColor(LINE);c.setLineWidth(.5);c.line(18*mm,H-17*mm,W-18*mm,H-17*mm)
    c.setFont('Body',7.6);c.setFillColor(MUTED);c.drawString(18*mm,11*mm,'v2.7 · Çalışma sürümü');c.drawRightString(W-18*mm,11*mm,str(number))


def cover(c,title,subtitle):
    W,H=A4;c.setFillColor(INK);c.rect(0,0,W,H,fill=1,stroke=0)
    c.setFillColor(PAPER);c.setFont('Title',35);c.drawString(18*mm,H-32*mm,'FOULWAKE')
    c.setFont('Book',19);c.drawString(18*mm,H-44*mm,'KURU PAY')
    path=ASSETS/'GUC-27.png'
    if path.exists():fitted_image(c,path,0,69*mm,W,153*mm,contain=False)
    boxtext(c,title,18*mm,54*mm,W-36*mm,21,'Title',PAPER)
    boxtext(c,subtitle,18*mm,31*mm,W-36*mm,10,'Body',PAPER)


def build_cards():
    path=PDF/'FOULWAKE_121_KART_CALISMA_v2.7.pdf'
    c=canvas.Canvas(str(path),pagesize=A4,invariant=1,pageCompression=1)
    c.setTitle('FOULWAKE - 121 Kart Çalışma Prototipi');c.setAuthor('FOULWAKE / CHIEF_EDITOR')
    cover(c,'121 kart · Baskı prototipi','12 resimli pilot; kalan ön yüzler güncel metin prototipidir.\nA4 · %100 ölçek · uzun kenardan çift taraflı baskı');c.showPage()
    page_frame(c,2,'BASKIDAN ÖNCE')
    text='''Bu dosya oyunun bütün 121 kartını içerir. On iki kartın resmi vardır; diğer kartlar okunabilir metin prototipidir. Yeni arka yüzler bütün ailelere uygulanmıştır.\n\nYazdırma: A4, gerçek boyut / %100; sayfaya sığdır kapalı. İlk iki sayfa kullanım notudur. Kart yaprakları 3. sayfadan başlar; tek sayılı önün arkasına onu izleyen çift sayılı arka gelir. Uzun kenardan çevirme için arka sütunlar aynalanmıştır.\n\nÖnce yalnız 3-4. sayfalarla bir çift taraflı deneme yapın. Kesmeden önce kenar hizasını ışığa tutarak kontrol edin. Ortak arka yüzün çalışması için opak karton veya aynı opak kılıf gerekir.\n\nKesim çizgileri arasından kesin; renkli taşma alanını kart boyuna katmayın. Karakter ve yardımcılar 70×120 mm; Güç/Erzak ve Sadakat 63,5×88,9 mm; Harita 70×70 mm.\n\nArka yüzlerde yazı bulunmaz. Kimlik, aile adı ve sayfa bilgileri yalnız kesim dışında veya ön yüzde bulunur. Her aile kendi tek masterını kullanır; Tayfa/Hain ve Deniz/Kayalık için ayrı ton üretilmemiştir.\n\nFiziksel çift taraflı baskı, ışıkta opaklık ve insan masası denemesi henüz yapılmadı. Bu dosya üretim matbaası kabulü veya release değildir.'''
    y=263*mm
    for t in text.split('\n\n'):y-=boxtext(c,t,20*mm,y,170*mm,11)+6*mm
    c.setStrokeColor(INK);c.setLineWidth(.8);c.line(20*mm,38*mm,120*mm,38*mm)
    boxtext(c,'Ölçek kontrolü: bu çizgi 100 mm olmalı.',20*mm,34*mm,170*mm,9)
    c.showPage();number=3
    groups=[([r for r in records if dimensions(r)[1]==120*mm],2,2),
            ([r for r in records if r['collection']in ('powers','provisions','loyalties')],2,3),
            ([r for r in records if r['collection']=='maps'],2,3)]
    for rs,ncol,nrow in groups:
        w,h=dimensions(rs[0]);gap_y=9*mm if h<100*mm and h>80*mm else 12*mm;pitchw=w+12*mm;pitchh=h+gap_y
        startx=(A4[0]-(ncol*w+(ncol-1)*12*mm))/2
        starty=(A4[1]-(nrow*h+(nrow-1)*gap_y))/2
        for start in range(0,len(rs),ncol*nrow):
            batch=rs[start:start+ncol*nrow]
            for side in ('front','back'):
                c.saveState();c.translate(10*mm,135*mm);c.rotate(90)
                c.setFont('Body',7);c.setFillColor(MUTED);c.drawString(0,0,f'FOULWAKE · {"ÖN" if side=="front" else "ARKA"} · {number}');c.restoreState()
                for i,r in enumerate(batch):
                    col=i%ncol;row=i//ncol
                    x=startx+col*pitchw;y=starty+(nrow-1-row)*pitchh
                    if side=='back':x=A4[0]-x-w;back(c,back_id(r),x,y,w,h)
                    else:
                        front(c,r,x,y);PAGE_RECORDS.append({'id':r['id'],'page_1based':number,'bbox_pt':[x,A4[1]-y-h,x+w,A4[1]-y]})
                    crop_marks(c,x,y,w,h)
                c.showPage();number+=1
    c.save();assert number-1==48,number-1
    return path


class Horizon(Flowable):
    def __init__(self):super().__init__();self.width=160*mm;self.height=52*mm
    def draw(self):
        c=self.canv;sz=12*mm;x=44*mm
        for row in range(3):
            for col in range(5):
                xx=x+col*sz;yy=(2-row)*sz
                active=(row<2 and col in (1,2,3))or(row==2 and col==2)
                c.setFillColor(PAPER if active else WHITE);c.setStrokeColor(LINE);c.rect(xx,yy,sz-1*mm,sz-1*mm,fill=1,stroke=1)
                if row==2 and col==2:
                    c.setFillColor(INK);p=c.beginPath();p.moveTo(xx+3*mm,yy+3*mm);p.lineTo(xx+9*mm,yy+3*mm);p.lineTo(xx+6*mm,yy+9*mm);p.close();c.drawPath(p,fill=1,stroke=0)
        for label,yy in [('UZAK UFUK',29*mm),('YAKIN UFUK',17*mm),('GEMİ',5*mm)]:boxtext(c,label,0,yy+4*mm,42*mm,8,'Strong')
        boxtext(c,'Örnek: gemi ortadayken üç sütun. Sınır ve yasal rota koşulları ayrıca uygulanır.',0,48*mm,160*mm,9)


class BookDoc(SimpleDocTemplate):
    def afterFlowable(self,flowable):
        if hasattr(flowable,'toc_title'):
            key='s'+str(flowable.toc_number);self.canv.bookmarkPage(key)
            self.canv.addOutlineEntry(flowable.toc_title,key,0,False)
            self.notify('TOCEntry',(0,flowable.toc_title,self.page,key))


def book_page(c,doc):
    if doc.page==1:cover(c,'Kural kitabı','6-15 oyuncu ve 1 tarafsız Moderatör\nGizli sadakat · ortak gemi · birlikte seçilen rota')
    else:page_frame(c,doc.page)


def build_book():
    path=PDF/'FOULWAKE_KURAL_KITABI_v2.7.pdf'
    doc=BookDoc(str(path),pagesize=A4,leftMargin=21*mm,rightMargin=21*mm,topMargin=24*mm,bottomMargin=21*mm,title='FOULWAKE - Kuru Pay - Kural Kitabı',author='FOULWAKE / CHIEF_EDITOR')
    flow=[Spacer(1,230*mm),PageBreak(),para('Kitabı kullanırken',22,'Title',after=14)]
    flow.append(para('İlk oyunda önce hazırlık ve kurulum. Oyun sırasında günlük akış açık kalsın; nadir etkileşimlere gerektiğinde bakın. Arka planı baştan sona sesli okumak gerekmiyor.',11,after=14))
    toc=TableOfContents();toc.levelStyles=[ParagraphStyle('toc',fontName='Body',fontSize=10.2,leading=16,textColor=INK,spaceBefore=3)]
    flow.extend([toc,PageBreak()])
    lines=(P/'FOULWAKE_KURAL_KITABI_v2.7.md').read_text().splitlines();i=0;section=0
    while i<len(lines):
        line=lines[i].strip()
        if not line or line=='---' or line.startswith('# '):i+=1;continue
        if line.startswith('## '):
            section+=1;title=line[3:]
            flow.append(PageBreak()if title.startswith(('3. ','4. ','13. ','17. ','Masada')) else CondPageBreak(50*mm))
            h=para(title,18,'Title',after=12,keepWithNext=True);h.toc_title=clean(title);h.toc_number=section;flow.append(h);i+=1;continue
        if line.startswith('### '):
            if not hasattr(flow[-1],'toc_title'):flow.append(CondPageBreak(42*mm))
            flow.append(para(line[4:],13,'Strong',after=8,spaceBefore=8,keepWithNext=True))
            if line.startswith('### 6.2'):flow.append(Horizon())
            i+=1;continue
        if line.startswith('|'):
            rows=[]
            while i<len(lines)and lines[i].strip().startswith('|'):
                cells=[s.strip()for s in lines[i].strip().strip('|').split('|')]
                if not all(re.fullmatch(r'[:\- ]+',c)for c in cells):rows.append(cells)
                i+=1
            n=len(rows[0]);width=168*mm
            weights={2:[.37,.63],3:[.28,.20,.52],4:[.24,.23,.29,.24],5:[.21,.18,.20,.20,.21],6:[.12,.17,.18,.17,.18,.18]}.get(n,[1/n]*n)
            if section==13 and n==3:weights=[.31,.08,.61]
            if section in (14,15)and n==3:weights=[.29,.22,.49]
            data=[[para(t,9.2,'Strong'if r==0 else'Body',12.3,PAPER if r==0 else INK)for t in row]for r,row in enumerate(rows)]
            table=LongTable(data,colWidths=[v*width for v in weights],repeatRows=1,hAlign='LEFT')
            pad=6 if section==16 else 7
            table.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),INK),('ROWBACKGROUNDS',(0,1),(-1,-1),[WHITE,colors.HexColor('#EDE7D9')]),('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),6),('RIGHTPADDING',(0,0),(-1,-1),6),('TOPPADDING',(0,0),(-1,-1),pad),('BOTTOMPADDING',(0,0),(-1,-1),pad),('LINEBELOW',(0,0),(-1,0),.5,INK)]))
            flow.extend([table,Spacer(1,9)]);continue
        if line.startswith('- ') or re.match(r'^\d+\. ',line):
            content=line[2:]if line.startswith('- ')else line
            if line.startswith('- '):content='• '+content
            flow.append(para(content,10.7,after=6,leftIndent=8,firstLineIndent=-8));i+=1;continue
        buf=[line];i+=1
        while i<len(lines)and lines[i].strip()and not lines[i].startswith(('#','|','- ')):
            buf.append(lines[i].strip());i+=1
        text=' '.join(buf)
        if text in ('**OKU**','**YAP**')or text.startswith('**OKU -'):
            flow.append(para(text,9,'Strong',color=RUST,after=6,keepWithNext=True,spaceBefore=7))
        else:flow.append(para(text,10.8,leading=15.2,after=9))
    doc.multiBuild(flow,onFirstPage=book_page,onLaterPages=book_page)
    return path


def build_back_masters():
    for bid in BACKS:
        example=next(r for r in records if back_id(r)==bid);w,h=dimensions(example)
        c=canvas.Canvas(str(PDF/(bid+'.pdf')),pagesize=(w+6*mm,h+6*mm),invariant=1,pageCompression=1)
        c.setTitle(bid+' / FOULWAKE / textless half-turn master')
        back(c,bid,3*mm,3*mm,w,h);c.showPage();c.save()


def build_review():
    path=PDF/'FOULWAKE_GORSEL_INCELEME_v2.7.pdf';c=canvas.Canvas(str(path),pagesize=A4,invariant=1,pageCompression=1)
    c.setTitle('FOULWAKE - 12 Ön / 7 Arka Görsel İnceleme')
    cover(c,'Görsel inceleme','12 ön yüz · 7 arka yüz\nAynı operatörün çalışma pilotu; proje sahibi estetik kabulü bekleniyor.');c.showPage()
    page_frame(c,2,'12 ÖN YÜZ / DESTE RİTMİ')
    for i,cid in enumerate(PILOTS):
        r=INDEX[cid];w,h=dimensions(r);s=min(39*mm/w,72*mm/h)
        x=18*mm+(i%4)*45*mm;y=184*mm-(i//4)*77*mm
        front(c,r,x,y,s,False)
    c.showPage()
    for i,cid in enumerate(PILOTS,3):
        r=INDEX[cid];page_frame(c,i,cid+' / '+r.get('name',r.get('title')).upper())
        w,h=dimensions(r);top=261*mm
        if cid=='SET-KP-01':fitted_image(c,CAPTAIN,15*mm,106*mm,98*mm,155*mm,source_rect=(22,180,874,1093))
        else:fitted_image(c,ASSETS/(cid+'.png'),15*mm,106*mm,98*mm,155*mm)
        front(c,r,125*mm,top-h,1,False)
        boxtext(c,'Gerçek kesim ölçüsü',125*mm,top-h-7*mm,70*mm,8,'Body',MUTED)
        brief=BRIEF[cid]
        y=93*mm
        for label,text in [('Sahnenin işi',brief['visual_narrative_aim']),('Kadraj',brief['framing_viewpoint_focus_negative_space']),('İnceleme sınırı','Görsel ve yerleşim aynı operatörce incelendi. Bu sayfa bağımsız sanat kabulü veya fiziksel baskı denemesi değildir.')]:
            y-=boxtext(c,label,18*mm,y,174*mm,9,'Strong',RUST)+2*mm
            y-=boxtext(c,text,18*mm,y,174*mm,9.4)+4*mm
        c.showPage()
    page_frame(c,15,'YEDİ ORTAK ARKA YÜZ')
    counts=Counter(back_id(r)for r in records)
    for i,bid in enumerate(BACKS):
        r=next(r for r in records if back_id(r)==bid);w,h=dimensions(r)
        s=min(37*mm/w,64*mm/h);ww,hh=w*s,h*s
        x=18*mm+(i%4)*45*mm;y=181*mm-(i//4)*96*mm
        back(c,bid,x,y,ww,hh,False)
        boxtext(c,bid.replace('BACK_','')+' · '+str(counts[bid]),x,y-4*mm,39*mm,7.4,'Strong')
    boxtext(c,'Aile içi tek master. Deniz ve Kayalık 42 kartta aynı; Tayfa ve Hain 15 kartta aynı. Yazı ve aile etiketleri bu inceleme sayfasındadır, kartların arkasında bulunmaz.',18*mm,46*mm,174*mm,10)
    c.showPage();page_frame(c,16,'MASADA ORTAK DENİZ')
    for ncol,nrow,x,y,sz in [(5,5,19,138,27),(6,5,19,49,12),(5,7,113,25,12)]:
        for row in range(nrow):
            for col in range(ncol):
                bid='BACK_SEA_ROCK'
                if (row,col)in [(1,1),(3,3)]:bid='BACK_ISLAND'
                if (row,col)==(2,4):bid='BACK_LIGHTHOUSE'
                back(c,bid,(x+col*sz)*mm,(y+row*sz)*mm,sz*mm,sz*mm,False)
    boxtext(c,'5×5, 6×5 ve 5×7 yerleşim örnekleri. Ortak su dokusu; ada ve fener aileleri seçilir. Bunlar görsel komşuluk örnekleridir, gizli kurulum kontrolleri yapılmış oyun haritaları değildir.',18*mm,131*mm,174*mm,10)
    c.showPage();c.save();return path


if __name__=='__main__':
    build_back_masters();a=build_cards();b=build_book();d=build_review()
    data={'task_id':'FOULWAKE-RECHECK-VISUAL-001','status':'GENERATED / AWAITING_RENDER_INSPECTION','cards':PLACEMENTS,'card_pdf_positions':PAGE_RECORDS,'pilot_ids':PILOTS,'back_counts':dict(Counter(back_id(r)for r in records)),'files':{p.name:hashlib.sha256(p.read_bytes()).hexdigest()for p in PDF.glob('*.pdf')}}
    (QA/'render_manifest.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'cards':len(PLACEMENTS),'illustrated_fronts':sum(p['illustration']for p in PLACEMENTS),'pdfs':len(data['files'])}))
