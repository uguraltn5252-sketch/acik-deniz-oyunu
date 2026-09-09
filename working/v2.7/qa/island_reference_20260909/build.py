"""Replace one shared back in an already verified A4 duplex print package.

No image editing: the original generated PNG is embedded unchanged in a native
76 mm PDF master, including 3 mm bleed. All unchanged pages are copied natively.
"""
from pathlib import Path
import json,hashlib,sys,shutil
import fitz
from reportlab.pdfgen import canvas
R=Path(__file__).resolve().parents[4];P=R/'working/v2.7';Q=Path(__file__).parent
sys.path.insert(0,str(P/'qa/print_preparation_20260909'))
import common as base
from impose import marks
mm=base.mm;A4=base.A4
OUT=P/'print_island_20260909';PDF=OUT/'pdf';ART=R.parent/'artifacts/island_reference_20260909';TMP=R.parent/'tmp/island_reference_20260909'
for p in [PDF,ART,TMP]:p.mkdir(parents=True,exist_ok=True)
OLD=R.parent/'artifacts/print_20260909/FOULWAKE_KARTLAR_A4_CIFT_TARAFLI_v2.7.pdf'
NAME='FOULWAKE_KARTLAR_A4_CIFT_TARAFLI_v2.7.pdf'
def digest(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def dump(p,d):Path(p).write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
def build():
    assert digest(OLD)=='9116e7995623e0f16bae97fbeb18a025e69f04eaa43746d13dbd759b820eac9a'
    image=OUT/'assets/BACK_ISLAND.png';master=fitz.open();p=master.new_page(width=76*mm,height=76*mm);p.insert_image(p.rect,filename=str(image));base.save_pdf(master,PDF/'BACK_ISLAND.pdf',False)
    m=json.loads((P/'qa/print_preparation_20260909/imposition_manifest.json').read_text());places=[p for p in m['placements'] if p['side']=='back' and p['back']=='BACK_ISLAND']
    assert len(places)==6 and {p['page'] for p in places}=={43} and {p['id'] for p in places}=={f'HAR-AA-{i:02d}' for i in range(1,7)}
    bg=TMP/'page44_background.pdf';c=canvas.Canvas(str(bg),pagesize=A4,invariant=1,pageCompression=1);c.setFillColor(base.INK);c.setFont('Body',7)
    c.drawString(12*mm,12*mm,'FOULWAKE | Yaprak 22 | ARKA');c.drawRightString(198*mm,12*mm,'A4 | %100 | Uzun kenar | v2.7 / 09.09.2026')
    for j in places:
        b=fitz.Rect(j['bbox']);marks(c,b.x0,A4[1]-b.y1,b.width,b.height)
    c.showPage();c.save()
    back=fitz.open(bg);master=fitz.open(PDF/'BACK_ISLAND.pdf')
    for j in places:back[0].show_pdf_page(fitz.Rect(j['bbox'])+(-3*mm,-3*mm,3*mm,3*mm),master,0,rotate=j['rotation'])
    base.save_pdf(back,TMP/'page44.pdf');back=fitz.open(TMP/'page44.pdf')
    d=fitz.open(OLD);assert len(d)==46;d.delete_page(43);d.insert_pdf(back,start_at=43);base.save_pdf(d,ART/NAME)
    with fitz.open(ART/NAME)as deck:
        pair=fitz.open();pair.insert_pdf(deck,from_page=42,to_page=43);base.save_pdf(pair,PDF/'KARTLAR_A4_22.pdf')
    shutil.copy2(PDF/'KARTLAR_A4_22.pdf',ART/'FOULWAKE_ADA_YAPRAK_22_A4_ON_ARKA.pdf')
    dump(Q/'build_manifest.json',{'task_id':'FOULWAKE-ISLAND-REFERENCE-001','baseline_head':'368f94f4132fdc43467854d186d49a6cc1726980','activation_commit':'5d4c3ced364cfa3c05a276f30ab4957bcc7d68d4','baseline_pdf_sha256':digest(OLD),'updated_pdf':{'name':NAME,'bytes':(ART/NAME).stat().st_size,'sha256':digest(ART/NAME),'pages':46},'replacement_sheet':{'file':'FOULWAKE_ADA_YAPRAK_22_A4_ON_ARKA.pdf','original_pages':[43,44],'pages':2,'sha256':digest(PDF/'KARTLAR_A4_22.pdf')},'image_sha256':digest(image),'master_sha256':digest(PDF/'BACK_ISLAND.pdf'),'placement_source':'working/v2.7/qa/print_preparation_20260909/imposition_manifest.json','changed_page_one_based':44,'placements':places,'native_trim_mm':[70,70],'master_mm':[76,76],'bleed_mm':3,'a4_mm':[210,297],'duplex':'LONG_EDGE','scale':1,'orientation':'ONE_UPRIGHT_ORIGINAL_SCENE','image_transformations':'NONE / ORIGINAL_PNG_EMBEDDED_UNCHANGED','retained_page_count':45})
    print(json.dumps({'full_pdf':str(ART/NAME),'replacement_sheet':str(ART/'FOULWAKE_ADA_YAPRAK_22_A4_ON_ARKA.pdf')},ensure_ascii=False),flush=True)
if __name__=='__main__':build()
