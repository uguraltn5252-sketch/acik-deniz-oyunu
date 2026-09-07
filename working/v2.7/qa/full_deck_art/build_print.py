"""Extend the verified print geometry with selected full-deck artwork.

Retained pilot sources are read in place. New artwork has priority only inside
this task's directory. Canonical text and the binding captain crop are reused.
"""
from pathlib import Path
import importlib.util,json,hashlib,sys
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
R=Path(__file__).resolve().parents[4]
P=R/'working/v2.7'
OUT=P/'visual/full_deck_20260907';PDF=OUT/'pdf';PDF.mkdir(parents=True,exist_ok=True)
spec=importlib.util.spec_from_file_location('pilot_layout',P/'qa/recheck_visual/build_print.py')
layout=importlib.util.module_from_spec(spec);spec.loader.exec_module(layout)
class Sources:
 def __truediv__(self,name):
  new=OUT/'assets'/name
  return new if new.exists() else P/'visual/recheck_20260907/assets'/name
layout.ASSETS=Sources();layout.PDF=PDF;layout.OUT=OUT;layout.QA=P/'qa/full_deck_art'
def back(c,bid,x,y,w,h,bleed=True):
 pad=3*mm if bleed else 0;x-=pad;y-=pad;w+=2*pad;h+=2*pad
 path=layout.ASSETS/(bid+'.png')
 c.saveState();c.translate(x,y)
 for rot in (0,180):
  c.saveState()
  if rot:c.translate(w,h);c.rotate(180)
  clip=c.beginPath();clip.rect(0,h/2,w,h/2);c.clipPath(clip,stroke=0)
  layout.fitted_image(c,path,0,0,w,h,contain=False)
  c.restoreState()
 c.restoreState()
layout.back=back
def lighthouse():
 p=PDF/'BACK_LIGHTHOUSE.pdf'
 c=canvas.Canvas(str(p),pagesize=(76*mm,76*mm),invariant=1,pageCompression=1)
 c.setTitle('FOULWAKE - Fener ortak arka yüz - yandan görünüm')
 back(c,'BACK_LIGHTHOUSE',3*mm,3*mm,70*mm,70*mm);c.showPage();c.save()
 print(json.dumps({'file':str(p.relative_to(R)),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}))
if __name__=='__main__':
 if '--lighthouse' in sys.argv:lighthouse()
 else:raise SystemExit('Full deck builder is completed after all selected artwork is present.')
