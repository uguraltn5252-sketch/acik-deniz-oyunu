# OYUN Değişiklik Kaydı v2.3

**Durum:** Geliştirme - teknik PASS, insan masa testi bekleniyor.  
**Temel:** v2.2 stabil prototip.

## v2.3-001 - Geçilmez Kayalık 52 Harita kartına entegre edildi

- Ayrı Geçilmez Kayalık işaret/token sistemi kaldırıldı.
- Toplam Harita kartı **52** kalır; Kayalık kategorisi **12** kalır; toplam kart kimliği **118** kalır.
- `HAR-KY-01` ve `HAR-KY-03` Geçilmez Kayalık olayına dönüştürüldü.
- İki kartın kategori yüzü normal `KAYALIK` yüzüdür ve diğer Kayalıklardan ayırt edilemez.
- Küçük Haritalarda bu iki karttan 1'i, büyük Haritalarda ikisi normal Kayalık kotasının içinde kurulumda bulunur.
- Kartlar normal Harita kurallarının tamamına tabidir: kapalı olay yüzü, Ufuk hedefi, özel bakma, bilgi paylaşma/yalan, kart yer değiştirme ve normal açılma.
- Açıldığında Gemi o kareye girmez; önceki konumda kalır. Normal rota günündeyse günün hareketi harcanır; kart açık kalır.
- Açılmış Geçilmez Kayalık bundan sonra kamusal engeldir.
- Acil geri dönüş yalnız açılmış/bilinen Geçilmez Kayalıkların bütün ileri rotaları kapatması halinde uygulanır.
- Son Liman/Ufuk hattında Geçilmez Kayalık bulunmaması ve gerçek başlangıç-Ada-Liman yolunun kurulumda korunması devam eder; bu bilgi oyunculara verilmez.

## Kart dönüşümü

- `HAR-KY-01`: Ufak Kayalık -> **Duvar Gibi Kayalık / Geçilmez Kayalık**
- `HAR-KY-03`: Batık Kalyon kopyası -> **Yolun Bittiği Yer / Geçilmez Kayalık**
- `HAR-KY-02`: Batık Kalyon olarak kalır.

Bu seçim 5 hasarlı Kayalık kartını ve benzersiz Kayalık mekaniklerinin tamamını korur.

## Test

- 4 kart çifti karşılaştırması: 7.200 oyun.
- Seçilen çift temsilî doğrulama: 6.000 oyun.
- 6-15 oyuncu tam duyarlılık: 9.000 oyun.
- Kalıcı rota kilidi: 0.
- Kurulum hatası: 0.
- Tam geometri: 51.204 teorik / 51.102 yasal / 102 reddedilecek.
- v2.3 çekirdek doğrulayıcı: PASS.
- Kart PDF ve kural kitabı görsel preflight: PASS.
