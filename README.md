# Açık Deniz Sosyal Çıkarım Oyunu

Bu repository oyunun kalıcı ve denetlenebilir kaynak kaydıdır. Amaç, ChatGPT oturumları veya model sürümleri değişse bile kuralları, testleri, anlatı kararlarını ve sürüm geçmişini kaybetmemektir.

## Kanonik durum

- Son kullanıcı-onaylı kilitli/stabil sürüm: **v2.5 STABLE / LOCKED**
- Kanonik release kaydı: `releases/v2.5/`
- `releases/v2.6/` **DRAFT / NOT LOCKED** durumundadır; kullanıcı onayı olmadan kilitlendiği için kanonik release sayılmaz.
- Yeni bir sürüm ancak kullanıcı açıkça onay verirse STABLE/LOCKED ilan edilir.

## Her yeni ChatGPT oturumunda

1. `AI_HANDOFF.md` okunur.
2. `PROJECT_STATE.md` okunur.
3. Kanonik oyun için `releases/v2.5/README_RELEASE_v2.5.md`, `V25_RELEASE_MANIFEST.json`, `SOURCE_PACKAGE.md` ve `BINARY_ARTIFACTS.md` kontrol edilir.
4. v2.6 yalnız kural kitabı/anlatı/Moderatör akışı taslağı olarak incelenebilir.
5. Son commit/PR/issue durumu kontrol edilir.
6. Kullanıcı açıkça istemeden yeni sürüm kilitlenmez.

## v2.5 kaynak hiyerarşisi

1. **İnsan kuralı:** v2.5 tam kural kaynağı ve `OYUN_Kural_Kitabi_v2.5.pdf`.
2. **Makine kuralı:** v2.5 JSON/spec ve doğrulama motorları.
3. **Tam kart baseline:** `OYUN_Kartlar_A4_Prototip_v2.5.pdf` — Karakter + Güç + Çürümüş Erzak + Sadakat + Harita kartlarının tamamı.
4. **Kart sayıları:** 20 Karakter / 30 Güç / 1 Çürümüş Erzak / 15 Sadakat / 52 Harita / 118 ana kimlik.

## v2.6 taslak notu

v2.6 kural kitabı taslağı; Siyah Mühür/Gusto anlatısı ve okunabilirlik düzenlemelerini içerir. Taslak paket içinde `OYUN_Kartlar_A4_Prototip_v2.5_UNCHANGED.pdf` tam kart setini taşır. Ayrı `OYUN_Karakter_Kartlari_v2.5_UNCHANGED.pdf` yalnız yardımcı baskı dosyasıdır; oyunun kart seti değildir.

## Kilitli paket

`/Oyun-GitHub/OYUN_SIMULASYON_PAKETI_v2.5.zip`  
SHA-256: `975dd77d435a835fcf3faa864c5624b0542fadb419fa7d34217ed32fe87aa046`
