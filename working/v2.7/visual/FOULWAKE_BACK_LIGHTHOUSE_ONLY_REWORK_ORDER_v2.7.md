# FOULWAKE BACK_LIGHTHOUSE-Only Pilot Rework Order v2.7

**Status:** AUTHORIZED / ONE PRIMARY ASSET ONLY / RELEASE BLOCKED  
**Chief Editor base:** `v2.7-design@74ac7eb764089a894b109990c1bc10304b7a614d`  
**Art Direction source:** `work/v2.7-art-direction@7418d9c2c89c265cb6efd30f6a5a7f2addd528da`  
**Reviewed Visual head:** `work/v2.7-visual@0cb2bd6f03e2d84948741c162f22b8fd2ff064ad`  
**Canonical targeted delivery:** `88907294edd326c118573f5ada7406e5fc42ee4d`  
**Review evidence:** `governance/ART_DIRECTION_LIGHTHOUSE_ONLY_REVIEW_20260830.json`  
**Work branch:** `work/v2.7-visual`  
**Official visible chat:** `FOULWAKE Görsel Tasarım 2`  
**Baseline:** `v2.6 STABLE / LOCKED`

Bu emir, dört ana görselli reworkün üç kabulünü dondurur. Yalnız
`BACK_LIGHTHOUSE` ve doğrudan bağlı kanıtları değişebilir. Pilot hâlâ sanat
adayı değildir; tam 121, PDF, Simülasyon, release ve kilit yetkili değildir.

## 1. Yeni kabul edilen üç rework — byte-exact dondur

Aşağıdakiler yeniden üretilmez veya rötuşlanmaz:

- `pilot_fronts/KAR-01_front.png`
- `source_art/KAR-01_illustration.jpg`
- `sketch_gates/KAR-01_three_thumbnail_gate.jpg`
- `pilot_fronts/HAR-AA-06_front.png`
- `source_art/HAR-AA-06_illustration.jpg`
- `sketch_gates/HAR-AA-06_three_thumbnail_gate.jpg`
- `pilot_backs/BACK_ISLAND.png`
- `source_art/BACK_ISLAND_source.jpg`

Önceden kabul edilmiş diğer bütün ana görseller ve kaynaklar da korunur.
Bu turda toplam 18/19 ana görsel, 16/17 source-art ve 10/10 sketch gate
`0cb2bd6f03e2d84948741c162f22b8fd2ff064ad` commitine göre byte-exact kalmalıdır.

## 2. Yetkili tek ana rework

Yalnız şu iki ana dosya değişir:

- `pilot_backs/BACK_LIGHTHOUSE.png`
- `source_art/BACK_LIGHTHOUSE_source.jpg`

Mevcut ortak deniz, alçak çapraz kaya sırtı ve ölçülü/kesintili köpük dili
korunur. Merkezdeki yığma-taş kule; normal dijital masa-layout kanıtında
çokgen duvarları ile sade üst ateş/seyir haznesi seçilecek kadar büyütülür ve
değer olarak kaya sırtından ayrılır.

Fener, 1721'e uygun anonim bir seyir yapısı olarak okunmalıdır; kaya,
kulübe veya kapstan gibi görünmemelidir. Aile görünür kalır fakat exact ön
fener kimliği ve sonuç bilgisi gizlidir.

Şunlar kesinlikle eklenmez:

- ışın, glow veya halo;
- Fresnel/Argand, yuvarlak lens veya modern beacon;
- dairesel platform/islet, konsantrik surf, hedef/rozet;
- amblem, madalyon veya exact ön fener özelliği.

Yeni bir fener konsepti kurulmaz; mevcut çapraz-sırt çözümünün ölçek, değer ve
okunurluğu düzeltilir.

## 3. Yalnız etkilenen türev kanıtları yeniden üret

Değişecek contact sheetler:

- `contact_sheets/FOULWAKE_ACCEPTED_7_BACKS_CONTACT_SHEET_v2.7.png`
- `contact_sheets/FOULWAKE_3_VARIABLE_MAP_LAYOUTS_CONTACT_SHEET_v2.7.png`

Değişecek map-layout rasterları:

- `FOULWAKE_VARIABLE_MAP_COMPACT_CLUSTER_CLOSED_v2.7.png`
- `FOULWAKE_VARIABLE_MAP_COMPACT_CLUSTER_PARTIALLY_OPEN_v2.7.png`
- `FOULWAKE_VARIABLE_MAP_ELONGATED_ROUTE_CLOSED_v2.7.png`
- `FOULWAKE_VARIABLE_MAP_ELONGATED_ROUTE_PARTIALLY_OPEN_v2.7.png`
- `FOULWAKE_VARIABLE_MAP_IRREGULAR_BRANCH_CLOSED_v2.7.png`
- `FOULWAKE_VARIABLE_MAP_IRREGULAR_BRANCH_PARTIALLY_OPEN_v2.7.png`

Kart kimlikleri, hücreleri, açık/kapalı durumları, rastgele 180° yönleri ve
üç geometri exact korunur.

Şu üç contact sheet byte-exact kalır:

- `FOULWAKE_ACCEPTED_12_PILOT_FRONTS_CONTACT_SHEET_v2.7.png`
- `FOULWAKE_ACCEPTED_12_PILOT_SEMANTIC_BLIND_CONTACT_SHEET_v2.7.png`
- `FOULWAKE_ACCEPTED_10_REDRAW_THUMBNAIL_GATES_v2.7.png`

## 4. Rapor ve dört kanıt kaydı

Yeni exact hash/provenance ile güncellenir:

- `FOULWAKE_ACCEPTED_12_CARD_PILOT_REWORK_v2.7.md`
- `manifests/FOULWAKE_ACCEPTED_12_PILOT_ART_BRIEF_MANIFEST_v2.7.json`
- `manifests/FOULWAKE_ACCEPTED_PILOT_CONTROL_CHECKS_v2.7.json`
- `manifests/FOULWAKE_ACCEPTED_PILOT_PROVENANCE_v2.7.json`
- `manifests/FOULWAKE_ACCEPTED_PILOT_SHA256SUMS_v2.7.txt`

## 5. Exact değişiklik bütçesi

`CHANGED_FILES: 15`

- 1 lighthouse source-art
- 1 lighthouse render
- 2 contact sheet
- 6 map-layout rasterı
- 1 teslim raporu
- 4 manifest/checksum/provenance kaydı

Başka dosya değişirse teslim `BLOCKED_SCOPE_DRIFT` olur. Değiştirilen
dosyayı geri yazmaya çalışma; Baş Editöre exact farkı bildir.

## 6. Zorunlu kontroller

- `BACK_LIGHTHOUSE` 300 dpi ve exact 180° piksel güvenliği
- 4/4 Fener arka eşlemesi ve toplam 121 topolojisi
- BACK_SEA_ROCK ile dört kenarda ortak deniz değer/çizgi zarfı
- iki contact sheet ve altı layoutta normal dijital masa mesafesinde güvenilir
  Fener ailesi okunurluğu
- kaya/kulübe/kapstan yanlış sınıflandırmasının kalkması
- exact ön fener ve sonuç körlüğü
- ışın/glow/halo/lens/modern beacon/rozet yokluğu
- 18/18 ana KEEP, 16/16 source-art, 10/10 gate ve 3/3 etkilenmeyen sheet
  byte-exact
- SHA-256 ve source→render→sheet/layout provenance
- `.writing.png=0`
- fiziksel testler `NOT_RUN` olarak dürüstçe korunur

## 7. Yasak kapsam

KAR-01, HAR-AA-06, BACK_ISLAND veya başka KEEP rötuşu; yeni gate; diğer
contact sheetler; yeni map geometrisi; kalan 109 ön; tam 121; tam PDF;
Simülasyon; governance; `main`; `v2.6`; `releases/**`; lock; exact
metin/mekanik/lore değişikliği ve geçici alt ajan yasaktır.

## 8. Zorunlu görünür handoff

```text
WORKSTREAM: Görsel Tasarım
VISIBLE_CHAT: FOULWAKE Görsel Tasarım 2
VISIBLE_CHAT_ACK: YES
EVIDENCE_TYPE: VISIBLE_CHAT_WORKSTREAM
SOURCE_BRANCH: work/v2.7-visual
SOURCE_COMMIT: <40_HEX>
CANONICAL_DELIVERY_COMMIT: <40_HEX>
CHIEF_EDITOR_SOURCE: <BU_İŞ_EMRİNİ_İÇEREN_v2.7-design_COMMIT>
ART_DIRECTION_REVIEW_EVIDENCE: governance/ART_DIRECTION_LIGHTHOUSE_ONLY_REVIEW_20260830.json
INPUT_VISUAL_COMMIT: 0cb2bd6f03e2d84948741c162f22b8fd2ff064ad
BASELINE_RELEASE: v2.6 STABLE / LOCKED
PILOT_OR_FULL: PILOT_ONLY
SCOPE: BACK_LIGHTHOUSE source/render ve yalnız bağlı kanıtların son hedefli reworkü
CHANGED_FILES: 15
BYTE_EXACT_KEEP_VERIFIED: YES — 18 ana görsel; 16 source-art; 10 gate; 3 etkilenmeyen contact sheet
PROTECTED_FIELDS_CONFIRMED: YES
LIGHTHOUSE_FAMILY_VISIBILITY_CHECK: <PASS_OR_FAIL>
EXACT_FRONT_IDENTITY_AND_RESULT_BLINDNESS: <PASS_OR_FAIL>
TESTS_RUN: <EXACT_KONTROLLER>
TEMPORARY_SUBAGENTS: NONE
FULL_121_PRODUCTION_AUTHORIZED: NO
SIMULATION_AUTHORIZED: NO
RESULT: BACK_LIGHTHOUSE_ONLY_REWORK_DELIVERED / PENDING_ART_DIRECTION_PROJECT_OWNER_AND_CHIEF_EDITOR_ACCEPTANCE
OPEN_RISKS: Fiziksel baskı/kesim/duplex/ışık/gerçek masa-mesafesi ve SRC-002 açık
NEXT_RECIPIENT: Baş Editör
LOCK_REQUESTED: NO
```

GitHub commit/push görünür handoff değildir.
