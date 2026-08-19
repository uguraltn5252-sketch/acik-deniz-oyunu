# OYUN v2.6 — STABLE / LOCKED

**Taban mekanik:** v2.5 STABLE / LOCKED  
**Durum:** STABLE / LOCKED  
**Tarih:** 19 Ağustos 2026  
**Sürüm tipi:** Kural kitabı / öğretme akışı / anlatı / Moderatör kullanılabilirliği revizyonu. **Yeni mekanik yoktur.**

v2.6, v2.5'in kilitli oyun motoruna dokunmadan kural kitabını ilk kez oynayan masa için yeniden düzenler ve Siyah Mühür ana hikâyesini kanonik anlatı katmanı olarak ekler.

## v2.6'da değişenler

- Kural kitabı 26 sayfalık öğretme + referans yapısına dönüştürüldü.
- Zorunlu hikâye okuması kısa tutuldu; ayrıntılı evren metni `Siyah Mühür Dosyası` ekine taşındı.
- Gusto'nun kayboluşu Kaptan oylamasının anlatısal gerekçesi olarak kilitlendi; akıbeti bilinçli olarak çözümsüz bırakıldı.
- İlk tarafsız gece / Gusto'nun seyir defteri / Sadakat öncesi Siyah Mühür metinleri doğru zamanlama kutularına yerleştirildi.
- Kör kural kitabı denetiminde bulunan karakter kurulum yoğunluğu, erken terim yükü, başlangıç Güç hazırlığı, Kaptan masumiyet algısı ve Kaptan değişim görünürlüğü sorunları düzeltildi.
- Karakter kartları ve tüm fiziksel kart mekanikleri **değişmedi**.
- v2.5 kart PDF'si byte-for-byte korunur; SHA-256 aynı kalır.

## Mekanik omurga değişmedi

- Gövde 2.
- İlk gün yalnız Kaptan seçimi; Kaptan Sadakatleri bilmeden ilk tarafsız gecede tam 1 yasal Yakın Ufka bakar.
- Sadakat ertesi sabah; ilk gerçek rota normal eşzamanlı oylama ve Kaptan rota oyu 2.
- Hainler ilk yolculuk gecesinde tanışır, 1 Yakın Ufka bakar ve saldırı yapamaz.
- Çürümüş Erzak / İskorbüt / Ada zorunluluğu v2.5 ile aynıdır.
- Geçilmez, relocation guard, Ada çevresi invariantı, Kaderi×Geçilmez, Suçlama/İsyan/Kamara, Pusula/Kayıkçı ve Liman Gecesi hükümleri v2.5 ile aynıdır.
- 20 Karakter / 30 Güç / 1 Çürümüş Erzak / 15 Sadakat / 52 Harita / 12 Kayalık / 118 ana kimlik aynıdır.

## Doğrulama

- v2.5 tam release validatorı yeniden çalıştırıldı: **PASS**.
- Geometry / relocation / final full balance / PDF audit / package hashes: **PASS**.
- v2.6 kör kural kitabı denetimi: **PASS**.
- v2.6 release validator: **PASS**.
- 20/20 Karakter adı kural kitabında mevcut; karakter kurulum yoğunluğu ilk kurulum akışına taşındı.
- v2.5 tam Kart PDF hash'i korunur: `e158b33b77d2fff962420170d87aea407c87c97c9d611e19a6b72e7827aba4cc`.

## Sürüm politikası

`v2.6` bu belge/anlatı düzeniyle kilitlenmiştir. v2.5 mekanik geri dönüş tabanıdır. Bundan sonraki mekanik veya tasarım değişiklikleri **v2.7+** hattında yapılmalıdır.
