# Project State

**Son güncelleme:** 2026-08-18  
**Stabil temel:** v2.1  
**Aktif geliştirme:** v2.1 sonrası kararların `develop` hattına taşınması.

## Stabil temel

`releases/v2.1/` mevcut stabil geri dönüş referansıdır ve yerinde değiştirilmez.

## v2.1 sonrası kesinleşmiş yeni omurga kararları

- Gemi Haritanın alt kenarının dışında herhangi bir hizada başlayabilir; ilk Ufuk ve ilk Sis yasağı seçilen başlangıca göre dinamikleşir.
- Kaptan rolü kalıcıdır ve **asla kaldırılmaz**.
- Geminin ilk rotasını Kaptan tek başına ve olay bilgisi olmadan seçer.
- Kaptan gece ayrıca uyanmaz; makamı otomatik Ufuk bilgisi vermez.
- Gemi bütün Harita boylarında **2 Gövdeyle** başlar.
- Geçilmez Kayalık her oyunda bulunur.
- Geçilmez Kayalık adedi: `5×5`, `5×6`, `6×5` = 1; `5×7`, `6×6`, `6×7` = 2.
- Geçilmez Kayalık Limanın hemen kıçındaki son Harita/Ufuk hattına konulamaz.
- Normalde geri hareket yasaktır. Yalnız Geçilmez Kayalık bütün yasal ileri rotaları kapatmışsa Gemi bir önceki bulunduğu kareye bir adım geri dönebilir.
- Bu acil geri dönüş bir tam hareket/gün tüketir; çözülmüş kartın olayı tekrar çalışmaz.
- İlk rota tamamen kapatılamaz ve başlangıçtan itibaren matematiksel olarak çözümsüz Harita kurulamaz.

Ayrıntılı gerekçeler: `docs/DECISION_LOG.md` ve `docs/V2_1_SONRASI_KARSILASTIRMA.md`.

## Henüz uygulanması gereken teknik işler

1. İnsan kural metnini yeni başlangıç + Geçilmez Kayalık + acil geri dönüş hükümleriyle güncelle.
2. JSON/spec'te sabit başlangıç sütununu kaldır; dinamik başlangıç ve 1/2 Geçilmez Kayalık sayısını ekle.
3. Ufuk yasallığında Geçilmez Kayalığı erişilemez hedef yap.
4. Geri dönüş tetikleyicisini yalnız `sıfır ileri rota + Geçilmez Kayalık nedenselliği` durumunda aç.
5. Daha önce çözülmüş karta geri dönüldüğünde olay tekrarını engelle.
6. Regresyon testlerini bütün 6 Harita boyunda çalıştır.
7. v2.1'in stabil doğrulamasını değişmeden koru.

## Değişiklik tamamlanmış sayılma ölçütü

Bir değişiklik ancak aşağıdakilerin hepsi tamamlandığında resmîdir:

- İnsan kural metni güncel.
- Makine JSON kaynağı güncel.
- İlgili kod/test güncel.
- Statik doğrulama geçiyor.
- Denge/rota davranışını etkiliyorsa ilgili simülasyon veya grafik test geçiyor.
- Baskı dosyası etkileniyorsa yeniden üretilmiş ve görsel kontrolden geçmiş.
- `docs/DECISION_LOG.md` güncel.
- `docs/TEST_LOG.md` güncel.
