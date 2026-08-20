# FOULWAKE Baş Editör Koordinasyon Kaydı

## 20 Ağustos 2026 — Baş editörlük düzeninin yürürlüğe alınması

**Kanonik baseline:** v2.6 STABLE / LOCKED  
**Aktif çalışma:** v2.7 STORY + VISUAL DRAFT / NOT LOCKED  
**Aktif branch:** `v2.7-design`

### Hikâye Editörüne iletilen yönlendirme

- Mevcut v2.7 hikâye ve kart dili dosyaları Görsel Tasarımın metin kaynağıdır.
- Kural kitabı akışı, kart sayıları, kimlikler, etkiler, zamanlamalar, başlangıç havuzu ve deste davranışları korunacaktır.
- Görsel dosyalarda doğrudan değişiklik yapılmayacak; görsel ihtiyaçlar handoff ile iletilecektir.
- Mekanik risk olarak görülen konular kural değişikliğine çevrilmeden Simülasyon Testine aktarılacaktır.

### Görsel Tasarıma iletilen yönlendirme

- `FOULWAKE_STORY_FRAMEWORK.md`, `FOULWAKE_RULEBOOK_STORY_v2.7.md`, `FOULWAKE_CARD_TEXTS_v2.7.json` ve anlatı doğrulama raporu metin/lore kaynağıdır.
- `FOULWAKE_VISUAL_SYSTEM.md` onaylı sanat yönüdür; release kilidi değildir.
- Mizah yalnız fareye dayanmayacaktır. Fare, martı, beceriksiz veya hırsız tayfa, sessiz bakış ve nesne kaynaklı kuru mizah dönüşümlü kullanılacaktır.
- Tam 121 kartlık yayılım aile bazında okunabilirlik ve tutarlılık kontrolüyle ilerleyecektir.
- Mekanik veya kanonik metin değiştirilmeden taşma/okunabilirlik sorunu Baş Editöre bildirilecektir.

### Simülasyon Testine iletilen yönlendirme

- Denetim yalnız kazanma oranı veya eski statik validator ile sınırlı değildir.
- Mekanik, matematik, mantık, strateji, sosyal deneyim, sıkılma, adalet, moderatör yükü, görsel okunabilirlik, PDF ve manifest bütünlüğü ayrı katmanlarda test edilecektir.
- Hikâye ve Görsel Tasarım çıktıları aktif v2.7 DRAFT olarak denetlenecek; v2.6 yalnız değişmeyen baseline olacaktır.
- Sonuç `PASS`, `PASS WITH MINOR ISSUES`, `FAIL` veya `BLOCKER` olarak raporlanacaktır.
- FAIL/BLOCKER kapanmadan Baş Editör release kilidi uygulamayacaktır.

### Baş Editör kararı

- Hiçbir çalışma hattı tek başına kanonik durum, release manifesti veya `STABLE / LOCKED` kaydı oluşturamaz.
- Başka hattın alanında sorun görüldüğünde sessiz düzenleme yapılmaz; handoff oluşturulur.
- Bu kayıt, yeni çalışma oturumlarında zorunlu okunacaktır.

## 20 Ağustos 2026 — Çapraz çalışma hattı denetimi

Hikâye, Görsel Tasarım ve Simülasyon Testi hatları `v2.7-design` dalındaki
`1a5b23051a3a625d6de9b98c2503a0181956af3c` commitini birbirinden bağımsız,
salt okunur biçimde denetledi. Hikâye bulguları Görsel ve Simülasyon hatlarına;
Görsel bulguları Simülasyon hattına; Simülasyon hükmü Baş Editöre iletildi.

**Ortak hüküm:** `v2.7 = BLOCKER / RELEASE VE KİLİT İÇİN UYGUN DEĞİL`.

| Kimlik | Ortak bulgu | Kapanma koşulu |
|---|---|---|
| `MEC-001` | Ortak Deniz + Kayalık arka yüzü, v2.6'nın ayrı Kayalık arka yüzü ve gizli bilgi mimarisiyle çakışıyor. | Proje sahibinin açık mekanik kararı, kaynak hizalama ve tam yeniden test |
| `SRC-001` | Görsel sistem v2.6 metnini kaynak gösteriyor; aktif v2.7 kart/rulebook metni ve üretilmiş PDF arasında provenance yok. | Tek kaynak sırası ve source → render → PDF birebir kanıtı |
| `ART-001` | Tam 121 kartlık aday ve GitHub'dan doğrulanabilir görsel artefakt seti yok. | Tam aday, manifest/hash, baskı ve duplex prova |
| `QA-001` | v2.7 anlatı PASS'i yeniden üretilemiyor; exact candidate'a bağlı tam Simülasyon QA attestation yok. | Sürümlü script/baseline, ham çıktılar, hashli attestation |
| `QA-002` | Yeni düzen için kör insan masa testi ve fiziksel prova yok. | Sosyal deneyim ölçümleri ile gerçek baskı/kesim/ışık kaydı |
| `GOV-001` | `main` ve `v2.7-design` durum kayıtları çakışıyor; dal 45 ahead / 2 behind, v2.7 PR ve zorunlu check yok. | Bilinçli dal uzlaştırması, release PR ve zorunlu yönetişim check'i |
| `CAN-001` | Genel olarak DRAFT olan Story Framework, özellikle yeni `CAN-08/09` maddelerini kullanıcı kilidi olmadan KANON etiketliyor. | Taslak kısıta yeniden sınıflandırma veya proje sahibinin açık kanon kararı |

### Baş Editör dispozisyonu

- Bu bulgular `governance/ACTIVE_WORKSTREAMS.json` içinde açık BLOCKER olarak kaydedildi.
- Hiçbiri sessizce mekanik, hikâye veya görsel değişikliğe çevrilmedi.
- `releases/v2.6/` değiştirilmedi.
- Proje sahibinin açık `kilitle/stable/release` talimatı gelse bile açık BLOCKER'lar kapanmadan kilit uygulanmayacak.
- Yeni bir candidate commit, önceki bütün v2.7 PASS/attestation sonuçlarını geçersiz kılar.

## 20 Ağustos 2026 — Sorumlu hatlara çözüm dağıtımı

Proje sahibi açık engellerin sorumlularına iletilmesini ve hatların uyumlu
çalışmasını istedi. Hikâye, Görsel Tasarım ve Simülasyon Testi hatları
`af064df83ac4132c7d8d75aec67a3f1b51150fdb` üzerinde read-only çalıştı,
önerilerini birbirlerine iletti ve Baş Editöre tek handoff verdi.

### Baş Editörün kaynak ve karar dispozisyonu

- Önceki kullanıcı kararı doğrulandı: v2.7 DRAFT için Açık Deniz ve Kayalık aynı
  binary arka yüzü kullanır. Bu konu yeniden karar beklemez.
- Ortak arka yüz v2.6'nın ayrı Kayalık arka yüz modelinden bilinçli bir
  bilgi-mimarisi değişikliğidir; `MEC-001` tam Simülasyon ve kör fiziksel sızıntı
  testi bitene kadar açık kalır.
- `CAN-08/09`, release kanonu değil v2.7 DRAFT koruma ilkesidir; `TASLAK`
  sınıfına alınır.
- Görsel üretimin metin sırası: v2.6 değişmeyen mekanik baseline → v2.7 Card
  Texts → tanımlı v2.7 Rulebook Story blokları → Story Framework ton/lore çiti →
  Visual System yerleşim/sanat standardı.
- `FOULWAKE_NARRATIVE_VALIDATION_v2.7.md` üretim metni veya bağlayıcı release
  PASS'i değildir; yeniden üretilebilir kanıt bekler.
- Reset öncesi 121/121 üretim ve final preflight tarihsel kanıttır; güncel branch
  ve exact candidate'a yeniden bağlanmadan `ART-001`i kapatmaz.

### Kabul edilen görevler

| Hat | Kabul edilen teslim | Durum |
|---|---|---|
| Hikâye | CAN-08/09 `KANON → TASLAK`; kesin metin alanları ve korunan mekanik alanlar | Dokümantasyon düzeltmesi kabul edildi |
| Görsel | Kaynak hiyerarşisi; Sea=Rock draft/retest çiti; 121 manifest ve provenance şartı | Spec düzeltmesi kabul edildi; üretim bekliyor |
| Simülasyon | Paired A/B, mekanik/fuzz, strateji, sosyal, kör insan ve fiziksel sızıntı planı | QA planı kabul edildi; candidate bekliyor |
| Baş Editör | Karar kaydı, görev haritası, source state ve tek GitHub entegrasyonu | Uygulandı |

Hatların ayrı commit/push oluşturması yasaklandı; bütün kapsam değişiklikleri Baş
Editör tarafından tek entegrasyonda birleştirildi. Güncel hüküm BLOCKER olarak
kalır; bu koordinasyon bir release veya kilit değildir.
