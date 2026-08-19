# Project State

**Son güncelleme:** 19 Ağustos 2026  
**Son stabil prototip:** **v2.6 STABLE / LOCKED**  
**Kilitli mekanik baseline / rollback:** **v2.5 STABLE / LOCKED**  
**Kanonik release kaydı:** `releases/v2.6/`  
**Mekanik doğrulama kaynağı:** `releases/v2.5/`  
**Sonraki tasarım hattı:** **v2.7+**

v2.6 yeni mekanik eklemez. v2.5'in kilitli oyun motorunu koruyarak kural kitabını ilk kez oynayan masa için yeniden düzenler, Moderatör kullanımını sadeleştirir ve Siyah Mühür/Gusto anlatısını kanonik hikâye katmanı olarak kilitler.

## v2.6 kilitli kararları

- v2.5 mekaniklerinin tamamı aynen korunur; denge motoru v2.5'tir.
- Kural kitabı öğretme + referans mimarisine geçirilmiştir.
- İlk oyun için ağır istisnalar referansa taşınmış, kritik kurulum ve zamanlama bilgileri öne alınmıştır.
- Karakter kurulum yoğunluğu ilk kurulum bölümünde görünürdür; 6–7 kişide Uzakgören ve Kıyıçizen birlikte seçilmez.
- Kaptan Gusto kalkıştan hemen önce kaybolur; ikinci kaptan olmadığı için tayfa kendi Kaptanını seçer.
- Gusto'nun akıbeti çözümsüzdür; Siyah Mühür bağlantısı şüphe olarak kalır.
- İlk tarafsız gece bilgisi Gusto'nun seyir defteriyle anlatısallaştırılır; Sadakatler ertesi sabah dağıtılır ve Kaptan da Hain olabilir.
- Ayrıntılı arka plan hikâyesi `Siyah Mühür Dosyası` ekindedir; zorunlu masa okumaları kısa tutulur.
- Kart mekanikleri ve Karakter kartlarının yüzleri değiştirilmemiştir. Tam kart PDF'si v2.5 ile byte-for-byte aynıdır.

## v2.5 mekanik omurga — v2.6'da geçerli

- Kaptan kalıcı rol; ilk gün yalnız seçim. İlk tarafsız gecede Sadakat bilinmeden tam 1 Yakın Ufka gizli bakış; sonraki gecelerde makam otomatik bilgi vermez.
- Sadakat ertesi sabah; ilk gerçek rota normal eşzamanlı oylama, Kaptan oyu 2.
- N-1 gerçek Güç + Çürümüş Erzak kurulum paketi; Erzak sahibi sonuçtan sonra 1 gerçek Güç çeker. Her oyuncu ilk yolculuk gününe 1 gerçek Güçle başlar.
- Kalkış Limanı `SET-KL-01` 118 kimliğin dışında fiziksel kurulum bileşenidir; geri dönüş hedefidir.
- Kamusal açılan Harita kapanmaz; ziyaret edilmedikçe olayı çözülmez; kamusal Geçilmez blocker olur.
- İskorbüt aktifse relocation sonrası Ada→Hedef Liman kazanılabilirliği zorunlu; İskorbüt temizse Hedef Liman yolu zorunlu.
- Girdap/Ters Akıntı Ada 8-komşuluk yasağı oyun-boyu invarianttır ve relocation bunu bozamaz.
- Kaderi Geçilmezde kullanılabilir; Geçilmez ziyaret sayılmaz ve açık engel kalır. Ada girişi İskorbütü olaydan önce temizler.
- Gövde 2; Hain tablosu 6:1, 7:2, 8–10:3, 11–13:4, 14–15:5.
- 20 Karakter / 30 Güç / 1 Çürümüş Erzak / 15 Sadakat / 52 Harita / 12 Kayalık / 118 ana kimlik.

## Doğrulama kapıları

- v2.5 tam release validatorı v2.6 hazırlanırken yeniden çalıştırıldı: **PASS**.
- Geometri / relocation / final full balance / PDF audit / package hashes: **PASS**.
- v2.6 kör kural kitabı denetimi: **PASS**.
- v2.6 release validator: **PASS**.
- 20/20 Karakter adı ve 15 kritik mekanik işaret kural kitabında doğrulandı.
- Tam kart PDF hash'i korunur: `e158b33b77d2fff962420170d87aea407c87c97c9d611e19a6b72e7827aba4cc`.

## Kalan insan-only sorular

Eğlence, masa gerilimi, mizah, bekleme hissi, gerçek güven/şüphe, konuşma eşitsizliği ve özellikle 7 kişilik Uzun oyunun hissi gerçek kör insan playtestiyle ölçülmeye devam etmelidir. v2.6 kör denetimi kural kitabının izlenebilirliğini sınar; gerçek oyuncu davranışını kanıtlamaz.

## Artefaktlar

Library ZIP: `/Oyun-GitHub/OYUN_SIMULASYON_PAKETI_v2.6.zip`  
SHA-256: `9878c00e1f72f587e75f84b480bb2ff33fd815cf95e45fdaee019beb2fe465a4`

Kural PDF: `/Oyun-GitHub/v2.6/OYUN_Kural_Kitabi_v2.6.pdf`  
Ayrı Karakter baskı PDF: `/Oyun-GitHub/v2.6/OYUN_Karakter_Kartlari_v2.5_UNCHANGED.pdf`
