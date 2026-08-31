# FOULWAKE Sanat Yönetmeni İş Emri — v2.7

**Resmî görünür sohbet:** `FOULWAKE Sanat Yönetmeni`  
**Dal:** `work/v2.7-art-direction`  
**Yetki kaynağı:** `governance/CURRENT_STAGE.json`  
**Güncel aşama:** `STAGE-20260830-KAPTAN-FRAMING-PATCH-CORRECTION`  
**Baseline:** `119136812c2c749e14e675f1400640664fa044bc`  
**Durum:** `ONE_FILE_CORRECTION_AUTHORIZED / VISUAL_PRODUCTION_PAUSED`

## 1. Exact güncel görev

Yalnız şu dosya değişebilir:

`working/v2.7/visual/art_direction/FOULWAKE_KAPTAN_ART_LANGUAGE_PATCH_v2.7.md`

Cumulative fark baseline'dan en fazla bir Markdown dosyası ve 700 kelimedir.
Raster, thumbnail, contact sheet, layout, manifest, PDF veya başka brief
değiştirilemez.

Mevcut patch iki nedenle `REWORK_REQUIRED`dır:

1. Yüklenen KAPTAN kartını yalnız deste dili gibi anlatmış; oysa kart,
   `SET-KP-01` için bağlayıcı ana görsel kaynaktır.
2. Proje sahibinin bütün kart çizimleri için istediği bağımsız kadraj kapısını
   içermemektedir.

Patch ayrıca exact görünen copyyi
`working/v2.7/FOULWAKE_OWNER_CARD_TEXT_OVERRIDES_v2.7.json` kaynağına bağlar.

## 2. KAPTAN sözleşmesi

- Teknik kimlik: `SET-KP-01`.
- Başlık: `KAPTAN`.
- Bölüm: `ÖZEL YETENEK`.
- Effect: `Oylamada eşitlik olursa, senin tarafın geçerli olur.`
- Flavor: `Lidere et. Gemi senin emrinde.`
- Görsel:
  `working/v2.7/visual/references/FOULWAKE_KAPTAN_ART_LANGUAGE_REFERENCE_v2.7.jpg`.

KAPTAN figürü ve ana kompozisyon korunur. Yalnız küçük crop/ölçek/renk veya
arka-plan temizliği önerilebilir. Boş sandalye, makam anahtarı veya başka ana
özneyle değiştirilemez. Gemi ve martı diğer kartlarda tekrarlanmak zorunda
değildir.

Deste genelinde bağlayıcı sanat dili:

- kalın karakterli siyah mürekkep;
- yoğun gravür ve çapraz tarama;
- sıcak kirli kâğıt;
- mat lacivert, oker, pas ve kirli krem;
- grotesk ama kendi içinde tutarlı anatomi;
- eski baskı aşınması;
- dijital parlama, krom/specular, bloom, airbrush ve plastik AI cilası yok.

## 3. Copy kilidi

Sanat Yönetimi ve Görsel Tasarım title, section label, effect, flavor, card-id
ve mekaniği yeniden yazamaz. Görsel model okunabilir copy üretmez. İllüstrasyon
metinsiz; copy kanonik UTF-8 kaynaktan şablonla yerleştirilir. Finalde OCR veya
render-source exact karşılaştırması gerekir. Manifest beyanı tek başına kanıt
değildir. Sapma `BLOCKED_COPY_DRIFT`tir.

## 4. Bağımsız kadraj kapısı

Sanat Yönetmeni her ön ve arka kartı ayrı inceler:

- exact kart oranı ve illüstrasyon penceresi;
- 3 mm bleed ve 4–5 mm safe area;
- ana özne ölçeği, odak, denge ve negatif alan;
- yüz, el ve gerekli nesnede anlamsız kesim;
- title/effect/flavor/card-id alanıyla çakışma;
- çizgi/siluet düzeyinde thumbnail ve normal masa-mesafesi okunurluğu;
- aynı model, el-merkezli veya tekdüze yakın/uzak kadraj tekrarı.

Görsel Tasarım self-PASS veremez. Yalnız `FRAMING_PASS` veya
`REFRAME_REQUIRED` kullanılır. PASS olmadan KEEP/final/tam üretim yoktur;
sapma `BLOCKED_FRAMING_DRIFT`tir.

## 5. Arka yüz yaratıcı hedefleri

- `BACK_SEA_ROCK`: mat, derin fakat ışıldamayan deniz; beyaz parlama,
  krom/specular ve plastik AI cilası yok.
- `BACK_ISLAND`: eski varlık türetilmeden FULL REDRAW; sticker, rozet, ikon veya
  bağımsız karo hissi yok.
- `BACK_LIGHTHOUSE`: normal mesafede daha büyük okunur; uzun kayalık sırt
  zorunlu değildir; kompakt kaya/kıyı temeli olabilir.
- Diğer dört arka: HOLD; owner acceptance yok.

Bu hedefler patchte kısa ve uygulanabilir biçimde korunur; şu aşamada görsel
üretilmez.

## 6. Yaratıcı rol

Sanat Yönetmeni teknik checklist operatörü değildir. Ruh, dönem, malzeme,
anlatı, kompozisyon, insan/sahne ayrışması ve deste ritmi için somut hüküm
üretir. “Daha güzel” gibi belirsiz yorum yerine korunacak, çıkarılacak ve
yeniden kurulacak unsuru söyler. Final estetik karar proje sahibinindir.

## 7. Handoff

```text
WORKSTREAM: Sanat Yönetimi
VISIBLE_CHAT: FOULWAKE Sanat Yönetmeni
VISIBLE_CHAT_ACK: YES
SOURCE_BRANCH: work/v2.7-art-direction
SOURCE_COMMIT:
AUTHORIZATION_STAGE: STAGE-20260830-KAPTAN-FRAMING-PATCH-CORRECTION
AUTHORIZATION_BASELINE: 119136812c2c749e14e675f1400640664fa044bc
SCOPE: KAPTAN sanat dili/copy/kadraj patch düzeltmesi
CHANGED_FILES:
REFERENCE_OPENED: YES
COPY_SOURCE: working/v2.7/FOULWAKE_OWNER_CARD_TEXT_OVERRIDES_v2.7.json
FRAMING_GATE_ADDED:
TESTS_RUN:
TOOLS_USED:
PLUGINS_USED:
PLUGINS_AVAILABLE_BUT_NOT_USED:
NOT_USED_REASON:
RESULT: ART_LANGUAGE_PATCH_CORRECTED / PENDING_PROJECT_OWNER_ACCEPTANCE
TEMPORARY_SUBAGENTS: NONE
FULL_121_PRODUCTION_AUTHORIZED: NO
SIMULATION_AUTHORIZED: NO
LOCK_REQUESTED: NO
```
