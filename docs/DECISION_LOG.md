# Decision Log

## D-20260818-001 - v2.1'i değiştirilemez stabil temel olarak koru
- **Durum:** Kabul.
- **Karar:** `releases/v2.1/` yerinde değiştirilmez.

## D-20260818-002 - Kaptan kalıcı omurgadır ve ilk rotayı seçer
- **Durum:** Kabul.
- **Karar:** Kaptan rolü asla kaldırılmaz. İlk rotayı Kaptan tek başına, olay bilgisi olmadan seçer. Başarılı İsyan, ölüm, Kamara, mahsur kalma veya Kayıkçı seferinde yeni Kaptan seçilir. Kaptan gece ayrıca uyanmaz ve otomatik Ufuk bilgisi almaz.

## D-20260818-003 - Geçilmez Kayalık Liman yaklaşım hattına konulamaz
- **Durum:** Kabul.
- **Karar:** Geçilmez Kayalık son Liman/Ufuk hattında bulunamaz; kurulum baştan çözümsüz olamaz.

## D-20260818-004 - Gövde bütün Haritalarda 2 kalır
- **Durum:** Kabul.

## D-20260818-005 - Kayalık kaynaklı tam çıkmazda acil geri dönüş
- **Durum:** Kabul.
- **Karar:** Normal geri hareket yasaktır; yalnız Geçilmez Kayalık kaynaklı tam ileri çıkmazda önceki ziyaret edilmiş kareye bir tam hareket/gün harcayarak dönülebilir; çözülmüş olay tekrar çalışmaz.

## D-20260818-006 - v2.2 sürüm adı
- **Durum:** Kabul.

## D-20260818-007 - v2.2 stabil prototip kilidi
- **Durum:** Kabul.
- **Karar:** `releases/v2.2/` değiştirilemez stabil geri dönüş sürümüdür.

## D-20260818-008 - Geçilmez Kayalıklar v2.3'te gizli Harita kartıdır
- **Durum:** Kabul.
- **Karar:** Ayrı görünür işaret sistemi kaldırılır. `HAR-KY-01` ve `HAR-KY-03`, mevcut 12 Kayalık kartının içindeki iki Geçilmez Kayalıktır. Harita 52, Kayalık 12, toplam kimlik 118 kalır.
- **Gizlilik:** Kategori yüzleri diğer Kayalıklarla aynıdır; kapalıyken ayırt edilemez ve bütün normal Harita bilgi/Ufuk/bakma/blöf kurallarına tabidir.
- **Açılma:** Rota/olay hareketi bu karta yönelirse kart açılır fakat Gemi kareye girmez; mevcut konumunda kalır. Normal rota günündeyse hareket harcanır. Kart açık kamusal engel olur.
- **Test:** T-20260818-007 PASS.

## D-20260818-009 - v2.3 stabil prototip olarak kilitlenir
- **Durum:** **Kabul / LOCKED.**
- **Karar:** Teknik, geometri, kart sözleşmesi ve PDF doğrulaması PASS alan v2.3 `releases/v2.3/` altında değiştirilemez stabil prototip olarak kilitlenir. İnsan masa testi sonraki iyileştirmeler için önerilir ancak stabil kilidin ön koşulu değildir.
- **Sonuç:** Sonraki tasarım değişiklikleri **v2.4+** olarak açılmalıdır.
