"""Persist manually inspected generated assets and their exact provenance."""
from pathlib import Path
import sys,json,shutil,hashlib,subprocess
from PIL import Image
R=Path(__file__).resolve().parents[4]
OUT=R/'working/v2.7/visual/full_deck_20260907'
def main():
 data=json.loads(sys.argv[1]);f=OUT/'prompts.json';doc=json.loads(f.read_text())
 plan={x['id']:x for x in json.loads((OUT/'generation_plan.json').read_text())['records']}
 results=[]
 for a in data:
  s=plan.get(a['id'],{});src=Path(a['source_generated_path']);raw=src.read_bytes()
  a.setdefault('prompt',s.get('prompt'));a.setdefault('references',s.get('references',[]))
  a['sha256']=hashlib.sha256(raw).hexdigest();a['pixel_size']=list(Image.open(src).size)
  a['git_blob']=subprocess.check_output(['git','hash-object',str(src)],cwd=R,text=True).strip()
  if a['review_status']=='SAME_OPERATOR_SELECTED_FOR_LAYOUT':
   a['asset_path']=s.get('asset_path',a.get('asset_path'))
   p=R/a['asset_path'];assert not p.exists(),'Do not silently overwrite a selected source'
   shutil.copyfile(src,p)
  doc['records'].append(a);results.append({k:a[k]for k in ['id','review_status','git_blob','sha256','pixel_size']})
 f.write_text(json.dumps(doc,ensure_ascii=False,indent=2)+'\n');print(json.dumps(results))
if __name__=='__main__':main()
