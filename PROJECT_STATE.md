# Project State

**Son güncelleme:** 2026-08-18  
**Stabil temel:** v2.1  
**Aktif geliştirme sürümü:** **v2.2**  
**Durum:** v2.2 geliştirme / entegrasyon aşaması.

## Sürüm politikası

- `v2.1` mevcut stabil geri dönüş referansıdır ve yerinde değiştirilmez.
- v2.1 sonrasında kesinleşen yeni kurallar **v2.2** altında toplanır.
- v2.2; insan kural metni, JSON/spec, doğrulayıcı, regresyon testleri ve gerekiyorsa baskı PDF'leri aynı sürüme getirildikten sonra stabil olarak kilitlenir.
- Bu işlemler tamamlanmadan v2.2 "geliştirme sürümü"dür; v2.1 ise son stabil sürümdür.

## v2.2 altında kesinleşmiş yeni omurga kararları

- Gemi Haritanın alt kenarının dışında herhangi bir hizada başlayabilir; ilk Ufuk ve ilk Sis yasağı seçilen başlangıca göre dinamikleşir.
- Kaptan rolü kalıcıdır ve **asla kaldırılmaz**.
- Geminin ilk rotasını Kaptan tek başına ve olay bilgisi olmadan seçer.
- Kaptan gece ayrıca uyanmaz; makamı otomatik Ufuk bilgisi vermez.
- İsyan başarılı olduğunda mevcut Kaptan değişir ve yeni Kaptan seçilir.
- Kaptan ölürse yeni Kaptan seçilir.
- Kaptan mevcut kurallarda görev yapamayacak duruma girerse Kaptanlık boş bırakılmaz; yeni Kaptan seçilir.
- Gemi bütün Harita boylarında **2 Gövdeyle** başlar.
- Geçilmez Kayalık her oyunda bulunur.
- Geçilmez Kayalık adedi: `5×5`, `5×6`, `6×5` = 1; `5×7`, `6×6`, `6×7` = 2.
- Geçilmez Kayalık Limanın hemen kıçındaki son Harita/Ufuk hattına konulamaz.
- Normalde geri hareket yasaktır. Yalnız Geçilmez Kayalık bütün yasal ileri rotaları kapatmışsa Gemi bir önceki bulunduğu kareye bir adım geri dönebilir.
- Bu acil geri dönüş bir tam hareket/gün tüketir; çözülmüş kartın olayı tekrar çalışmaz.
- Kayalık nedeniyle çıkmaz olduğu öğrenilmiş kola başka yasal seçenek varken hemen yeniden girilmez.
- İlk rota tamamen kapatılamaz ve başlangıçtan itibaren matematiksel olarak çözümsüz Harita kurulamaz.
- Girdap gibi zorunlu ek hareket Geçilmez Kayalık yüzünden yapılamıyorsa zorunlu ek hareket boşa düşer; aynı gün geri dönüş tetiklenmez. Sonraki normal rota gününde hâlâ hiçbir ileri rota yoksa acil geri dönüş uygulanır.

Ayrıntılı gerekçeler: `docs/DECISION_LOG.md` ve `docs/V2_1_SONRASI_KARSILASTIRMA.md`.

## Geçilmez Kayalık teknik test durumu

**PASS.** `T-20260818-004` tamamlandı.

- 51.204 teorik geometri yerleşimi kesin tarandı.
- 15.000 yeni-kural davranışsal oyunu çalıştırıldı.
- 6.000 kontrol oyunu çalıştırıldı.
- Kalıcı rota kilidi: 0.
- Kurulum hatası: 0.
- Temsilî yeni-kural Tayfa ortalaması: %54,8.
- Geri dönüş yaklaşık %4,2 oyunda görüldü.
- Ortalama etki: +0,12 gün / +0,09 gece / yaklaşık +0,70 dakika.

Ayrıntılı rapor: `docs/GECILMEZ_KAYALIK_V22_RAPOR.md`.

## v2.2'nin stabil sayılması için kalan işler

1. İnsan kural metnini v2.2 hükümleriyle güncelle.
2. JSON/spec'te sabit başlangıç sütununu kaldır; dinamik başlangıç ve 1/2 Geçilmez Kayalık sayısını ekle.
3. Ufuk yasallığında Geçilmez Kayalığı erişilemez hedef yap.
4. Asıl doğrulayıcıya kurulum erişilebilirliği, Kayalık adedi ve geri dönüş kenar hükümlerini ekle.
5. Kaptan değişimi/İsyan/ölüm hükümlerinin yeni sürümde eksiksiz kaldığını regresyonla doğrula.
6. v2.1'in stabil doğrulamasını değişmeden koru.
7. Yeni kaynak seti üretildiğinde bütün regresyonu tekrar çalıştır.
8. Baskı PDF'leri v2.2 için yeniden üretilecekse görsel kontrol yap.
9. Bütün kaynaklar aynı sürümü gösterdiğinde `v2.2` stabil olarak kilitlenir.

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
