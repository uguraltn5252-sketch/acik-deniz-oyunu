# Changelog

## v2.2 — Geliştirme sürümü

**Durum:** Aktif geliştirme. Henüz stabil sürüm olarak kilitlenmedi.

v2.1 sonrası kesinleşen değişiklikler bu sürüm altında toplanır:

- Gemi Haritanın alt kenarının dışında herhangi bir hizada başlayabilir; ilk Ufuk ve ilk Sis yasağı seçilen başlangıca göre dinamikleşir.
- Kaptan rolü kalıcıdır ve asla kaldırılmaz.
- İlk rotayı Kaptan tek başına ve olay bilgisi olmadan seçer.
- Başarılı İsyan, Kaptanın ölümü veya mevcut kurallardaki görev yapamama durumlarında yeni Kaptan seçilir.
- Kaptan gece ayrıca uyanmaz ve makamı otomatik Ufuk bilgisi vermez.
- Gemi bütün Harita boylarında 2 Gövdeyle başlar.
- Geçilmez Kayalık artık çekirdek mekaniktir.
- `5×5`, `5×6`, `6×5` Haritalarda 1; `5×7`, `6×6`, `6×7` Haritalarda 2 Geçilmez Kayalık bulunur.
- Geçilmez Kayalık Limanın hemen kıçındaki son Harita/Ufuk hattına konulamaz.
- Normal geri hareket yasaktır; yalnız Geçilmez Kayalık bütün ileri rotaları kapatmışsa Gemi bir önceki kareye bir tam hareket/gün harcayarak geri dönebilir.
- Geri dönülen çözülmüş kartın olayı tekrar çalışmaz.
- Başlangıçtan itibaren matematiksel olarak çözümsüz Harita kurulamaz.
- Geçilmez Kayalık + acil geri dönüş teknik testi PASS: 51.204 geometri yerleşimi, 15.000 yeni-kural simülasyonu ve 6.000 kontrol oyunu; kalıcı rota kilidi 0.

### v2.2 stabil kilidi için gerekenler

- İnsan kural metni v2.2'ye güncellenecek.
- JSON/spec v2.2'ye güncellenecek.
- Asıl doğrulayıcı ve regresyon testleri v2.2'ye güncellenecek.
- İlgili PDF/baskı çıktıları yeniden üretilecek ve görsel kontrol edilecek.
- Bütün kaynaklar aynı sürümü gösterdiğinde `v2.2` stabil sürüm olarak kilitlenecek.

## v2.1 — Stabil temel

Ayrıntılı tarihçe için `releases/v2.1/OYUN_DEGISIKLIK_KAYDI_v2.1.md` dosyasına bakın.

`v2.1` değiştirilemez geri dönüş referansıdır; v2.2 çalışmaları v2.1 dosyalarının üzerine yazılmaz.
