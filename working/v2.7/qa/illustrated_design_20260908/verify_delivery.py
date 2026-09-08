"""Verify the actual final PDFs, canonical copy and exact reviewed artwork."""
import hashlib,json,re,subprocess,sys
from collections import Counter,defaultdict
from pathlib import Path
import fitz
from PIL import Image
from card_layout import R,P,QA,OUT,ASSETS,records,INDEX,BACK_ID,dimensions,metadata,mm
from build_deck import ARTIFACTS,BACKS

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def norm(s):return re.sub(r'\s+','',s.replace('\u00ad','').replace('\u200b',''))
def plain(s):return re.sub(r'[*`]','',s)
def git(*args):return subprocess.check_output(['git',*args],cwd=R,text=True).strip()

def main():
    m=json.loads((QA/'render_manifest.json').read_text());v=json.loads((QA/'individual_visual_review.json').read_text());proof={x['id']:x for x in json.loads((QA/'proof_index.json').read_text())}
    faults=[]
    def check(ok,label):
        if not ok:faults.append(label)
    task=json.loads((R/'governance/v4/tasks/FOULWAKE-ILLUSTRATED-DESIGN-002.json').read_text())
    for source in task['inputs']:check(git('hash-object',source['path'])==source['git_blob'],'Pinned input '+source['path'])
    check(git('rev-parse','HEAD:releases/v2.6')==task['source']['locked_release_tree_sha'],'Locked v2.6 tree')
    check(len(records)==len(INDEX)==len(v)==len(proof)==121,'121 complete review identities')
    check(len(list(ASSETS.glob('*.png')))==121,'121 original PNG plates')
    check(len({sha(p)for p in ASSETS.glob('*.png')})==121,'121 distinct lossless originals')
    front=fitz.open(ARTIFACTS/'fronts_master.pdf');check(len(front)==121,'121 native front master pages')
    dpis=[];front_digests={};canonical={}
    for i,r in enumerate(records):
        identity=r['id'];p=front[i];w,h=dimensions(r);asset=ASSETS/(identity+'.png')
        check(proof[identity]['geometry']=='PASS','Measured geometry '+identity)
        check(v[identity]['status']=='SELF_CHECK_PASS' and v[identity]['viewed_complete_card'],'Visual review '+identity)
        check(v[identity]['asset_sha256']==sha(asset)==proof[identity]['asset_sha256'],'Reviewed current art '+identity)
        check(v[identity]['proof_sha256']==sha(proof[identity]['proof']),'Reviewed complete card hash '+identity)
        px=p.get_pixmap(matrix=fitz.Matrix(3.5,3.5))
        check(hashlib.sha256(px.tobytes('png')).hexdigest()==v[identity]['proof_sha256'],'Final master equals individually reviewed card '+identity)
        footer=identity
        if r['collection']=='powers' and r.get('returns_to_power_deck') is False:footer+=' · Kullanım sonrası oyun dışı'
        expected=' '.join([r.get('name',r.get('title')),metadata(r),r['effect'],r['flavor'],footer])
        canonical[identity]=norm(plain(expected));check(norm(p.get_text())==canonical[identity],'Exact full native copy '+identity)
        check(abs(p.rect.width-w)<.001 and abs(p.rect.height-h)<.001,'Trim dimensions '+identity)
        images=p.get_image_info(hashes=True);check(len(images)==1,'One complete original plate '+identity)
        if len(images)==1:
            im=images[0];front_digests[identity]=im['digest'].hex();box=fitz.Rect(im['bbox'])
            check(max(abs(box[k]-p.rect[k])for k in range(4))<.002,'No inset or cropped plate '+identity)
        with Image.open(asset)as im:dpis.append(min(im.width/(w/72),im.height/(h/72)))
        for word in p.get_text('words'):
            check(p.rect.contains(fitz.Rect(word[:4])),'No clipped native word '+identity+': '+word[4])
        check('\ufffd'not in p.get_text(),'No replacement glyph '+identity)
    check(len(set(front_digests.values()))==121,'121 distinct encoded illustration objects')
    check(min(dpis)>=300,'Minimum original resolution 300 DPI')
    names=list(m['masters']);pn=next(n for n in names if '121_KART_'in n);rn=next(n for n in names if 'GORSEL_'in n)
    docs={n:fitz.open(ARTIFACTS/n)for n in names};check(len(docs[pn])==48,'48 print pages');check(len(docs[rn])==34,'34 complete-card review pages')
    check(Counter(BACK_ID.values())==Counter(m['back_counts']),'Seven back family counts')
    byid={x['id']:x for x in m['print_positions']if x['side']=='front'}
    backjobs={x['id']:x for x in m['print_positions']if x['side']=='back'}
    check(len(byid)==len(backjobs)==len(m['review_positions'])==121,'121 front/back/review positions')
    families=defaultdict(set)
    # Nested PDF forms retain the original page resources outside their clip.
    # get_image_info lists those invisible images too; it cannot establish which
    # composition is visible inside a retained back. Verify the clipped top form
    # and its shared, byte-identical native source page instead.
    back_sources={bid:fitz.open(OUT/'pdf'/f'{bid}.pdf') for bid in BACKS}
    image_cache={}
    def page_images(name,num):
        key=(name,num)
        if key not in image_cache:image_cache[key]=docs[name][num].get_image_info(hashes=True)
        return image_cache[key]
    for identity,pos in byid.items():
        p=docs[pn][pos['page']];box=fitz.Rect(pos['bbox']);rear=backjobs[identity];rb=fitz.Rect(rear['bbox'])
        check(pos['page']%2==0 and rear['page']==pos['page']+1,'Adjacent duplex pair '+identity)
        check(abs(rb.x0-(p.rect.width-box.x1))<.001 and abs(rb.y0-box.y0)<.001,'Long-edge mirrored back '+identity)
        check(norm(p.get_text(clip=box))==canonical[identity],'Printed exact copy '+identity)
        hits=[i for i in page_images(pn,pos['page'])if fitz.Rect(i['bbox']).intersects(box)]
        check(len(hits)==1 and hits[0]['digest'].hex()==front_digests[identity],'Printed original art '+identity)
        back=docs[pn][rear['page']];check(not back.get_text(clip=rb).strip(),'Textless hidden back '+identity)
        bid=BACK_ID[identity];expected=rb+(-3*mm,-3*mm,3*mm,3*mm)
        forms=back.get_xobjects()
        containers=[x for x in forms if x[2]==0 and max(abs((fitz.Rect(x[3])*back.transformation_matrix)[k]-expected[k])for k in range(4))<.002]
        check(len(containers)==1,'One correctly clipped back placement '+identity)
        if len(containers)==1:
            children=[x for x in forms if x[2]==containers[0][0]]
            check(len(children)==1,'One native back source '+identity)
            if len(children)==1:
                source=children[0][0];families[bid].add(source)
                check(docs[pn].xref_stream(source)==back_sources[bid][0].read_contents(),'Byte-identical native back composition '+identity)
        if bid=='BACK_LIGHTHOUSE':
            hits=[i for i in page_images(pn,rear['page'])if fitz.Rect(i['bbox']).intersects(rb)]
            check(all(i['transform'][0]>0 and i['transform'][3]>0 for i in hits),'Upright lighthouse '+identity)
    check(len(families)==7 and all(len(x)==1 for x in families.values()),'One identical shared composition per back family')
    check(len({next(iter(x)) for x in families.values() if len(x)==1})==7,'Seven distinct embedded back family sources')
    for pos in m['review_positions']:
        p=docs[rn][pos['page']];box=fitz.Rect(pos['bbox']);identity=pos['id']
        check(norm(p.get_text(clip=box))==canonical[identity],'Review contains full card copy '+identity)
        hits=[i for i in page_images(rn,pos['page'])if fitz.Rect(i['bbox']).intersects(box)]
        check(len(hits)==1 and hits[0]['digest'].hex()==front_digests[identity],'Review contains selected original '+identity)
    lighthouse=OUT/'pdf/BACK_LIGHTHOUSE.pdf'
    check(sha(lighthouse)=='3357f0a1efcde62b767b9b385da2f1a3742ef4cc8c03c28d97a629c830a3adee','Liked single lighthouse master byte-identical')
    for bid in BACKS:
        with fitz.open(OUT/'pdf'/f'{bid}.pdf')as d:
            check(len(d)==1 and not d[0].get_text().strip(),'One textless back master '+bid)
    cache={};covered={pn:[],rn:[]};compared=0
    def render_hash(p):
        fitz.TOOLS.glyph_cache_empty();fitz.TOOLS.store_shrink(100)
        return hashlib.sha256(p.get_pixmap(dpi=72).samples).hexdigest()
    for volume in m['volumes']:
        path=R/volume['path'];name=pn if path.name.startswith('FOULWAKE_KARTLAR')else rn;intro=2 if name==pn else 1;pages=volume['pages_1based']
        check(sha(path)==volume['sha256'] and path.stat().st_size==volume['bytes']<=10_800_000,'Volume bytes '+path.name)
        with fitz.open(path)as d:
            check(len(d)==len(pages) and pages[:intro]==list(range(1,intro+1)),'Volume page structure '+path.name)
            if intro==2:
                check(len(d)%2==0,'Even duplex volume '+path.name)
                for j in range(2,len(pages),2):check(pages[j]%2==1 and pages[j+1]==pages[j]+1,'Unbroken duplex volume '+path.name)
            covered[name]+=pages[intro:]
            for j,num in enumerate(pages):
                key=(name,num)
                if key not in cache:cache[key]=render_hash(docs[name][num-1])
                check(render_hash(d[j])==cache[key],'Volume render equals master '+path.name+': '+str(j+1));compared+=1
    check(covered[pn]==list(range(3,49)) and covered[rn]==list(range(2,35)),'All master content once in ordered volumes')
    for name,info in m['masters'].items():check(sha(ARTIFACTS/name)==info['sha256'] and (ARTIFACTS/name).stat().st_size==info['bytes'],'Master identity '+name)
    result={'task_id':m['task_id'],'status':'PASS'if not faults else'FAIL','classification':'SAME_OPERATOR_TECHNICAL_SELF_CHECK','failures':faults,'complete_cards_individually_reviewed':121,'exact_copy_front_print_review_checks':363,'original_art_plates':121,'minimum_original_dpi':round(min(dpis),2),'back_counts':m['back_counts'],'front_master_matches_individual_proofs':121,'volume_pages_render_compared':compared,'lighthouse_master_sha256':sha(lighthouse),'source_head':git('rev-parse','HEAD'),'limits':['No physical print, opacity, cut or registration proof','No human play or independent aesthetic acceptance','No locked release']}
    (QA/'delivery_checks.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(result,ensure_ascii=False,indent=2));return not faults

if __name__=='__main__':sys.exit(0 if main()else 1)
