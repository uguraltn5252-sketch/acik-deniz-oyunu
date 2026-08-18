# Test Log

## T-20260818-001..006 - v2.1/v2.2 geçmiş doğrulamaları
- v2.1 stabil doğrulaması: PASS.
- Dinamik başlangıç/geometri: PASS; çözümsüz kurulumların reddi zorunlu.
- 3 Gövde adayı: RED; bütün Haritalar 2 Gövde.
- v2.2 görünür Geçilmez + geri dönüş teknik testi: PASS.
- v2.2 kaynak sözleşmesi ve baskı/release doğrulaması: PASS; `releases/v2.2/` kilitlendi.

## T-20260818-007 - v2.3 gizli/entegre Geçilmez Kayalık

### Kart dönüşüm seçimi
- 4 aday çift × 6 temsilî hücre × 300 = **7.200 oyun**.
- Seçilen: `HAR-KY-01` Ufak Kayalık + `HAR-KY-03` ikinci Batık Kalyon.
- Gerekçe: bütün 5 hasarlı Kayalık ve bütün benzersiz Kayalık mekanikleri korunuyor.

### Seçilen çift temsilî doğrulama
- **6.000 oyun**.
- Tayfa: **%55,47**.
- En az bir gizli Geçilmeze çarpma: **%31,63**.
- İlk rotada çarpma: **%5,17**.
- Acil geri dönüş: **%3,43**.
- Kalıcı rota kilidi: **0**; kurulum hatası: **0**.

### 6–15 oyuncu tam duyarlılık
- 10 oyuncu sayısı × 3 süre × 300 = **9.000 oyun**.
- Tayfa ortalaması: **%55,51**.
- Gizli Geçilmeze çarpma: **%32,21**.
- İlk rota çarpması: **%5,26**.
- Acil geri dönüş: **%3,50**.
- Kalıcı rota kilidi: **0**; kurulum hatası: **0**.
- Süre bandı Tayfa: Hızlı %57,23 / Standart %55,20 / Uzun %54,10.

### Statik/geometri doğrulaması
- Tam kaynak paketindeki `oyun_simulasyon_v2_3.py --validate-only --geometry-audit`: **PASS**.
- GitHub release tarafındaki `python releases/v2.3/validate_release_v2_3.py`: **PASS**.
- 52 Harita / 12 Kayalık / 2 gizli Geçilmez / 118 kimlik.
- Geometri: **51.204 teorik / 51.102 yasal / 102 reddedilecek**.

### PDF/prototip
- v2.3 Kart PDF: **32 sayfa**, preflight PASS; `HAR-KY-01` ve `HAR-KY-03` olay yüzlerinde Geçilmez, kapalı kategori yüzlerinde diğer Kayalıklardan ayırt edilemez.
- v2.3 Kural Kitabı: **32 sayfa**, render/görsel tarama PASS.
- Kaynak ↔ PDF çapraz kontrol: PASS.

### Hüküm
**PASS / v2.3 stabil prototip kilidine uygun.**

## T-20260818-008 - v2.3 release kilidi
- Stabil metadata ile tam kaynak doğrulayıcı yeniden çalıştırıldı: **PASS**.
- Geometri: 51.204 / 51.102 / 102 değişmedi.
- PDF SHA-256: kart `91d34850bc8b0bc895d36d0090fbd682c723484ed615ffc6e383bcc186511d63`; kural `aec5acc83ced2931401c066d9cd570e844952573940f97e9d9603531d501ff87`.
- Tam ZIP SHA-256: `d0c5562cfbb81c752b01f549026e11b281ea54f57b0d3545c7d4e25fdcdd331b`.
- Sonuç: `releases/v2.3/` **STABLE / LOCKED**.
