# FOULWAKE v2.7 — Tam Deste Görsel Rework Pilotu

Durum: `PILOT_DELIVERED / PENDING_PROJECT_OWNER_AND_CHIEF_EDITOR_ACCEPTANCE`

Bu teslim yalnız pilot kapısıdır. Kalan 109 ön yüz, tam kart PDF'si, tam kural kitabı entegrasyonu ve Simülasyon Testi başlatılmamıştır.

## Teslim kapsamı

- 121/121 kart için kısa ve semantik olarak ayrı art brief
- 12 özgün pilot ön yüz: 3 Karakter, 2 Güç, 1 Çürümüş Erzak, 1 Sadakat, 1 Açık Deniz, 1 Kayalık, 1 Ada, 1 Deniz Feneri, 1 yardımcı kart
- 7 metinsiz binary arka yüz ve 121 kartlık eşleme
- 12 ön yüz contact sheeti
- 7 arka yüz contact sheeti
- Başlık, kart metni ve kimlik alanları kapatılmış semantik karşılaştırma contact sheeti
- Kaynak sanat → 300 dpi kart renderı için SHA-256, byte, ölçü ve exact visible-copy kaydı

## Bağlayıcı kontroller

- KAPTAN görseli yalnız `STYLE_ONLY` kullanıldı; karakter, yüz, beden, poz, kompozisyon, kadraj, nesne, dekor, çizgi veya piksel kopyalanmadı.
- `work/v2.7-visual@e91581bb336dfcbab5da1d48a256577f9251f891` reddedilmiş sanat varlıkları üretim girdisi yapılmadı.
- Karakter ve Güç metinleri `working/v2.7/FOULWAKE_CARD_TEXTS_v2.7.json` / blob `38a03b71cd3232fd844db8d80d8e53662510b6a3` üzerinden exact taşındı.
- `text_in_illustration=false`: 12 ön ve 7 arka kaynak sanatında okunabilir yazı bulunmuyor. İlk Pusula üretimindeki kadran harfleri yakalanıp yalnız bu alan temizlenerek yeniden doğrulandı.
- `rejected_asset_reused=false`: hash karşılaştırması yalnız yardımcı kontroldür; semantik özgünlük ayrıca metinsiz contact sheet üzerinden incelendi.
- 7 arka yüzün her biri piksel düzeyinde exact 180° güvenlidir.
- Açık Deniz ve Kayalık 42 kartta aynı `BACK_SEA_ROCK` binary varlığına bağlıdır.

## Arka yüz eşleme

| Binary | Kart |
|---|---:|
| `BACK_CHARACTER` | 20 |
| `BACK_POWER` | 31 |
| `BACK_LOYALTY` | 15 |
| `BACK_SEA_ROCK` | 42 |
| `BACK_ISLAND` | 6 |
| `BACK_LIGHTHOUSE` | 4 |
| `BACK_SUPPORT` | 3 |

Toplam: 7 binary / 121 eşleme.

## Açık riskler ve kapalı üretim kapısı

- Proje Sahibi ve Baş Editör pilotu henüz kabul etmedi.
- Fiziksel baskı, kesim, duplex hizalama, ışık sızıntısı ve kör yön-sızıntı testleri çalıştırılmadı.
- İngilizce-only OCR ve gravür dokusu sahte glif sonuçları ürettiği için illüstrasyon içi yazı kontrolü OCR'a tek başına bırakılmadı; büyütülmüş manuel inceleme ile tamamlandı.
- Kullanıcı ve Baş Editör açık kabul vermeden kalan 109 ön yüz, tam PDF ve Simülasyon Testi kapalıdır.

`LOCK_REQUESTED: NO`
