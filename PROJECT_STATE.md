# Project State

**Son güncelleme:** 19 Ağustos 2026  
**Son kullanıcı-onaylı stabil prototip:** **v2.5 STABLE / LOCKED**  
**Kanonik kaynak:** `releases/v2.5/`  
**v2.6 durumu:** **DRAFT / NOT LOCKED**  
**Not:** v2.6 kullanıcı onayı olmadan kilitlendiği için release statüsü geri alınmıştır.

v2.5 oyunun son onaylı mekanik ve fiziksel kart baseline'ıdır. v2.6 yalnızca kural kitabı okunabilirliği, Moderatör akışı ve Siyah Mühür/Gusto anlatısı üzerine taslak çalışmadır.

## v2.5 kilitli kararları

- Kaptan kalıcı rol; ilk gün yalnız seçim. İlk tarafsız gecede Sadakat bilinmeden tam 1 Yakın Ufka gizli bakış; sonraki gecelerde makam otomatik bilgi vermez.
- Sadakat ertesi sabah; ilk gerçek rota normal eşzamanlı oylama, Kaptan oyu 2.
- N-1 gerçek Güç + Çürümüş Erzak kurulum paketi; Erzak sahibi sonuçtan sonra 1 gerçek Güç çeker. Her oyuncu ilk yolculuk gününe 1 gerçek Güçle başlar.
- Kalkış Limanı `SET-KL-01` 118 kimliğin dışında fiziksel kurulum bileşenidir; geri dönüş hedefidir.
- Kamusal açılan Harita kapanmaz; ziyaret edilmedikçe olayı çözülmez; kamusal Geçilmez blocker olur.
- İskorbüt aktifse relocation sonrası Ada→Hedef Liman kazanılabilirliği zorunlu; İskorbüt temizse Hedef Liman yolu zorunlu.
- Girdap/Ters Akıntı Ada 8-komşuluk yasağı oyun-boyu invarianttır ve relocation bunu bozamaz.
- Kaderi Geçilmezde kullanılabilir; Geçilmez ziyaret sayılmaz ve açık engel kalır. Ada girişi İskorbütü olaydan önce temizler.
- Gövde 2; Hain tablosu 6:1, 7:2, 8–10:3, 11–13:4, 14–15:5.
- **Tam kart seti:** 20 Karakter / 30 Güç / 1 Çürümüş Erzak / 15 Sadakat / 52 Harita / 12 Kayalık / 118 ana kimlik.

## v2.6 taslak durumu

- Kural kitabı öğretme + referans mimarisi taslağıdır.
- Gusto/Siyah Mühür anlatısı taslak kanon önerisidir; kullanıcı onayı olmadan release kanonu sayılmaz.
- v2.6 paketindeki `OYUN_Kartlar_A4_Prototip_v2.5_UNCHANGED.pdf` tam kart setidir ve v2.5 tam kart PDF'siyle byte-for-byte aynıdır.
- Ayrı `OYUN_Karakter_Kartlari_v2.5_UNCHANGED.pdf` yalnız yardımcı baskı çıktısıdır; tam set değildir.
- Kullanıcı açıkça onaylamadan v2.6 veya sonraki hiçbir taslak STABLE/LOCKED ilan edilmez.

## Test kapıları

- v2.5: çekirdek regresyon PASS; tam motor PASS; geometri/relocation/İskorbüt/PDF audit PASS.
- v2.6 kör kural kitabı denetimi yalnız taslak kullanılabilirlik kontrolüdür; release onayı değildir.

## Kanonik artefakt

Library ZIP: `/Oyun-GitHub/OYUN_SIMULASYON_PAKETI_v2.5.zip`  
SHA-256: `975dd77d435a835fcf3faa864c5624b0542fadb419fa7d34217ed32fe87aa046`
