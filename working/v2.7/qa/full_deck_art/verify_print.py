"""Verify canonical copy, selected source art and complete duplex PDF volumes.

These are operator technical checks. Human play, independent aesthetic review,
physical opacity and print registration are not inferred from digital evidence.
"""
from pathlib import Path
from collections import Counter,defaultdict
import hashlib,json,re,subprocess,sys
import fitz
import numpy as np
from PIL import Image
import build_print as b

def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def norm(s):return re.sub(r'\s+','',s.replace('\u00ad','').replace('\u200b',''))
def plain(s):return re.sub(r'[*`]','',s)
def git(*args):return subprocess.check_output(['git',*args],cwd=b.R,text=True).strip()

def main():
 m=json.loads((b.QA/'render_manifest.json').read_text());faults=[]
 def check(ok,label):
  if not ok:faults.append(label)
 result={'task_id':m['task_id'],'classification':'SAME_OPERATOR_TECHNICAL_SELF_CHECK','failures':faults}
 ids=[r['id']for r in b.records]
 check(len(ids)==121 and len(set(ids))==121,'121 canonical identities')
 check(len(m['cards'])==121 and set(ids)=={r['id']for r in m['cards']},'121 placement identities')
 check(sum(r['illustration']for r in m['cards'])==121,'121 illustrated fronts')
 check(len(m['card_pdf_positions'])==121,'121 PDF positions')
 check(Counter(b.back_id(r)for r in b.records)==Counter(m['back_counts']),'Back-family counts')

 prompts=json.loads((b.OUT/'prompts.json').read_text())
 selected=[r for r in prompts['records']if r['review_status']=='SAME_OPERATOR_SELECTED_FOR_LAYOUT']
 new_ids=[r['id']for r in selected if not r['id'].startswith('BACK_')]
 check(len(new_ids)==109 and len(set(new_ids))==109,'109 distinct selected new fronts')
 check(Counter(r['id']for r in selected)['BACK_LIGHTHOUSE']==1,'One selected replacement lighthouse back')
 for r in selected:check(sha(b.R/r['asset_path'])==r['sha256'],'Selected PNG hash '+r['id'])
 check({p.name for p in (b.OUT/'assets').glob('*.png')}=={Path(r['asset_path']).name for r in selected},'No unselected or missing production PNG')
 check(len({sha(b.R/r['asset_path'])for r in selected})==110,'110 distinct selected source images')
 task=json.loads((b.R/'governance/v4/tasks/FOULWAKE-FULL-DECK-ART-001.json').read_text())
 pins=[]
 for item in task['inputs']:
  path=item['path']
  if path.startswith('working/'):
   actual=git('hash-object',path);check(actual==item['git_blob'],'Protected input unchanged '+path)
   pins.append({'path':path,'expected_git_blob':item['git_blob'],'actual_git_blob':actual})
 result['protected_working_inputs']=pins

 card_name=next(n for n in m['compiled_masters']if '121_KART_'in n)
 review_name=next(n for n in m['compiled_masters']if 'GORSEL_'in n)
 docs={card_name:fitz.open(b.ARTIFACTS/card_name),review_name:fitz.open(b.ARTIFACTS/review_name)}
 doc=docs[card_name];check(len(doc)==48,'48 complete master card pages')
 check(len(docs[review_name])==24,'24 complete all-deck review pages')
 families=defaultdict(set);front_digests=set()
 for pos in m['card_pdf_positions']:
  r=b.INDEX[pos['id']];page=doc[pos['page_1based']-1];rect=fitz.Rect(pos['bbox_pt'])
  extracted=norm(page.get_text(clip=rect))
  for field in [r.get('name',r.get('title')),b.metadata(r),r['effect'],r['flavor'],r['id']]:
   check(norm(plain(field))in extracted,'Canonical PDF copy '+r['id']+': '+field)
  safe=fitz.Rect(rect.x0+4*b.mm,rect.y0+3.7*b.mm,rect.x1-4*b.mm,rect.y1-3.7*b.mm)
  for word in page.get_text('words',clip=rect):check(safe.contains(fitz.Rect(word[:4])),'Text safe area '+r['id']+': '+word[4])
  w,h=b.dimensions(r)
  check(abs(rect.width-w)<.001 and abs(rect.height-h)<.001,'Trim size '+r['id'])
  art=[im for im in page.get_image_info(hashes=True)if fitz.Rect(im['bbox']).intersects(rect)]
  check(len(art)==1,'Exactly one front illustration '+r['id'])
  front_digests.update(im['digest'].hex()for im in art)
  check(pos['page_1based']%2==1,'Odd front page '+r['id'])
  rear=doc[pos['page_1based']];rr=fitz.Rect(page.rect.width-rect.x1,rect.y0,page.rect.width-rect.x0,rect.y1)
  hits=[im for im in rear.get_image_info(hashes=True)if fitz.Rect(im['bbox']).intersects(rr)]
  check(len(hits)==2,'Two half-turn placements '+r['id'])
  signatures={im['digest'].hex()for im in hits}
  check(len(signatures)==1,'Same source for both back halves '+r['id'])
  families[b.back_id(r)].update(signatures)
  check(not rear.get_text(clip=rr).strip(),'Textless card back '+r['id'])
 check(len(front_digests)==121,'121 different front illustration objects')
 check(len(families)==7 and all(len(v)==1 for v in families.values()),'One source per each of seven back families')
 check(len({next(iter(v))for v in families.values()if v})==7,'Seven different back masters')
 dpis=[r['effective_art_dpi']for r in m['cards']]
 check(min(dpis)>=300,'Front effective resolution >=300 DPI')
 result.update(cards_checked=121,illustrated_fronts=121,text_only_fronts=0,new_fronts=109,retained_fronts=12,
  minimum_front_dpi=min(dpis),back_counts=m['back_counts'],family_pdf_image_digests={k:sorted(v)for k,v in families.items()})

 rendered={}
 def page_hash(name,index):
  key=(name,index)
  if key not in rendered:rendered[key]=hashlib.sha256(docs[name][index].get_pixmap(dpi=72).samples).hexdigest()
  return rendered[key]
 covered={card_name:[],review_name:[]};volume_pages=0
 for volume in m['volumes']:
  path=b.R/volume['file'];v=fitz.open(path);pages=volume['master_pages_1based']
  name=card_name if Path(volume['file']).name.startswith('FOULWAKE_KARTLAR')else review_name
  intro=2 if name==card_name else 1
  check(sha(path)==volume['sha256'],'Volume SHA '+path.name)
  check(path.stat().st_size==volume['bytes']<=10_800_000,'Complete transport-sized volume '+path.name)
  check(len(v)==len(pages),'Volume page count '+path.name)
  check(pages[:intro]==list(range(1,intro+1)),'Volume introduction '+path.name)
  if name==card_name:
   check(len(v)%2==0,'Even duplex volume '+path.name)
   for j in range(2,len(pages),2):check(pages[j]%2==1 and pages[j+1]==pages[j]+1,'Unbroken duplex pair '+path.name)
  covered[name].extend(pages[intro:])
  for j,original in enumerate(pages):
   digest=hashlib.sha256(v[j].get_pixmap(dpi=72).samples).hexdigest()
   check(digest==page_hash(name,original-1),'Volume render equals master '+path.name+' page '+str(j+1))
   volume_pages+=1
  v.close()
 check(covered[card_name]==list(range(3,49)),'All card sheets appear once in ordered volumes')
 check(covered[review_name]==list(range(2,25)),'All review content appears once in ordered volumes')
 result['volume_pages_render_compared']=volume_pages
 result['compiled_masters']=m['compiled_masters'];result['volumes']=m['volumes']
 for name,info in m['compiled_masters'].items():
  check(sha(b.ARTIFACTS/name)==info['sha256'],'Master SHA '+name)
  for page in docs[name]:
   check('\ufffd'not in page.get_text(),'No replacement glyph '+name)
   for font in page.get_fonts():check(font[1]in ('ttf','cff')or font[3]in ('Helvetica','Times-Roman','Courier'),'Embedded typeface '+str(font))

 rotations={}
 for bid in b.BACKS:
  path=b.PDF/(bid+'.pdf')if bid=='BACK_LIGHTHOUSE'else b.P/'visual/recheck_20260907/pdf'/(bid+'.pdf')
  d=fitz.open(path);check(len(d)==1,'One back master page '+bid);page=d[0]
  r=next(r for r in b.records if b.back_id(r)==bid);w,h=b.dimensions(r)
  check(abs(page.rect.width-w-6*b.mm)<.001 and abs(page.rect.height-h-6*b.mm)<.001,'Back master size '+bid)
  ims=page.get_image_info(hashes=True);check(len(ims)==2 and ims[0]['digest']==ims[1]['digest'],'Shared back image '+bid)
  if len(ims)==2:
   a,z=[im['transform']for im in ims]
   check(all(abs(a[k]+z[k])<.002 for k in range(4)),'Half-turn basis '+bid)
   check(abs(a[4]+z[4]-page.rect.width)<.002 and abs(a[5]+z[5]-page.rect.height)<.002,'Half-turn centre '+bid)
  check(not page.get_text().strip(),'No text on master '+bid)
  tmp=fitz.open();pp=tmp.new_page(width=1000,height=1000);pp.show_pdf_page(pp.rect,d,0,keep_proportion=False)
  px=pp.get_pixmap();a=np.frombuffer(px.samples,dtype=np.uint8).reshape(px.height,px.width,3)
  delta=np.abs(a.astype(int)-a[::-1,::-1].astype(int))
  rotations[bid]={'mean_channel_delta':round(float(delta.mean()),6),'max_channel_delta':int(delta.max()),
   'nonzero_channel_fraction':round(float((delta>0).mean()),6),'interpretation':'Shared source and PDF half-turn geometry checked. Nonzero render differences are reported; pixel-exact rotational equality is not claimed.'}
  tmp.close();d.close()
 result['back_rotation_render']=rotations
 result['limits']=['No human playtest in this art task','No physical duplex registration or opacity test','No independent aesthetic acceptance','No pixel-exact back-render claim','Not a locked release']
 result['assets']={r['id']:{'path':r['asset_path'],'sha256':r['sha256'],'pixels':list(Image.open(b.R/r['asset_path']).size)}for r in selected}
 result['status']='PASS'if not faults else'FAIL'
 (b.QA/'print_checks.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
 print(json.dumps({k:result[k]for k in ['status','cards_checked','illustrated_fronts','minimum_front_dpi','volume_pages_render_compared','failures']},ensure_ascii=False,indent=2))
 return not faults

if __name__=='__main__':sys.exit(0 if main()else 1)
