# FOULWAKE Çalışma Hatları ve İletişim Protokolü

## Her çalışma başlangıcında zorunlu okuma

1. `AI_HANDOFF.md`
2. `PROJECT_STATE.md`
3. `governance/EDITORIAL_CHARTER.md`
4. `governance/ACTIVE_WORKSTREAMS.json`
5. İlgili çalışma hattının kaynak dosyaları

Çalışma başlamadan önce aktif branch, son commit ve son STABLE / LOCKED baseline doğrulanır.

## Çalışma hattı sınırları

### Hikâye Editörü

Birincil v2.7 kaynakları:

- `working/v2.7/FOULWAKE_STORY_FRAMEWORK.md`
- `working/v2.7/FOULWAKE_RULEBOOK_STORY_v2.7.md`
- `working/v2.7/FOULWAKE_CARD_TEXTS_v2.7.json`
- `working/v2.7/FOULWAKE_NARRATIVE_VALIDATION_v2.7.md`

Kurallar:

- Kural kitabı akışını korur.
- Kart sayısı ve kimliklerini korur.
- `effect`, zamanlama, başlangıç havuzu, desteye dönüş ve mekanik alanları değiştirmez.
- Görsel Tasarıma görünen metin/flavor kaynağını devreder; görsel üretim dosyasını sessizce değiştirmez.

### Görsel Tasarım

Birincil v2.7 kaynakları:

- Hikâye Editörünün yukarıdaki dört onaylı kaynağı
- `working/v2.7/FOULWAKE_VISUAL_SYSTEM.md`
- `working/v2.7/BINARY_ARTIFACTS.md`

Kurallar:

- Mekanik metni kısaltmaz, yeniden yorumlamaz veya değiştirmez.
- Lore hakkında kesin yeni cevap üretmez.
- Kart ailesi, gizlilik, arka yüz, ölçü ve kategori ayrımlarını korur.
- Mizahı yalnız fareye bağlamaz; fare, martı, beceriksiz/hırsız tayfa, sessiz bakış ve nesne kaynaklı kuru mizah dönüşümlü kullanılır.
- Her illüstrasyonda en fazla bir ikincil görsel şaka kullanılır.
- Tam deste yayılımından önce aile bazında okunabilirlik ve tutarlılık kontrolü bırakır.

### Simülasyon Testi

Okuma kapsamı bütün projedir. Yazılı raporlar `working/v2.7/qa/` altında tutulur.

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

## Çakışma kuralı

- Başka hattın sahip olduğu alanda sorun görülürse değişiklik yapılmaz.
- Sorun handoff içinde dosya ve alan adıyla kaydedilir.
- Baş Editör yönlendirmeden iki farklı çözüm aynı dosyaya uygulanmaz.
- GitHub’daki güncel kaynak, yalnız sohbet hafızasına dayanan metinden üstündür.

## İletişim kaydı

Baş Editörün çalışma hatlarına verdiği bağlayıcı yönlendirmeler `governance/COORDINATION_LOG.md` içinde tutulur. Çalışma hatları her yeni oturumda son kaydı kontrol eder.

Sohbet içindeki onay veya özet tek başına kanonik kayıt değildir. Handoff ve
Baş Editör dispozisyonu GitHub'a yazılmadan çalışma tamamlanmış sayılmaz.
