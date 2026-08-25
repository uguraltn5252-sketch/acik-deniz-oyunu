# FOULWAKE v2.7 Çalışma Hattı Görevleri

**Durum:** ACTIVE / RELEASE BLOCKED  
**Baseline:** v2.6 STABLE / LOCKED  
**Entegrasyon hedefi:** `v2.7-design`

## Güncel teslim tablosu

| Hat | Görünür sohbet / dal | Durum | Bağlayıcı kanıt |
|---|---|---|---|
| Hikâye | `Foulwake Hikâye Editör` / `work/v2.7-story` | `ACCEPTED_STORY_WORKSTREAM_PASS / READY_FOR_VISUAL_INPUT` | `STORY_HANDOFF_20260820.json`, commit `e04eef7...` |
| Sanat Yönetimi | `FOULWAKE Sanat Yönetmeni` / `work/v2.7-art-direction` | `ART_DIRECTION_BRIEF_ACCEPTED / READY_FOR_EXACT_PILOT_REVIEW` | `ART_DIRECTION_HANDOFF_20260825.json`, commit `7418d9c2...` |
| Görsel | `FOULWAKE görsel tasarım` / `work/v2.7-visual` | `PRE_BRIEF_PILOT_DETECTED / VISIBLE_HANDOFF_AND_ART_REVIEW_PENDING` | Reddedilen teslim `e91581...`; gözlenen pilot head `b4afbcf...` |
| Simülasyon | `Simülasyon Testi` / `work/v2.7-simulation` | `ACKNOWLEDGED_COMMUNICATION_TEST_ONLY / PENDING_NEW_ART_CANDIDATE` | Dal henüz yok |
| Baş Editör | `v2.7-design` | `GOVERNANCE_FIXED / RELEASE_BLOCKED` | `CHIEF_EDITOR_AUDIT_20260825.md` |

## Hikâye Editörü

- Kabul edilen kaynak commitini korur; yeni görsel üretim sırasında exact metin
  sorusu gelirse yalnız hikâye/görünen metin alanında cevap verir.
- Kart kimliği, effect, zamanlama ve deste davranışını değiştirmez.
- `SRC-002` için tahmin yürütmez; exact baseline karşılaştırmasını Baş Editör ve
  Simülasyona bırakır.
- Yeni görev yoksa dalı değiştirmez.

## Sanat Yönetmeni — kabul edilen brief ve exact pilot incelemesi

Bağlayıcı kaynaklar:

- `governance/ART_DIRECTION_HANDOFF_20260825.json`
- `working/v2.7/visual/art_direction/FOULWAKE_ART_DIRECTION_BIBLE_v2.7.md`
- `working/v2.7/visual/art_direction/FOULWAKE_121_ART_BRIEF_MANIFEST_v2.7.json`
- `working/v2.7/visual/art_direction/FOULWAKE_12_PILOT_PRODUCTION_BRIEFS_v2.7.md`
- `working/v2.7/visual/art_direction/FOULWAKE_7_BACK_BRIEFS_v2.7.md`

1. Exact kabul edilen brief source `7418d9c2c89c265cb6efd30f6a5a7f2addd528da`dır; içerik brief kapısını geçmiştir.
2. İlk sonraki görev `work/v2.7-visual@b4afbcf49784b85338453cbf29a956cbb620c9e6` pilotunu ve contact sheetlerini
   salt-okunur incelemektir. Bu pilot kabul edilen brief öncesinde üretildiği
   için otomatik PASS veya otomatik ret değildir.
3. 12 ön yüzü başlık/metin açık ve kapalı; 7 arka yüzü aile, exact kimlik,
   180° güvenliği, resim-içi yazı, tekrar, dönem, doku ve deste ritmi açısından
   değerlendirir.
4. Harita arkalarında aile görünürlüğünü ve exact ön-kart körlüğünü ayrı test
   eder; sabit 5×5 aramaz, değişken kurala uygun düzen kanıtı ister.
5. Sonuç `ART_DIRECTION_PILOT_PASS_RECOMMENDATION` veya exact dosya/kart
   düzeyinde `REWORK_REQUIRED` olur. `KEEP`, `REMOVE`, `REDRAW_BRIEF`
   ve Görsel Tasarımın uygulayacağı somut öncelik sırası verilir.
6. Final illüstrasyon, render, PDF ve baskı üretmez; brief dışında alan
   değiştirmez ve geçici ajan kullanmaz.

## Görsel Tasarım — pilot-only yetki

Bağlayıcı kaynaklar kabul edilen `7418d9c2c89c265cb6efd30f6a5a7f2addd528da` Sanat Yönetimi paketi,
`FOULWAKE_FULL_DECK_ART_REWORK_DIRECTIVE_v2.7.md` ve exact kart metnidir.

1. `b4afbcf49784b85338453cbf29a956cbb620c9e6` pilotu korunur; ancak görünür sohbet handoffu ve Sanat Yönetmeni
   incelemesi olmadan kabul edilmiş pilot veya aktif candidate sayılamaz.
2. Sanat Yönetmeninin exact review handoffundan sonra yalnız belirtilen 12 ön
   yüz, 7 arka yüz, contact sheet ve değişken harita mockup'larında rework
   yapabilir.
3. Reddedilen `e91581...` varlıkları, altı aile plakası ve türevleri yeni
   sanatın girdisi olamaz.
4. KAPTAN yalnız STYLE_ONLY kullanılır; illüstrasyon alanında gereksiz veya
   anlamsız okunabilir yazı üretilmez; exact copy değiştirilmez.
5. Harita arkaları: Sea/Rock genel deniz ve subtype kör; Island anonim genel ada;
   Lighthouse 1721'e uygun anonim genel fener. Aile görünür, exact ön kart ve
   sonuç kördür; sabit 5×5 şartı yoktur.
6. Kullanıcı + Baş Editör pilot kabulü olmadan kalan 109 ön yüz, tam 121
   üretim, tam PDF veya Simülasyon handoffu başlatılmaz.
7. Sonuç `PILOT_REWORK_DELIVERED / PENDING_ART_DIRECTION_PROJECT_OWNER_AND_CHIEF_EDITOR_ACCEPTANCE`
   olmalı; `LOCK_REQUESTED: NO` kalmalıdır.

## Simülasyon Testi — bekleyen görev

Yeni görsel candidate Baş Editörce kabul edilmeden iş başlatılmaz ve
`work/v2.7-simulation` oluşturulmaz. Yetkili handoff geldiğinde:

- `SRC-002` GUC-22/GUC-23 exact baseline karşılaştırması;
- 121 kimlik, mekanik eşdeğerlik ve source→render→PDF;
- Sanat Yönetmeni dispozisyonu ile kör contact-sheet sanat tekrar incelemesi;
- resim-içi yazı, dönem uyumu, mizah tekrarı ve bilgi sızıntısı;
- yedi arka-yüz binary eşlemesi, 180° yön güvenliği, kesim/parlaklık/duplex;
- fiziksel proof, kör insan ve oyun/sosyal deneyim testleri;
- exact candidate bağlı `SIM_QA_ATTESTATION_v2.7.json`

üretir. Bulguyu mekanik veya görsel değişikliğe dönüştürmez.

## Baş Editör

- Exact handoff, dal kapsamı, kaynak ve kanıt zincirini doğrular.
- Sanat Yönetmeni tavsiyesini kullanıcı kararıyla birlikte doğrular ve pilot
  kabul/ret dispozisyonunu kaydeder.
- `SRC-002`, `GOV-001` ve çalışma hattı çakışmalarını yönetir.
- Release candidate yalnız bütün blockerlar kapanınca ve Simülasyon kapısı
  geçince oluşturulur.
- Kilit yalnız proje sahibinin açık talimatıyla ve Baş Editör tarafından yapılır.

## Açık blocker sahipliği

| Blocker | Sahip | Durum |
|---|---|---|
| `MEC-001` | Simülasyon | Yeni candidate bekliyor |
| `SRC-001` | Görsel | Yeni provenance bekliyor |
| `SRC-002` | Baş Editör + Simülasyon | Exact baseline çözümü bekliyor |
| `ART-001` | Sanat Yönetimi + Görsel | Brief kapısı geçti; exact pilot review/rework ve tam özgün yayılım bekleniyor |
| `QA-001`, `QA-002` | Simülasyon | Yeni candidate bekliyor |
| `GOV-001`, `COM-001` | Baş Editör | Açık |

## Zorunlu handoff

Her teslim `WORKSTREAM`, `VISIBLE_CHAT`, `VISIBLE_CHAT_ACK: YES`,
`EVIDENCE_TYPE: VISIBLE_CHAT_WORKSTREAM`, `SOURCE_BRANCH`, exact
`SOURCE_COMMIT`, `BASELINE_RELEASE`, `SCOPE`, `CHANGED_FILES`,
`PROTECTED_FIELDS_CONFIRMED`, `TESTS_RUN`, `RESULT`, `OPEN_RISKS`,
`NEXT_RECIPIENT` ve `LOCK_REQUESTED: NO` alanlarını içerir. Sanat Yönetimi
ayrıca iş emrindeki `ART_DIRECTION_STAGE`, exact Görsel girdi commit'i,
`CREATIVE_VERDICT`, `KEEP`, `REMOVE` ve `REDRAW_BRIEF` alanlarını verir.
