# Açık Deniz Sosyal Çıkarım Oyunu

Bu repository oyunun kalıcı ve denetlenebilir kaynak kaydıdır. Amaç, ChatGPT oturumları veya model sürümleri değişse bile kuralları, testleri, anlatı kararlarını ve sürüm geçmişini kaybetmemektir.

## Kanonik durum

- Son kullanıcı-onaylı kilitli/stabil sürüm: **v2.5 STABLE / LOCKED**
- Kanonik release kaydı: `releases/v2.5/`
- Güncel geliştirme hattı: **v2.6 DRAFT / NOT LOCKED**
- v2.6 kullanıcı açıkça onaylamadan kanonik release sayılmaz.

## Her yeni ChatGPT oturumunda

1. `AI_HANDOFF.md` okunur.
2. `PROJECT_STATE.md` okunur.
3. Kilitli mekanik kaynak için `releases/v2.5/` incelenir.
4. Güncel tasarım taslağı için `releases/v2.6/README_RELEASE_v2.6.md`, `BINARY_ARTIFACTS.md`, `CARD_BASELINE.md` ve `V26_RELEASE_MANIFEST.json` okunur.
5. Bir çelişkide v2.5 kilitli mekanik baseline geçerlidir.
6. Kullanıcı açıkça istemeden yeni sürüm kilitlenmez.

## v2.5 kaynak hiyerarşisi

1. **İnsan kuralı:** v2.5 tam kural kaynağı ve `OYUN_Kural_Kitabi_v2.5.pdf`.
2. **Makine kuralı:** v2.5 JSON/spec ve doğrulama motorları.
3. **Tam kart baseline:** `OYUN_Kartlar_A4_Prototip_v2.5.pdf`.
4. **Ana kart sayıları:** 20 Karakter / 30 Güç / 1 Çürümüş Erzak / 15 Sadakat / 52 Harita / 118 ana kimlik.

## Güncel v2.6 taslağı

### Kural kitabı

`/Oyun-GitHub/v2.6/OYUN_Kural_Kitabi_v2.6_DRAFT.pdf`

- 29 sayfa A4.
- Oyuncu kuralları + Moderatör/storyteller akışı + referanslar + Siyah Mühür arka plan hikâyesi tek kitapta.
- Ayrı Moderatör kartı güncel taslakta yoktur.

### Kart seti

`/Oyun-GitHub/v2.6/OYUN_Kartlar_A4_Prototip_v2.6_DRAFT.pdf`

- 34 sayfa A4.
- 118 ana oyun kimliği korunur.
- Ana sayının dışında yardımcı kartlar: Kalkış Limanı + Varış/Hedef Limanı + Kaptan makamı.
- Mahkûm için ayrı kart/token yok; Moderatör not alır.
- Çürümüş Erzak ve Bayat Peksimet değiştirilmemiştir.

### Güncel taslak paket

`/Oyun-GitHub/OYUN_v2.6_DRAFT_GUNCEL.zip`  
SHA-256: `ba39598ba0d5be7f592a5ab52fec65230e46d61b8885545321ea8734c024d483`

## Kilitli paket

`/Oyun-GitHub/OYUN_SIMULASYON_PAKETI_v2.5.zip`  
SHA-256: `975dd77d435a835fcf3faa864c5624b0542fadb419fa7d34217ed32fe87aa046`
