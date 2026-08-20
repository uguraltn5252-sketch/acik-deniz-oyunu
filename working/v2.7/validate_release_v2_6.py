from pathlib import Path
from hashlib import sha256
import re, sys
import fitz

ROOT=Path(__file__).resolve().parent
RULE=ROOT/'OYUN_Kural_Kitabi_v2.6.pdf'
CARDS=ROOT/'OYUN_Kartlar_A4_Prototip_v2.6.pdf'
BASE=ROOT/'MEKANIK_BASELINE_OYUN_SIMULASYON_PAKETI_v2.5.zip'
EXPECTED={
    RULE.name:'192f790d89e987a312d6a36879e7b063ee13426c9508b4e474f16f2cad723c2a',
    CARDS.name:'769eaadf989b3d7e4b35ca00d62b0505bcafd7dc61174a11314b607887de9298',
    BASE.name:'975dd77d435a835fcf3faa864c5624b0542fadb419fa7d34217ed32fe87aa046'
}

def h(p):
    x=sha256()
    with p.open('rb') as f:
        for b in iter(lambda:f.read(1024*1024),b''): x.update(b)
    return x.hexdigest()

fail=[]
for p in [RULE,CARDS,BASE]:
    if not p.exists(): fail.append(f'missing {p.name}')
    elif h(p)!=EXPECTED[p.name]: fail.append(f'hash mismatch {p.name}')
if fail:
    print('SONUC: FAIL'); [print('-',x) for x in fail]; sys.exit(1)
rd=fitz.open(RULE); cd=fitz.open(CARDS)
if len(rd)!=29: fail.append(f'rule pages {len(rd)} != 29')
if len(cd)!=34: fail.append(f'card pages {len(cd)} != 34')
rt='\n'.join(p.get_text() for p in rd)
ct='\n'.join(p.get_text() for p in cd)
for forbidden in ['DRAFT','NOT LOCKED','Bu belge kilitli değildir']:
    if forbidden in rt or forbidden in ct: fail.append(f'forbidden release marker: {forbidden}')
if 'STABLE / LOCKED' not in rt: fail.append('rulebook stable marker missing')
ids=set(re.findall(r'\b(?:KAR-\d{2}|GUC-\d{2}[AB]?|ERZ-01|SAD-[TH]-\d{2}|HAR-(?:AD|KY|AA|FN)-\d{2})\b',ct))
helpers=set(re.findall(r'\bSET-(?:KL|VL|KP)-01\b',ct))
if 'AÇIK DENIZ' not in ct: fail.append('Açık Deniz category back missing')
if 'KAYALIK' not in ct: fail.append('Kayalık category back missing')
if 'Kaptanın Abarttığı Kayalık' in ct or 'Kaptan-ı Deryanın Eski Faturası' in ct: fail.append('stale hidden rock text present')
fam={
 'characters':len([x for x in ids if x.startswith('KAR-')]),
 'powers':len([x for x in ids if x.startswith('GUC-')]),
 'erzak':len([x for x in ids if x.startswith('ERZ-')]),
 'loyalties':len([x for x in ids if x.startswith('SAD-')]),
 'maps':len([x for x in ids if x.startswith('HAR-')])
}
expected={'characters':20,'powers':30,'erzak':1,'loyalties':15,'maps':52}
if fam!=expected: fail.append(f'card family counts {fam} != {expected}')
if helpers!={'SET-KL-01','SET-VL-01','SET-KP-01'}: fail.append(f'helper ids {helpers}')
if fail:
    print('SONUC: FAIL'); [print('-',x) for x in fail]; sys.exit(1)
print('SONUC: PASS')
print('RULE_PAGES',len(rd),'CARD_PAGES',len(cd))
print('COUNTS',fam,'HELPERS',sorted(helpers),'PRINTABLE_TOTAL',sum(fam.values())+len(helpers))
print('RULE_SHA256',h(RULE))
print('CARD_SHA256',h(CARDS))
print('BASELINE_SHA256',h(BASE))
print('ROCK_BACK_POLICY','PASS - KAYALIK distinct from AÇIK DENIZ')
print('STALE_HIDDEN_TEXT','PASS')
