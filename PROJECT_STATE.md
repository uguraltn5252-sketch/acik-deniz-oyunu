# Project State

**Son güncelleme:** 2026-08-18  
**Stabil temel:** v2.1  
**Aktif geliştirme sürümü:** **v2.2**  
**Aktif kaynak branch'i:** `release/v2.2-dev`  
**Durum:** çekirdek kaynak seti üretildi ve teknik doğrulaması PASS; baskı/release stabilizasyonu bekliyor.

## Sürüm politikası

- `v2.1` mevcut stabil geri dönüş referansıdır ve yerinde değiştirilmez.
- v2.1 sonrasında kesinleşen yeni kurallar **v2.2** altında toplanır.
- v2.2, bütün release gate maddeleri tamamlanmadan "development" statüsündedir.
- Kural kitabı/PDF, görsel kontrol ve son release kilidi tamamlandığında `releases/v2.2/` altında stabil kopya oluşturulur.

## v2.2 altında kesinleşmiş omurga

- Gemi Haritanın alt kenarının dışında herhangi bir sütun hizasında başlayabilir; sabit merkez başlangıcı yoktur.
- İlk Yakın Ufuk ve ilk Sis yasağı seçilen başlangıca, Liman erişimine ve Geçilmez Kayalıklara göre dinamik hesaplanır.
- **Kaptan rolü kalıcıdır ve asla kaldırılmaz.**
- Geminin ilk rotasını Kaptan tek başına, olay bilgisi olmadan seçer.
- Kaptanın rota oyu 2; diğer resmî oyları 1'dir; rota beraberliğini berabere yasal rotalar arasında Kaptan çözer.
- Başarılı İsyan, Kaptanın ölümü, Kamara, mahsur kalma veya Kayıkçı seferi durumunda yeni Kaptan seçilir.
- Kaptan gece ayrıca uyanmaz; makamı otomatik Yakın/Uzak Ufuk bilgisi vermez.
- Gemi bütün Harita boylarında **2 Gövdeyle** başlar.
- Geçilmez Kayalık her oyunda bulunur: `5×5`, `5×6`, `6×5` = 1; `5×7`, `6×6`, `6×7` = 2.
- Geçilmez Kayalık 52 Harita kartından ayrı, görünür bir kurulum işaretidir; 118 kart kimliği değişmez.
- Geçilmez Kayalık Limanın hemen kıçındaki son Harita/Ufuk hattına konulamaz; ilk rotayı kapatamaz ve kurulum başlangıçtan erişilebilir Ada üzerinden Limana en az bir ileri yol bırakmalıdır.
- Normal geri hareket yasaktır. Yalnız bütün yasal ileri rotalar Geçilmez Kayalık nedeniyle kapanmışsa Gemi geldiği bir önceki kareye bir tam hareket/gün harcayarak geri çekilebilir.
- Geri dönülen çözülmüş olay yeniden çalışmaz. Çıkmaz sürerse sonraki normal günde koşullar yeniden sağlanıyorsa bir kare daha geri dönülebilir.
- Bilinen Kayalık çıkmaz koluna başka yasal seçenek varken yeniden girilemez.
- Girdap/olay içi ek hareket yalnız Geçilmez Kayalık yüzünden hedef bulamazsa ek hareket boşa düşer; aynı gün acil geri dönüş başlamaz.

## v2.2 çekirdek kaynak seti

`working/v2.2/` altında:

- `OYUN_TAM_KURALLAR_v2.2.md` — **DONE**
- `OYUN_SIMULASYON_SPEC_v2.2.json` — **DONE**; v2.1 kart kataloğunu hash + sayım sözleşmesiyle miras alan makine delta spec'i
- `oyun_simulasyon_v2_2.py` — **DONE**
- `OYUN_DEGISIKLIK_KAYDI_v2.2.md` — **DONE**
- `README_SIMULASYON_v2.2.md` — **DONE**
- `V22_VALIDATE_OUTPUT.txt` — **PASS çıktısı**

## Teknik doğrulama

`T-20260818-005`: **PASS**.

Komut:

```bash
python oyun_simulasyon_v2_2.py --validate-only --geometry-audit
```

Kesin geometri:

- toplam: **51.204**
- yasal: **51.102**
- kurulumda reddedilecek: **102**
- geçersiz dağılım: `5×5=0`, `5×6=0`, `5×7=20`, `6×5=8`, `6×6=50`, `6×7=24`

Önceki hedefli davranışsal test de PASS:

- 15.000 yeni-kural oyunu + 6.000 kontrol
- kalıcı rota kilidi: 0
- kurulum hatası: 0
- temsilî Tayfa ortalaması: %54,8
- acil geri dönüş yaklaşık %4,2 oyunda
- ortalama +0,12 gün / +0,09 gece / ~+0,70 dakika

Bu sayısal sonuçlar insan masa testinin yerini tutmaz.

## v2.2 release gate

- [x] İnsan kural metni
- [x] Makine JSON/spec
- [x] v2.2 doğrulayıcı
- [x] Çekirdek statik/geometri regresyonu
- [x] Geçilmez Kayalık hedefli davranışsal teknik test
- [ ] v2.2 masa kural kitabı PDF
- [ ] Geçilmez Kayalık fiziksel işaret/çıktı tasarımı
- [ ] PDF görsel taşma, sayfa ve baskı kontrolü
- [ ] Son kaynak/PDF çapraz doğrulaması
- [ ] `releases/v2.2/` stabil kilidi

Bu son maddeler tamamlanana kadar **v2.2-dev**; son stabil sürüm **v2.1** olarak kalır.
