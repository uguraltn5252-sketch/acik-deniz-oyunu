# FOULWAKE v2.7 Çalışma Hattı Görevleri

**Durum:** ACTIVE / RELEASE BLOCKED  
**Baseline:** v2.6 STABLE / LOCKED  
**Entegrasyon hedefi:** `v2.7-design`

## Güncel teslim tablosu

| Hat | Görünür sohbet / dal | Durum | Bağlayıcı kanıt |
|---|---|---|---|
| Hikâye | `Foulwake Hikâye Editör` / `work/v2.7-story` | `ACCEPTED_STORY_WORKSTREAM_PASS / READY_FOR_VISUAL_INPUT` | `STORY_HANDOFF_20260820.json`, commit `e04eef7...` |
| Sanat Yönetimi | `FOULWAKE Sanat Yönetmeni` / `work/v2.7-art-direction` | `PILOT_ART_DIRECTION_PASS / OWNER + CHIEF PENDING` | `governance/ART_DIRECTION_LIGHTHOUSE_FINAL_REVIEW_20260830.json`; input `23c062f6...` |
| Görsel | `FOULWAKE Görsel Tasarım 2` / `work/v2.7-visual` | `PILOT_ART_DIRECTION_PASS_RECORDED / PRODUCTION_PAUSED` | kanonik `c8081aa9...`; head `23c062f6...` |
| Simülasyon | `Simülasyon Testi` / `work/v2.7-simulation` | `ACKNOWLEDGED_COMMUNICATION_TEST_ONLY / PENDING_OWNER_CHIEF_PILOT_ACCEPTANCE` | Dal henüz yok |
| Baş Editör | `v2.7-design` | `GOVERNANCE_FIXED / RELEASE_BLOCKED` | `CHIEF_EDITOR_AUDIT_20260825.md` |

## Hikâye Editörü

- Kabul edilen kaynak commitini korur; yeni görsel üretim sırasında exact metin
  sorusu gelirse yalnız hikâye/görünen metin alanında cevap verir.
- Kart kimliği, effect, zamanlama ve deste davranışını değiştirmez.
- `SRC-002` için tahmin yürütmez; exact baseline karşılaştırmasını Baş Editör ve
  Simülasyona bırakır.
- Yeni görev yoksa dalı değiştirmez.

## Sanat Yönetmeni — final inceleme tamamlandı

Bağlayıcı nihai inceleme kaydı `governance/ART_DIRECTION_LIGHTHOUSE_FINAL_REVIEW_20260830.json`dır.

1. Exact `work/v2.7-visual@23c062f6de06c32eab224b3440c8474725d4fe9e` üzerinde 9/9 raster açıldı.
2. `BACK_LIGHTHOUSE: KEEP`; final pilot dispozisyonu `12 FRONT KEEP / 7 BACK KEEP`.
3. `PILOT_ART_DIRECTION_PASS` yalnız Sanat Yönetimi kapısını geçer; proje sahibi veya release/kilit PASS'i değildir.
4. Yeni sanat yönü veya üretim görevi yoktur. Proje sahibinin açık pilot estetik kararı beklenir.
5. Tarihsel `EXACT_PILOT_REVIEW_COMPLETE`, `REVISED_EXACT_PILOT_REVIEW_COMPLETE`, `REDRAW_BRIEF`, `ART_DIRECTION_REVISED_PILOT_REVIEW_20260828.json`, `ART_DIRECTION_LIGHTHOUSE_ONLY_REVIEW_20260830.json` ve `VISUAL_LIGHTHOUSE_ONLY_HANDOFF_20260830.json` kayıtları korunur.

## Görsel Tasarım — handoff teslim edildi / üretim durdu

1. Exact dal başı `23c062f6de06c32eab224b3440c8474725d4fe9e`; kanonik lighthouse-only üretim `c8081aa9f781737b0d7e14c8b224bf1fd988e8bb`dır.
2. Cumulative `0cb2bd6f03e2d84948741c162f22b8fd2ff064ad..23c062f6de06c32eab224b3440c8474725d4fe9e` farkı exact 15 dosyadır.
3. Sanat Yönetimi exact pakete `PILOT_ART_DIRECTION_PASS` vermiştir; bu proje sahibi estetik kabulü veya aktif candidate değildir.
4. Yeni görsel, düzeltme, contact sheet/layout türetimi, tam 121, PDF, Simülasyon, release veya kilit üretmez.
5. Proje sahibi + Baş Editör pilot kararı gelene kadar dalı değiştirmez; kapsam açılması ancak yeni exact Baş Editör emriyle olur.
6. `TEMPORARY_SUBAGENTS: NONE` ve `LOCK_REQUESTED: NO` korunur.

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
| `ART-001` | Proje sahibi + Baş Editör | Sanat Yönetimi PASS; açık pilot estetik kabulü ve Baş Editör dispozisyonu bekleniyor |
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
