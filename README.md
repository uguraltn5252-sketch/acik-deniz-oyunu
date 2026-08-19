# Açık Deniz Sosyal Çıkarım Oyunu

Bu repository oyunun kalıcı ve denetlenebilir kaynak kaydıdır. Amaç, ChatGPT oturumları veya model sürümleri değişse bile kuralları, testleri, anlatı kararlarını ve sürüm geçmişini kaybetmemektir.

## Kanonik durum

- Son kullanıcı-onaylı kilitli/stabil sürüm: **v2.6 STABLE / LOCKED**
- Kanonik release kaydı: `releases/v2.6/`
- v2.5 önceki kilitli mekanik baseline/tarihsel geri dönüş referansıdır.
- Bundan sonraki herhangi bir değişiklik v2.7+ DRAFT hattında yapılır; v2.6 yerinde değiştirilmez.

## Her yeni ChatGPT oturumunda

1. `AI_HANDOFF.md` okunur.
2. `PROJECT_STATE.md` okunur.
3. Son kilitli sürüm için `releases/v2.6/README_RELEASE_v2.6.md`, `V26_RELEASE_MANIFEST.json`, `BINARY_ARTIFACTS.md`, `CARD_BASELINE.md` ve doğrulama raporları kontrol edilir.
4. Mekanik tarihsel baseline gerektiğinde `releases/v2.5/` incelenir.
5. Bir çelişkide son kullanıcı-onaylı v2.6 release kaydı kanonik sürüm statüsünü belirler; v2.5 mekanik hükümleri v2.6 tarafından değiştirilmemiş alanlarda baseline'dır.
6. v2.6 artefaktları yerinde değiştirilmez. Yeni çalışma v2.7+ DRAFT olarak açılır.

## v2.6 kilitli sürüm

### Kural kitabı

`/Oyun-GitHub/v2.6/OYUN_Kural_Kitabi_v2.6_DRAFT.pdf`

- 29 sayfa A4.
- Oyuncu kuralları + Moderatör/storyteller akışı + referanslar + Siyah Mühür arka plan hikâyesi tek kitapta.
- Ayrı Moderatör kartı yoktur.
- Dosya adı ve PDF içindeki `DRAFT` ibaresi kullanıcı talebiyle içerik değişmeden kilitlendiği için aynen korunmuştur.

### Kart seti

`/Oyun-GitHub/v2.6/OYUN_Kartlar_A4_Prototip_v2.6_DRAFT.pdf`

- 34 sayfa A4.
- 118 ana oyun kartı: 20 Karakter / 30 Güç / 1 Çürümüş Erzak / 15 Sadakat / 52 Harita.
- 3 yardımcı kart: `SET-KL-01` Kalkış Limanı + `SET-VL-01` Varış/Hedef Limanı + `SET-KP-01` Kaptan makamı.
- Toplam 121 basılabilir fiziksel kart.
- Mahkûm için ayrı kart/token yok; Moderatör not alır.
- Çürümüş Erzak ve Bayat Peksimet değiştirilmemiştir.
- Kayalık kartlarının mevcut arka yüzleri korunmuştur; Açık Deniz arka yüzü varyantı uygulanmamıştır.

### Kilitli paket

`/Oyun-GitHub/OYUN_v2.6_DRAFT_GUNCEL.zip`  
SHA-256: `cfb1fe5071270900610669ae6863f8fb96e6d7bba311276c2569b767336f7e8c`

## Önceki kilitli baseline

`/Oyun-GitHub/OYUN_SIMULASYON_PAKETI_v2.5.zip`  
SHA-256: `975dd77d435a835fcf3faa864c5624b0542fadb419fa7d34217ed32fe87aa046`
