# OYUN — Değişiklik Kaydı v2.5

## v2.4 → v2.5

1. İskorbüt aktifken Harita relocation guard artık yalnız Liman yolunu değil, en az bir Ada üzerinden Hedef Limana kazanılabilir yolu da korur.
2. Girdap/Ters Akıntı - Ada 8-komşuluk yasağı yalnız kurulum kuralı olmaktan çıkarılıp oyun-boyu invariant yapıldı; relocation bunu bozamaz.
3. Kaderi Yeniden Yaz × Geçilmez kesinleştirildi: kart açık blocker kalır, Gemi girmiş/ziyaret etmiş sayılmaz, aynı hareket penceresinde başka yasal Yakın Ufka yönlenebilir.
4. Çürümüş Erzak fiziksel kartıyla insan kuralı/spec yeniden hizalandı: sahibi İskorbüt sonucu belirlendikten sonra 1 gerçek Güç çeker; ilk yolculuk gününe herkes 1 gerçek Güçle başlar.
5. Full JSON spec'e Hain tablosu, oyuncu×süre Gövde-hasarı kotaları ve final release gate'leri eksiksiz işlendi.
6. Boş regression output / stale development-manifest sınıfı final stabil paketten çıkarıldı; yalnız final kanıtlar paketlenir.
7. Tam kanonik Tayfa/Hain motoru ve persona/policy/AB testleri v2.5 pakete dahil edildi.
8. v2.4'teki Kalkış Limanı, Kaptanın tarafsız tek bakışı, kamusal açılan kartın açık kalması, geri dönüş, Kaptan tie fallback'i, Hull 2 ve kart sayıları korunur.
9. Kart PDF'sinde yalnız kapak ve `GUC-27 Kaderi Yeniden Yaz` metni değişti; diğer 30 sayfa v2.4 ile piksel olarak aynıdır.
10. Sonraki tasarım değişiklikleri v2.6+ hattına aittir.
