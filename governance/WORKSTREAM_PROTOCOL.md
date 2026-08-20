# FOULWAKE Çalışma Hatları ve İletişim Protokolü

## Her çalışma başlangıcında zorunlu okuma

1. `AI_HANDOFF.md`
2. `PROJECT_STATE.md`
3. `governance/EDITORIAL_CHARTER.md`
4. `governance/DECISION_REGISTER.md`
5. `governance/ACTIVE_WORKSTREAMS.json`
6. `governance/WORKSTREAM_ASSIGNMENTS.md`
7. İlgili çalışma hattının kaynak dosyaları

Çalışma başlamadan önce aktif branch, son commit ve son STABLE / LOCKED baseline doğrulanır.

## Resmî görünür sohbet ve ajan kuralı

- Resmî uzman alanları `Foulwake Hikâye Editör`, `FOULWAKE görsel tasarım` ve
  `Simülasyon Testi` adlı görünür sohbetlerdir.
- Geçici alt ajan oluşturulmaz. Çok zorunlu istisna proje sahibinden önceden
  açık izin ister; böyle bir çıktı `TEMPORARY_SUBAGENT` olarak kalır ve görünür
  uzman teslimi yerine geçmez.
- Baş Editör bu sohbetten diğer görünür sohbetlerin geçmişine mesaj ekleyemez.
  GitHub'a görev yazılması yalnız bir iş emridir; ilgili sohbet kendi geçmişinde
  okuyup handoff vermeden `ACKNOWLEDGED` veya `DELIVERED` kaydedilemez.

## Çalışma dalları

| Görünür sohbet | Çalışma dalı | Yazma kapsamı | Entegrasyon hedefi |
|---|---|---|---|
| `Foulwake Hikâye Editör` | `work/v2.7-story` | Onaylı hikâye ve görünen metin kaynakları | `v2.7-design` |
| `FOULWAKE görsel tasarım` | `work/v2.7-visual` | Görsel, yerleşim, baskı ve artefakt kayıtları | `v2.7-design` |
| `Simülasyon Testi` | `work/v2.7-simulation` | `working/v2.7/qa/**` test ve kanıtları | `v2.7-design` |

Uzman çalışma dalı ilk yetkili teslim sırasında oluşturulur. Uzman sohbetler
`governance/**`, `releases/**`, `PROJECT_STATE.md`, `AI_HANDOFF.md`, `main` veya
kilit etiketlerine yazamaz. Baş Editör yalnız doğrulanmış handoffları
`v2.7-design`a entegre eder.

## Çalışma hattı sınırları

### Hikâye Editörü

Birincil v2.7 kaynakları:

- `working/v2.7/FOULWAKE_STORY_FRAMEWORK.md`
- `working/v2.7/FOULWAKE_RULEBOOK_STORY_v2.7.md`
- `working/v2.7/FOULWAKE_CARD_TEXTS_v2.7.json`
- `working/v2.7/FOULWAKE_NARRATIVE_VALIDATION_v2.7.md`

`FOULWAKE_NARRATIVE_VALIDATION_v2.7.md` kayıtlı doğrulama kanıtıdır; üretim
metni veya bağlayıcı release PASS kaynağı değildir.

Kurallar:

- Kural kitabı akışını korur.
- Kart sayısı ve kimliklerini korur.
- `effect`, zamanlama, başlangıç havuzu, desteye dönüş ve mekanik alanları değiştirmez.
- Görsel Tasarıma görünen metin/flavor kaynağını devreder; görsel üretim dosyasını sessizce değiştirmez.

### Görsel Tasarım

Birincil v2.7 kaynakları:

- `working/v2.7/SOURCE_HIERARCHY_v2.7.json`
- v2.6 değişmeyen mekanik baseline'ı
- `FOULWAKE_CARD_TEXTS_v2.7.json` görünen Karakter/Güç metni
- `FOULWAKE_RULEBOOK_STORY_v2.7.md` tanımlı anlatı blokları
- `FOULWAKE_STORY_FRAMEWORK.md` ton/lore çiti
- `working/v2.7/FOULWAKE_VISUAL_SYSTEM.md`
- `working/v2.7/BINARY_ARTIFACTS.md`

Kurallar:

- Mekanik metni kısaltmaz, yeniden yorumlamaz veya değiştirmez.
- Lore hakkında kesin yeni cevap üretmez.
- `DECISION_REGISTER.md` içindeki gizlilik, arka yüz, ölçü ve kategori kararlarını korur.
- Mizahı yalnız fareye bağlamaz; fare, martı, beceriksiz/hırsız tayfa, sessiz bakış ve nesne kaynaklı kuru mizah dönüşümlü kullanılır.
- Her illüstrasyonda en fazla bir ikincil görsel şaka kullanılır.
- Tam deste yayılımından önce aile bazında okunabilirlik ve tutarlılık kontrolü bırakır.

### Simülasyon Testi

Okuma kapsamı bütün projedir. Yazılı raporlar `working/v2.7/qa/` altında tutulur.
Aktif kapanış planı `working/v2.7/qa/RELEASE_BLOCKER_RESOLUTION_PLAN_v2.7.md`
dosyasıdır.

Kurallar:

- Önce son STABLE / LOCKED baseline ve aktif DRAFT belirlenir.
- Mekanik, matematik, mantık, strateji, sosyal deneyim, sıkılma, adalet, görsel okunabilirlik, baskı, PDF ve manifest bütünlüğü ayrı test katmanlarıyla denetlenir.
- Tek bir Monte Carlo veya statik doğrulama sonucu yeterli sayılmaz.
- Bulgular `PASS`, `PASS WITH MINOR ISSUES`, `FAIL` veya `BLOCKER` olarak sınıflandırılır.
- Mekanik değişiklik yapmaz; öneriyi ve kanıtı Baş Editöre gönderir.
- Release adayı için nihai kanıtı
  `working/v2.7/qa/SIM_QA_ATTESTATION_v2.7.json` adıyla, exact candidate
  commitine bağlı ve `governance/SIM_QA_ATTESTATION_SCHEMA.json` ile uyumlu
  üretir.
- Candidate commit değişirse eski attestation'ı geçerli saymaz.

### Baş Editör

- Handoffları karşılaştırır ve kapsam ihlalini geri çevirir.
- İki çalışma hattı çakıştığında kaynak önceliğini uygular.
- Gerçek yaratıcı veya mekanik belirsizliği proje sahibine taşır.
- Kabul edilen kaynakları release candidate’a entegre eder.
- Simülasyon Testi yeniden doğrulamasından sonra kilit değerlendirmesi yapar.

## Zorunlu handoff biçimi

Her çalışma hattı tesliminde aşağıdaki alanlar bulunur:

```text
WORKSTREAM:
VISIBLE_CHAT:
VISIBLE_CHAT_ACK: YES
EVIDENCE_TYPE: VISIBLE_CHAT_WORKSTREAM
SOURCE_BRANCH:
SOURCE_COMMIT:
BASELINE_RELEASE:
SCOPE:
CHANGED_FILES:
PROTECTED_FIELDS_CONFIRMED:
TESTS_RUN:
RESULT:
OPEN_RISKS:
NEXT_RECIPIENT:
LOCK_REQUESTED: NO
```

`VISIBLE_CHAT_ACK: YES` ve `EVIDENCE_TYPE: VISIBLE_CHAT_WORKSTREAM` bulunmayan
bir kayıt resmî uzman teslimi değildir. İzinli geçici alt ajan kaydı varsa
`EVIDENCE_TYPE: TEMPORARY_SUBAGENT` kullanılır; bu kayıt blocker kapatamaz,
release PASS'i üretemez ve uzman sohbet adına onay veremez.

## Çakışma kuralı

- Başka hattın sahip olduğu alanda sorun görülürse değişiklik yapılmaz.
- Sorun handoff içinde dosya ve alan adıyla kaydedilir.
- Baş Editör yönlendirmeden iki farklı çözüm aynı dosyaya uygulanmaz.
- GitHub’daki güncel kaynak, yalnız sohbet hafızasına dayanan metinden üstündür.

## İletişim kaydı

Baş Editörün çalışma hatlarına verdiği bağlayıcı yönlendirmeler `governance/COORDINATION_LOG.md` içinde tutulur. Çalışma hatları her yeni oturumda son kaydı kontrol eder.

Proje sahibinin açık ve tekrar sorulmaması gereken kararları
`governance/DECISION_REGISTER.md`; aktif görev sahipleri ve teslimleri
`governance/WORKSTREAM_ASSIGNMENTS.md` içinde tutulur.

Sohbet içindeki onay veya özet tek başına kanonik kayıt değildir. Aynı şekilde
GitHub iş emri de görünür sohbet kabulü değildir. Resmî çalışma; görünür sohbet
geçmişi, zorunlu handoff, uzman dalındaki exact commit ve Baş Editör
dispozisyonu birlikte bulunmadan tamamlanmış sayılmaz.
