# Açık Deniz Sosyal Çıkarım Oyunu

Bu repository oyunun kalıcı ve denetlenebilir kaynak kaydıdır. Amaç, ChatGPT oturumları veya model sürümleri değişse bile kuralları, testleri, anlatı kararlarını ve sürüm geçmişini kaybetmemektir.

## Kanonik durum

- Son kilitli/stabil sürüm: **v2.6 STABLE / LOCKED**
- Kanonik release kaydı: `releases/v2.6/`
- Kilitli mekanik baseline / geri dönüş: `releases/v2.5/`
- v2.6 **yeni mekanik eklemez**; v2.5 motorunu korur ve kural kitabı/öğretme/Moderatör/anlatı katmanını kilitler.
- `releases/v2.5/` ve `releases/v2.6/` yerinde değiştirilmez.
- Yeni tasarım veya mekanik değişiklikleri **v2.7+** çalışma hattında yapılır.

## Her yeni ChatGPT oturumunda

1. `AI_HANDOFF.md` okunur.
2. `PROJECT_STATE.md` okunur.
3. `releases/v2.6/README_RELEASE_v2.6.md`, `SOURCE_PACKAGE.md`, `BINARY_ARTIFACTS.md`, `V26_RELEASE_MANIFEST.json` ve `V26_BLIND_RULEBOOK_AUDIT.md` kontrol edilir.
4. Mekanik ayrıntı/test gerekiyorsa `releases/v2.5/` baseline kaynakları ve v2.5 tam paket validatorı kullanılır.
5. Son commit/PR/issue durumu kontrol edilir.
6. Yeni değişiklikler doğrudan kilitli release klasörlerine yazılmaz; v2.7+ açılır.

## v2.6 kaynak hiyerarşisi

1. **Oyuncu/Moderatör kuralı:** `/Oyun-GitHub/v2.6/OYUN_Kural_Kitabi_v2.6.pdf` ve düzenlenebilir DOCX.
2. **Mekanik kaynak:** v2.5 STABLE / LOCKED tam insan kuralı + JSON/spec + doğrulama motorları.
3. **Kart baseline:** v2.5 tam Kart PDF'si byte-for-byte korunur; v2.6 paketinde `OYUN_Kartlar_A4_Prototip_v2.5_UNCHANGED.pdf` adıyla bulunur.
4. **Karakter baskı dosyası:** kilitli v2.5 kart PDF'sinden yalnız baskı talimatı + Karakter yapraklarının seçilmiş kopyası; kart yüzleri değiştirilmez.
5. **Anlatı kanonu:** Kaptan Gusto'nun kayboluşu, Siyah Mühür, Arden/San Cordelio/Saint Verena ve kural kitabındaki `Siyah Mühür Dosyası`. Gusto'nun kesin akıbeti bilinçli olarak çözümsüzdür.
6. **Release doğrulaması:** `releases/v2.6/V26_RELEASE_MANIFEST.json` + v2.5 baseline yeniden doğrulaması.

## Kilitli paket

`/Oyun-GitHub/OYUN_SIMULASYON_PAKETI_v2.6.zip`  
SHA-256: `9878c00e1f72f587e75f84b480bb2ff33fd815cf95e45fdaee019beb2fe465a4`

Uyuşmazlık bulunursa sessiz varsayım yapılmaz; kilitli hash/release kayıtları ile karşılaştırılır ve yeni değişiklik ayrı sürüm hattında ele alınır.
