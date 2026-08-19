# AI Handoff Protocol

Bu dosya farklı ChatGPT oturumları/model sürümleri arasında oyunun kanonik durumunu yeniden kurmak için zorunlu protokoldür.

## Sürüm durumu

- **Son kilitli stabil sürüm:** `v2.6 STABLE / LOCKED` — `releases/v2.6/`.
- **Kilitli mekanik baseline / geri dönüş:** `v2.5 STABLE / LOCKED` — `releases/v2.5/`.
- v2.6 **yeni mekanik içermez**; v2.5 oyun motorunu korur, kural öğretimini, Moderatör akışını ve Siyah Mühür anlatı katmanını kilitler.
- Otomatik "en yeni LOCKED/STABLE" çalışma protokolü artık **v2.6'yı** seçmelidir; mekanik doğrulama gerektiğinde v2.5 baseline ayrıca yüklenmelidir.
- `releases/v2.6/` ve `releases/v2.5/` yerinde değiştirilmez; sonraki tasarım/mekanik değişiklikleri **v2.7+** hattında açılır.

## Her yeni çalışma oturumunda

1. `AI_HANDOFF.md` ve `PROJECT_STATE.md` dosyalarını oku.
2. `releases/v2.6/README_RELEASE_v2.6.md`, `SOURCE_PACKAGE.md`, `BINARY_ARTIFACTS.md`, `V26_RELEASE_MANIFEST.json` ve `V26_BLIND_RULEBOOK_AUDIT.md` dosyalarını kontrol et.
3. Mekanik ayrıntı/test gerektiğinde `releases/v2.5/README_RELEASE_v2.5.md` ve v2.5 tam baseline paketini kullan.
4. v2.6 tam Library ZIP'ini SHA-256 ile doğrula. Tam kart PDF'sinin v2.5 hash'iyle aynı kaldığını kontrol et.
5. Yeni değişikliği v2.6'ya veya v2.5'e yazma; **v2.7+** çalışma hattı aç.

## v2.6 anlatı ve öğretim kilidi

- Oyun dünyası 1721 civarı kurgusal veba dönemidir; Arden Krallığı, Kraliçe Eleonora, San Cordelio, Saint Verena Karantina Limanı ve `Siyah Mühür` ana anlatı katmanıdır.
- Kaptan Gusto kalkıştan hemen önce kaybolur; ikinci kaptan olmadığı ve gemi bekleyemediği için ilk Kaptan tayfa oylamasıyla seçilir.
- Gusto'nun akıbeti **kanonda çözümsüzdür**; Siyah balmumu kesin kanıt değildir.
- İlk tarafsız gece Kaptanın tek Yakın Ufuk bilgisi Gusto'nun seyir defteriyle anlatısallaştırılır.
- Sadakatler dağıtılmadan önce Siyah Mühür'ün rüşvet/tehdit ağı kısa okunur; Kaptan da Hain olabilir.
- Zorunlu hikâye okumaları kısa tutulur; ayrıntılı arka plan `Siyah Mühür Dosyası` ekindedir.
- Kartların kuru/absürt mizah dili korunur; mekanik kart metinleri değiştirilmez.

## v2.5 mekanik omurga — v2.6'da aynen geçerli

- Gemi fiziksel `SET-KL-01` Kalkış Limanında başlar; Hedef Liman üst sıradadır.
- İlk gün yalnız Kaptan seçimi; ilk tarafsız gecede Kaptan Sadakatini bilmeden tam 1 yasal Yakın Ufka gizlice bakar; Sadakatler ertesi sabah; ilk gerçek rota normal eşzamanlı oylamadır ve Kaptan oyu 2 sayar.
- Başlangıç paketi N-1 gerçek Güç + Çürümüş Erzak; Erzak sahibi İskorbüt sonucu belirlendikten sonra 1 gerçek Güç çeker. İlk yolculuk gününe herkes 1 gerçek Güçle başlar.
- Kamusal Harita açmaları açık kalır; ziyaret edilmedikçe olay çözülmez; kamusal Geçilmez anında blocker olur.
- Acil geri dönüş ziyaret yolunu Kalkış Limanına kadar izleyebilir; bilinen çıkmaza alternatif varken yeniden girilmez.
- Relocation guard: İskorbüt aktif ve temizlenmemişse en az bir Ada üzerinden Hedef Limana kazanılabilir yolu; aksi halde Hedef Liman yolunu korur. Ayrıca Girdap/Ters Akıntı - Ada 8-komşuluk yasağını oyun boyunca korur.
- Kaderi Yeniden Yaz × Geçilmez: Geçilmez açık blocker kalır, Gemi girilmiş/ziyaret edilmiş sayılmaz, aynı hareket penceresinde başka yasal Yakın Ufka yönlenebilir. Ada girişi İskorbütü önce temizler.
- Kaptan ilk beraberlikte bir yeniden oy; ikinci beraberlikte yalnız eşit adaylar Kader Zarıyla sonuca gider.
- Gövde 2; Hain tablosu 6:1, 7:2, 8–10:3, 11–13:4, 14–15:5.
- 20 Karakter / 30 Güç / 1 Çürümüş Erzak / 15 Sadakat / 52 Harita / 12 Kayalık / 118 ana kimlik korunur.
- `HAR-KY-01` ve `HAR-KY-03` gizli Geçilmezdir.

## Doğrulama özeti

- v2.5 tam release validatorı v2.6 hazırlanırken yeniden çalıştırıldı: **PASS**.
- v2.5 çekirdek/tam motor, geometri, relocation, İskorbüt ve PDF/package kapıları korunur.
- v2.6 kör kural kitabı denetimi: **PASS**.
- v2.6 release validator: **PASS**; 20/20 Karakter, 15 kritik kural işareti PASS.
- Tam kart PDF hash'i v2.5 ile birebir aynı: `e158b33b77d2fff962420170d87aea407c87c97c9d611e19a6b72e7827aba4cc`.

## Kilitli artefaktlar

- v2.6 Full ZIP: `/Oyun-GitHub/OYUN_SIMULASYON_PAKETI_v2.6.zip`
  - SHA-256: `9878c00e1f72f587e75f84b480bb2ff33fd815cf95e45fdaee019beb2fe465a4`
- v2.6 Kural PDF: `/Oyun-GitHub/v2.6/OYUN_Kural_Kitabi_v2.6.pdf`
  - SHA-256: `dc3811e1387398904f9473d03f83b4ee703dc48908500695ff2adf0982947c77`
- v2.6 ayrı Karakter baskı PDF: `/Oyun-GitHub/v2.6/OYUN_Karakter_Kartlari_v2.5_UNCHANGED.pdf`
  - Karakter yüzleri değiştirilmemiştir.
- v2.5 mekanik baseline ZIP: `/Oyun-GitHub/OYUN_SIMULASYON_PAKETI_v2.5.zip`
  - SHA-256: `975dd77d435a835fcf3faa864c5624b0542fadb419fa7d34217ed32fe87aa046`

## Kısa devam komutu

> GitHub'daki Açık Deniz oyun reposunu aç; `AI_HANDOFF.md`, `PROJECT_STATE.md` ve `releases/v2.6/README_RELEASE_v2.6.md` dosyalarını okuyup en son kilitli v2.6 sürümünden devam et. Mekanik doğrulama için v2.5 baseline'ı kullan. Yeni tasarım değişikliklerini v2.7+ hattında yap.
