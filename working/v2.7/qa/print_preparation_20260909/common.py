"""Native PDF prepress utilities; all distances are millimetres or PDF points."""
from pathlib import Path
from html import escape
import re,json,hashlib
import fitz
from reportlab import rl_config
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph

R=Path(__file__).resolve().parents[4]; P=R/'working/v2.7'; QA=Path(__file__).resolve().parent
OUT=P/'print_20260909'; PDF=OUT/'pdf'; ART=R.parent/'artifacts/print_20260909'; TMP=R.parent/'tmp/print_20260909'
for d in [OUT,PDF,ART,TMP]:d.mkdir(parents=True,exist_ok=True)
rl_config.invariant=1;rl_config.useA85=0
fontroot=Path('/usr/share/fonts/truetype/dejavu')
if not fontroot.exists():
    from matplotlib import get_data_path
    fontroot=Path(get_data_path())/'fonts/ttf'
for n,f in [('Body','DejaVuSans.ttf'),('Bold','DejaVuSans-Bold.ttf'),('Title','DejaVuSerif-Bold.ttf'),('Italic','DejaVuSerif-Italic.ttf')]:
    fp=fontroot/f
    if not fp.exists():
        from matplotlib import get_data_path
        fp=Path(get_data_path())/'fonts/ttf'/f
    pdfmetrics.registerFont(TTFont(n,str(fp)))
pdfmetrics.registerFontFamily('Body',normal='Body',bold='Bold',italic='Italic',boldItalic='Bold')
INK=colors.CMYKColor(0,0,0,1); NAVY=colors.HexColor('#263F49'); RUST=colors.HexColor('#805037'); PALE=colors.HexColor('#F3F1EA')
source=json.loads((P/'FOULWAKE_CARD_TEXTS_v2.7.json').read_text());records=[]
for group in ['characters','powers','provisions','loyalties','maps','utilities']:
    records += [{**x,'collection':group}for x in source[group]]
records += [{**x,'collection':'override'}for x in json.loads((P/'FOULWAKE_OWNER_CARD_TEXT_OVERRIDES_v2.7.json').read_text())['records']]
INDEX={x['id']:x for x in records}
brief=json.loads((P/'visual/art_direction/FOULWAKE_121_ART_BRIEF_MANIFEST_v2.7.json').read_text())
BACK={x['card_identity']['id']:x['card_identity']['back_binary']for x in brief['records']}
BACK_ROOT=P/'visual/illustrated_design_20260908/pdf'
def dims(r):
    if r['collection']=='maps':return 70*mm,70*mm
    if r['collection']in ('characters','utilities','override'):return 70*mm,120*mm
    return 63.5*mm,88.9*mm
def sha(p):
    with Path(p).open('rb')as f:return hashlib.file_digest(f,'sha256').hexdigest()
def dump(p,x):Path(p).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def rich(t):
    t=escape(str(t));t=re.sub(r'`([^`]+)`',r'\1',t)
    t=re.sub(r'\*\*([^*]+)\*\*',r'<b>\1</b>',t)
    return re.sub(r'(?<!\*)\*([^*]+)\*(?!\*)',r'<i>\1</i>',t)
def para(t,size=10.6,font='Body',leading=None,after=0,color=INK,**kw):
    return Paragraph(rich(t),ParagraphStyle('p',fontName=font,fontSize=size,leading=leading or size*1.4,textColor=color,spaceAfter=after,splitLongWords=False,**kw))
def text(c,t,x,y,w,size=10.6,font='Body',**kw):
    p=para(t,size,font,**kw);_,h=p.wrap(w,10000);p.drawOn(c,x,y-h);return h
def rect(x,y,w,h):return fitz.Rect(x,A4[1]-y-h,x+w,A4[1]-y)
def save_pdf(doc,path,duplex=True):
    doc.set_metadata({'title':Path(path).stem.replace('_',' '),'author':'FOULWAKE / CHIEF_EDITOR','subject':'A4 / %100 gerçek boyut / uzun kenardan çift taraflı baskı'})
    doc.xref_set_key(doc.pdf_catalog(),'ViewerPreferences','<</PrintScaling /None /Duplex /DuplexFlipLongEdge /PickTrayByPDFSize false>>'if duplex else'<</PrintScaling /None>>')
    temp=Path(path).with_suffix('.pending.pdf');n=len(doc);doc.save(temp,garbage=4,deflate=True);doc.close()
    with fitz.open(temp)as check:assert len(check)==n and not check.is_encrypted
    temp.replace(path)
