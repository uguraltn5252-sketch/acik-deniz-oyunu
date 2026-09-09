"""Targeted checks for one replaced page; baseline fronts are not reimposed."""
from build import *
import subprocess
def verify():
    m=json.loads((Q/'build_manifest.json').read_text());new=fitz.open(ART/NAME);old=fitz.open(OLD);unchanged=[]
    assert len(new)==len(old)==46
    for i in range(46):
        assert max(abs(a-b)for a,b in zip(new[i].rect,fitz.Rect(0,0,*A4)))<.001
        assert new[i].get_text()==old[i].get_text(),f'Page {i+1} text drift'
        if i==43:continue
        a=old[i].get_pixmap(dpi=96,alpha=False);b=new[i].get_pixmap(dpi=96,alpha=False)
        assert a.width==b.width and a.height==b.height and a.samples==b.samples,f'Page {i+1} rendering drift'
        unchanged.append({'page':i+1,'native_text':'IDENTICAL','rgb_96dpi_sha256':hashlib.sha256(b.samples).hexdigest()})
    print('All 45 retained pages render identically; all 46 pages retain exact text.',flush=True)
    image=fitz.Pixmap(str(OUT/'assets/BACK_ISLAND.png'));expected=hashlib.md5(image.samples).digest()
    info=new[43].get_image_info(hashes=True,xrefs=True);assert len(info)==6
    assert all(x['digest']==expected and (x['width'],x['height'])==(image.width,image.height)for x in info)
    assert len({x['xref']for x in info})==1,'The six backs must share exactly one image object'
    placements=m['placements'];baseline=json.loads((P/'qa/print_preparation_20260909/imposition_manifest.json').read_text())['placements'];witness=[]
    for j in placements:
        box=fitz.Rect(j['bbox']);extent=box+(-3*mm,-3*mm,3*mm,3*mm)
        entry=min(info,key=lambda x:sum(abs(a-b)for a,b in zip(x['bbox'],extent)))
        error=max(abs(a-b)for a,b in zip(entry['bbox'],extent));assert error<.001
        assert abs(entry['transform'][1])<.001 and abs(entry['transform'][2])<.001 and entry['transform'][0]>0 and entry['transform'][3]>0
        front=next(x for x in baseline if x['id']==j['id'] and x['side']=='front');fb=fitz.Rect(front['bbox'])
        reflected=fitz.Rect(A4[0]-fb.x1,fb.y0,A4[0]-fb.x0,fb.y1);reflect_error=max(abs(a-b)for a,b in zip(reflected,box));assert reflect_error<.00001
        assert abs(box.width/mm-70)<.0001 and abs(box.height/mm-70)<.0001
        witness.append({'id':j['id'],'front_page':43,'back_page':44,'bbox_mm':[x/mm for x in box],'shared_image_xref':entry['xref'],'image_bbox_error_pt':error,'long_edge_reflection_error_pt':reflect_error,'upright':True})
        new[43].get_pixmap(dpi=300,clip=box,alpha=False).save(TMP/(j['id']+'_back_300dpi.png'))
    for i in [42,43]:new[i].get_pixmap(dpi=150,alpha=False).save(TMP/f'page{i+1}_150dpi.png')
    with fitz.open(PDF/'BACK_ISLAND.pdf')as master:
        assert len(master)==1 and not master[0].get_text().strip()
        assert max(abs(a-b)for a,b in zip(master[0].rect,fitz.Rect(0,0,76*mm,76*mm)))<.001
        master[0].get_pixmap(dpi=300,alpha=False).save(TMP/'master_300dpi.png')
    with fitz.open(PDF/'KARTLAR_A4_22.pdf')as pair:
        assert len(pair)==2
        assert pair.xref_get_key(pair.pdf_catalog(),'ViewerPreferences/Duplex')[1]=='/DuplexFlipLongEdge'
        assert pair.xref_get_key(pair.pdf_catalog(),'ViewerPreferences/PrintScaling')[1]=='/None'
    # Compare this separately exported pair in a fresh renderer process, without
    # inheriting display-list/font-cache state from 300-dpi clipped inspections.
    code="import fitz,sys,json,hashlib;a=fitz.open(sys.argv[1]);b=fitz.open(sys.argv[2]);out=[]\nfor i in range(2):\n x=a[i].get_pixmap(dpi=96).samples;y=b[42+i].get_pixmap(dpi=96).samples;assert x==y;out.append(hashlib.sha256(x).hexdigest())\nprint(json.dumps(out))"
    pair_hashes=json.loads(subprocess.check_output([sys.executable,'-c',code,str(PDF/'KARTLAR_A4_22.pdf'),str(ART/NAME)],text=True))
    assert new.xref_get_key(new.pdf_catalog(),'ViewerPreferences/Duplex')[1]=='/DuplexFlipLongEdge'
    assert new.xref_get_key(new.pdf_catalog(),'ViewerPreferences/PrintScaling')[1]=='/None'
    embedded=[];unused_resources=[]
    used_fonts={span['font']for block in new[43].get_text('dict')['blocks']if block['type']==0 for line in block['lines']for span in line['spans']}
    for font in new[43].get_fonts(full=True):
        data=new.extract_font(font[0]);name=data[0].split('+')[-1]
        if name not in used_fonts:
            unused_resources.append(data[0]);continue
        assert data[3];embedded.append({'name':name,'embedded_bytes':len(data[3])})
    assert used_fonts=={f['name']for f in embedded},'An actually used font is not embedded'
    preserved={}
    for pin in json.loads((R/'governance/v4/tasks/FOULWAKE-ISLAND-REFERENCE-001.json').read_text())['inputs']:
        assert subprocess.check_output(['git','hash-object',pin['path']],cwd=R,text=True).strip()==pin['git_blob'];preserved[pin['path']]={'git_blob':pin['git_blob'],'sha256':digest(R/pin['path'])}
    for path,sha in json.loads((P/'qa/print_preparation_20260909/imposition_manifest.json').read_text())['retained_back_sha256'].items():assert digest(P/'visual/illustrated_design_20260908/pdf'/(path+'.pdf'))==sha
    out={'status':'PASS / TARGETED_DIGITAL_CHECK / SAME_OPERATOR','task_id':m['task_id'],'full_pdf_sha256':digest(ART/NAME),'retained_pages':unchanged,'exact_text_pages':46,'all_121_fronts_preserved_by_native_page_copy':True,'changed_back_page':44,'changed_island_count':6,'image_pixels':[image.width,image.height],'effective_image_dpi':image.width/(76/25.4),'six_same_original_image_digest':expected.hex(),'placements':witness,'bleed_mm':3,'master_mm':[76,76],'trim_mm':[70,70],'viewer_preferences':'PrintScaling None / DuplexFlipLongEdge','new_page_embedded_fonts':embedded,'replacement_pair_matches_master':True,'preserved_inputs':preserved,'other_six_back_master_hashes_unchanged':True,'physical_print_test':False,'independent_review':False,'visual_review_ref':'visual_review.json'}
    out['replacement_pair_rgb_96dpi_sha256']=pair_hashes
    out['unused_font_resources']=unused_resources
    dump(Q/'verification.json',out);print(json.dumps({k:out[k]for k in ['status','changed_island_count','effective_image_dpi','replacement_pair_matches_master']}),flush=True)
if __name__=='__main__':verify()
