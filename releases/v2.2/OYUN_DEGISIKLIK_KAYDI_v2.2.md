# OYUN - Değişiklik Kaydı v2.2

**Temel:** v2.1  
**Tarih:** 18 Ağustos 2026  
**Durum:** Stabil prototip

## v2.2'de değişenler

- Gemi başlangıcı alt kenarda sabit merkezden çıkarıldı; 5/6 sütundaki herhangi bir sütun kullanılabilir.
- İlk Yakın Ufuk ve ilk Sis yasağı seçilen başlangıca göre dinamikleşti.
- Kaptanın kalıcı çekirdek rol olduğu açıkça kilitlendi.
- İlk rotayı Kaptan tek başına, olay bilgisi olmadan seçmeye devam eder.
- Başarılı İsyan, Kaptanın ölümü, Kamara, mahsur kalma veya Kayıkçı seferi durumlarında yeni Kaptan seçimi korunur.
- Kaptan gece ayrıca uyanmaz ve makam otomatik Ufuk bilgisi vermez.
- Gemi bütün Harita boylarında 2 Gövdeyle başlar; 3 Gövde adayı reddedildi.
- Ayrı görünür `Geçilmez Kayalık` işaretleri eklendi; 52 Harita kartı/118 kimlik değişmedi.
- 5x5, 5x6, 6x5'te 1; 5x7, 6x6, 6x7'de 2 Geçilmez Kayalık kullanılır.
- Geçilmez Kayalık son Liman/Ufuk hattına konulamaz; kurulum başlangıç -> erişilebilir Ada -> Liman yolunu korumalıdır.
- Geçilmez Kayalık tam çıkmaz yaratırsa Gemi bir önceki kareye bir gün tüketerek geri çekilebilir.
- Geri dönülen çözülmüş olay yeniden tetiklenmez; bilinen çıkmaz kola başka rota varken yeniden girilemez.
- Girdap/ek hareket Kayalık nedeniyle hedef bulamazsa yalnız hareket boşa düşer; aynı gün acil geri dönüş olmaz.

## Kart havuzu

Kart metinleri ve kart kimlikleri v2.1 ile aynıdır:

- 20 Karakter
- 30 Güç
- 1 Çürümüş Erzak
- 15 Sadakat
- 52 Harita
- toplam 118 kimlik

Geçilmez Kayalıklar kart değil, ayrı kurulum işaretidir.

## Teknik test

Geçilmez Kayalık + acil geri dönüş hedefli test:

- 51.204 geometri yerleşimi
- 15.000 yeni-kural davranışsal oyun
- 6.000 kontrol oyunu
- kalıcı rota kilidi: 0
- kurulum hatası: 0
- temsilî Tayfa ortalaması: %54,8
- geri dönüş görülen oyun: yaklaşık %4,2
- ortalama etki: +0,12 gün / +0,09 gece / ~+0,70 dakika

Bu test tam v2.2 sosyal denge simülasyonu değildir.

## Stabilizasyon

- v2.2 kural kitabı PDF üretildi ve 32 sayfanın tamamı görsel olarak tarandı.
- Kart PDF'si 32 sayfa olarak korundu; sayfa 2-32 içerikleri v2.1 kart çıktısıyla eşleşiyor, yalnız kapak v2.2 olarak yenilendi.
- 12 adet kesilebilir Geçilmez Kayalık işareti içeren A4 fiziksel işaret sayfası eklendi.
- Kaynak/PDF çapraz doğrulaması ve PDF preflight kontrolleri PASS.
- Sürüm `releases/v2.2/` altında kilitlenmiştir.
