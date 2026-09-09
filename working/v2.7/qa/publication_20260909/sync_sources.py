"""Refresh current publication records without replaying historical generators."""
from pathlib import Path
import json,hashlib,subprocess,re
R=Path(__file__).resolve().parents[4];P=R/'working/v2.7';Q=Path(__file__).resolve().parent
TASK='FOULWAKE-PUBLICATION-REDESIGN-001';BASE='d4072fbff19aeae3508801b733164fdae8517e7a'
def read(f):return json.loads((P/f).read_text())
def write(f,d):(P/f).write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def blob(p):return subprocess.check_output(['git','hash-object',str(p)],cwd=R,text=True).strip()
def update():
 d=read('FOULWAKE_CARD_TEXTS_v2.7.json');o=read('FOULWAKE_OWNER_CARD_TEXT_OVERRIDES_v2.7.json')
 groups=[('Karakter',d['characters']),('Güç',d['powers']),('Sadakat',d['loyalties']),('Erzak',d['provisions']),('Harita',d['maps']),('Makam ve Liman',o['records']+d['utilities'])]
 text=['# FOULWAKE — 121 kartın metni','','**v2.7 · 9 Eylül 2026**','','Güncel kart kaynağının okunabilir dökümü. Tat metni ek kural veya görev değildir. Sadakat gerekçesi yalnız kart sahibine aittir.','']
 cards={}
 for group,records in groups:
  text+=['## '+group,'']
  for c in records:
   cards[c['id']]=c;text+=['### '+c['id']+' — '+c.get('name',c.get('title','')),'']
   meta=[label+': '+str(c[k])for k,label in [('role','İş'),('impact','Kurulum etkisi'),('use_mode','Kullanım'),('time','Zaman'),('category','Kategori'),('family','Olay'),('side','Taraf'),('place','Yer')]if k in c and c[k]!='-']
   if meta:text+=[' · '.join(meta),'']
   text+=['**Etki:** '+c['effect'],'','*'+c['flavor']+'*','']
 assert len(cards)==121
 (P/'FOULWAKE_KART_METINLERI_v2.7.md').write_text('\n'.join(text))
 e=read('FOULWAKE_EDITORIAL_DECISIONS_v2.7.json')
 e['current_revision']={'task_id':TASK,'date':'2026-09-09','authority':'governance/v4/evidence/OWNER_PUBLICATION_AUTHORITY_20260909.json','evidence':'working/v2.7/qa/publication_20260909/review.md','class':'SAME_OPERATOR_SELF_CHECK / OWNER_REVIEW_PENDING / NOT_LOCKED'}
 e['prior_revision_permalink']=f'https://github.com/uguraltn5252-sketch/acik-deniz-oyunu/blob/{BASE}/working/v2.7/FOULWAKE_EDITORIAL_DECISIONS_v2.7.json'
 for item in e['decisions']:
  if item['id']=='ED-01':item.update(subject='Malum',disposition='SUPERSEDED_BY_OWNER_CANON_20260909',decision='Malum gizli örgüttür; borç ve izinler üzerinden etkisi hissedilir. Merkezi, üyeleri ve emir zinciri açıklanmaz. Önceki adlandırma kararı Git geçmişindedir.')
  if item['id']=='ED-06':item['subject']='Örgüt anlatısındaki kesinlik sınırı'
 e['decisions']=[v for v in e['decisions']if not v['id'].startswith('PUB-')]
 e['decisions'] += [
  {'id':'PUB-01','task_id':TASK,'subject':'Kesin adlar ve anlatı işlevleri','disposition':'IMPLEMENTED','decision':'Kraliçe Tesella, Port Avanta, Santa Veda ve Malum kaynak, hikâye, kart dökümü, sanat manifesti ve PDF metinlerinde birlikte güncellenir. Arden, Veyr ve Gusto korunur. Tesella siyasi yetki taşır; Port Avanta ticaret hareketidir; Santa Veda umut ile karantina baskısını birleştirir. Malum gizli örgüttür; Gusto veya tek bir şüpheli üzerinden çözülmez.'},
  {'id':'PUB-02','task_id':TASK,'subject':'Tipografi ve yayın düzeni','disposition':'IMPLEMENTED','decision':'Tek Alegreya ailesi: karakterli başlık, okunur gövde, italik tat metni. Kartlarda sakin okuma panelleri, kitapta OKU/YAP kutuları, yinelenen tablo başlıkları, içindekiler ve kurala bağlı Harita/Ufuk şemaları. Kapakta yalnız FOULWAKE.'},
  {'id':'PUB-03','task_id':TASK,'subject':'Kimlik, özgün sanat ve baskı','disposition':'IMPLEMENTED','decision':'121 kart kimliği ve mekanik değerleri, 121 özgün ön levha ve yedi ortak arka korunur. Tek kuleli Fener ve kumlu palmiye Adası değiştirilmez. 23 yapraklık A4 uzun-kenar çift taraflı yerleşim, 3 mm taşma ve eski kesin kesim ölçüleri korunur. Kartlar tek PDF olarak teslim edilir.'}]
 write('FOULWAKE_EDITORIAL_DECISIONS_v2.7.json',e)
 m=read('visual/art_direction/FOULWAKE_121_ART_BRIEF_MANIFEST_v2.7.json')
 m.update(current_stage='PUBLICATION_20260909',authority=f'governance/v4/tasks/{TASK}.json',scope='121 original illustration plates, seven unchanged shared backs, current canon, new native typography and quiet copy panels; one A4 duplex PDF.')
 m['binding_sources']['task']=f'governance/v4/tasks/{TASK}.json'
 m['binding_sources']['owner_publication']='governance/v4/evidence/OWNER_PUBLICATION_AUTHORITY_20260909.json'
 src=P/'FOULWAKE_CARD_TEXTS_v2.7.json';m['binding_sources']['card_copy'].update(sha256=sha(src),git_blob=blob(src))
 m['global_prohibitions'][0]='No mechanic, card identity or card-count change; proper-name revision is explicitly owner-authorized.'
 for row in m['records']:
  c=cards[row['card_identity']['id']];row['exact_copy']={k:c[k]for k in ['name','title','role','place','time','effect','flavor']if k in c}
  if c['id']!='SET-KP-01':row['exact_source'].update(git_blob=blob(src),sha256=sha(src),revision_task=TASK)
  impl=row['current_implementation'];legacy={k:impl.pop(k)for k in ['complete_card_proof_sha256','status','visual_review_note','copy_geometry']if k in impl}
  if legacy:impl['original_art_review']=legacy
  impl['publication_review']='working/v2.7/qa/publication_20260909/visual_review.json'
  row['current_print'].update(retained_front_art=True,retained_front=False,print_index='working/v2.7/publication_20260909/README.md',native_copy_revision=TASK)
  for key in ['source_scene_plan']:
   if key in row:
    for old,new in [('San Cordelio','Port Avanta'),('Saint Verena','Santa Veda'),('Eleonora','Tesella'),('Kuru Pay','Malum'),('Siyah Mühür','Malum'),('Kara Mühür','Malum')]:row[key]=row[key].replace(old,new)
 m['print_preparation']={'task_id':TASK,'index':'working/v2.7/publication_20260909/README.md','imposition':'working/v2.7/qa/publication_20260909/cards_manifest.json','source_imposition':'working/v2.7/qa/print_preparation_20260909/imposition_manifest.json','scope':'121 updated native fronts; original art and seven back masters retained; 46 A4 pages.'}
 write('visual/art_direction/FOULWAKE_121_ART_BRIEF_MANIFEST_v2.7.json',m)
 # These are historical art instructions, not newly accepted scenes or canon.
 for filename in ['FOULWAKE_ART_DIRECTION_BIBLE_v2.7.md','FOULWAKE_7_BACK_BRIEFS_v2.7.md','FOULWAKE_12_PILOT_PRODUCTION_BRIEFS_v2.7.md']:
  f=P/'visual/art_direction'/filename
  f.write_text('# Tarihsel sanat kaydı\n\nBu dosyanın eski içeriği güncel üretim yetkisi değildir. Özgün kayıt '+f'[Git geçmişinde](https://github.com/uguraltn5252-sketch/acik-deniz-oyunu/blob/{BASE}/working/v2.7/visual/art_direction/{filename}) korunur.\n\nGüncel [sanat yönü](FOULWAKE_CURRENT_ART_DIRECTION_v2.7.md), [121 uygulama manifesti](FOULWAKE_121_ART_BRIEF_MANIFEST_v2.7.json) ve [yayın teslimi](../../publication_20260909/README.md) kullanılır.\n\nKesin adlar: Kraliçe Tesella, Port Avanta, Santa Veda, Malum.\n')
 print({'card_records':len(cards),'updated_manifest_records':len(m['records'])})
if __name__=='__main__':update()
