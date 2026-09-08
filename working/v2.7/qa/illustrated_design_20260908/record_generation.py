"""Checkpoint a generated original without modifying its pixels."""
import argparse,hashlib,json,re,shutil
from pathlib import Path
from PIL import Image
from card_layout import QA,ASSETS,INDEX

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--id',required=True);ap.add_argument('--source',required=True);ap.add_argument('--revision',type=int,default=1);a=ap.parse_args()
    assert a.id in INDEX or a.id.startswith('BACK_')
    assert re.fullmatch(r'[A-Z0-9-]+|BACK_[A-Z_]+',a.id)
    source=Path(a.source);dest=ASSETS/(a.id+'.png')
    shutil.copy2(source,dest)
    with Image.open(dest)as im:size=list(im.size)
    prompt=QA/'prompts'/f'{a.id}.txt'
    evidence={'id':a.id,'revision':a.revision,'tool':'image_gen.imagegen','tool_model':'NOT_SELECTED_OR_VERIFIED_BY_OPERATOR','source_output':str(source),'selected_asset':str(dest),'sha256':hashlib.sha256(dest.read_bytes()).hexdigest(),'pixels':size,'planned_prompt_file':str(prompt),'planned_prompt_sha256':hashlib.sha256(prompt.read_bytes()).hexdigest()if prompt.exists()else None,'reference_role':'STYLE_ONLY / ORIGINAL_COMPLETE_CARD_PLATE','pixel_editing':'NONE / BYTE_IDENTICAL_COPY','status':'GENERATED_AWAITING_NATIVE_COPY_AND_VISUAL_QA'}
    requests=QA/'actual_requests.json'
    request=json.loads(requests.read_text()).get(a.id) if requests.exists() else None
    if request and a.revision==1:
        evidence['actual_request_file']=str(requests)
        evidence['actual_prompt_sha256']=hashlib.sha256(request['prompt'].encode()).hexdigest()
    else:evidence['actual_prompt_status']='SEE_REVISION_REQUEST_RECORD / NOT_ASSUMED_IDENTICAL_TO_PLAN'
    folder=QA/'generation';folder.mkdir(exist_ok=True)
    previous=folder/(a.id+'.json')
    if previous.exists():
        old=json.loads(previous.read_text());evidence['previous_selected_sha256']=old['sha256']
    previous.write_text(json.dumps(evidence,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'id':a.id,'pixels':size,'sha256':evidence['sha256']}))

if __name__=='__main__':main()
