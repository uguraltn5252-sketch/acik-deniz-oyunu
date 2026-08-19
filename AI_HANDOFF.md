# AI Handoff Protocol

Bu dosya farklı ChatGPT oturumları/model sürümleri arasında oyunun kanonik durumunu yeniden kurmak için zorunlu protokoldür.

## Sürüm durumu

- **Son kullanıcı onaylı kilitli stabil sürüm:** `v2.5 STABLE / LOCKED` — `releases/v2.5/`.
- `v2.6` klasörü **DRAFT / NOT LOCKED** durumundadır. Kullanıcı onayı olmadan kilitlenmiş olduğu için kanonik release sayılmaz.
- Otomatik "en yeni LOCKED/STABLE" çalışma protokolü **v2.5'i** seçmelidir.
- `releases/v2.5/` yerinde değiştirilmez; yeni çalışmalar kullanıcı açıkça onay verene kadar taslak sürüm olarak tutulur.

## Her yeni çalışma oturumunda

1. `AI_HANDOFF.md` ve `PROJECT_STATE.md` dosyalarını oku.
2. Kanonik mekanik ve kart seti için `releases/v2.5/README_RELEASE_v2.5.md`, `V25_RELEASE_MANIFEST.json`, `SOURCE_PACKAGE.md`, `BINARY_ARTIFACTS.md` ve `V25_TEST_REPORT.md` dosyalarını kontrol et.
3. v2.6 yalnız kural kitabı/öğretme/anlatı taslağı olarak incelenebilir; otomatik olarak release veya kilitli sürüm kabul edilmez.
4. Tam insan kuralı, full JSON/spec, tam Tayfa/Hain motoru, tüm kartlar ve test kanıtları için v2.5 tam paketini SHA-256 ile doğrula.
5. Kullanıcı açıkça istemeden hiçbir taslak sürümü STABLE/LOCKED ilan etme.

## v2.5 kilitli omurga

- Gemi fiziksel `SET-KL-01` Kalkış Limanında başlar; Hedef Liman üst sıradadır.
- İlk gün yalnız Kaptan seçimi; ilk tarafsız gecede Kaptan Sadakatini bilmeden tam 1 yasal Yakın Ufka gizlice bakar; Sadakatler ertesi sabah; ilk gerçek rota normal eşzamanlı oylamadır ve Kaptan oyu 2 sayar.
- Başlangıç paketi N-1 gerçek Güç + Çürümüş Erzak; Erzak sahibi İskorbüt sonucu belirlendikten sonra 1 gerçek Güç çeker. İlk yolculuk gününe herkes 1 gerçek Güçle başlar.
- Kamusal Harita açmaları açık kalır; ziyaret edilmedikçe olay çözülmez; kamusal Geçilmez anında blocker olur.
- Acil geri dönüş ziyaret yolunu Kalkış Limanına kadar izleyebilir; bilinen çıkmaza alternatif varken yeniden girilmez.
- Relocation guard: İskorbüt aktif ve temizlenmemişse en az bir Ada üzerinden Hedef Limana kazanılabilir yolu; aksi halde Hedef Liman yolunu korur. Ayrıca Girdap/Ters Akıntı - Ada 8-komşuluk yasağını oyun boyunca korur.
- Kaderi Yeniden Yaz × Geçilmez: Geçilmez açık blocker kalır, Gemi girilmiş/ziyaret edilmiş sayılmaz, aynı hareket penceresinde başka yasal Yakın Ufka yönlenebilir. Ada girişi İskorbütü önce temizler.
- Kaptan ilk beraberlikte bir yeniden oy; ikinci beraberlikte yalnız eşit adaylar Kader Zarıyla sonuca gider.
- Gövde 2; Hain tablosu 6:1, 7:2, 8–10:3, 11–13:4, 14–15:5.
- **Tam kart seti:** 20 Karakter / 30 Güç / 1 Çürümüş Erzak / 15 Sadakat / 52 Harita / 12 Kayalık / 118 ana kimlik.
- `HAR-KY-01` ve `HAR-KY-03` gizli Geçilmezdir.

## v2.6 taslak notu

- v2.6 kural kitabı taslağı; Siyah Mühür/Gusto anlatısı, Moderatör akışı ve okunabilirlik düzenlemelerini içerir.
- Taslak paketteki `OYUN_Kartlar_A4_Prototip_v2.5_UNCHANGED.pdf` **tam kart PDF'sidir** ve Karakter + Güç + Sadakat + Çürümüş Erzak + Harita kartlarının tamamını içerir.
- `OYUN_Karakter_Kartlari_v2.5_UNCHANGED.pdf` yalnızca yardımcı/ayrı baskı çıktısıdır; oyunun kart setinin tamamı değildir.
- Bu taslak kullanıcı onayı olmadan kilitlenemez.

## Kilitli artefaktlar

- v2.5 Full ZIP: `/Oyun-GitHub/OYUN_SIMULASYON_PAKETI_v2.5.zip`
  - SHA-256: `975dd77d435a835fcf3faa864c5624b0542fadb419fa7d34217ed32fe87aa046`
- v2.5 Kural PDF: `/Oyun-GitHub/v2.5/OYUN_Kural_Kitabi_v2.5.pdf`
- v2.5 Tam Kart PDF: `/Oyun-GitHub/v2.5/OYUN_Kartlar_A4_Prototip_v2.5.pdf`
  - SHA-256: `e158b33b77d2fff962420170d87aea407c87c97c9d611e19a6b72e7827aba4cc`

## Kısa devam komutu

> GitHub'daki Açık Deniz oyun reposunu aç; `AI_HANDOFF.md`, `PROJECT_STATE.md` ve `releases/v2.5/README_RELEASE_v2.5.md` dosyalarını okuyup son kullanıcı-onaylı kilitli v2.5 sürümünden devam et. `releases/v2.6/` yalnız taslaktır; kullanıcı açıkça onaylamadan kilitleme.
