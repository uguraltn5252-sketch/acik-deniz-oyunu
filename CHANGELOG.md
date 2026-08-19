# Changelog

## v2.6 - Stabil / kilitli kural ve anlatı revizyonu

**Tarih:** 19 Ağustos 2026  
**Durum:** **STABLE / LOCKED - `releases/v2.6/`**  
**Mekanik baseline:** **v2.5 STABLE / LOCKED**

v2.6 yeni mekanik içermez. Başlıca değişiklikler:

- Kural kitabı ilk kez oynayan masa için öğretme + referans yapısına dönüştürüldü.
- Kaptan Gusto'nun kalkıştan hemen önce kayboluşu Kaptan oylamasının kanonik anlatısal gerekçesi oldu.
- Siyah Mühür, Arden Krallığı, San Cordelio, Saint Verena ve veba ekonomisi ana hikâye katmanı olarak kural kitabına işlendi; Gusto'nun gerçek akıbeti çözümsüz bırakıldı.
- Zorunlu masa anlatıları kısa `OKU` kutularına ayrıldı; ayrıntılı arka plan `Siyah Mühür Dosyası` ekine taşındı.
- Kör kural kitabı denetiminde karakter kurulum yoğunluğu, erken terim yükü, başlangıç Güç hazırlığı, Kaptan masumiyet algısı ve Kaptan değişim görünürlüğü sorunları düzeltildi.
- Moderatör için 2 sayfalık masa kartı oluşturuldu.
- 20 Karakter kartına ve diğer kart mekaniklerine dokunulmadı; v2.5 tam kart PDF'si byte-for-byte korundu.
- Ayrı Karakter baskı PDF'si, kilitli v2.5 kart PDF'sinin yalnız baskı talimatı + Karakter yapraklarından üretildi.
- v2.5 tam release validatorı yeniden çalıştırıldı ve PASS; v2.6 kör denetim ve release validatorı PASS.
- Bundan sonraki tasarım/mekanik değişiklikleri v2.7+ hattında yapılır.

## v2.5 - Stabil mekanik baseline

**Tarih:** 19 Ağustos 2026  
**Durum:** **STABLE / LOCKED - `releases/v2.5/`**

- İskorbüt aktif relocation sonrası Ada üzerinden Hedef Liman kazanılabilirliği zorunlu hâle getirildi.
- Girdap/Ters Akıntı - Ada 8-komşuluk yasağı oyun-boyu invariant olarak korundu.
- Kaderi Yeniden Yaz × Geçilmez hükmü kesinleştirildi.
- Çürümüş Erzak sahibinin İskorbüt sonucu sonrası gerçek Güç çekimi ve ilk yolculuk gününde herkesin 1 Güçle başlaması sabitlendi.
- Gövde 2 ve 118 ana kimlik korundu.
- Tam-sistem 100.200 oyun: Tayfa yaklaşık %50,28; motor hatası 0.
- v2.6'nın mekanik geri dönüş/baseline sürümüdür.

## v2.4 - Önceki mekanik stabil

- Fiziksel Kalkış Limanı, Kaptanın tarafsız ilk-gece bakışı, kalıcı kamusal Harita bilgisi ve rota/relocation güvenlik hükümleri kilitlendi.
- v2.5 tarafından mekanik olarak devralındı.

## v2.3 - Stabil prototip

**Tarih:** 18 Ağustos 2026  
**Durum:** **Kilitli release - `releases/v2.3/`**

- Ayrı görünür Geçilmez Kayalık işaret/token sistemi kaldırıldı.
- Geçilmez Kayalıklar 52 Harita kartının içindeki 12 Kayalık kartına entegre edildi; toplam kart kimliği 118 kaldı.
- `HAR-KY-01` ve `HAR-KY-03` Geçilmez Kayalık oldu; kapalı kategori yüzleri normal Kayalıktan ayırt edilemez.
- Küçük Haritalarda 1, büyük Haritalarda 2 Geçilmez normal Kayalık kotasının içinde zorunludur.
- Kapalı Geçilmez normal Harita/Ufuk hedefidir ve bütün gizli bilgi/bakma/blöf kurallarına tabidir.
- Seçilip açıldığında Gemi kareye girmez; mevcut konumda kalır. Normal rota gününde hareket harcanır ve kart açık kalıcı engele dönüşür.
- Acil geri dönüş yalnız açılmış/bilinen Geçilmezlerin oluşturduğu tam ileri çıkmazda uygulanır.
- Kaptan kalıcı rol, Kaptan yenileme kuralları ve bütün Haritalarda 2 Gövde korunur.
- 51.204 geometri taraması ve v2.3 stabil doğrulayıcı PASS.

## v2.2 - Önceki stabil prototip

`releases/v2.2/` değiştirilemez geri dönüş referansıdır. Ayrı görünür Geçilmez Kayalık işareti sistemi yalnız bu tarihsel sürümde kalır.

## v2.1 - Tarihsel stabil temel

`releases/v2.1/` değiştirilemez tarihsel geri dönüş referansıdır.
