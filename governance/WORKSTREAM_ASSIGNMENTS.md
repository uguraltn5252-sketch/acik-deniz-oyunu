# FOULWAKE v2.7 Çalışma Hattı Görevleri

**Durum:** ACTIVE / RELEASE BLOCKED  
**Baseline:** v2.6 STABLE / LOCKED  
**Entegrasyon hedefi:** `v2.7-design`

## Güncel teslim tablosu

| Hat | Görünür sohbet / dal | Durum | Bağlayıcı kanıt |
|---|---|---|---|
| Hikâye | `Foulwake Hikâye Editör` / `work/v2.7-story` | `ACCEPTED_STORY_WORKSTREAM_PASS / READY_FOR_VISUAL_INPUT` | `STORY_HANDOFF_20260820.json`, commit `e04eef7...` |
| Sanat Yönetimi | `FOULWAKE Sanat Yönetmeni` / `work/v2.7-art-direction` | `REVISED_EXACT_PILOT_REVIEW_COMPLETE / REWORK_REQUIRED` | `ART_DIRECTION_REVISED_PILOT_REVIEW_20260828.json`; input `1b27232a...` |
| Görsel | `FOULWAKE Görsel Tasarım 2` / `work/v2.7-visual` | `TARGETED_FOUR_MASTER_PILOT_REWORK_AUTHORIZED` | `FOULWAKE_REVISED_PILOT_TARGETED_REWORK_ORDER_v2.7.md`; base `1b27232a...` |
| Simülasyon | `Simülasyon Testi` / `work/v2.7-simulation` | `ACKNOWLEDGED_COMMUNICATION_TEST_ONLY / PENDING_NEW_ART_CANDIDATE` | Dal henüz yok |
| Baş Editör | `v2.7-design` | `GOVERNANCE_FIXED / RELEASE_BLOCKED` | `CHIEF_EDITOR_AUDIT_20260825.md` |

## Hikâye Editörü

- Kabul edilen kaynak commitini korur; yeni görsel üretim sırasında exact metin
  sorusu gelirse yalnız hikâye/görünen metin alanında cevap verir.
- Kart kimliği, effect, zamanlama ve deste davranışını değiştirmez.
- `SRC-002` için tahmin yürütmez; exact baseline karşılaştırmasını Baş Editör ve
  Simülasyona bırakır.
- Yeni görev yoksa dalı değiştirmez.

## Sanat Yönetmeni — revize exact review tamamlandı / hedefli rework bekleniyor

Bağlayıcı kanıt `governance/ART_DIRECTION_REVISED_PILOT_REVIEW_20260828.json`dır.

1. Exact `work/v2.7-visual@1b27232a53b09ac3ff00030f625bfc2703d15764` girdisindeki 40/40 görsel açıldı.
2. Önler 10 KEEP / 2 REWORK: `KAR-01`, `HAR-AA-06`.
3. Arkalar 5 KEEP / 2 REWORK: `BACK_ISLAND`, `BACK_LIGHTHOUSE`.
4. Sanatsal 180° Ada/Fener nedeniyle 5/7; teknik exact 180° 7/7.
5. Beş contact sheet ve altı layout aynı geometri/konum/yönlerle yenilenir.
6. Hedefli teslim geldiğinde aynı brieflerle yeniden inceler; final üretmez,
   kullanıcı/release/kilit PASS'i vermez ve geçici ajan kullanmaz.

Tarihsel `EXACT_PILOT_REVIEW_COMPLETE`,
`governance/ART_DIRECTION_PILOT_REVIEW_20260825.json` ve
`REDRAW_BRIEF` kayıtları korunur; yeni hüküm 28 Ağustos kanıtıdır.

## Görsel Tasarım — dört ana asset / 25 dosya hedefli rework yetkili

Bağlayıcı kaynak `working/v2.7/visual/FOULWAKE_REVISED_PILOT_TARGETED_REWORK_ORDER_v2.7.md`dır. Tarihsel
`working/v2.7/visual/FOULWAKE_PILOT_REWORK_ORDER_v2.7.md` korunur.

1. Byte-exact KEEP önler: `KAR-06`, `KAR-19`, `GUC-06`, `GUC-27`, `ERZ-01`, `SAD-H-03`, `HAR-AD-08`, `HAR-KY-06`, `HAR-FN-04`, `SET-KP-01`.
2. Byte-exact KEEP arkalar: `BACK_CHARACTER`, `BACK_POWER`, `BACK_LOYALTY`, `BACK_SEA_ROCK`, `BACK_SUPPORT`.
3. Yalnız `KAR-01`, `HAR-AA-06`, `BACK_ISLAND`,
   `BACK_LIGHTHOUSE` render/source dosyaları değişir.
4. Yalnız `KAR-01` gate'i üç beden geometrisiyle yenilenir.
   `HAR-AA-06` gate'i korunur; kapalı-sepet yönü finale taşınır.
5. Beş sheet ve altı layout aynı kimlik/konum/yön/geometriyle türetilir.
6. Rapor ve dört manifest yeni hash/provenance ile güncellenir.
7. Exact `CHANGED_FILES` 25'tir; başka değişiklik `BLOCKED_SCOPE_DRIFT`.
8. Tam 121, PDF, Simülasyon, release ve kilit yoktur. Sonuç
   `TARGETED_PILOT_REWORK_DELIVERED / PENDING_ART_DIRECTION_PROJECT_OWNER_AND_CHIEF_EDITOR_ACCEPTANCE`
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
| `ART-001` | Sanat Yönetimi + Görsel | `1b27232a...` resmî handoffu kabul edildi; yeniden review ve kullanıcı/Baş Editör pilot kabulü bekleniyor |
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
