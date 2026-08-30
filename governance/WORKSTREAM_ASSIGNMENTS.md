# FOULWAKE v2.7 Çalışma Hattı Görevleri

**Durum:** ACTIVE / RELEASE BLOCKED  
**Baseline:** v2.6 STABLE / LOCKED  
**Entegrasyon hedefi:** `v2.7-design`

## Güncel teslim tablosu

| Hat | Görünür sohbet / dal | Durum | Bağlayıcı kanıt |
|---|---|---|---|
| Hikâye | `Foulwake Hikâye Editör` / `work/v2.7-story` | `ACCEPTED_STORY_WORKSTREAM_PASS / READY_FOR_VISUAL_INPUT` | `STORY_HANDOFF_20260820.json`, commit `e04eef7...` |
| Sanat Yönetimi | `FOULWAKE Sanat Yönetmeni` / `work/v2.7-art-direction` | `THREE_TARGETED_REWORKS_KEEP / BACK_LIGHTHOUSE_REWORK_REQUIRED` | `ART_DIRECTION_LIGHTHOUSE_ONLY_REVIEW_20260830.json`; input `0cb2bd6f...` |
| Görsel | `FOULWAKE Görsel Tasarım 2` / `work/v2.7-visual` | `BACK_LIGHTHOUSE_ONLY_PILOT_REWORK_AUTHORIZED` | `FOULWAKE_BACK_LIGHTHOUSE_ONLY_REWORK_ORDER_v2.7.md`; base `0cb2bd6f...` |
| Simülasyon | `Simülasyon Testi` / `work/v2.7-simulation` | `ACKNOWLEDGED_COMMUNICATION_TEST_ONLY / PENDING_NEW_ART_CANDIDATE` | Dal henüz yok |
| Baş Editör | `v2.7-design` | `GOVERNANCE_FIXED / RELEASE_BLOCKED` | `CHIEF_EDITOR_AUDIT_20260825.md` |

## Hikâye Editörü

- Kabul edilen kaynak commitini korur; yeni görsel üretim sırasında exact metin
  sorusu gelirse yalnız hikâye/görünen metin alanında cevap verir.
- Kart kimliği, effect, zamanlama ve deste davranışını değiştirmez.
- `SRC-002` için tahmin yürütmez; exact baseline karşılaştırmasını Baş Editör ve
  Simülasyona bırakır.
- Yeni görev yoksa dalı değiştirmez.

## Sanat Yönetmeni — üç rework KEEP / yalnız BACK_LIGHTHOUSE açık

Bağlayıcı kanıt `governance/ART_DIRECTION_LIGHTHOUSE_ONLY_REVIEW_20260830.json`dır.

1. Exact `work/v2.7-visual@0cb2bd6f03e2d84948741c162f22b8fd2ff064ad` incelendi.
2. `KAR-01`, `HAR-AA-06` ve `BACK_ISLAND`: KEEP.
3. `BACK_LIGHTHOUSE`: REWORK_REQUIRED; kule kapalı düzen ve contact sheet
   ölçeğinde kayboluyor, Fener ailesi yerine ikinci Ada/kayalık okunuyor.
4. Yeni fener tesliminde yalnız aile görünürlüğü, exact kimlik/sonuç körlüğü,
   1721 uygunluğu, ortak deniz ve yasak motifleri yeniden inceler.
5. Final üretmez, kullanıcı/release/kilit PASS'i vermez, geçici ajan kullanmaz.

Tarihsel `REVISED_EXACT_PILOT_REVIEW_COMPLETE`,
`ART_DIRECTION_REVISED_PILOT_REVIEW_20260828.json` ve
`REDRAW_BRIEF` kayıtları korunur.

## Görsel Tasarım — BACK_LIGHTHOUSE-only / 15 dosya

Bağlayıcı emir `working/v2.7/visual/FOULWAKE_BACK_LIGHTHOUSE_ONLY_REWORK_ORDER_v2.7.md`dır. Önceki dört-varlık emri tarihsel teslim
zinciri olarak korunur.

1. Yalnız `BACK_LIGHTHOUSE.png` ve `BACK_LIGHTHOUSE_source.jpg` değişir.
2. Mevcut ortak deniz ve çapraz kaya sırtı korunur; kule 1721'e uygun anonim
   seyir yapısı olarak normal dijital masa mesafesinde okunacak kadar büyütülür
   ve değer olarak ayrılır.
3. Işın, glow, halo, lens, modern beacon, dairesel platform, rozet veya exact
   ön fener/sonuç sızıntısı yoktur.
4. Yalnız 2 contact sheet, 6 mevcut layout, 1 rapor ve 4 kanıt kaydı yenilenir.
5. Exact `CHANGED_FILES: 15`; 18 ana görsel, 16 source-art, 10 gate ve
   3 etkilenmeyen sheet byte-exact kalır.
6. Başka fark `BLOCKED_SCOPE_DRIFT`dır.
7. Tam 121, PDF, Simülasyon, release ve kilit yoktur. Sonuç
   `BACK_LIGHTHOUSE_ONLY_REWORK_DELIVERED / PENDING_ART_DIRECTION_PROJECT_OWNER_AND_CHIEF_EDITOR_ACCEPTANCE`
   ve `LOCK_REQUESTED: NO` olmalıdır.

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
| `ART-001` | Sanat Yönetimi + Görsel | Yalnız `BACK_LIGHTHOUSE` reworkü ve son sanat kabulü bekleniyor |
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
