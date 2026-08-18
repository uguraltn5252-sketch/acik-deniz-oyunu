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
- **Sorun:** Geçilmez Kayalık son yaklaşımda Limanı geometrik olarak kilitleyebilir.
- **Karar:** Geçilmez Kayalık Limanın hemen kıçındaki son Harita/Ufuk hattına konulamaz.
- **Gerekçe:** Final yaklaşımının doğrudan fiziksel engelle kapanmasını önlemek.
- **Etkilenen dosyalar:** Harita kurulum kuralı, JSON/spec, harita doğrulayıcı, simülasyon.
- **İlgili issue/PR:** #1 / PR #2

### D-20260818-004 — Gövde bütün Haritalarda 2 olarak kalır

- **Durum:** Kabul; önceki 3 Gövde adayı reddedildi
- **Sorun:** Uzun Haritalarda 3 Gövde kullanılması değerlendirilmişti.
- **Karar:** Gemi bütün Harita boylarında **2 Gövdeyle** başlar. Harita boyuna göre 3 Gövdeye çıkılmaz.
- **Gerekçe:** Önceki simülasyonlarda 3 Gövde Hainin batırma yolunu belirgin biçimde zayıflattı; kullanıcı 2 Gövdeyi kesinleştirdi.
- **Etkilenen dosyalar:** Kurulum tablosu, Gövde göstergesi, Tersane Koyu onarım tavanı, JSON/spec, simülasyon.
- **Test:** Eski 2/3 Gövde duyarlılık testleri referans; yeni regresyonda yalnız 2 Gövde kanonik olacak.
- **Sonuç:** 2 Gövde kilitli kural.
- **İlgili issue/PR:** #1 / PR #2

### D-20260818-005 — Geçilmez Kayalık her oyunda bulunur; çıkmazda geri dönüş açar

- **Durum:** Kabul
- **Sorun:** Geçilmez Kayalığın yalnız deneysel bir modül olması istenmiyor; her oyunda rota baskısı yaratması, fakat oyunu kalıcı kilitlememesi gerekiyor.
- **Karar:** Harita büyüklüğüne göre her oyunda 1 veya 2 Geçilmez Kayalık bulunur. Mevcut boylarda `5×5`, `5×6`, `6×5` için 1; `5×7`, `6×6`, `6×7` için 2 kullanılır. Normalde Gemi geri gidemez. Ancak rota seçimi anında hiçbir yasal ileri rota kalmamışsa ve bunun nedeni Geçilmez Kayalık ise Gemi bir önceki bulunduğu kareye bir adım geri dönebilir.
- **Nedensellik testi:** Geçilmez Kayalıklar yok sayıldığında en az bir ileri rota doğuyorsa geri dönüş istisnası açılır. En az bir ileri rota zaten varsa geri dönüş yasaktır.
- **Maliyet:** Geri dönüş o günün normal hareketini tüketir; ücretsiz geri alma değildir. Daha önce çözülmüş karta dönülürse olay yeniden çalışmaz. Aynı şart sonraki turda sürüyorsa yeniden bir adım geri dönülebilir.
- **Kurulum güvenliği:** İlk rota tamamen kapatılamaz; başlangıçtan itibaren matematiksel olarak çözümsüz Harita kurulamaz. Acil geri hareket oyuncuların/rota etkilerinin oluşturduğu gerçek bir çıkmazdan çıkmak içindir.
- **Gerekçe:** Geçilmez Kayalık somut rota hafızası ve yol uzaması üretirken, oyunun temel 'ileri git' kuralını yalnız çok dar ve kontrol edilebilir bir durumda esnetir.
- **Etkilenen dosyalar:** Harita kurulum tablosu, hareket kuralı, Ufuk yasallığı, JSON/spec, simülasyon ve regresyon testleri.
- **Test:** T-20260818-004.
- **İlgili issue/PR:** #1 / PR #2

### D-20260818-006 — Geçilmez Kayalık + geri dönüş teknik olarak kabul edildi

- **Durum:** Kabul
- **Sorun:** 1/2 Geçilmez Kayalık ve yalnız Kayalık çıkmazında geri dönüşün oyunu kilitleyip kilitlemediği ve dengeyi aşırı bozup bozmadığı bilinmiyordu.
- **Karar:** D-20260818-005'teki sistem teknik olarak korunur; çekirdek kurala taşınabilir.
- **Gerekçe:** 15.000 yeni-kural davranışsal oyunda kalıcı rota kilidi 0; 51.204 kesin geometri kombinasyonunda çözümsüz kurulumlar açıkça tanımlanıp kurulum filtresiyle elenebiliyor. Temsilî hücrelerde Tayfa ortalaması %54,8 ve geri dönüş yalnız yaklaşık %4,2 oyunda görülüyor.
- **Ek kenar hükmü:** Girdap gibi zorunlu ek hareket Geçilmez Kayalık nedeniyle yapılamıyorsa zorunlu ek hareket boşa düşer; bu durum acil geri hareketi aynı gün tetiklemez. Sonraki normal rota gününde gerçekten hiç ileri rota yoksa geri dönüş kuralı uygulanır.
- **Etkilenen dosyalar:** İnsan kuralları, JSON/spec, doğrulayıcı, simülasyon ve masa testi formu.
- **Test:** T-20260818-004 — PASS.
- **Sonuç:** Sayısal/yapısal kabul; eğlence ve algılanan adalet kör insan masa testinde doğrulanmalı.
- **İlgili issue/PR:** #1 / PR #2 ve Geçilmez Kayalık test branch'i.
