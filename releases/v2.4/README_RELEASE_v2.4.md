# OYUN v2.4 — Test-Passed Geliştirme Adayı

**Taban:** v2.3 STABLE / LOCKED  
**Durum:** TEST-PASSED / NOT LOCKED  
**Tarih:** 18 Ağustos 2026

Bu klasör, v2.3 kapsamlı kırma testinde bulunan rota kilitleri, kamusal Harita görünürlüğü belirsizliği, Kaptan açılış akışı, seçim beraberliği ve eksik simülasyon bağımlılığı sorunlarını düzeltmek için oluşturulan v2.4 geliştirme hattıdır. v2.3 yerinde değiştirilmez.

## v2.4 ana değişiklikleri

- Gemi artık soyut Harita-dışı başlangıçta değil, seçilen sütun hizasındaki **Kalkış Limanı** kurulum kartı/alanında başlar.
- Acil geri dönüş ilk Harita satırından **Kalkış Limanına** dönebilir.
- İlk gün yalnız Kaptan seçilir.
- İlk tarafsız gecede Kaptan Sadakatini bilmeden yalnız **1 yasal Yakın Ufuk** kartına gizlice bakar; kart kapalı kalır.
- Sadakatler ertesi sabah dağıtılır.
- İlk gerçek rota artık Kaptanın tek başına kör seçimi değil, normal eşzamanlı rota oylamasıdır; Kaptanın rota oyu 2 sayar.
- Kamusal olarak açılan Harita kartı tekrar kapanmaz. Açık ama ziyaret edilmemiş kartın olayı ilk gerçek girişe kadar çözülmez.
- Kamusal açılan Geçilmez Kayalık anında bilinen fiziksel engel olur.
- Harita kartı yer değiştirme etkileri Kalkış Limanı→Hedef Liman bütün gerçek yollarını yok ederse değişiklik iptal edilir/geri alınır.
- Kaptan seçimi iki kez berabere kalırsa Kader Zarı fallback'i seçimi sonlandırır.
- Rota/sosyal-proxy simülatörü proje-içi bağımlılık kullanmayacak şekilde self-contained yeniden yazıldı; yalnız Python standart kütüphanesi ve v2.4 JSON spec gerekir.

## Doğrulama

- Regresyon testleri: **8/8 PASS**.
- Geometri: **51.204 teorik / 51.102 legal / 102 rejected**.
- Kalkış Limanı sonrası kalıcı ilk-kol kilidi: **0**.
- Exhaustive Near-Horizon relocation denemesi: **1.667.231**.
- Solvability guard tarafından geri alınan unsafe relocation: **20**.
- Guard sonrası kabul edilen kalıcı relocation kilidi: **0**.
- Self-contained rota/sosyal-proxy matrisi: **9.000 oyun**, **0 setup error**, **0 hard route lock**, **%100 Hedef Limana ulaşma**.
- Bu matris tam Tayfa/Hain kazanma dengesi değildir; yeni rota ve bilgi akışının güvenlik regresyonudur.

Ayrıntılar `V24_TEST_REPORT.md`, `V24_EXHAUSTIVE_AUDIT.json` ve `V24_ROUTE_MATRIX_SUMMARY.json` içindedir. Tam ham matris ve tam kaynak paket `SOURCE_PACKAGE.md` içindeki Library ZIP'inde tutulur.

## Stabil release için eksikler

- v2.4 kural PDF'si yeniden üretilmeli.
- Etkilenen kart metinleriyle v2.4 kart PDF'si yeniden üretilmeli.
- PDF kaynak-kural çapraz kontrolü ve görsel preflight yapılmalı.
- Son manifest/hashler binary artefaktlardan sonra yeniden üretilmeli.

Bu eksikler tamamlanmadan v2.4 `STABLE / LOCKED` olarak işaretlenmemelidir.
