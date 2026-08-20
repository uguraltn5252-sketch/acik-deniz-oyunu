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
