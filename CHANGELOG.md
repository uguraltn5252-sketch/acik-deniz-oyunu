# Changelog

## v2.3 - Stabil prototip

**Tarih:** 18 Ağustos 2026  
**Durum:** **Kilitli release - `releases/v2.3/`**

v2.2'ye göre başlıca değişiklikler:

- Ayrı görünür Geçilmez Kayalık işaret/token sistemi kaldırıldı.
- Geçilmez Kayalıklar 52 Harita kartının içindeki 12 Kayalık kartına entegre edildi; toplam kart kimliği 118 kaldı.
- `HAR-KY-01` ve `HAR-KY-03` Geçilmez Kayalık oldu; kapalı kategori yüzleri normal Kayalıktan ayırt edilemez.
- Küçük Haritalarda 1, büyük Haritalarda 2 Geçilmez normal Kayalık kotasının içinde zorunludur.
- Kapalı Geçilmez normal Harita/Ufuk hedefidir ve bütün gizli bilgi/bakma/blöf kurallarına tabidir.
- Seçilip açıldığında Gemi kareye girmez; mevcut konumda kalır. Normal rota gününde hareket harcanır ve kart açık kalıcı engele dönüşür.
- Acil geri dönüş yalnız açılmış/bilinen Geçilmezlerin oluşturduğu tam ileri çıkmazda uygulanır.
- Kaptan kalıcı rol, ilk rota, Kaptan yenileme kuralları ve bütün Haritalarda 2 Gövde korunur.
- 7.200 kart çifti testi + 6.000 temsilî + 9.000 tam duyarlılık testinde kalıcı rota kilidi 0.
- 51.204 geometri taraması ve v2.3 stabil doğrulayıcı PASS.
- 32 sayfalık kural kitabı ve 32 sayfalık kart PDF'i preflight/görsel kontrolden geçti.

## v2.2 - Önceki stabil prototip

`releases/v2.2/` değiştirilemez geri dönüş referansıdır. Ayrı görünür Geçilmez Kayalık işareti sistemi yalnız bu tarihsel sürümde kalır.

## v2.1 - Tarihsel stabil temel

`releases/v2.1/` değiştirilemez tarihsel geri dönüş referansıdır.
