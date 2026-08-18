# Changelog

## v2.2 - Stabil prototip

**Tarih:** 18 Ağustos 2026  
**Durum:** Kilitli release - `releases/v2.2/`

v2.1'e göre başlıca değişiklikler:

- Gemi başlangıcı sabit merkezden çıkarıldı; alt kenarın dışında herhangi bir sütun hizası kullanılabilir.
- İlk Yakın Ufuk ve ilk Sis yasağı başlangıç/Liman geometrisine göre dinamikleşti.
- Kaptanın kalıcı çekirdek rol olduğu kilitlendi; ilk rotayı tek başına kör seçer.
- Başarılı İsyan, Kaptanın ölümü, Kamara, mahsur kalma ve Kayıkçı seferinde yeni Kaptan seçimi korunur.
- Kaptan gece ayrıca uyanmaz ve makamı otomatik Ufuk bilgisi vermez.
- Gemi bütün haritalarda 2 Gövdeyle başlar; 3 Gövde adayı reddedildi.
- Harita büyüklüğüne göre 1 veya 2 ayrı Geçilmez Kayalık işareti çekirdek mekaniğe eklendi.
- Geçilmez Kayalık son Liman yaklaşım hattına konulamaz ve baştan çözümsüz kurulum yasaktır.
- Yalnız Geçilmez Kayalık kaynaklı tam ileri çıkmazda bir önceki kareye bir tam gün harcayarak acil geri dönüş açılır; çözülmüş olay tekrar çalışmaz.
- Kural kitabı PDF, kart PDF ve Geçilmez Kayalık işaret sayfası üretildi; görsel ve kaynak/PDF doğrulaması PASS.

Teknik kanıt: 51.204 geometri yerleşimi, 15.000 yeni-kural davranışsal oyun + 6.000 kontrol; kalıcı rota kilidi 0.

## v2.1 - Önceki stabil temel

`releases/v2.1/` değiştirilemez geri dönüş referansı olarak korunur.
