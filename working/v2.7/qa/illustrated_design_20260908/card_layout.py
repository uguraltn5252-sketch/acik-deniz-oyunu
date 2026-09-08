"""Full-card illustrated plates with exact native Turkish type.

The source artwork is never cropped into a picture box. Text geometry is
measured before generation; completed cards are the review unit.
"""
from pathlib import Path
from html import escape
import json,re,math,hashlib
from io import BytesIO
from functools import lru_cache
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from PIL import Image

R=Path(__file__).resolve().parents[4]
P=R/'working/v2.7'
QA=Path(__file__).resolve().parent
OUT=P/'visual/illustrated_design_20260908'
ASSETS=OUT/'assets'
fontroot=Path('/opt/codex/runtimes/codex-primary-runtime/dependencies/native/libreoffice-headless/libreoffice/share/fonts/truetype')
for name,suffix in [('FWBody','Regular'),('FWBold','Bold'),('FWItalic','Italic'),('FWBoldItalic','BoldItalic')]:
    pdfmetrics.registerFont(TTFont(name,str(fontroot/f'LiberationSerif-{suffix}.ttf')))
pdfmetrics.registerFontFamily('FWBody',normal='FWBody',bold='FWBold',italic='FWItalic',boldItalic='FWBoldItalic')
INK=colors.HexColor('#201A14')
PAPER=colors.HexColor('#D9BB87')
records=[]
source=json.loads((P/'FOULWAKE_CARD_TEXTS_v2.7.json').read_text())
for group in ['characters','powers','provisions','loyalties','maps','utilities']:
    records.extend({**r,'collection':group} for r in source[group])
records.extend({**r,'collection':'override'} for r in json.loads((P/'FOULWAKE_OWNER_CARD_TEXT_OVERRIDES_v2.7.json').read_text())['records'])
INDEX={r['id']:r for r in records}
oldbriefs=json.loads((P/'visual/art_direction/FOULWAKE_121_ART_BRIEF_MANIFEST_v2.7.json').read_text())
BACK_ID={r['card_identity']['id']:r['card_identity']['back_binary'] for r in oldbriefs['records']}

def dimensions(r):
    if r['collection']=='maps':return 70*mm,70*mm
    if r['collection'] in ('characters','utilities','override'):return 70*mm,120*mm
    return 63.5*mm,88.9*mm

def metadata(r):
    k=r['collection']
    if k=='characters':
        role=r.get('role','').strip()
        return role if role not in ('','-','—') else 'KARAKTER'
    if k=='powers':return f"{r['group']} · {r['time']}"
    if k=='provisions':return 'Başlangıçta aç · Gerçek Güç değildir'
    if k=='loyalties':return ''  # Side is already the large native title.
    if k=='maps':return f"{r['category']} · {r['family']}"
    if k=='override':return r['section_label']
    if k=='utilities':return r.get('place','Seferin eşiği')
    return 'Seferin eşiği'

def rich(t):
    t=escape(str(t)).replace('\n','<br/>')
    t=re.sub(r'`([^`]+)`',r'\1',t)
    t=re.sub(r'\*\*([^*]+)\*\*',r'<b>\1</b>',t)
    return t

def para(t,size=9.2,font='FWBody',leading=None,align=1):
    return Paragraph(rich(t),ParagraphStyle('card',fontName=font,fontSize=size,leading=leading or size*1.15,textColor=INK,alignment=align,splitLongWords=False))

def measure(r):
    w,h=dimensions(r);cw=w-(9 if r['collection']=='maps' else 10)*mm
    body=9.2 if r['collection']!='maps' else 9.0
    flavor=8.8 if r['collection']!='maps' else 8.6
    _,eh=para(r['effect'],body).wrap(cw,10000)
    _,fh=para(r['flavor'],flavor,'FWItalic').wrap(cw,10000)
    _,mh=para(metadata(r),7.2,'FWBold').wrap(cw,10000)
    padding=11.1 if r['collection']=='maps' else (12.1 if mh else 10.9)
    need=eh+fh+mh+padding*mm
    minimum=.29*h if h>110*mm else .35*h
    bottom=math.ceil(max(need,minimum)/h*100)
    top=14 if h>110*mm else 18
    return {'id':r['id'],'trim_mm':[w/mm,h/mm],'body_pt':body,'flavor_pt':flavor,'effect_mm':round(eh/mm,2),'flavor_mm':round(fh/mm,2),'meta_mm':round(mh/mm,2),'minimum_copy_mm':round(need/mm,2),'copy_panel_percent':bottom,'title_bottom_percent':top,'art_band_percent':100-bottom-top}

@lru_cache(maxsize=12)
def print_image(path):
    # Delivery encoding only, with no change to dimensions, crop or illustration.
    # The lossless generated PNG is retained beside every final card.
    stream=BytesIO()
    with Image.open(path) as im:
        im.convert('RGB').save(stream,'JPEG',quality=93,subsampling=0,optimize=True)
    stream.seek(0)
    return ImageReader(stream)

def tr_upper(s):return s.replace('i','İ').replace('ı','I').upper()

def ornament(c,cx,y,width):
    c.saveState();c.setStrokeColor(INK);c.setLineWidth(.45)
    gap=1.6*mm;c.line(cx-width/2,y,cx-gap,y);c.line(cx+gap,y,cx+width/2,y)
    p=c.beginPath();p.moveTo(cx,y+1.0*mm);p.lineTo(cx+gap*.65,y);p.lineTo(cx,y-1.0*mm);p.lineTo(cx-gap*.65,y);p.close()
    c.drawPath(p,fill=0,stroke=1);c.restoreState()

def draw_front(c,r,x,y,scale=1,annotation=None,bleed=True):
    w,h=dimensions(r);g=measure(r);a=annotation or {}
    source=ASSETS/(r['id']+'.png')
    if not source.exists():raise ValueError('Missing original full-card plate: '+r['id'])
    # Cartouche boundary is recorded after visual inspection, never inferred as PASS.
    panel=a.get('panel_top_from_top',1-(g['copy_panel_percent']+5)/100)
    title_top=a.get('title_top_from_top',.045)
    title_bottom=a.get('title_bottom_from_top',.14 if h>110*mm else .18)
    c.saveState();c.translate(x,y);c.scale(scale,scale)
    if bleed:
        c.setFillColor(PAPER);c.rect(-3*mm,-3*mm,w+6*mm,h+6*mm,fill=1,stroke=0)
    # Full image visible. No source_rect, mask crop, inset artwork box or fallback.
    c.drawImage(print_image(str(source)),0,0,w,h,mask='auto')
    title=r.get('name',r.get('title'))
    title_width=w*a.get('title_width_fraction',.66 if h<100*mm and r['collection']!='maps' else .72);available=(title_bottom-title_top)*h-1.5*mm
    title_hscale=a.get('title_horizontal_scale',1.0)
    paragraph_width=title_width/title_hscale
    ts=24 if r['id']=='SET-KP-01' else 17 if h>110*mm else 13.6
    minimum=12.0 if h>110*mm else 10.0
    while True:
        tp=para(title,ts,'FWBold',ts*1.04)
        _,th=tp.wrap(paragraph_width,10000)
        longest=max(pdfmetrics.stringWidth(word,'FWBold',ts) for word in title.split())
        if th<=available and longest<=paragraph_width:break
        ts-=.2
        if ts<minimum:raise ValueError(('Title does not fit ribbon',r['id'],th,available))
    ty=h*(1-title_top)-(available-th)/2-.75*mm
    c.saveState();c.translate((w-title_width)/2,0);c.scale(title_hscale,1)
    tp.drawOn(c,0,ty-th);c.restoreState()
    is_map=r['collection']=='maps'
    left=(4.5 if is_map else 5)*mm;cw=w-2*left
    mp=para(metadata(r),7.2,'FWBold');_,mh=mp.wrap(cw,10000)
    body_size=g['body_pt'];flavor_size=g['flavor_pt']
    def copy_paragraphs(bs,fs):
        ep=para(r['effect'],bs,align=0 if len(r['effect'])>160 else 1);_,eh=ep.wrap(cw,10000)
        fp=para(r['flavor'],fs,'FWItalic',align=0 if len(r['flavor'])>170 else 1);_,fh=fp.wrap(cw,10000)
        return ep,eh,fp,fh
    ep,eh,fp,fh=copy_paragraphs(body_size,flavor_size)
    panel_top=h*(1-panel)
    pad_top=(1.4 if is_map else 1.8)*mm
    meta_gap=(1.0 if is_map else 1.2)*mm if mh else 0
    separator_gap=(2.0 if is_map else 2.4)*mm
    padding=pad_top+meta_gap+separator_gap+6.7*mm
    required=mh+eh+fh+padding
    if required>panel_top:
        raise ValueError(('Copy panel too small; revise art, never shrink copy',r['id'],required/mm,panel_top/mm))
    # Spare room improves reading size; the measured minimum is never reduced.
    for step in range(1,11):
        bs=g['body_pt']+step*.2;fs=g['flavor_pt']+step*.16
        ep2,eh2,fp2,fh2=copy_paragraphs(bs,fs)
        if mh+eh2+fh2+14.0*mm>panel_top:break
        body_size,flavor_size=bs,fs;ep,eh,fp,fh=ep2,eh2,fp2,fh2
    required=mh+eh+fh+padding
    slack=panel_top-required
    top=panel_top-pad_top-slack*.30
    mp.drawOn(c,left,top-mh);top-=mh+meta_gap
    ep.drawOn(c,left,top-eh);top-=eh
    ornament(c,w/2,top-separator_gap/2,cw*.60)
    top-=separator_gap
    fp.drawOn(c,left,top-fh)
    if top-fh<6.7*mm:raise ValueError(('Unsafe lower copy',r['id']))
    c.setFillColor(INK);c.setFont('FWBody',6.5)
    footer=r['id']
    if r['collection']=='powers' and r.get('returns_to_power_deck') is False:footer+=' · Kullanım sonrası oyun dışı'
    c.drawCentredString(w/2,4.5*mm,footer)
    c.restoreState()
    return {'id':r['id'],'source':str(source.relative_to(R)),**g,'body_pt':round(body_size,2),'flavor_pt':round(flavor_size,2),'actual_panel_mm':round(panel_top/mm,2),'title_pt':round(ts,2),'native_exact_copy':{k:r[k] for k in ['name','title','effect','flavor'] if k in r},'back':BACK_ID[r['id']]}

def sample(ids,annotations):
    dest=OUT/'pdf';dest.mkdir(exist_ok=True)
    p=dest/'DESIGN_INTERNAL_CHECK.pdf'
    c=canvas.Canvas(str(p),pagesize=(210*mm,297*mm),invariant=1,pageCompression=1)
    for identity in ids:
        r=INDEX[identity];w,h=dimensions(r);s=min(160*mm/w,245*mm/h)
        draw_front(c,r,(210*mm-w*s)/2,(297*mm-h*s)/2,s,annotations[identity],bleed=False);c.showPage()
    c.save();return p

if __name__=='__main__':
    g=[measure(r) for r in records]
    (QA/'copy_geometry.json').write_text(json.dumps(g,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(sorted(g,key=lambda x:x['art_band_percent'])[:10],ensure_ascii=False,indent=2))
