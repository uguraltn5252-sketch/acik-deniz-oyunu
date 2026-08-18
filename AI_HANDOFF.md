# AI Handoff Protocol

Bu dosya farklı ChatGPT oturumları/model sürümleri arasında oyunun kanonik durumunu yeniden kurmak için zorunlu protokoldür.

## Sürüm durumu

- **Son kilitli stabil sürüm:** `v2.5 STABLE / LOCKED` — `releases/v2.5/`.
- **Önceki stabil geri dönüş:** `v2.4 STABLE / LOCKED` — `releases/v2.4/`.
- Otomatik "en yeni LOCKED/STABLE" çalışma protokolü artık **v2.5'i** seçmelidir.
- `releases/v2.5/` yerinde değiştirilmez; sonraki tasarım değişiklikleri **v2.6+** hattında açılır.

## Her yeni çalışma oturumunda

1. `AI_HANDOFF.md` ve `PROJECT_STATE.md` dosyalarını oku.
2. `releases/v2.5/README_RELEASE_v2.5.md`, `V25_RELEASE_MANIFEST.json`, `SOURCE_PACKAGE.md`, `BINARY_ARTIFACTS.md` ve `V25_TEST_REPORT.md` dosyalarını kontrol et.
3. Release validatorı gerekiyorsa tam Library ZIP'ini açıp `python validate_release_v2_5.py` çalıştır; geometri ve baseline relocation hesapları yeniden yapılır, iç hashler doğrulanır.
4. Tam insan kuralı, full JSON/spec, tam Tayfa/Hain motoru, ham test kanıtları ve PDF'ler için `SOURCE_PACKAGE.md` içindeki kilitli ZIP'i SHA-256 ile doğrula.
5. Yeni tasarım değişikliğini v2.5'e yazma; **v2.6+** çalışma hattı aç.

## v2.5 kilitli omurga

- Gemi fiziksel `SET-KL-01` Kalkış Limanında başlar; Hedef Liman üst sıradadır.
- İlk gün yalnız Kaptan seçimi; ilk tarafsız gecede Kaptan Sadakatini bilmeden tam 1 yasal Yakın Ufka gizlice bakar; Sadakatler ertesi sabah; ilk gerçek rota normal eşzamanlı oylamadır ve Kaptan oyu 2 sayar.
- Başlangıç paketi N-1 gerçek Güç + Çürümüş Erzak; Erzak sahibi İskorbüt sonucu belirlendikten sonra 1 gerçek Güç çeker. İlk yolculuk gününe herkes 1 gerçek Güçle başlar.
- Kamusal Harita açmaları açık kalır; ziyaret edilmedikçe olay çözülmez; kamusal Geçilmez anında blocker olur.
- Acil geri dönüş ziyaret yolunu Kalkış Limanına kadar izleyebilir; bilinen çıkmaza alternatif varken yeniden girilmez.
- Relocation guard: İskorbüt aktif ve temizlenmemişse en az bir Ada üzerinden Hedef Limana kazanılabilir yolu; aksi halde Hedef Liman yolunu korur. Ayrıca Girdap/Ters Akıntı - Ada 8-komşuluk yasağını oyun boyunca korur.
- Kaderi Yeniden Yaz × Geçilmez: Geçilmez açık blocker kalır, Gemi girilmiş/ziyaret edilmiş sayılmaz, aynı hareket penceresinde başka yasal Yakın Ufka yönlenebilir. Ada girişi İskorbütü önce temizler.
- Kaptan ilk tie'da bir yeniden oy; ikinci tie'da yalnız eşit adaylar Kader Zarıyla sonuca gider.
- Gövde 2; 20 Karakter / 30 Güç / 1 Çürümüş Erzak / 15 Sadakat / 52 Harita / 12 Kayalık / 118 ana kimlik korunur.
- `HAR-KY-01` ve `HAR-KY-03` gizli Geçilmezdir.

## v2.5 doğrulama özeti

- Çekirdek regresyon **13/13 PASS**; tam motor **8/8 PASS**.
- 51.204 teorik / 51.102 legal geometri; kalıcı ilk-kol kilidi 0.
- Baseline relocation 1.667.231 transition; 20 unsafe rollback; kabul edilen kalıcı kilit 0.
- İskorbüt 5x5 exact 1.836.984 transition; 5.288 gerekli rollback; kabul edilen ihlal 0.
- Altı kritik Harita boyunda 6.000.000 relocation örneklemi; kabul edilen İskorbüt-kazanılabilirlik ihlali 0.
- Ada çevresi 50k: 2.461 ihlal önerisi, 2.461 rollback, 0 kabul.
- Stateful fuzz 448.812 eylem; invariant/hard-lock hatası 0.
- Final tam-sistem Monte Carlo 100.200 oyun; Tayfa %50,28; yaklaşık %95 GA %49,97-%50,59; motor hatası 0.
- Kural PDF 24 sayfa A4, kart PDF 32 sayfa A4; preflight/görsel audit PASS; 118/118 kimlik; Kayalık arka-yüz piksel sızıntısı 0.

## Kilitli artefaktlar

- Full ZIP: `/Oyun-GitHub/OYUN_SIMULASYON_PAKETI_v2.5.zip`
  - SHA-256: `975dd77d435a835fcf3faa864c5624b0542fadb419fa7d34217ed32fe87aa046`
- Kural PDF: `/Oyun-GitHub/v2.5/OYUN_Kural_Kitabi_v2.5.pdf`
  - SHA-256: `0e2f2c4ab3e908116f53776b7c46ebfb5cc9c0cb10050c012940eac85e9834e4`
- Kart PDF: `/Oyun-GitHub/v2.5/OYUN_Kartlar_A4_Prototip_v2.5.pdf`
  - SHA-256: `e158b33b77d2fff962420170d87aea407c87c97c9d611e19a6b72e7827aba4cc`

## Kısa devam komutu

> GitHub'daki Açık Deniz oyun reposunu aç; `AI_HANDOFF.md`, `PROJECT_STATE.md` ve `releases/v2.5/README_RELEASE_v2.5.md` dosyalarını okuyup en son kilitli v2.5 sürümünden devam et. Yeni tasarım değişikliklerini v2.6+ hattında yap.
