# Project State

**Son güncelleme:** 2026-08-18  
**Son stabil prototip:** **v2.2**  
**Stabil kanonik kaynak:** `releases/v2.2/`  
**Aktif geliştirme:** **v2.3 - gizli Geçilmez Kayalık**  
**Aktif branch:** `change/v2.3-gizli-gecilmez-kayalik`  
**Durum:** teknik doğrulama + prototip PDF PASS; insan masa testi bekleniyor.

## v2.3 kesin tasarım kararı

- Geçilmez Kayalık artık ayrı işaret/token değildir.
- Mevcut 52 Harita kartının 12 Kayalık kartı içinde **2 fiziksel Geçilmez Kayalık kartı** bulunur.
- Toplam Harita = 52; Kayalık = 12; toplam kart kimliği = 118. Kart eklenmez.
- `HAR-KY-01` = **Duvar Gibi Kayalık / Geçilmez Kayalık**.
- `HAR-KY-03` = **Yolun Bittiği Yer / Geçilmez Kayalık**.
- `HAR-KY-02` tek Batık Kalyon olarak kalır.
- İki Geçilmez kartın kategori yüzü diğer Kayalıklarla birebir aynıdır; kapalıyken ayırt edilemez.
- Bütün normal Harita kartı gizlilik, Ufuk, bilgi, Pusula, kart bakma/değiştirme ve yerleştirme kurallarına tabidir.
- Küçük Haritalar (`5x5`, `5x6`, `6x5`) Kayalık kotasının içinde 1; büyük Haritalar (`5x7`, `6x6`, `6x7`) 2 Geçilmez içerir.
- Geçilmez kart son Liman/Ufuk hattına kurulamaz. Moderatör konumlarını açıklamadan başlangıçtan erişilebilir bir Ada üzerinden Limana gerçek ileri yol kaldığını doğrular.
- Kapalı Geçilmez normal rota/Ufuk hedefidir. Rota veya olay içi hareketle açılırsa Gemi kareye girmez ve önceki konumunda kalır; kart açık kalır.
- Normal rota gününde açıldıysa hareket/gün harcanır. Olay içi ek hareket sırasında açıldıysa yalnız ek hareket sona erer.
- Açılmış Geçilmez kamusal engeldir ve artık rota/Ufuk hedefi değildir.
- Acil geri dönüş yalnız açılmış/bilinen Geçilmez Kayalıklar bütün ileri rotaları kapatmışsa çalışır; gizli kart bu nedensellik hesabında engel sayılmaz.

## Korunan v2.2 omurgası

- Kaptan kalıcıdır; ilk rotayı Kaptan tek başına ve olay bilgisi olmadan seçer.
- Kaptan değişimini gerektiren mevcut İsyan ve görev dışı kalma hükümleri korunur.
- Kaptan gece ayrıca uyanmaz ve makamı otomatik Ufuk bilgisi vermez.
- Gemi bütün Haritalarda 2 Gövdeyle başlar.
- Gemi alt kenarın dışında herhangi bir sütun hizasında başlayabilir.

## v2.3 teknik kanıt

- Kart çifti karşılaştırması: 7.200 oyun.
- Seçilen çift temsilî doğrulama: 6.000 oyun; Tayfa %55,47; gizli Kayalığa çarpılan oyun %31,63; ilk rota çarpması %5,17; geri dönüş %3,43; kalıcı kilit 0.
- 6-15 oyuncu tam duyarlılık: 9.000 oyun; Tayfa %55,51; gizli Kayalığa çarpma %32,21; geri dönüş %3,50; kalıcı kilit 0; kurulum hatası 0.
- Kesin geometri: 51.204 toplam / 51.102 yasal / 102 Moderatörce reddedilecek.
- `python working/v2.3/oyun_simulasyon_v2_3.py --validate-only --geometry-audit`: PASS.
- Kural kitabı PDF: 32 sayfa; kart PDF: 32 sayfa; render/preflight ve görsel tarama PASS.

## Release durumu

v2.3 **henüz stabil değildir**. İnsan masa testi ve son release kararı beklenir. Bu sırada `releases/v2.2/` değiştirilemez stabil geri dönüş noktasıdır.
