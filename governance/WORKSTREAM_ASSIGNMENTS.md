# FOULWAKE v2.7 Çalışma Hattı Görevleri

**Durum:** ACTIVE / RELEASE BLOCKED  
**Baseline:** v2.6 STABLE / LOCKED  
**Entegrasyon hedefi:** `v2.7-design`

## Güncel teslim tablosu

| Hat | Görünür sohbet / dal | Durum | Bağlayıcı kanıt |
|---|---|---|---|
| Hikâye | `Foulwake Hikâye Editör` / `work/v2.7-story` | `ACCEPTED_STORY_WORKSTREAM_PASS / READY_FOR_VISUAL_INPUT` | `STORY_HANDOFF_20260820.json`, commit `e04eef7...` |
| Sanat Yönetimi | `FOULWAKE Sanat Yönetmeni` / `work/v2.7-art-direction` | `EXACT_PILOT_REVIEW_COMPLETE / REWORK_REQUIRED` | `ART_DIRECTION_PILOT_REVIEW_20260825.json`; input `b4afbcf...` |
| Görsel | `FOULWAKE Görsel Tasarım 2` / `work/v2.7-visual` | `PERMANENT_SUCCESSOR_ACK_ACCEPTED / EXISTING_PILOT_HANDOFF_PENDING` | `VISUAL_SUCCESSOR_ACK_20260826.json`; gözlenen head `1b27232a...` |
| Simülasyon | `Simülasyon Testi` / `work/v2.7-simulation` | `ACKNOWLEDGED_COMMUNICATION_TEST_ONLY / PENDING_NEW_ART_CANDIDATE` | Dal henüz yok |
| Baş Editör | `v2.7-design` | `GOVERNANCE_FIXED / RELEASE_BLOCKED` | `CHIEF_EDITOR_AUDIT_20260825.md` |

## Hikâye Editörü

- Kabul edilen kaynak commitini korur; yeni görsel üretim sırasında exact metin
  sorusu gelirse yalnız hikâye/görünen metin alanında cevap verir.
- Kart kimliği, effect, zamanlama ve deste davranışını değiştirmez.
- `SRC-002` için tahmin yürütmez; exact baseline karşılaştırmasını Baş Editör ve
  Simülasyona bırakır.
- Yeni görev yoksa dalı değiştirmez.

## Sanat Yönetmeni — exact pilot review tamamlandı

Bağlayıcı inceleme kanıtı
`governance/ART_DIRECTION_PILOT_REVIEW_20260825.json`dır.

1. `work/v2.7-visual@b4afbcf49784b85338453cbf29a956cbb620c9e6`
   için sonuç `REWORK_REQUIRED`: 3 ön KEEP, 9 ön REWORK; 7 arka yüz REWORK.
2. Sonraki Görsel candidate gelene kadar yeni brief veya final sanat üretmez.
3. Revize exact commit geldiğinde 12 kabul edilmiş zor-vaka kartını, 7 arka
   yüzü ve bütün contact-sheet/mockup kanıtını yeniden inceler.
4. Sonraki sonuç `ART_DIRECTION_PILOT_PASS_RECOMMENDATION` veya exact
   dosya/kart düzeyinde yeni `REWORK_REQUIRED` olur.
5. Final kullanıcı onayı, release veya kilit vermez; geçici ajan kullanmaz.

## Görsel Tasarım — kalıcı halef ACK kabulü / final pilot handoffu bekleniyor

Bağlayıcı uygulama kaynağı
`working/v2.7/visual/FOULWAKE_PILOT_REWORK_ORDER_v2.7.md`dır.

Resmî görünür sohbet artık `FOULWAKE Görsel Tasarım 2`dir. Önceki
`FOULWAKE görsel tasarım` sohbeti yanıt vermez hâle geldiği için emekli
edilmiştir; geçmiş teslimlerinin GitHub kanıtı korunur. Kalıcı halef exact
`work/v2.7-visual@1b27232a53b09ac3ff00030f625bfc2703d15764` başını ve zorunlu
kaynakları salt-okunur doğrulamış, dosya değiştirmeden devir ACK'i vermiştir.
Kanıt `governance/VISUAL_SUCCESSOR_ACK_20260826.json`dır.

Pilot üretimi `bf944125ee35fecd722628f6a9be5f5dfcd5707a` üzerinde, teslim
metadata'sı `1ab579c27ee26205cbc87718995da021ef6da84d` üzerinde ve geçici encoder
dosyalarının temizliği `1b27232a...` üzerinde gözlenmiştir. Bu GitHub paketi
henüz resmî Görsel teslim handoffu veya sanat kabulü değildir. Yeni üretim
yetkisi yoktur. Halefin sıradaki tek görevi mevcut paketi değiştirmeden,
görsele özgü zorunlu alanlarla final handoff vermektir.

1. Tarihsel üretim `work/v2.7-visual@b4afbcf49784b85338453cbf29a956cbb620c9e6`
   üzerinden başlamış ve geçmiş yeniden yazılmadan tamamlanmıştır.
2. Exact pilot seti yalnız şunlardır: `KAR-01, KAR-06, KAR-19, GUC-06,
   GUC-27, ERZ-01, SAD-H-03, HAR-AD-08, HAR-KY-06, HAR-AA-06, HAR-FN-04,
   SET-KP-01`.
3. `SAD-H-03` ve `HAR-KY-06` exact KEEP varlıkları değiştirilmeden alınır.
   Diğer on kart accepted brief ve review kararına göre üretilir/yeniden çizilir.
4. `GUC-24` provisional KEEP olarak bu turun dışında saklanır. `KAR-02,
   KAR-05, KAR-18, GUC-03, HAR-AA-04, SET-KL-01` reworkleri pilot PASS
   sonrasına ertelenir; bu turda 12 ön yüz sınırı aşılmaz.
5. Yedi arka yüzün tamamı mevcut sanattan türetilmeden sıfırdan yapılır.
   Madalyon/arma/rozet/kaleidoskopik simetri yoktur.
6. Harita arkaları aile-görünür/exact-kimlik-kördür; Sea/Rock subtype kör,
   Island anonim ada, Lighthouse 1721'e uygun anonim fenerdir.
7. Sabit 5×5 aranmaz. En az üç kurala uygun farklı düzenin kapalı ve kısmen
   açılmış mockup'ları, rastgele 180° karşılıkları ve kör testleri üretilir.
8. Exact copy değişmez; resim-içi gereksiz/anlamsız yazı veya glyph yoktur.
9. Tam 121, PDF, Simülasyon, release ve kilit yoktur. Resmî teslim sonucu
   `PILOT_REWORK_DELIVERED / PENDING_ART_DIRECTION_PROJECT_OWNER_AND_CHIEF_EDITOR_ACCEPTANCE`
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
| `ART-001` | Sanat Yönetimi + Görsel | `1b27232a...` paketi gözlendi; resmî Görsel handoff, yeniden review ve tam özgün yayılım bekleniyor |
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
