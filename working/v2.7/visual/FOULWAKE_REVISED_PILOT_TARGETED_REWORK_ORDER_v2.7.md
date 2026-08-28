# FOULWAKE Revize Pilot — Hedefli Rework İş Emri v2.7

**Durum:** AUTHORIZED / PILOT ONLY / RELEASE BLOCKED  
**Baş Editör baz kaynağı:** `v2.7-design@6cbdeacc4618332d6e8efc03a7558b0b7c5bf799`  
**Kabul edilmiş Sanat Yönetimi:** `work/v2.7-art-direction@7418d9c2c89c265cb6efd30f6a5a7f2addd528da`  
**İncelenen Görsel:** `work/v2.7-visual@1b27232a53b09ac3ff00030f625bfc2703d15764`  
**İnceleme kanıtı:** `governance/ART_DIRECTION_REVISED_PILOT_REVIEW_20260828.json`  
**Uygulama dalı:** `work/v2.7-visual`  
**Resmî görünür sohbet:** `FOULWAKE Görsel Tasarım 2`  
**Baseline:** `v2.6 STABLE / LOCKED`

Bu iş emri, revize kabul edilmiş-12 pilot incelemesindeki
`REWORK_REQUIRED` kararını uygular. Mevcut pilot kabul edilmez; yalnız
aşağıdaki dar pilot rework kapsamı açılır. Tam 121, PDF, Simülasyon, release
ve kilit yetkili değildir.

## 1. Byte-exact KEEP

Şu 15 ana görsel ve source-art kayıtları değiştirilmez:

- Önler: `KAR-06`, `KAR-19`, `GUC-06`, `GUC-27`, `ERZ-01`, `SAD-H-03`, `HAR-AD-08`, `HAR-KY-06`, `HAR-FN-04`, `SET-KP-01`.
- Arkalar: `BACK_CHARACTER`, `BACK_POWER`, `BACK_LOYALTY`, `BACK_SEA_ROCK`, `BACK_SUPPORT`.

Diğer dokuz başarılı sketch gate de byte-exact korunur.
`HAR-AA-06_three_thumbnail_gate.jpg` içindeki kabul edilebilir kapalı-sepet
yönü finale taşınır; bu gate yeniden çizilmez ve seçilen yön provenance
kaydında belirtilir.

## 2. Yetkili dört ana rework

### KAR-01

Değişir: `pilot_fronts/KAR-01_front.png`,
`source_art/KAR-01_illustration.jpg`,
`sketch_gates/KAR-01_three_thumbnail_gate.jpg`.

Çok uzun kırklı kadın gözcü, ana direk çarmıhı ve geniş gök korunur. Heykelsi
kahraman profili kalkar. Sağ omuz halat yüküyle düşer; gövde armaya fiziksel
ağırlık verir. Çıplak göz ve küçük baş eğimi, kart boyunda seçilen tek ince
hardal değer kırılmasına kilitlenir. Dürbün, işaret parmağı, kuş ve
doğaüstü göz efekti yoktur. Yeni gate üç aynı kadraj varyasyonu değil, üç ayrı
göz–omuz–halat beden geometrisidir.

### HAR-AA-06

Değişir: `pilot_fronts/HAR-AA-06_front.png`,
`source_art/HAR-AA-06_illustration.jpg`.

Altı ayrı beden, tek odalı gümrük kulübesi, uzun masa, küçük yüz-kılsız memur
ve kapalı hasır sepet korunur. Seçen el doğrudan sepet kapağına gider; fazla
nesne dar kapak aralığından aşağı geçerken görünür, iç görünmez. Her kişi için
tek kalan nesne sahibiyle hizalanır. Masa üstü tartım/inceleme puku kaldırılır.
Memurun kendi fazla nesnesi aynı kapağın altında tek küçük maddi izdir; ikinci
şaka yoktur.

### BACK_ISLAND

Değişir: `pilot_backs/BACK_ISLAND.png`,
`source_art/BACK_ISLAND_source.jpg`.

`BACK_SEA_ROCK` deniz ölçeği/kenar değerleri kullanılır. Alçak isimsiz kara
omurgası asimetrikleşir. Tam çevre köpük halkası kalkar; köpük yalnız iki küçük
koy ve rüzgâr alan taşlarda kesintilidir. Deniz dört kenara sürer; temiz grafik
boşluk, yapı, insan, ürün, özel bitki ve exact ada özelliği yoktur.

### BACK_LIGHTHOUSE

Değişir: `pilot_backs/BACK_LIGHTHOUSE.png`,
`source_art/BACK_LIGHTHOUSE_source.jpg`.

Dairesel islet ve konsantrik surf sıfırdan değiştirilir. Çok dik kuşbakışında,
dönüş merkezinden geçen alçak çapraz kaya sırtına gömülü küçük sade çokgen
yığma-taş kule kurulur. Sırt iki yönde sahneyi genişletir. Işın, glow, halka,
yuvarlak lens, Fresnel/Argand, modern beacon ve özel ateş davranışı yoktur.
Dört kenar denizi `BACK_SEA_ROCK` değer/çizgi zarfındadır.

## 3. Zorunlu türev kanıt

Dört reworkten sonra kimlik, konum, rastgele 180° yön ve üç geometri
değişmeden yeniden türetilir:

- `contact_sheets/` altında 5/5 sheet;
- `map_layouts/` altında kompakt, uzayan ve düzensiz/dallanan düzenlerin
  kapalı/kısmen açık 6/6 rasterı.

Yeni grid, kart sayısı, mekanik, yerleşim kuralı veya dördüncü geometri yoktur.

## 4. Rapor ve provenance

Yeni hash/kaynak ilişkileriyle güncellenir:

- `FOULWAKE_ACCEPTED_12_CARD_PILOT_REWORK_v2.7.md`
- `manifests/FOULWAKE_ACCEPTED_12_PILOT_ART_BRIEF_MANIFEST_v2.7.json`
- `manifests/FOULWAKE_ACCEPTED_PILOT_CONTROL_CHECKS_v2.7.json`
- `manifests/FOULWAKE_ACCEPTED_PILOT_PROVENANCE_v2.7.json`
- `manifests/FOULWAKE_ACCEPTED_PILOT_SHA256SUMS_v2.7.txt`

Exact metin, kimlik, frame, mekanik, effect, flavor, zamanlama, deste davranışı,
lore ve arka-yüz adetleri değişmez.

## 5. Exact değişiklik bütçesi

`CHANGED_FILES`: **25** — 4 ana render, 4 source-art, 1 `KAR-01` gate,
5 contact sheet, 6 map-layout, 1 rapor ve 4 manifest/kanıt.

`HAR-AA-06` gate'i veya başka KEEP/gate değişirse
`BLOCKED_SCOPE_DRIFT` olur; yeni Baş Editör emri olmadan kapsam genişlemez.

## 6. Yeniden çalıştırılacak kontroller

12/12 exact metin; ön-yüz bağlayıcı fiil; 7/7 aynı-binary ve exact/sanatsal
180°; Sea/Rock subtype körlüğü; Ada/Fener aile görünürlüğü ile exact kimlik ve
sonuç körlüğü; dört kenarda ortak deniz; masa mesafesinde halo/rozet yokluğu;
3 geometri/6 layout; resim-içi yazı/glyph yokluğu; KAPTAN STYLE_ONLY; 1721;
mat indigo–oker mürekkep/tarama; SHA-256 ve source→render→sheet/layout
provenance; `.writing.png=0`.

## 7. Yasak kapsam

Kalan 109 ön, tam 121, tam PDF, Simülasyon, `main`, `v2.6`,
`releases/**`, governance, kilit, exact metin/mekanik/lore değişikliği ve
geçici alt ajan yasaktır.

## 8. Zorunlu görünür handoff

```text
WORKSTREAM: Görsel Tasarım
VISIBLE_CHAT: FOULWAKE Görsel Tasarım 2
VISIBLE_CHAT_ACK: YES
EVIDENCE_TYPE: VISIBLE_CHAT_WORKSTREAM
SOURCE_BRANCH: work/v2.7-visual
SOURCE_COMMIT: <40_HEX>
CHIEF_EDITOR_SOURCE: <BU_İŞ_EMRİNİ_İÇEREN_v2.7-design_COMMIT>
ART_DIRECTION_REVIEW_EVIDENCE: governance/ART_DIRECTION_REVISED_PILOT_REVIEW_20260828.json
INPUT_VISUAL_COMMIT: 1b27232a53b09ac3ff00030f625bfc2703d15764
BASELINE_RELEASE: v2.6 STABLE / LOCKED
PILOT_OR_FULL: PILOT_ONLY
SCOPE: Dört ana görsel ve bağlı pilot kanıtlarının hedefli reworkü
CHANGED_FILES: 25
BYTE_EXACT_KEEP_VERIFIED: YES — 15 ana KEEP ve 9 korunmuş gate
PROTECTED_FIELDS_CONFIRMED: YES
TESTS_RUN: <EXACT_KONTROLLER>
TEMPORARY_SUBAGENTS: NONE
FULL_121_PRODUCTION_AUTHORIZED: NO
SIMULATION_AUTHORIZED: NO
RESULT: TARGETED_PILOT_REWORK_DELIVERED / PENDING_ART_DIRECTION_PROJECT_OWNER_AND_CHIEF_EDITOR_ACCEPTANCE
OPEN_RISKS: Fiziksel baskı/kesim/duplex/ışık/masa-mesafesi ve SRC-002 açık
NEXT_RECIPIENT: Baş Editör
LOCK_REQUESTED: NO
```

GitHub commit/push görünür handoff değildir.
