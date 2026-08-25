# FOULWAKE v2.7 Çalışma Hattı Görevleri

**Durum:** ACTIVE / RELEASE BLOCKED  
**Baseline:** v2.6 STABLE / LOCKED  
**Entegrasyon hedefi:** `v2.7-design`

## Güncel teslim tablosu

| Hat | Görünür sohbet / dal | Durum | Bağlayıcı kanıt |
|---|---|---|---|
| Hikâye | `Foulwake Hikâye Editör` / `work/v2.7-story` | `ACCEPTED_STORY_WORKSTREAM_PASS / READY_FOR_VISUAL_INPUT` | `STORY_HANDOFF_20260820.json`, commit `e04eef7...` |
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
6. Kullanıcı + Baş Editör pilot kabulü olmadan tam 121 üretim/PDF yapma.
7. Tam üretimde her kart için semantik özgünlük ve text-in-art alanlarını
   manifestte kaydet; `unique SHA`yı sanat özgünlüğü sayma.
8. Exact kart metnini değiştirme; taşmayı Baş Editöre handoff et.

Görsel hattın bir sonraki sonucu `PILOT_DELIVERED / PENDING_CHIEF_EDITOR_AND_OWNER_ACCEPTANCE`
olmalıdır; release veya Simülasyon PASS'i değildir.

## Simülasyon Testi — bekleyen görev

Yeni görsel candidate Baş Editörce kabul edilmeden iş başlatılmaz ve
`work/v2.7-simulation` oluşturulmaz. Yetkili handoff geldiğinde:

- `SRC-002` GUC-22/GUC-23 exact baseline karşılaştırması;
- 121 kimlik, mekanik eşdeğerlik ve source→render→PDF;
- kör contact-sheet sanat tekrar incelemesi;
- resim-içi yazı, dönem uyumu, mizah tekrarı ve bilgi sızıntısı;
- yedi arka-yüz binary eşlemesi, 180° yön güvenliği, kesim/parlaklık/duplex;
- fiziksel proof, kör insan ve oyun/sosyal deneyim testleri;
- exact candidate bağlı `SIM_QA_ATTESTATION_v2.7.json`

üretir. Bulguyu mekanik veya görsel değişikliğe dönüştürmez.

## Baş Editör

- Exact handoff, dal kapsamı, kaynak ve kanıt zincirini doğrular.
- Pilot kabul/ret dispozisyonunu kaydeder.
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
| `ART-001` | Görsel | Tam rework gerekiyor |
| `QA-001`, `QA-002` | Simülasyon | Yeni candidate bekliyor |
| `GOV-001`, `COM-001` | Baş Editör | Açık |

## Zorunlu handoff

Her teslim `WORKSTREAM`, `VISIBLE_CHAT`, `VISIBLE_CHAT_ACK: YES`,
`EVIDENCE_TYPE: VISIBLE_CHAT_WORKSTREAM`, `SOURCE_BRANCH`, exact
`SOURCE_COMMIT`, `BASELINE_RELEASE`, `SCOPE`, `CHANGED_FILES`,
`PROTECTED_FIELDS_CONFIRMED`, `TESTS_RUN`, `RESULT`, `OPEN_RISKS`,
`NEXT_RECIPIENT` ve `LOCK_REQUESTED: NO` alanlarını içerir.
