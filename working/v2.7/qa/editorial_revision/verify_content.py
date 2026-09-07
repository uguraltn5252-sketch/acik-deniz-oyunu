"""Verify copy completeness, preserved mechanics, source coverage and regeneration."""
import hashlib
import json
import re
from pathlib import Path
from render_texts import build

QA=Path(__file__).resolve().parent
P=QA.parent.parent
ROOT=QA.parents[3]


def check():
    cards=json.loads((P/'FOULWAKE_CARD_TEXTS_v2.7.json').read_text())
    owner=json.loads((P/'FOULWAKE_OWNER_CARD_TEXT_OVERRIDES_v2.7.json').read_text())
    inventory=json.loads((QA/'source_inventory.json').read_text())
    groups=['characters','powers','loyalties','provisions','maps','utilities']
    records=[r for group in groups for r in cards[group]]+owner['records']
    index={r['id']:r for r in records}
    assert len(index)==len(records)==121
    assert set(index)==set(inventory['baseline_records'])
    manifest=json.loads((P/'visual/art_direction/FOULWAKE_121_ART_BRIEF_MANIFEST_v2.7.json').read_text())
    manifest_ids=set(re.findall(r'"id"\s*:\s*"((?:KAR|GUC|SAD|HAR|SET|ERZ)-[^" ]+)"', json.dumps(manifest)))
    if not manifest_ids:
        manifest_ids=set(re.findall(r'"card_id"\s*:\s*"((?:KAR|GUC|SAD|HAR|SET|ERZ)-[^" ]+)"', json.dumps(manifest)))
    assert set(index)==manifest_ids, (len(manifest_ids), set(index)-manifest_ids)
    assert [len(cards[k]) for k in groups]==[20,30,15,1,52,2]
    for cid, current in index.items():
        assert current.get('name',current.get('title'))
        assert current['effect'].strip() and current['flavor'].strip()
        base=inventory['baseline_records'][cid]
        for field in ('impact','use_mode','time','start','returns_to_power_deck','score','damage','family','category'):
            if field in base:
                assert current[field]==base[field], (cid,field)
    for cid,name in {'GUC-22':'Kaptanın Çatlak Kupası','GUC-23':'Bayat Peksimet','GUC-24':'Islak Çorap'}.items():
        assert index[cid]['name']==name
    assert len({r['flavor'] for r in cards['loyalties'] if r['id'].startswith('SAD-H-')})==5
    assert len(inventory['pdf_front_crosscheck'])==70
    assert all(all(e.get('fields',{}).values()) or e.get('reviewed') for e in inventory['pdf_front_crosscheck'].values())
    before={name:(P/name).read_bytes() for name in ('FOULWAKE_KURAL_KITABI_v2.7.md','FOULWAKE_KART_METINLERI_v2.7.md')}
    build()
    assert all((P/name).read_bytes()==data for name,data in before.items()), 'Generated text was stale'
    player_text='\n'.join((P/name).read_text() for name in (*before,'FOULWAKE_RULEBOOK_STORY_v2.7.md'))
    for term in ('Siyah Mühür','Kara Mühür','Tanışma gecesi','oyuncının','konserve','kargo şubesi','geri vites'):
        assert term.casefold() not in player_text.casefold(), term
    assert '<!--' not in player_text
    story=(P/'FOULWAKE_RULEBOOK_STORY_v2.7.md').read_text()
    word_counts={}
    for section in ('3.1','3.3','3.6'):
        text=re.search(r'^## '+re.escape(section)+r' [^\n]*\n\n### OKU\n(.*?)(?=^### )',story,re.M|re.S)[1]
        word_counts[section]=len(text.split())
    changes=[]
    for cid, current in index.items():
        base=inventory['baseline_records'][cid]
        for field in ('name','title','effect','flavor'):
            if current.get(field)!=base.get(field):
                changes.append({'id':cid,'field':field,'before':base.get(field),'after':current.get(field)})
    (QA/'copy_changes.json').write_text(json.dumps({'baseline':'source_inventory.json#baseline_records','field_change_count':len(changes),'changes':changes},ensure_ascii=False,indent=2)+'\n')
    outputs=[p for p in P.glob('*.md') if p.name in ('FOULWAKE_RULEBOOK_STORY_v2.7.md','FOULWAKE_KURAL_KITABI_v2.7.md','FOULWAKE_KART_METINLERI_v2.7.md','FOULWAKE_STORY_FRAMEWORK.md')]
    outputs += [P/'FOULWAKE_CARD_TEXTS_v2.7.json',P/'FOULWAKE_OWNER_CARD_TEXT_OVERRIDES_v2.7.json',QA/'observation_engine.py',QA/'run_simulation.py',QA/'test_rules.py',QA/'simulation_results.json',QA/'simulation_games.csv']
    result={'status':'PASS / SAME_OPERATOR_CONTENT_CHECK','card_records':121,'recovered_source_records':70,'field_change_count':len(changes),'opening_block_word_counts':word_counts,'opening_three_blocks_total':sum(word_counts.values()),'previous_three_blocks_total':386,'word_count_scope':'Only the three matched OKU blocks; not total setup duration or human boredom evidence.','sha256':{str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in outputs}}
    (QA/'content_checks.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='sha256'},ensure_ascii=False))


if __name__=='__main__':check()
