# FOULWAKE Görsel Sistem

**Durum:** v2.7 DRAFT / OWNER-REJECTED / VISUAL PRODUCTION PAUSED  
**Güncel yetki:** `governance/CURRENT_STAGE.json`  
**Mekanik baseline:** v2.6 STABLE / LOCKED  
**Sanat Yönetimi:** `visual/art_direction/FOULWAKE_ART_DIRECTOR_WORK_ORDER_v2.7.md`  
**Bağlayıcı rework:** `visual/FOULWAKE_FULL_DECK_ART_REWORK_DIRECTIVE_v2.7.md`  
**Kapsam:** 121 kartın bütün ön/arka yüzleri ve 29 sayfalık kural kitabı

Bu dosya ortak sanat, yerleşim ve baskı sistemini tanımlar. Kart başına üretim,
arka-yüz topolojisi, pilot ve QA ayrıntılarında rework direktifi üstündür.
`work/v2.7-visual@e91581...` teslimindeki sanat ve önceki “onaylı örnekler”
reddedilmiştir; yalnız teknik üretim hattı tarihidir.

## 1. Kaynak sözleşmesi

1. Güncel görev/yazma yetkisi: `governance/CURRENT_STAGE.json`.
2. Değişmeyen mekanik/kimlik/adet/effect/zamanlama/deste davranışı/kural akışı:
   `releases/v2.6/` ve `AI_HANDOFF.md`.
3. 20 Karakter + 30 Güç görünen metni:
   `FOULWAKE_CARD_TEXTS_v2.7.json`.
4. Tanımlı rulebook anlatı blokları:
   `FOULWAKE_RULEBOOK_STORY_v2.7.md`.
5. Ton/lore çiti: `FOULWAKE_STORY_FRAMEWORK.md`.
6. Sanat Yönetmeni yaratıcı rolü ve inceleme yöntemi:
   `visual/art_direction/FOULWAKE_ART_DIRECTOR_WORK_ORDER_v2.7.md`.
7. En yeni sanat kararı:
   `visual/FOULWAKE_FULL_DECK_ART_REWORK_DIRECTIVE_v2.7.md`.
8. Ortak yerleşim/baskı standardı: bu dosya.

Çelişki otomatik seçilmez; üretim durur ve exact alanla Baş Editöre handoff
edilir. Özellikle `SRC-002` GUC-22/GUC-23 çelişkisi Görsel hattı tarafından
yeniden numaralandırılamaz.

## 2. Sanat dili

- Yüklenen KAPTAN kartı `SET-KP-01` için bağlayıcı ana görsel kaynaktır.
  KAPTAN figürü ve ana kart kompozisyonu korunur; yalnız küçük crop, ölçek,
  renk ve arka-plan temizliği yapılabilir. Boş sandalye veya başka özneyle
  değiştirilemez.
- Aynı görsel bütün deste için mürekkep, gravür taraması, sıcak kirli kâğıt ve
  mat lacivert–oker–pas sanat dili anahtarıdır. Gemi, martı ve aynı sahne diğer
  kartlar için zorunlu değildir.
- Elde çizilmiş mürekkep; ince karakterli kontur; çapraz tarama ve gravür
  dokusu.
- Hacim tarama/çizgiyle; sinematik boya gradyanı ve parlak yapay zekâ renderı
  olmadan kurulur.
- Mat, sınırlı palet: kâğıt, lacivert, kirli mavi-gri, pas/kahverengi; kontrollü
  hardal ve kırmızı vurgu.
- 1721 dönemi gemi/liman/giysi/araç dili; modern nesne, büyü, neon, 3B,
  fotogerçekçilik ve çocuk kitabı estetiği yok.
- Aynı çizerin tek evreni hissi vardır; aynı insan/sahne/plakanın türevleri yoktur.

## 3. Özgünlük sistemi

- 121 kartın her biri ayrı `art_brief_id` ve `original_artwork_id` alır.
- Aynı aile plakasının crop/recolor/mirror/rotate/kostüm varyasyonu kabul edilmez.
- Karakterlerde yaş, yüz geometrisi, saç/sakal, beden, siluet, poz, ifade,
  kıyafet ve mesleki el/beden izi ayrı tasarlanır.
- Diğer ailelerde kart metni/işlevi ayrı görsel olaya dönüşür; yalnız başlığı
  değişmiş ortak sahne kullanılmaz.
- `unique render SHA` dosya farkını kanıtlar; özgün sanat kanıtı değildir.
- Kör contact sheet incelemesi ve manuel semantik hüküm zorunludur.

## 4. Resim-içi yazı ve mizah

- İllüstrasyon alanında tabela, pankart, slogan, konuşma balonu, isimlik,
  açıklama, etiket veya saçma/anlamsız okunabilir yazı yoktur.
- Harita, kitap, defter, sandık/fıçı üstü ve dekor yalnız okunamayan çizgisel
  doku kullanabilir; harf/sayı/kelime üretemez.
- Okunabilir metin yalnız exact başlık, effect, flavor ve kart kimliğidir.
- Şaka zorunlu değildir; varsa karttan türeyen en fazla bir ikincil şakadır.
- Fare, martı, papağan, aynı tayfa, düşme/kayma veya çalınan nesne kalıbı
  tekrar eden maskot olamaz.

## 5. Kesin ölçüler

| Bileşen | Kesim | Taşmalı çalışma |
|---|---:|---:|
| Harita | 70 × 70 mm | 76 × 76 mm |
| Karakter | 70 × 120 mm | 76 × 126 mm |
| Poker | 63,5 × 88,9 mm | 69,5 × 94,9 mm |
| Kural kitabı | A4 | 210 × 297 mm |

Kartlar `%100` ölçekte basılır; fit-to-page kapalıdır. Her kenarda 3 mm taşma
payı vardır. Etkin çözünürlük en az 300 dpi'dır.

## 6. Kart ön yüzü

Sıra: **başlık → illüstrasyon → effect → flavor → kart kimliği**.

- Bağlayıcı metin kelimesi kelimesine kullanılır; kısaltma ve yeniden yazım yok.
- `SET-KP-01` görünen copy kaynağı
  `FOULWAKE_OWNER_CARD_TEXT_OVERRIDES_v2.7.json`dır: KAPTAN / ÖZEL YETENEK /
  “Oylamada eşitlik olursa, senin tarafın geçerli olur.” /
  “Lidere et. Gemi senin emrinde.”
- Görsel model okunabilir kart yazısı üretmez. Metin kanonik UTF-8 kaynaktan
  şablonla yerleştirilir; OCR veya render-source exact karşılaştırması
  zorunludur. Sapma `BLOCKED_COPY_DRIFT`tir.
- Başlık yüksek kontrastlı eski kâğıt şerittedir.
- İllüstrasyon en büyük alandır fakat metin kutusunu sıkıştırmaz.
- Effect ve flavor tipografik olarak açıkça ayrılır.
- Kart kimliği baskıda okunur; FOULWAKE logosu kart yüzünde kullanılmaz.
- Taşma çözümü metni budamak veya okunamayacak kadar küçültmek değildir.

## 6A. Bağımsız kadraj kapısı

Bütün ön ve arka kart illüstrasyonlarını Sanat Yönetmeni exact oran, 3 mm
taşma, 4–5 mm güvenli alan, özne ölçeği, odak, yüz/el/ana nesne kesimi,
metin alanı çakışması, thumbnail/masa-mesafesi okunurluğu ve kadraj çeşitliliği
için inceler. Görsel Tasarım kendi kadrajına PASS veremez. Yalnız
`FRAMING_PASS` veya `REFRAME_REQUIRED`; sapma
`BLOCKED_FRAMING_DRIFT`tir.

## 7. Kart arka yüzü

Arka yüz ön yüzün kopyası değil, aynı çizgi/tarama/mat palet dilinde metinsiz
bir desendir.

| Binary | Eşleme |
|---|---:|
| `BACK_CHARACTER` | 20 |
| `BACK_POWER` | 31 |
| `BACK_LOYALTY` | 15 |
| `BACK_SEA_ROCK` | 42 |
| `BACK_ISLAND` | 6 |
| `BACK_LIGHTHOUSE` | 4 |
| `BACK_SUPPORT` | 3 |

Toplam 7 binary / 121 eşleme. Aile içinde exact aynı binary; yazı/logo/etiket
yok; exact 180° yön güvenli; kesim, kenar, parlaklık, opaklık ve duplex sızıntısı
yok. BACK_SEA_ROCK mat ve ışıldamayan denizdir; BACK_ISLAND eski varlıktan
türetilmeden FULL REDRAW yapılır; BACK_LIGHTHOUSE daha büyük okunur ve uzun
kayalık sırt zorunlu değildir. Sea=Rock v2.7 DRAFT kararıdır; v2.6'nın ayrı
Kayalık arka yüzünü
değiştirmez ve tam Simülasyon + kör fiziksel test geçmeden release olamaz.

## 8. Kural kitabı

- A4 ve 29 sayfalık içerik akışı korunur.
- Mekanik tablo, şema ve hızlı referans bezeme uğruna küçültülmez.
- v2.6 mekanik sayfaları ile exact v2.7 anlatı blokları kaynak sözleşmesine göre
  yerleştirilir; metin yeniden yazılmaz.
- Kapak ve iç sanat kartlarla aynı mürekkep/gravür/palet dilindedir.
- Dekor yazısı ve tekrarlı maskot kullanılmaz.

## 9. Üretim kapısı

1. Sanat Yönetmeni dünya/doku/kompozisyon/deste ritmi omurgası.
2. 121 art brief + 7 arka-yüz briefi ve bağımsız yaratıcı brief incelemesi.
3. 12 ön-yüz pilotu + 7 arka-yüz taslağı.
4. Sanat Yönetmeni pilot tavsiyesi; ardından kullanıcı ve Baş Editör açık kabulü.
5. 121/121 tam yayılım ve Sanat Yönetmeni + kör contact sheet QA.
6. Exact source→render→PDF, metin, ölçü, DPI, glif, taşma ve duplex preflight.
7. Fiziksel baskı/kesim/ışık ve kör sızıntı testi.
8. Bağımsız Simülasyon Testi exact candidate attestation.

Sanat Yönetmeni incelemesi ile kullanıcı/Baş Editör pilot kabulü olmadan tam
üretim veya PDF yapılmaz. Eski e91581 render/PDF/hash
zinciri yeni adayda kullanılamaz.

## 10. Candidate hükmü

Güncel aktif v2.7 görsel candidate **yoktur**. Yeni candidate ancak rework
direktifindeki sanat, metin, arka-yüz, provenance, teknik ve fiziksel kanıtların
tamamı exact commite bağlandıktan, Sanat Yönetmeni yaratıcı incelemesinden
geçtikten ve proje sahibi ile Baş Editörce kabul edildikten sonra vardır.
