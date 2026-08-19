from pathlib import Path
from hashlib import sha256
from pypdf import PdfReader
import re, sys, logging
logging.getLogger('pypdf').setLevel(logging.ERROR)

ROOT=Path(__file__).resolve().parent
RULE=ROOT/'OYUN_Kural_Kitabi_v2.6_DRAFT.pdf'
CARDS=ROOT/'OYUN_Kartlar_A4_Prototip_v2.6_DRAFT.pdf'
BASE=ROOT/'MEKANIK_BASELINE_OYUN_SIMULASYON_PAKETI_v2.5.zip'
EXPECTED_RULE='f369d6947dc22afde0af4bdeb72e00fa48ca26f072c49f025b97b8d071e0347d'
EXPECTED_CARDS='73b88869609076aec8690ecc7812f00ba26a6226a7af94b3db7725af30874382'
EXPECTED_BASE='975dd77d435a835fcf3faa864c5624b0542fadb419fa7d34217ed32fe87aa046'

def h(p):
    x=sha256()
    with p.open('rb') as f:
        for b in iter(lambda:f.read(1024*1024),b''): x.update(b)
    return x.hexdigest()

def txt(p): return '\n'.join((x.extract_text() or '') for x in PdfReader(str(p)).pages)

fail=[]
for p in [RULE,CARDS,BASE]:
    if not p.exists(): fail.append('missing '+p.name)
if fail:
    print('SONUC: FAIL'); [print('-',x) for x in fail]; sys.exit(1)
if h(RULE)!=EXPECTED_RULE: fail.append('rulebook hash changed')
if h(CARDS)!=EXPECTED_CARDS: fail.append('card hash changed')
if h(BASE)!=EXPECTED_BASE: fail.append('v2.5 baseline hash changed')
rr=PdfReader(str(RULE)); cr=PdfReader(str(CARDS))
if len(rr.pages)!=29: fail.append('rulebook page count')
if len(cr.pages)!=34: fail.append('card page count')
rt,ct=txt(RULE),txt(CARDS)
chars=set(re.findall(r'\bKAR-\d{2}\b',ct))
powers=set(re.findall(r'\bGUC-(?:01[AB]|02[AB]|(?:0[3-9]|1\d|2[0-8]))\b',ct))
erzak=set(re.findall(r'\bERZ-01\b',ct))
loys=set(re.findall(r'\bSAD-[TH]-\d{2}\b',ct))
maps=set(re.findall(r'\bHAR-(?:AD|KY|AA|FN)-\d{2}\b',ct))
helpers=set(re.findall(r'\bSET-(?:KL|VL|KP)-01\b',ct))
exp_chars={f'KAR-{i:02d}' for i in range(1,21)}
exp_powers={'GUC-01A','GUC-01B','GUC-02A','GUC-02B'}|{f'GUC-{i:02d}' for i in range(3,29)}
exp_loys={f'SAD-T-{i:02d}' for i in range(1,11)}|{f'SAD-H-{i:02d}' for i in range(1,6)}
exp_maps={f'HAR-AD-{i:02d}' for i in range(1,31)}|{f'HAR-KY-{i:02d}' for i in range(1,13)}|{f'HAR-AA-{i:02d}' for i in range(1,7)}|{f'HAR-FN-{i:02d}' for i in range(1,5)}
if chars!=exp_chars: fail.append('characters mismatch')
if powers!=exp_powers: fail.append('powers mismatch')
if erzak!={'ERZ-01'}: fail.append('ERZ-01 mismatch')
if loys!=exp_loys: fail.append('loyalties mismatch')
if maps!=exp_maps: fail.append('maps mismatch')
if helpers!={'SET-KL-01','SET-VL-01','SET-KP-01'}: fail.append('helper cards mismatch')
if len(chars)+len(powers)+len(erzak)+len(loys)+len(maps)!=118: fail.append('main total != 118')
for stale in ['Kaptanın Abarttığı Kayalık','Kaptan-ı Deryanın Eski Faturası']:
    if stale in ct: fail.append('stale hidden text: '+stale)
for m in ['Bu gece saldırı yok','Kaptanın rota oyu 2','Kalkış Limanı kartını alt kenarın hemen dışında','Varış Limanı kartını Haritanın üst kenarında','ayrı işaretle değil, Moderatör notuyla takip edilir','Atmosfer Moderatörden gelir; şüphe oyunculardan']:
    if m not in rt: fail.append('rule marker missing: '+m)
print('SONUC:', 'PASS' if not fail else 'FAIL')
print('RULE_PAGES',len(rr.pages),'CARD_PAGES',len(cr.pages))
print('MAIN_IDS',len(chars)+len(powers)+len(erzak)+len(loys)+len(maps),'HELPERS',len(helpers),'PHYSICAL_TOTAL',121)
print('RULE_SHA256',h(RULE)); print('CARD_SHA256',h(CARDS)); print('BASELINE_SHA256',h(BASE))
print('STALE_HIDDEN_TEXT','PASS' if not any(s in ct for s in ['Kaptanın Abarttığı Kayalık','Kaptan-ı Deryanın Eski Faturası']) else 'FAIL')
if fail:
    [print('-',x) for x in fail]; sys.exit(1)
