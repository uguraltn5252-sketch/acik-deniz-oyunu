"""Check delivered PDF objects, extracted canonical copy and print geometry.

This is operator technical evidence, not independent visual/physical acceptance.
"""
from pathlib import Path
import hashlib,json,re,sys
from collections import Counter
import fitz
import numpy as np
from PIL import Image,ImageDraw
import build_print as b

def norm(s):
    return re.sub(r'\s+','',s.replace('\u00ad','').replace('\u200b',''))

def plain(s):
    return re.sub(r'[*`]', '', s)

def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()

def verify():
    m=json.loads((b.QA/'render_manifest.json').read_text())
    faults=[];result={'task_id':m['task_id'],'classification':'SAME_OPERATOR_TECHNICAL_SELF_CHECK','failures':faults}
    def check(ok,msg):
        if not ok:faults.append(msg)
    ids=[r['id']for r in b.records]
    check(len(ids)==121 and len(set(ids))==121,'121 canonical identities')
    check(set(ids)==set(x['id']for x in m['cards']),'manifest coverage')
    check(sum(x['illustration']for x in m['cards'])==12,'12 illustrated fronts')
    check(Counter(b.back_id(r)for r in b.records)==Counter(m['back_counts']),'back family mapping')
    doc=fitz.open(b.PDF/'FOULWAKE_121_KART_CALISMA_v2.7.pdf')
    image_families={};copy_checked=0;safe_checked=0
    for pos in m['card_pdf_positions']:
        r=b.INDEX[pos['id']];page=doc[pos['page_1based']-1];rect=fitz.Rect(pos['bbox_pt'])
        extracted=norm(page.get_text(clip=rect));exact=[r.get('name',r.get('title')),b.metadata(r),r['effect'],r['flavor'],r['id']]
        for field in exact:check(norm(plain(field))in extracted,f"PDF copy: {r['id']}: {field}")
        copy_checked+=1
        safe=fitz.Rect(rect.x0+4*b.mm,rect.y0+3.7*b.mm,rect.x1-4*b.mm,rect.y1-3.7*b.mm)
        for word in page.get_text('words',clip=rect):
            check(safe.contains(fitz.Rect(word[:4])),f"Text safe area: {r['id']}: {word[4]}")
        safe_checked+=1
        w,h=b.dimensions(r)
        check(abs(rect.width-w)<.001 and abs(rect.height-h)<.001,'Trim size '+r['id'])
        rear=doc[pos['page_1based']];rr=fitz.Rect(page.rect.width-rect.x1,rect.y0,page.rect.width-rect.x0,rect.y1)
        hits=[i for i in rear.get_image_info(hashes=True,xrefs=True)if fitz.Rect(i['bbox']).intersects(rr)]
        check(len(hits)==2,'Two matching half-turn placements '+r['id'])
        if hits:
            signatures={i['digest'].hex()for i in hits};check(len(signatures)==1,'One source image per back '+r['id'])
            image_families.setdefault(b.back_id(r),set()).update(signatures)
        check(not rear.get_text(clip=rr).strip(),'Textless back '+r['id'])
    check(all(len(v)==1 for v in image_families.values()),'One identical raster object per family')
    check(len({next(iter(v))for v in image_families.values()})==7,'Seven distinct back sources')
    result.update(cards_checked=copy_checked,safe_areas_checked=safe_checked,illustrated_fronts=12,text_only_fronts=109,back_counts=m['back_counts'],family_pdf_image_digests={k:sorted(v)for k,v in image_families.items()})
    dpis=[r['effective_art_dpi']for r in m['cards']if r['illustration']]
    check(min(dpis)>=300,'Front art at least 300 DPI');result['minimum_front_dpi']=min(dpis)
    capsha='a3224299f1b868ec71b6f637e3cb4bdd48dd5ba978178a0a64bef3e052193a2a'
    check(digest(b.CAPTAIN)==capsha,'Accepted KAPTAN source unchanged');result['captain_reference_sha256']=capsha
    book=fitz.open(b.PDF/'FOULWAKE_KURAL_KITABI_v2.7.pdf')
    lines=[]
    for page in book:
        lines.extend(x for x in page.get_text().splitlines()if x not in ['FOULWAKE / KURU PAY','v2.7 · Çalışma sürümü']and not re.fullmatch(r'\d+',x))
    booktext=norm(' '.join(lines));segments=[]
    for line in (b.P/'FOULWAKE_KURAL_KITABI_v2.7.md').read_text().splitlines():
        s=line.strip()
        if not s or s=='---'or s.startswith('# '):continue
        if s.startswith('|'):
            cells=[c.strip()for c in s.strip('|').split('|')]
            if all(re.fullmatch(r'[:\- ]+',c)for c in cells):continue
            segments.extend(plain(c)for c in cells)
        else:segments.append(plain(re.sub(r'^(?:#{2,3} |\- )','',s)))
    for seg in segments:check(norm(seg)in booktext,'Rulebook copy: '+seg)
    result['rulebook_segments_checked']=len(segments)
    result['pdfs']={};result['back_rotation_render']={}
    expected={'FOULWAKE_121_KART_CALISMA_v2.7.pdf':48,'FOULWAKE_GORSEL_INCELEME_v2.7.pdf':16,'FOULWAKE_KURAL_KITABI_v2.7.pdf':30}
    for f in sorted(b.PDF.glob('*.pdf')):
        d=fitz.open(f);check(not d.is_repaired and len(d)==expected.get(f.name,1),'Complete PDF: '+f.name)
        check(digest(f)==m['files'][f.name],'PDF hash: '+f.name)
        result['pdfs'][f.name]={'pages':len(d),'bytes':f.stat().st_size,'sha256':digest(f)}
        for page in d:
            check('\ufffd'not in page.get_text(),'Replacement glyph '+f.name)
            for font in page.get_fonts():check(font[1]in ('ttf','cff')or font[3]in ('Helvetica','Times-Roman','Courier'),'Font type '+str(font))
        if f.stem.startswith('BACK_'):
            page=d[0];example=next(r for r in b.records if b.back_id(r)==f.stem);w,h=b.dimensions(example)
            check(abs(page.rect.width-(w+6*b.mm))<.001 and abs(page.rect.height-(h+6*b.mm))<.001,'Back master dimensions '+f.name)
            check(not page.get_text().strip(),'No text in master '+f.name)
            images=page.get_image_info(hashes=True)
            check(len(images)==2 and images[0]['digest']==images[1]['digest'],'Master reuses one source '+f.name)
            if len(images)==2:
                a0,a1=[im['transform']for im in images]
                check(all(abs(a0[k]+a1[k])<.002 for k in range(4)), 'Exact half-turn image basis '+f.name)
                check(abs(a0[4]+a1[4]-page.rect.width)<.002 and abs(a0[5]+a1[5]-page.rect.height)<.002,'Half-turn about page centre '+f.name)
            # A PDF's two identical images are transformed at exactly half-turn.
            # Render through an integer-size page to avoid fractional page-edge
            # resampling being mistaken for an intentional directional mark.
            tmp=fitz.open();pp=tmp.new_page(width=1000,height=1000);pp.show_pdf_page(pp.rect,d,0,keep_proportion=False)
            px=pp.get_pixmap();a=np.frombuffer(px.samples,dtype=np.uint8).reshape(px.height,px.width,3)
            delta=np.abs(a.astype(int)-a[::-1,::-1].astype(int))
            result['back_rotation_render'][f.stem]={'test_raster':[px.width,px.height],'mean_channel_delta':round(float(delta.mean()),6),'max_channel_delta':int(delta.max()),'nonzero_channel_fraction':round(float((delta>0).mean()),6),'interpretation':'PDF geometry and shared source checked; any nonzero values are reported, never labelled pixel-exact.'}
    result['source_files']={str(p.relative_to(b.ROOT)):digest(p)for p in [b.P/'FOULWAKE_CARD_TEXTS_v2.7.json',b.P/'FOULWAKE_OWNER_CARD_TEXT_OVERRIDES_v2.7.json',b.P/'FOULWAKE_KURAL_KITABI_v2.7.md',b.P/'visual/art_direction/FOULWAKE_121_ART_BRIEF_MANIFEST_v2.7.json',Path(__file__),Path(b.__file__)]}
    result['assets']={p.name:{'sha256':digest(p),'pixels':list(Image.open(p).size)}for p in sorted(b.ASSETS.glob('*.png'))}
    result['status']='PASS'if not faults else'FAIL'
    (b.QA/'print_checks.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items()if k in ('status','cards_checked','rulebook_segments_checked','failures','minimum_front_dpi','back_rotation_render')},ensure_ascii=False,indent=2))
    return not faults

if __name__=='__main__':sys.exit(0 if verify()else 1)
