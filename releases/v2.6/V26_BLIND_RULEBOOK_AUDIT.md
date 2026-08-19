# v2.6 Kör Kural Kitabı Denetimi

**Taban:** v2.5 STABLE / LOCKED mekanikleri  
**Kapsam:** İlk kez oynayan oyuncu + ilk kez yöneten Moderatör gözüyle öğretme sırası, terim yükü, kurulum riski ve karakter/kart uyumu.  
**Sonuç:** PASS - mekanik değişiklik yapılmadan açıklık düzeltmeleri uygulandı.

## Bulunan ve düzeltilen ana sürtünmeler

1. **Karakter kurulum yoğunluğu ilk öğretme akışında değildi.** İlk kez yöneten Moderatör 20 Karakteri gelişigüzel dağıtabilir, özellikle 6-7 kişide Uzakgören + Kıyıçizen yasağını ve toplam Etki sınırını ihlal edebilirdi. v2.6'da tablo doğrudan `3.1 Karakterleri dağıt` bölümüne ve Moderatör masa kartına taşındı.
2. **Harita kurulumunda kullanılan bazı terimler açıklanmadan önce geliyordu.** `Yakın Ufuk`, `yasal ilk rota` ve `gerçek yol` için kısa Moderatör kurulum sözlüğü eklendi. Ayrıntılı hareket kuralı yine Bölüm 6'da kaldı.
3. **“İlk Sefer = Bölüm 1-5” ifadesi bütün oyunu yalnız bu bölümlerle oynayabilirmiş izlenimi verebilirdi.** v2.6 metni, oyuncuların 1-5 ile başlayabileceğini ama Moderatörün 6, 7, 8, 12 ve Ek A'yı hazır tutması gerektiğini açıkça söyler.
4. **İlk Kaptan seçiminde henüz kullanılmayan Kamara/yaşama uygunluğu dili gereksiz bilişsel yük yaratıyordu.** İlk seçim için sade biçimde “her oyuncu aday olabilir ve oy verebilir” denildi; genel uygunluk hükümleri referansta korundu.
5. **Başlangıç Gücü hazırlığında “28 başlangıca uygun Güç” ifadesi gereksiz dolaylıydı.** `Kaderi Yeniden Yaz` ve `Seyir Zabtı` ayrılır, kalan 28 kart karıştırılır şeklinde yazıldı.
6. **Tarafsız Kaptanın ertesi sabah Hain çıkabileceği yeterince görünür değildi.** Sadakat dağıtımının yanına “Kaptanlık masumiyet kanıtı değildir” uyarısı eklendi.
7. **Kaptan oyun ortasında makamdan düştüğünde yeni seçimin ne kadar hızlı yapılacağı ana akışta görünür değildi.** Normal tur akışına “hemen yeni Kaptan seç, sonra kaldığın yerden devam et” kutusu eklendi.
8. **Temel kart dili ilk sayfada yalnız Karakter/Sadakat üzerinden anlatılıyordu.** Güç ve Harita kartlarının ne olduğu tek satırlık açıklamayla eklendi; kart metinlerine dokunulmadı.
9. **Küçük bir yazım tekrarı** (`Geçilmez ise geçilemezlik ise`) düzeltildi.

## Kör masa soruları

- Oyuncu ilk iki dakikada hedefini biliyor mu? **Evet.**
- Kaptan oylamasının hikâye gerekçesi anlaşılır mı? **Evet; Gusto kayıp, gemi bekleyemez, ikinci kaptan yok.**
- Kaptanın ilk bilgiyi Sadakatinden önce aldığı açık mı? **Evet.**
- Hainlerin ilk gece neden saldırmadığı açık mı? **Evet.**
- İskorbüt aktifse Ada zorunluluğu unutulabilir mi? **Düşük risk; ana bölüm + hızlı referans + Moderatör kartında tekrar ediliyor.**
- Kamusal açma ile gizli bakış ayrılıyor mu? **Evet; tablo ve arka kapak özeti var.**
- Kaptan değişim tetikleri görünür mü? **Evet; ana tur kutusu + Ek A + arka kapak.**
- Karakter kurulum yoğunluğu ilk oyunda uygulanabilir mi? **Evet; kurulum bölümünde tablo var.**
- İlk oyunda tüm kart referanslarını ezberlemek gerekiyor mu? **Hayır; zaman penceresi kart üstünde, ayrıntı referansta.**
- Arka plan hikâyesi oyunu başlatmayı geciktiriyor mu? **Hayır; zorunlu okuma kısa, uzun Siyah Mühür dosyası isteğe bağlı ek.**

## Mekanik koruma

- v2.5 tam release validatorı yeniden çalıştırıldı: **PASS**.
- Geometri / relocation / full balance / PDF audit / package hashes: **PASS**.
- v2.6 Karakter referansı v2.5 kanonik Karakter tablosundan üretilir; karakter kart metinleri değiştirilmedi.
- v2.6 paketindeki tam Kart PDF'si v2.5 kilitli kart PDF'sinin byte-for-byte kopyasıdır.
- Ayrı `OYUN_Karakter_Kartlari_v2.5_UNCHANGED.pdf` dosyası aynı kilitli PDF'nin yalnız baskı talimatı + Karakter yapraklarını içerir; kart yüzleri değiştirilmez.

## Son karar

v2.6, **mekanik revizyon değil; öğretme/anlatı/release düzenlemesidir**. Denge motoru v2.5 olarak korunur. Sonraki mekanik değişiklik yapılacaksa v2.7+ hattında açılmalıdır.
