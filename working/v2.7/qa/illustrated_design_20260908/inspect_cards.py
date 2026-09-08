"""Measure candidate art dividers and render complete individual card proofs.

Pixel measurement is a layout aid, never a substitute for visual acceptance.
"""
import argparse,json,hashlib
from io import BytesIO
import numpy as np
from PIL import Image
import fitz
from reportlab.pdfgen import canvas
from card_layout import QA,OUT,ASSETS,INDEX,dimensions,draw_front

PROOFS=OUT.parents[3].parent/'artifacts/illustrated_design_20260908/inspection'

def divider(path):
    with Image.open(path)as im:
        a=np.asarray(im.convert('RGB'));h,w=a.shape[:2]
    dark=a[:,:,[0,1,2]].mean(axis=2)<72
    row=dark[:,int(w*.18):int(w*.82)].mean(axis=1)
    candidates=[]
    for y in range(int(h*.30),int(h*.83)):
        if row[y]<.38:continue
        below=dark[y+int(h*.025):y+int(h*.10),int(w*.14):int(w*.86)].mean()
        if below<.045:candidates.append(y)
    if not candidates:raise ValueError('No clear candidate copy divider: '+str(path))
    # Last strong full-width edge above a long clear paper region.
    return round((max(candidates)+1)/h,5)

def scan(ids=None):
    p=QA/'art_annotations.json';ann=json.loads(p.read_text())if p.exists()else{}
    results=[]
    paths=sorted(ASSETS.glob('*.png'))
    for source in paths:
        identity=source.stem
        if identity not in INDEX or (ids and identity not in ids):continue
        try:
            if identity not in ann:
                r=INDEX[identity];_,h=dimensions(r)
                poker=r['collection'] in ('powers','provisions','loyalties')
                ann[identity]={'panel_top_from_top':divider(source),'title_top_from_top':.040 if poker else .050,'title_bottom_from_top':.120 if poker else .125 if h>100*72/25.4 else .130,'measurement_status':'CANDIDATE_REQUIRES_COMPLETE_CARD_VIEW'}
            r=INDEX[identity];w,h=dimensions(r);stream=BytesIO()
            c=canvas.Canvas(stream,pagesize=(w,h),invariant=1,pageCompression=1)
            placement=draw_front(c,r,0,0,annotation=ann[identity],bleed=False);c.showPage();c.save()
            d=fitz.open(stream=stream.getvalue(),filetype='pdf')
            PROOFS.mkdir(parents=True,exist_ok=True)
            target=PROOFS/(identity+'.png')
            data=d[0].get_pixmap(matrix=fitz.Matrix(3.5,3.5)).tobytes('png')
            with Image.open(BytesIO(data)) as check:check.verify()
            temporary=target.with_suffix('.pending.png')
            temporary.write_bytes(data)
            assert hashlib.sha256(temporary.read_bytes()).digest()==hashlib.sha256(data).digest()
            temporary.replace(target)
            results.append({'id':identity,'geometry':'PASS','proof':str(target),'proof_sha256':hashlib.sha256(target.read_bytes()).hexdigest(),'asset_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'placement':placement,'visual_review':'PENDING'})
        except Exception as e:results.append({'id':identity,'geometry':'FAIL','error':str(e),'annotation':ann.get(identity)})
    p.write_text(json.dumps(ann,ensure_ascii=False,indent=2)+'\n')
    index_path=QA/'proof_index.json'
    combined={x['id']:x for x in json.loads(index_path.read_text())} if ids and index_path.exists() else {}
    combined.update({x['id']:x for x in results})
    index_path.write_text(json.dumps([combined[k] for k in sorted(combined)],ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'rendered':sum(x['geometry']=='PASS'for x in results),'failed':[x for x in results if x['geometry']=='FAIL'],'proof_directory':str(PROOFS)},ensure_ascii=False))

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('ids',nargs='*');a=ap.parse_args();scan(a.ids)
