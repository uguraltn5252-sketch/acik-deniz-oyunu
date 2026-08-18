# Changelog

## v2.3 - Geliştirme: gizli Geçilmez Kayalık

**Tarih:** 18 Ağustos 2026  
**Durum:** Teknik PASS; insan masa testi bekleniyor.

v2.2'ye göre:

- Ayrı Geçilmez Kayalık işareti/token sistemi kaldırıldı.
- Geçilmez Kayalık, 52 Harita kartının içindeki normal Kayalık kartına dönüştürüldü.
- `HAR-KY-01` ve `HAR-KY-03` Geçilmez Kayalıktır; Kayalık kategori yüzleri diğer Kayalıklardan ayırt edilemez.
- 52 Harita / 12 Kayalık / 118 toplam kart kimliği korunur.
- Küçük Haritalarda 1, büyük Haritalarda 2 Geçilmez normal Kayalık kotasının içinde zorunludur.
- Kapalı Geçilmez normal Harita kartı gibi rota/Ufuk hedefidir ve bütün bilgi/gizlilik/kart değiştirme kurallarına tabidir.
- Seçilip açıldığında Gemi kareye girmez; önceki konumda kalır. Normal rota günü ise hareket harcanır; kart açık kalıp kamusal engele dönüşür.
- Acil geri dönüş yalnız açılmış/bilinen Geçilmezlerin oluşturduğu tam ileri çıkmazda çalışır.
- 7.200 kart-çifti karşılaştırması + 6.000 temsilî + 9.000 tam duyarlılık testinde kalıcı rota kilidi 0.
- v2.3 kural kitabı ve kart prototip PDF'leri üretildi ve görsel kontrolden geçti.

## v2.2 - Stabil prototip

`releases/v2.2/` değiştirilemez stabil geri dönüş referansıdır. v2.2'deki ayrı görünür Geçilmez Kayalık işareti sistemi yalnız v2.2 tarihsel sürümünde kalır.

## v2.1 - Önceki stabil temel

`releases/v2.1/` değiştirilemez tarihsel geri dönüş referansı olarak korunur.
