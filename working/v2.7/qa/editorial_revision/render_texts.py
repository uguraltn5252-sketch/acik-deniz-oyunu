"""Build readable, complete cards and rulebook from the editable copy sources."""
import json
import re
from pathlib import Path

QA = Path(__file__).resolve().parent
ROOT = QA.parent.parent


def build():
    data = json.loads((ROOT / 'FOULWAKE_CARD_TEXTS_v2.7.json').read_text())
    overrides = json.loads((ROOT / 'FOULWAKE_OWNER_CARD_TEXT_OVERRIDES_v2.7.json').read_text())
    story = (ROOT / 'FOULWAKE_RULEBOOK_STORY_v2.7.md').read_text()
    sections = {}
    for match in re.finditer(r'^## ([\d.]+) [^\n]+\n(.*?)(?=^## |\Z)', story, re.M | re.S):
        sections[match[1].rstrip('.')] = match[2].strip()

    def read_block(key):
        return '**OKU**\n\n' + sections[key].split('### OKU\n', 1)[1].split('\n### ', 1)[0].strip()

    book = (QA / 'rulebook_template.md').read_text()
    for key in ['3.1', '3.3', '3.5', '3.6', '3.7', '3.8']:
        book = book.replace('<!-- STORY:' + key + ' -->', read_block(key))
    endings = dict(re.findall(r'^### OKU - ([^\n]+)\n(.*?)(?=^### |\Z)', sections['4.4'], re.M | re.S))
    book = book.replace('<!-- STORY:4.4:LİMAN -->', '**OKU**\n\n' + endings.pop('LİMAN').strip())
    book = book.replace('<!-- STORY:4.4:KAPANIŞLAR -->', '\n\n'.join('**OKU - ' + k + '**\n\n' + v.strip() for k, v in endings.items()))
    for key in ['5.3', '17']:
        book = book.replace('<!-- STORY:' + key + ' -->', sections[key])

    def cell(value):
        return str(value).replace('|', '\\|').replace('\n', ' ')

    def table(headers, rows):
        return '\n'.join(['| ' + ' | '.join(headers) + ' |', '| ' + ' | '.join('---' for _ in headers) + ' |'] + ['| ' + ' | '.join(cell(v) for v in row) + ' |' for row in rows])

    grouped = {}
    for card in data['maps']:
        grouped.setdefault((card['category'], card['family'], card['effect']), []).append(card['id'])
    book = book.replace('<!-- MAP_REFERENCE -->', table(['Kategori / olay ailesi', 'Adet', 'Olay'], [(cat + ' / ' + fam, len(ids), effect) for (cat, fam, effect), ids in grouped.items()]))
    book = book.replace('<!-- CHARACTER_REFERENCE -->', table(['Kimlik / Karakter', 'Etki / kullanım', 'Yetenek'], [(c['id'] + ' - ' + c['name'], str(c['impact']) + ' / ' + c['use_mode'], c['effect']) for c in data['characters']]))
    book = book.replace('<!-- POWER_REFERENCE -->', table(['Kimlik / Güç', 'Zaman', 'Etki'], [(c['id'] + ' - ' + c['name'], c['time'], c['effect']) for c in data['powers']]))
    assert '<!--' not in book, 'Unresolved rulebook placeholder'
    (ROOT / 'FOULWAKE_KURAL_KITABI_v2.7.md').write_text(book)

    text = ['# FOULWAKE - 121 kartın metni', '', '**v2.7 çalışma sürümü · 8 Eylül 2026**', '', 'Bu belge kart metinlerinin okunabilir dökümüdür; baskı yerleşimi değildir. Tat metinleri ek kural veya görev vermez. Sadakat gerekçeleri yalnız kart sahibine aittir. Kimlikler korunmuştur.', '']
    groups = [('Karakter', data['characters']), ('Güç', data['powers']), ('Sadakat', data['loyalties']), ('Erzak', data['provisions']), ('Harita', data['maps']), ('Makam ve Liman', overrides['records'] + data['utilities'])]
    ids = []
    for name, cards in groups:
        text += ['## ' + name, '']
        for card in cards:
            ids.append(card['id'])
            text += ['### ' + card['id'] + ' - ' + card.get('name', card.get('title', '')), '']
            meta = []
            for key, label in [('role', 'İş'), ('impact', 'Kurulum etkisi'), ('use_mode', 'Kullanım'), ('time', 'Zaman'), ('category', 'Kategori'), ('family', 'Olay'), ('side', 'Taraf')]:
                if key in card:
                    meta.append(label + ': ' + str(card[key]))
            if meta:
                text += [' · '.join(meta), '']
            text += ['**Etki:** ' + card['effect'], '', '*' + card['flavor'] + '*', '']
    assert len(ids) == len(set(ids)) == 121
    (ROOT / 'FOULWAKE_KART_METINLERI_v2.7.md').write_text('\n'.join(text))
    return book


if __name__ == '__main__':
    book = build()
    print('Generated complete rulebook and 121 card records; rulebook words:', len(book.split()))
