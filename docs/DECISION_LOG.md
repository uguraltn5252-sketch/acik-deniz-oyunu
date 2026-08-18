# Decision Log

Tasarım kararlarının gerekçesi burada tutulur. Sohbet içinde alınmış bir karar, buraya ve ilgili kaynak dosyalara işlenmeden resmî sürüm kararı sayılmaz.

## Şablon

### D-YYYYMMDD-001 — Karar başlığı

- **Durum:** Öneri / Testte / Kabul / Reddedildi / Geri alındı
- **Sorun:**
- **Karar:**
- **Gerekçe:**
- **Etkilenen dosyalar:**
- **Test:**
- **Sonuç:**
- **İlgili issue/PR:**

---

### D-20260818-001 — v2.1'i değiştirilemez stabil temel olarak koru

- **Durum:** Kabul
- **Sorun:** Sohbet/model sürümleri değiştiğinde hangi dosyanın doğru sürüm olduğunun karışma riski.
- **Karar:** `releases/v2.1/` değiştirilemez stabil referans olacak; yeni değişiklikler ayrı branch/PR ile yapılacak.
- **Gerekçe:** Geri dönüş noktası ve izlenebilirlik sağlamak.
- **Etkilenen dosyalar:** Repository çalışma düzeni.
- **Test:** v2.1 `--validate-only` temiz geçti.

### D-20260818-002 — Kaptan kalıcı omurgadır ve ilk rotayı seçer

- **Durum:** Kabul
- **Sorun:** v2.1 sonrası notlarda Kaptanın tamamen kaldırılıp kaldırılmadığı belirsizleşmişti.
- **Karar:** Kaptan rolü asla kaldırılmayacak. Geminin ilk rotasını Kaptan tek başına, olay bilgisi olmadan seçer. Sonraki rota oyu/beraberlik/İsyan hükümleri Kaptan sistemine bağlı kalır. Kaptan gece ayrıca uyanmaz ve makamı otomatik Ufuk bilgisi vermez.
- **Gerekçe:** Kaptan oyunun siyasi ve rota kararlarının kamusal merkezi olarak korunuyor; kaldırılması çok sayıda bağlı sistemi ve oyunun kimliğini değiştirirdi.
- **Etkilenen dosyalar:** Kurallar, JSON/spec, simülasyon, Kaptan hedefleyen kartlar, gece sırası.
- **Test:** v2.1 ile uyumlu; yeni karar belirsizliği kaldırıyor.
- **İlgili issue/PR:** #1 / PR #2

### D-20260818-003 — Geçilmez Kayalık Liman yaklaşım hattına konulamaz

- **Durum:** Kabul
- **Sorun:** Geçilmez Kayalık son yaklaşımda veya zorunlu koridorda Limanı geometrik olarak kilitleyebilir.
- **Karar:** Geçilmez Kayalık Limanın hemen kıçındaki son Harita/Ufuk hattına konulamaz. Ayrıca yerleştirmeden sonra seçilen gemi başlangıcından seçilen Limana en az bir normal ileri yasal yol kaldığı doğrulanır; kalmıyorsa Kayalık başka kareye taşınır.
- **Gerekçe:** Son satır yasağı final kilidini engeller; dinamik başlangıç nedeniyle özellikle `6×5` karşı-uç başlangıç/Liman durumunda ek erişilebilirlik testi de gereklidir.
- **Etkilenen dosyalar:** Harita kurulum kuralı, JSON/spec, harita doğrulayıcı, simülasyon.
- **Test:** Tek engelli kesin grafik testi; `6×5` biçiminde karşı-uç rotalarda son satır dışındaki kritik çapraz karelerin de kilit üretebildiği görüldü.
- **İlgili issue/PR:** #1 / PR #2

### D-20260818-004 — Gövdeyi Harita boyuna göre ölçekleme

- **Durum:** Testte
- **Sorun:** Uzun seferin 3 Gövdeyi hak edip etmediği ve bunun Hainin batırma yolunu aşırı zayıflatıp zayıflatmadığı.
- **Karar adayı:** `5×7` Harita 3 Gövde kullanabilir ancak doğrudan hasar kotası mevcut fiziksel maksimum olan `9 Deniz + 5 Kayalık = 14` olmalıdır. Diğer mevcut Harita boylarında 2 Gövde korunur.
- **Gerekçe:** Mevcut hasar kotalarıyla 3 Gövde uzun Haritalarda Tayfa zaferini yaklaşık `%77–86` bandına taşıyor. `5×7` üzerinde 14 hasar kartıyla oran yaklaşık `%53–63` banda dönüyor. `6×7` üzerinde ise aynı maksimum havuzla `%75–81` seviyesinde kalıyor.
- **Etkilenen dosyalar:** Kurulum tablosu, Gövde göstergesi, Tersane Koyu onarım tavanı, JSON/spec, simülasyon.
- **Test:** T-20260818-003.
- **Sonuç:** Kullanıcı onayı bekleniyor; henüz çekirdek kurala kilitlenmedi.
- **İlgili issue/PR:** #1 / PR #2
