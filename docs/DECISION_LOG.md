# Decision Log

## D-20260818-001 - v2.1'i değiştirilemez stabil temel olarak koru
- **Durum:** Kabul.
- **Karar:** `releases/v2.1/` yerinde değiştirilmez.

## D-20260818-002 - Kaptan kalıcı omurgadır ve ilk rotayı seçer
- **Durum:** Kabul.
- **Karar:** Kaptan rolü asla kaldırılmaz. İlk rotayı Kaptan tek başına ve olay bilgisi olmadan seçer. Başarılı İsyan ve mevcut görev dışı kalma durumlarında yeni Kaptan seçilir. Kaptan gece ayrıca uyanmaz ve otomatik Ufuk bilgisi vermez.

## D-20260818-003 - Geçilmez Kayalık Liman yaklaşım hattına konulamaz
- **Durum:** Kabul.
- **Karar:** Geçilmez Kayalık son Liman/Ufuk hattında bulunamaz; kurulum baştan çözümsüz olamaz.

## D-20260818-004 - Gövde bütün Haritalarda 2 kalır
- **Durum:** Kabul.

## D-20260818-005 - Kayalık kaynaklı çıkmazda acil geri dönüş
- **Durum:** Kabul.
- **Karar:** Normal geri hareket yasaktır; yalnız Geçilmez Kayalık kaynaklı tam ileri çıkmazda önceki kareye bir tam hareket/gün harcayarak dönülebilir; çözülmüş olay tekrar çalışmaz.

## D-20260818-006 - v2.2 sürüm adı
- **Durum:** Kabul.

## D-20260818-007 - v2.2 stabil prototip kilidi
- **Durum:** Kabul.
- **Karar:** `releases/v2.2/` değiştirilemez son stabil prototiptir.

## D-20260818-008 - Geçilmez Kayalıklar v2.3'te gizli Harita kartıdır
- **Durum:** Kabul / v2.3 geliştirme.
- **Karar:** Ayrı görünür işaret sistemi v2.3'te kaldırılır. `HAR-KY-01` ve `HAR-KY-03` mevcut 12 Kayalık kartının içinde iki Geçilmez Kayalığa dönüşür. Harita 52, Kayalık 12, toplam kimlik 118 kalır.
- **Gizlilik:** Kategori yüzü diğer Kayalıklarla aynıdır. Kapalıyken ayırt edilemez ve bütün normal Harita kartı bilgi, Ufuk, bakma, Pusula, takas/yer değiştirme ve sosyal bilgi kurallarına tabidir.
- **Açılma:** Rota/olay hareketi bu karta yönelirse kart normal şekilde açılır fakat Gemi kareye girmez; önceki konumunda kalır. Normal rota günündeyse hareket harcanır. Kart açık kalır ve kamusal engel olur.
- **Geri dönüş:** Yalnız açılmış/bilinen Geçilmezlerin tam ileri çıkmaz oluşturması halinde acil geri dönüş açılır.
- **Kart seçimi:** `HAR-KY-01` eski etkisiz Ufak Kayalık; `HAR-KY-03` tekrarlı Batık Kalyon kopyasıdır. Böylece 5 hasarlı Kayalık ve bütün benzersiz Kayalık mekanikleri korunur.
- **Test:** T-20260818-007 PASS.
