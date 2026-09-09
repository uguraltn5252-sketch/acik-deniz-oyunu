"""Independent source/PDF comparisons and A4 duplex preflight, no game simulation."""
from pathlib import Path
import json,re,hashlib,subprocess,unicodedata,math
from collections import Counter
import fitz
from fontTools.ttLib import TTFont
from fontTools.pens.boundsPen import BoundsPen
R=Path(__file__).resolve().parents[4];P=R/'working/v2.7';Q=Path(__file__).resolve().parent;O=P/'publication_20260909';T=R.parent/'tmp/publication_20260909'
BASE='d4072fbff19aeae3508801b733164fdae8517e7a';MM=72/25.4
OLD=re.compile(r'San\s+Cordelio|Saint\s+Verena|Eleonora|Kuru\s+Pay|Siyah\s+Mühür|Kara\s+Mühür',re.I)
def load(p):return json.loads(p.read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def norm(s):return re.sub(r'\s+','',unicodedata.normalize('NFKC',s).replace('**','').replace('`','').replace('•','').replace('*',''))
def baseline(path):return subprocess.check_output(['git','show',BASE+':'+str(path.relative_to(R))],cwd=R)
def verify():
 checks={};fail=[]
 def ok(label,condition,detail=None):
  checks[label]={'pass':bool(condition),'detail':detail}
  if not condition:fail.append(label)
 src=load(P/'FOULWAKE_CARD_TEXTS_v2.7.json');old=json.loads(baseline(P/'FOULWAKE_CARD_TEXTS_v2.7.json'));capt=load(P/'FOULWAKE_OWNER_CARD_TEXT_OVERRIDES_v2.7.json')['records'];records=[];diff=[]
 for group in ['characters','powers','provisions','loyalties','maps','utilities']:
  a={c['id']:c for c in old[group]};b={c['id']:c for c in src[group]};ok('ids_'+group,a.keys()==b.keys())
  for id,c in b.items():
   records.append(c)
   for key in set(a[id])|set(c):
    if a[id].get(key)!=c.get(key):diff.append({'id':id,'field':key,'before':a[id].get(key),'after':c.get(key)})
 allowed={('KAR-18','flavor'),('SET-KL-01','place'),('SET-VL-01','place')}|{(f'SAD-T-{i:02d}','effect')for i in range(1,11)}
 mapping=[('San Cordelio','Port Avanta'),('Saint Verena','Santa Veda')]
 normalized=[]
 for x in diff:
  v=x['before']
  for a,b in mapping:v=v.replace(a,b)
  normalized.append((x['id'],x['field'])in allowed and v==x['after'])
 ok('authorized_copy_delta_only',all(normalized)and len(diff)==13,diff)
 records+=capt;ok('total_121',len({r['id']for r in records})==121)
 cp=P/'FOULWAKE_OWNER_CARD_TEXT_OVERRIDES_v2.7.json';ok('captain_exact_unchanged',cp.read_bytes()==baseline(cp),sha(cp))
 ok('four_allusions_unchanged',all(next(r for r in src['powers']if r['id']==i)==next(r for r in old['powers']if r['id']==i)for i in ['GUC-03','GUC-05','GUC-15','GUC-18']))
 primary=[P/f for f in ['FOULWAKE_CARD_TEXTS_v2.7.json','FOULWAKE_KURAL_KITABI_v2.7.md','FOULWAKE_RULEBOOK_STORY_v2.7.md','FOULWAKE_STORY_FRAMEWORK.md']]
 derived=[P/f for f in ['FOULWAKE_KART_METINLERI_v2.7.md','README_CURRENT_v2.7.md','FOULWAKE_EDITORIAL_DECISIONS_v2.7.json','FOULWAKE_STORY_REVALIDATION_v2.7.md','FOULWAKE_NARRATIVE_VALIDATION_v2.7.md','FOULWAKE_VISUAL_SYSTEM.md','visual/art_direction/FOULWAKE_CURRENT_ART_DIRECTION_v2.7.md','visual/art_direction/FOULWAKE_121_ART_BRIEF_MANIFEST_v2.7.json','visual/art_direction/FOULWAKE_ART_DIRECTION_BIBLE_v2.7.md','visual/art_direction/FOULWAKE_7_BACK_BRIEFS_v2.7.md','visual/art_direction/FOULWAKE_12_PILOT_PRODUCTION_BRIEFS_v2.7.md']]
 for i,files in enumerate([primary,derived],1):
  hits=[{'path':str(f.relative_to(R)),'term':m.group()}for f in files for m in OLD.finditer(f.read_text())];ok('canon_scan_pass_'+str(i),not hits,{'files':len(files),'hits':hits})
 manifest=load(Q/'cards_manifest.json');bm=load(Q/'book_manifest.json');fronts=fitz.open(T/'fronts_clean.pdf');deck=fitz.open(O/'pdf/FOULWAKE_KARTLAR_A4_CIFT_TARAFLI_v2.7.pdf');book=fitz.open(O/'pdf/FOULWAKE_KURAL_KITABI_A4_v2.7.pdf')
 exact=[];fields=0;metafails=[];safe=[];font_outlines={};bounds_cache={}
 for f in (O/'fonts').glob('*.ttf'):
  font=TTFont(f);font_outlines[f.stem]=(font.getGlyphSet(),font.getBestCmap(),font['head'].unitsPerEm)
 for i,r in enumerate(records):
  text=norm(fronts[i].get_text())
  for k in ['name'if'name'in r else'title','effect','flavor']:
   fields+=1
   if norm(r[k])not in text:exact.append({'id':r['id'],'field':k})
  for k in ['place','role','time']:
   if k in r and r[k]!='-'and norm(r[k])not in text:metafails.append({'id':r['id'],'field':k})
  # All content except the small production ID stays well inside trim edges.
  clip=fronts[i].rect+ (3*MM,3*MM,-3*MM,-3*MM)
  for block in fronts[i].get_text('rawdict')['blocks']:
   if block['type']!=0:continue
   for ln in block['lines']:
    for s in ln['spans']:
     text=''.join(c['c']for c in s['chars'])
     if r['id']in text:continue
     gs,cmap,up=font_outlines[s['font']]
     for ch in s['chars']:
      key=(s['font'],ch['c'])
      if key not in bounds_cache:
       name=cmap.get(ord(ch['c']));pen=BoundsPen(gs)
       if name:gs[name].draw(pen)
       bounds_cache[key]=pen.bounds
      glyph=bounds_cache[key]
      if not glyph:continue
      x,y=ch['origin'];scale=s['size']/up
      b=fitz.Rect(x+glyph[0]*scale,y-glyph[3]*scale,x+glyph[2]*scale,y-glyph[1]*scale)
      if b.x0<clip.x0+4.49*MM or b.x1>clip.x1-4.49*MM or b.y0<clip.y0+4.49*MM or b.y1>clip.y1-4.49*MM:safe.append({'id':r['id'],'text':ch['c'],'ink_bbox':list(b)})
 ok('front_exact_copy',not exact,{'fields':fields,'mismatches':exact});ok('front_metadata',not metafails,metafails);ok('card_safe_area',not safe,safe)
 artwork=[]
 for r in manifest['fronts']:
  p=R/r['source'];artwork.append(p.read_bytes()==baseline(p))
 ok('121_original_art_sources_unchanged',len(artwork)==121 and all(artwork))
 backfails=[]
 for b,v in manifest['shared_backs'].items():
  p=R/v['path']
  if p.read_bytes()!=baseline(p)or sha(p)!=v['sha256']:backfails.append(b)
 ok('seven_shared_backs_unchanged',not backfails,{'instances':{k:v['instances']for k,v in manifest['shared_backs'].items()},'failures':backfails})
 jobs=manifest['placements'];byid={};placementfails=[];imposedcopy=[]
 for j in jobs:byid.setdefault(j['id'],{})[j['side']]=j
 for r in records:
  pair=byid[r['id']];a,b=pair['front'],pair['back'];ar,br=fitz.Rect(a['bbox']),fitz.Rect(b['bbox']);target=fitz.Rect(deck[0].rect.width-ar.x1,ar.y0,deck[0].rect.width-ar.x0,ar.y1)
  if a['page']%2 or b['page']!=a['page']+1 or max(abs(x-y)for x,y in zip(br,target))>.01 or b['back']!=a['back'] or b['rotation']!=(270 if a['rotation']==90 else 0):placementfails.append(r['id'])
  t=norm(deck[a['page']].get_text(clip=ar))
  if any(norm(r[k])not in t for k in ['name'if'name'in r else'title','effect','flavor']):imposedcopy.append(r['id'])
 ok('duplex_121_pairs',len(jobs)==242 and not placementfails,placementfails);ok('imposed_exact_copy',not imposedcopy,imposedcopy)
 dimensions=[]
 for j in jobs:
  box=fitz.Rect(j['bbox']);trim=sorted([round(box.width/MM,1),round(box.height/MM,1)])
  if trim not in [[70.0,120.0],[63.5,88.9],[70.0,70.0]]or not deck[j['page']].rect.contains(box+(-3*MM,-3*MM,3*MM,3*MM)):dimensions.append(j['id'])
 ok('trim_and_bleed',not dimensions,dimensions)
 # Remove only the repeating running furniture; compare all parsed source units.
 pages=[p.get_text(clip=fitz.Rect(15*MM,22*MM,198*MM,275*MM))for p in book]
 bt=norm(''.join(pages));missing=[]
 for i,s in enumerate(bm['units']):
  s=re.sub(r'^\*\*(YAP|Örnek):\*\*\s*','',s)
  if norm(s)not in bt:missing.append({'unit':i,'text':s})
 ok('book_source_units',not missing,{'units':len(bm['units']),'missing':missing})
 ok('cover_only_title',book[0].get_text().strip()=='FOULWAKE',book[0].get_text().strip())
 toc=book.get_toc();ok('book_navigation',len(toc)==18 and all(norm(title)in norm(book[pg-1].get_text())for _,title,pg in toc),toc)
 pdfhits=[]
 for label,d in [('cards',deck),('book',book)]:
  for i,p in enumerate(d):
   for m in OLD.finditer(p.get_text()):pdfhits.append({'pdf':label,'page':i+1,'term':m.group()})
  if OLD.search(str(d.metadata)):pdfhits.append({'pdf':label,'metadata':d.metadata})
 ok('canon_scan_pass_3',not pdfhits,{'pages':len(deck)+len(book),'hits':pdfhits})
 pdf_results={}
 for label,d in [('cards',deck),('book',book)]:
  pp=[];low=[];fonts=set();renderhash=[];badglyphs=[];outofpage=[];fontfacts={}
  for i,p in enumerate(d):
   if max(abs(p.rect.width/MM-210),abs(p.rect.height/MM-297))>.01:outofpage.append(i+1)
   tx=p.get_text()
   if '\ufffd'in tx or '\x00'in tx:badglyphs.append(i+1)
   for b in p.get_text('dict')['blocks']:
    if b['type']==0:
     for line in b['lines']:
      for s in line['spans']:fonts.add(s['font'])
   for im in p.get_image_info():
    a,b,c,e,_,_=im['transform'];dpi=min(im['width']/(math.hypot(a,b)/72),im['height']/(math.hypot(c,e)/72));pp.append(dpi)
    if dpi<299.8:low.append({'page':i+1,'ppi':round(dpi,2)})
   pix=p.get_pixmap(dpi=90,alpha=False);renderhash.append(hashlib.sha256(pix.samples).hexdigest())
   for f in p.get_fonts(full=True):
    if 'Alegreya'in f[3]:fontfacts[f[3]]=len(d.extract_font(f[0])[3])
  prefs=d.xref_get_key(d.pdf_catalog(),'ViewerPreferences')[1]
  result={'pages':len(d),'minimum_image_ppi':round(min(pp),2),'low_resolution':low,'used_fonts':sorted(fonts),'embedded_fonts':fontfacts,'page_render_sha256':renderhash,'bad_glyph_pages':badglyphs,'non_a4_pages':outofpage,'preferences':prefs}
  pdf_results[label]=result
  ok(label+'_prepress',not low and not badglyphs and not outofpage and all(fontfacts.values())and len(d)%2==0 and'DuplexFlipLongEdge'in prefs and'None'in prefs,result)
 # Cross-document exact story sections; no template replay can quietly restore old names.
 bs=(P/'FOULWAKE_KURAL_KITABI_v2.7.md').read_text();ss=(P/'FOULWAKE_RULEBOOK_STORY_v2.7.md').read_text()
 def block(text,start,end):return text.split(start,1)[1].split(end,1)[0].strip()
 ok('story_chapter17_synchronized',block(bs,'## 17.','\n## Masada')==block(ss,'## 17.','\n## Uygulama'))
 result={'task_id':'FOULWAKE-PUBLICATION-REDESIGN-001','source_baseline':BASE,'class':'SAME_OPERATOR_SELF_CHECK','status':'PASS'if not fail else'FAIL','failed':fail,'checks':checks,'pdf_sha256':{k:sha(O/'pdf'/n)for k,n in [('cards','FOULWAKE_KARTLAR_A4_CIFT_TARAFLI_v2.7.pdf'),('book','FOULWAKE_KURAL_KITABI_A4_v2.7.pdf')]},'not_tested':['physical duplex registration','human playtest','independent aesthetic acceptance','full game simulation']}
 (Q/'verification.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
 print(json.dumps({'status':result['status'],'failed':fail,'front_fields':fields,'book_units':len(bm['units']),'minimum_ppi':{k:v['minimum_image_ppi']for k,v in pdf_results.items()}},ensure_ascii=False))
if __name__=='__main__':verify()
