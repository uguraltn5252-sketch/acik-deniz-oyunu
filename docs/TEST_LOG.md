# Test Log

## T-20260818-001..006 - v2.1/v2.2 geçmiş testleri
- v2.1 stabil doğrulaması: PASS.
- Dinamik başlangıç/geometri: PASS; çözümsüz kurulumların reddi zorunlu.
- 3 Gövde adayı: RED; bütün Haritalar 2 Gövde.
- v2.2 görünür Geçilmez + geri dönüş teknik testi: PASS.
- v2.2 kaynak sözleşmesi: PASS.
- v2.2 baskı/release çapraz doğrulaması: PASS; `releases/v2.2/` kilitlendi.

## T-20260818-007 - v2.3 gizli/entegre Geçilmez Kayalık

### Kart dönüşüm seçimi
- 4 aday çift x 6 temsilî hücre x 300 = **7.200 oyun**.
- Seçilen: `HAR-KY-01` Ufak Kayalık + `HAR-KY-03` ikinci Batık Kalyon.
- Gerekçe: bütün 5 hasarlı Kayalık ve bütün benzersiz Kayalık mekanikleri korunuyor.

### Seçilen çift temsilî doğrulama
- **6.000 oyun**.
- Tayfa: **%55,47**.
- En az bir gizli Geçilmez'e çarpma: **%31,63**.
- İlk rotada çarpma: **%5,17**.
- Acil geri dönüş: **%3,43** oyun.
- Kalıcı route lock: **0**; kurulum hatası: **0**.

### 6-15 oyuncu tam duyarlılık
- 10 oyuncu sayısı x 3 süre x 300 = **9.000 oyun**.
- Tayfa ortalaması: **%55,51**.
- Gizli Geçilmez'e çarpma: **%32,21**.
- İlk rota çarpması: **%5,26**.
- Acil geri dönüş: **%3,50**.
- Kalıcı route lock: **0**; kurulum hatası: **0**.
- Süre bandı Tayfa: Hızlı %57,23 / Standart %55,20 / Uzun %54,10.

### Statik/kart doğrulaması
- Komut: `python working/v2.3/oyun_simulasyon_v2_3.py --validate-only --geometry-audit`.
- Sonuç: **PASS**.
- 52 Harita / 12 Kayalık / 2 gizli Geçilmez / 118 kimlik.
- Geometri: 51.204 teorik / 51.102 yasal / 102 reddedilecek.

### PDF/prototip
- v2.3 Kart PDF: **32 sayfa**, preflight PASS; `HAR-KY-01` ve `HAR-KY-03` olay yüzlerinde Geçilmez, kategori yüzünde diğer Kayalıklardan ayırt edilemez.
- v2.3 Kural Kitabı: **32 sayfa**, bütün sayfalar render edilip görsel tarandı; görünür taşma/çakışma/kırık glif yok.
- Kaynak <-> PDF çapraz kontrol: PASS.

### Hüküm
**PASS / v2.3 geliştirme hattına teknik kabul.** İnsan masa testi hâlâ gereklidir; bu sayısal testler blöf, güven ve eğlenceyi kanıtlamaz.
