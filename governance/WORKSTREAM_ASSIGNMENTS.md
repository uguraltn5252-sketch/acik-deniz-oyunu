# FOULWAKE v2.7 Çalışma Hattı Görevleri

**Durum:** ACTIVE / RELEASE BLOCKED  
**Baseline:** v2.6 STABLE / LOCKED  
**Entegrasyon hedefi:** `v2.7-design`

## Güncel teslim tablosu

| Hat | Görünür sohbet / dal | Durum | Bağlayıcı kanıt |
|---|---|---|---|
| Hikâye | `Foulwake Hikâye Editör` / `work/v2.7-story` | `ACCEPTED_STORY_WORKSTREAM_PASS / READY_FOR_VISUAL_INPUT` | `STORY_HANDOFF_20260820.json`, commit `e04eef7...` |
| Sanat Yönetimi | `FOULWAKE Sanat Yönetmeni` / `work/v2.7-art-direction` | `WORK_ORDER_READY / PENDING_VISIBLE_CHAT_ACK` | `FOULWAKE_ART_DIRECTOR_WORK_ORDER_v2.7.md`; teslim henüz yok |
| Görsel | `FOULWAKE görsel tasarım` / `work/v2.7-visual` | `DELIVERED / REJECTED_ART_REWORK_REQUIRED` | `VISUAL_HANDOFF_20260825.json`, head `e91581...` |
| Simülasyon | `Simülasyon Testi` / `work/v2.7-simulation` | `ACKNOWLEDGED_COMMUNICATION_TEST_ONLY / PENDING_NEW_ART_CANDIDATE` | Dal henüz yok |
| Baş Editör | `v2.7-design` | `GOVERNANCE_FIXED / RELEASE_BLOCKED` | `CHIEF_EDITOR_AUDIT_20260825.md` |

## Hikâye Editörü

- Kabul edilen kaynak commitini korur; yeni görsel üretim sırasında exact metin
  sorusu gelirse yalnız hikâye/görünen metin alanında cevap verir.
- Kart kimliği, effect, zamanlama ve deste davranışını değiştirmez.
- `SRC-002` için tahmin yürütmez; exact baseline karşılaştırmasını Baş Editör ve
  Simülasyona bırakır.
- Yeni görev yoksa dalı değiştirmez.

## Sanat Yönetmeni — aktivasyon ve yaratıcı görev

Bağlayıcı iş emri:
`working/v2.7/visual/art_direction/FOULWAKE_ART_DIRECTOR_WORK_ORDER_v2.7.md`

1. İlk olarak yalnız salt-okunur iletişim testi ve `VISIBLE_CHAT_ACK: YES`
   verir; ACK öncesi brief, görsel, commit veya değerlendirme üretmez.
2. KAPTAN referansını yalnız STYLE_ONLY okur; asıl görsel kullanıcı tarafından
   bu görünür sohbete ayrıca eklenir.
3. FOULWAKE dünyasının ruhu, çizgi/tarama/malzeme dili, kompozisyon çeşitliliği
   ve deste ritmi için yaratıcı omurga kurar.
4. Görsel Tasarımın 121 ön + 7 arka briefini inceler, yeniden yazar veya somut
   düzeltme briefi verir.
5. 12 pilot ve 7 arka-yüz contact sheetini isim/metin kapalı da değerlendirir;
   aynı yüz, poz, sahne, hayvan, şaka, siluet ve yapay zekâ parlaklığını işaretler.
6. `ART_DIRECTION_*_PASS_RECOMMENDATION` veya `REWORK_REQUIRED` verir;
   kendisini kullanıcı/Chief Editor/release PASS'i yerine koymaz.
7. Final illüstrasyon, render, PDF ve baskı üretmez; bunlar Görsel Tasarımdadır.

Görsel pilot daha önceki iş emriyle başlamışsa çöpe atılmaz; exact Görsel commit
Sanat Yönetmeninin ilk review girdisi olur.

## Görsel Tasarım — aktif görev

Bağlayıcı iş emri:
`working/v2.7/visual/FOULWAKE_FULL_DECK_ART_REWORK_DIRECTIVE_v2.7.md`

1. Reddedilen `e91581...` görsellerini, altı aile plakasını, render/PDF'leri ve
   arka yüzleri yeni sanatın girdisi olarak kullanma.
2. 121 kart için ayrı art-brief envanteri; 7 arka yüz için ayrı brief üret.
3. KAPTAN referansını yalnız STYLE_ONLY kullan; karakter/yüz/poz/kompozisyon
   kopyalama.
4. İllüstrasyon alanında gereksiz veya anlamsız okunabilir yazı üretme.
5. 12 ön-yüz pilotu ve 7 arka-yüz taslağını tek contact sheetlerle teslim et.
6. Sanat Yönetmeni yaratıcı incelemesi ile kullanıcı + Baş Editör pilot kabulü
   olmadan tam 121 üretim/PDF yapma.
7. Tam üretimde her kart için semantik özgünlük ve text-in-art alanlarını
   manifestte kaydet; `unique SHA`yı sanat özgünlüğü sayma.
8. Exact kart metnini değiştirme; taşmayı Baş Editöre handoff et.

Görsel hattın bir sonraki sonucu `PILOT_DELIVERED / PENDING_ART_DIRECTION_PROJECT_OWNER_AND_CHIEF_EDITOR_ACCEPTANCE`
olmalıdır. Eski iş emrindeki sonuç etiketiyle gelen in-flight pilot reddedilmez;
Baş Editör onu Sanat Yönetmenine yönlendirir. Hiçbiri release veya Simülasyon
PASS'i değildir.

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
| `ART-001` | Sanat Yönetimi + Görsel | Yaratıcı kapı ve tam rework gerekiyor |
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
