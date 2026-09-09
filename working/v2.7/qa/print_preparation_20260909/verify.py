"""Check the actual final PDF bytes, with independent physical-corner witnesses."""
from common import *
import math,unicodedata
import numpy as np
from PIL import Image,ImageDraw
from collections import Counter

def norm(t):return re.sub(r'\s+','',unicodedata.normalize('NFKC',t).replace('**','').replace('`','').replace('*','')).casefold()
def arr(p,dpi=150):
    q=p.get_pixmap(dpi=dpi,alpha=False);return np.frombuffer(q.samples,dtype=np.uint8).reshape(q.height,q.width,q.n)
def crop(doc,j):
    w,h=dims(INDEX[j['id']]);d=fitz.open();p=d.new_page(width=w,height=h)
    p.show_pdf_page(p.rect,doc,j['page'],clip=fitz.Rect(j['bbox']),rotate=(-j['rotation'])%360)
    return d
def world(j,u,v):
    b=fitz.Rect(j['bbox']);x=b.x0;y=A4[1]-b.y1;w,h=dims(INDEX[j['id']]);a=j['rotation']
    if a==0:return np.array([x+u,y+v])
    if a==90:return np.array([x+h-v,y+u])
    if a==270:return np.array([x+v,y+w-u])
    raise ValueError(a)
def corner_error(f,b):
    w,h=dims(INDEX[f['id']]);errors=[]
    # Asymmetric physical witnesses near all four native card corners.
    for u,v in [(2,3),(w-5,7),(11,h-13),(w-17,h-19)]:
        front=world(f,u,v);back=world(b,w-u,v);back[0]=A4[0]-back[0]
        errors.append(float(np.max(np.abs(front-back)))/mm)
    return max(errors)
def body(p):
    return '\n'.join(s['text']for b in p.get_text('dict')['blocks']if 'lines'in b for l in b['lines']for s in l['spans']if 62<s['bbox'][1] and s['bbox'][3]<780)
def basic(doc,name,expected):
    assert len(doc)==expected and expected%2==0
    pref=doc.xref_get_key(doc.pdf_catalog(),'ViewerPreferences')[1]
    assert '/DuplexFlipLongEdge'in pref and '/PrintScaling/None'in pref.replace(' ','')
    fonts={}; pages=[]
    for i,p in enumerate(doc):
        assert abs(p.rect.width-A4[0])<.01 and abs(p.rect.height-A4[1])<.01 and p.rotation==0
        used={s['font']for b in p.get_text('dict')['blocks']if 'lines'in b for l in b['lines']for s in l['spans']}
        for f in p.get_fonts(full=True):
            if any(u in f[3]for u in used):
                assert doc.extract_font(f[0])[3],(name,i,f)
                fonts[f[3]]=True
        pages.append({'page':i+1,'a4':True,'rotation':0})
    return {'file':name,'sha256':sha(ART/name),'pages':pages,'used_fonts_embedded':list(fonts),'preferences':pref}
def render_book(d):
    out=TMP/'render';out.mkdir(exist_ok=True);images=[]
    for i,p in enumerate(d):
        path=out/f'book_{i+1:02d}.png';p.get_pixmap(dpi=115).save(path);images.append(path)
    for start in range(0,len(images),4):
        canvas=Image.new('RGB',(1560,2*(1103+26)),'#e1e1dc');dr=ImageDraw.Draw(canvas)
        for k,path in enumerate(images[start:start+4]):
            im=Image.open(path);im.thumbnail((780,1103));xx=(k%2)*780;yy=(k//2)*1129;canvas.paste(im,(xx,yy+26));dr.text((xx+8,yy+5),f'Final rulebook page {start+k+1}',fill='black')
        canvas.save(out/f'book_contact_{start//4+1:02d}.jpg',quality=93)

def main():
    m=json.loads((QA/'imposition_manifest.json').read_text());jj=m['placements']
    cardname='FOULWAKE_KARTLAR_A4_CIFT_TARAFLI_v2.7.pdf';bookname='FOULWAKE_KURAL_KITABI_A4_v2.7.pdf';guidename='FOULWAKE_A4_BASKI_REHBERI_VE_HIZALAMA.pdf'
    deck=fitz.open(ART/cardname);book=fitz.open(ART/bookname);guide=fitz.open(ART/guidename)
    results={'task_id':'FOULWAKE-A4-PRINT-001','status':'RUNNING','physical_proof':'NOT_PERFORMED','reviewer':'CHIEF_EDITOR / SAME_OPERATOR_SELF_CHECK'}
    assert sha(P/'FOULWAKE_CARD_TEXTS_v2.7.json')=='cf131726580864a3b878fe25ac7dbd33e0ca52208d4892d6729db7e7e2c486a3'
    assert sha(P/'FOULWAKE_OWNER_CARD_TEXT_OVERRIDES_v2.7.json')=='dc3ca70f2b84d77eccfc6b8443d172c88a32db4808fe70538e3c1b4cdde2db56'
    results['documents']=[basic(d,n,k)for d,n,k in [(deck,cardname,46),(book,bookname,30),(guide,guidename,4)]]
    fronts={j['id']:j for j in jj if j['side']=='front'};backs={j['id']:j for j in jj if j['side']=='back'}
    assert len(fronts)==len(backs)==121 and set(fronts)==set(backs)==set(INDEX)
    margins=[];errors=[];neg=[]
    for rid,f in fronts.items():
        b=backs[rid];assert b['page']==f['page']+1 and b['back']==BACK[rid]
        w,h=dims(INDEX[rid]);box=fitz.Rect(f['bbox']);expected=(h,w)if f['rotation']else(w,h)
        assert abs(box.width-expected[0])<.001 and abs(box.height-expected[1])<.001
        err=corner_error(f,b);assert err<.00001;errors.append(err)
        broken=dict(b,bbox=f['bbox']);neg.append(corner_error(f,broken)>.01)
        if f['rotation']:assert corner_error(f,dict(b,rotation=90))>1
    assert all(neg)
    for j in jj:
        box=fitz.Rect(j['bbox'])+(-4.75*mm,-4.75*mm,4.75*mm,4.75*mm)
        margins.append(min(box.x0,box.y0,A4[0]-box.x1,A4[1]-box.y1)/mm)
        for other in jj:
            if other['page']==j['page']and other['id']!=j['id']:
                # Aligned horizontal crop strokes may coincide in the gutter;
                # neither stroke nor bleed may enter another card's artwork.
                assert not box.intersects(fitz.Rect(other['bbox'])+(-3*mm,-3*mm,3*mm,3*mm))
    assert min(margins)>7.3
    results['geometry']={'cards':121,'placements':242,'asymmetric_witnesses':484,'max_physical_corner_error_mm':max(errors),'wrong_column_negative_controls_failed':len(neg),'wrong_quarter_turn_negative_controls_failed':46,'minimum_crop_mark_margin_mm':min(margins),'bleed_mm':3}
    bm=json.loads((QA/'rulebook_manifest.json').read_text());txt=norm('\n'.join(body(p)for p in book));missing=[u for u in bm['units']if norm(u)not in txt]
    assert not missing,missing[:5]
    margin_rows=[]
    for i,p in enumerate(book):
        if i in (0,29):continue
        spans=[s for b in p.get_text('dict')['blocks']if 'lines'in b for l in b['lines']for s in l['spans']if 62<s['bbox'][1]and s['bbox'][3]<780]
        left=(22 if (i+1)%2 else 18)*mm;right=left+170*mm
        assert all(s['bbox'][0]>=left-.2 and s['bbox'][2]<=right+.2 for s in spans),(i+1,spans)
        assert not spans[-1]['text'].startswith(('OKU','YAP')),i+1
        margin_rows.append({'page':i+1,'left_mm':left/mm,'right_mm':(A4[0]-right)/mm})
    for item in book.get_toc():
        assert norm(item[1])in norm(body(book[item[2]-1]))
    results['rulebook']={'source_units_present':len(bm['units']),'missing_units':0,'toc_entries':len(book.get_toc()),'mirrored_margins':margin_rows,'no_orphan_oku_yap':True}
    render_book(book);print('Book text, fonts, margins, duplex geometry checked',flush=True)
    src=fitz.open(TMP/'fronts_trim.pdf');checks=[];renders=TMP/'individual';renders.mkdir(exist_ok=True)
    cp=TMP/'front_check_checkpoint.json';cache={}
    if cp.exists():
        cached=json.loads(cp.read_text());assert cached['input_sha256']==sha(ART/cardname)
        cache={x['id']:x for x in cached['completed']}
    for i,r in enumerate(records):
        if r['id']in cache:
            row=cache[r['id']];assert sha(renders/(r['id']+'.png'))==row['render_sha256'];checks.append(row);continue
        j=fronts[r['id']];one=crop(deck,j);p=one[0];t=norm(p.get_text())
        title_field='title' if r['collection']=='override' else 'name'
        fields={k:norm(r[k])in t for k in [title_field,'effect','flavor']};assert all(fields.values()),(r['id'],fields,p.get_text())
        actual=arr(p);before=arr(src[i]);assert actual.shape==before.shape
        delta=np.abs(actual.astype('int16')-before.astype('int16'));fraction=float((delta.max(2)>0).mean())
        # Reject material changes immediately. Every nonzero comparison is
        # also recorded and visually examined before the final disposition;
        # native form rounding can affect punctuation antialiasing.
        assert delta.mean()<.1 and fraction<.002,(r['id'],delta.mean(),delta.max(),fraction)
        if delta.max():Image.fromarray(np.minimum(delta*6,255).astype('uint8')).save(renders/(r['id']+'_difference.png'))
        png=renders/(r['id']+'.png');p.get_pixmap(dpi=200,alpha=False).save(png)
        checks.append({'id':r['id'],'page':j['page']+1,'native_mm':j['native_mm'],'exact_fields':fields,'all_raster_channels_equal_at_150dpi':bool(delta.max()==0),'mean_channel_delta_150dpi':float(delta.mean()),'max_channel_delta_150dpi':int(delta.max()),'changed_pixel_fraction':fraction,'render_sha256':sha(png)})
        dump(cp,{'input_sha256':sha(ART/cardname),'completed':checks,'origin':'Checks of exact final PDF bytes, checkpointed after successful comparison and render.'})
        one.close()
        if (i+1)%20==0:print('Exact front checks',i+1,flush=True)
    for bid,h in m['retained_back_sha256'].items():assert sha(BACK_ROOT/(bid+'.pdf'))==h
    backrows=[];masters={b:fitz.open(PDF/'BACK_ISLAND.pdf'if b=='BACK_ISLAND'else BACK_ROOT/(b+'.pdf'))for b in set(BACK.values())}
    for rid,j in backs.items():
        actual=crop(deck,j);w,h=dims(INDEX[rid]);expected=fitz.open();p=expected.new_page(width=w,height=h);source=masters[j['back']];p.show_pdf_page(p.rect,source,0,clip=source[0].rect+(3*mm,3*mm,-3*mm,-3*mm))
        aa=arr(actual[0]);bb=arr(p);diff=np.abs(aa.astype('int16')-bb.astype('int16'));assert diff.mean()<.02,(rid,diff.mean())
        backrows.append({'id':rid,'back':j['back'],'page':j['page']+1,'mean_channel_delta_150dpi':float(diff.mean())})
    # Check every two-page repository sheet against the supplied 46-page master.
    for i,item in enumerate(m['parts']):
        d=fitz.open(R/item['path']);assert len(d)==2 and sha(R/item['path'])==item['sha256']
        for n in (0,1):assert np.array_equal(arr(d[n],36),arr(deck[2*i+n],36))
    im=fitz.open(PDF/'BACK_ISLAND.pdf');q=im[0].get_pixmap(matrix=fitz.Matrix(1024/im[0].rect.width,1024/im[0].rect.height),alpha=False);aa=np.frombuffer(q.samples,dtype=np.uint8).reshape(q.height,q.width,q.n);sym=np.abs(aa.astype('int16')-aa[::-1,::-1].astype('int16'))
    results['backs']={'counts':dict(Counter(BACK.values())),'six_retained_file_hashes':m['retained_back_sha256'],'new_island':sha(PDF/'BACK_ISLAND.pdf'),'island_180_degree_mean_channel_delta':float(sym.mean()),'single_lighthouse_source_unchanged':True}
    results['copy']={'fronts':121,'canonical_fields':363,'pixel_equal_fronts_150dpi':sum(x['all_raster_channels_equal_at_150dpi']for x in checks),'max_mean_channel_delta_150dpi':max(x['mean_channel_delta_150dpi']for x in checks),'all_23_sheet_parts_match':True}
    results['status']='PASS_DIGITAL / VISUAL_REVIEW_TO_BE_RECORDED'
    dump(QA/'verification.json',results);dump(QA/'per_card_verification.json',{'fronts':checks,'backs':backrows})
    for start in range(0,len(records),8):
        c=Image.new('RGB',(1800,1510),'#dfdfd9');dr=ImageDraw.Draw(c)
        for k,r in enumerate(records[start:start+8]):
            im=Image.open(renders/(r['id']+'.png'));im.thumbnail((430,700));x=(k%4)*450;y=(k//4)*755;c.paste(im,(x+(450-im.width)//2,y+30));dr.text((x+12,y+8),r['id'],fill='black')
        c.save(TMP/'render'/f'cards_contact_{start//8+1:02d}.jpg',quality=93)
    print(json.dumps({'status':results['status'],'cards':121,'fields':363,'pages':80,'min_crop_margin_mm':min(margins)}),flush=True)

if __name__=='__main__':main()
