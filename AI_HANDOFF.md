# AI Handoff Protocol

Bu dosya farklı ChatGPT oturumları/model sürümleri arasında oyunun kanonik durumunu yeniden kurmak için zorunlu protokoldür.

## Sürüm durumu

- **Son kilitli stabil sürüm:** `v2.3 STABLE / LOCKED` — `releases/v2.3/`.
- **Aktif geliştirme adayı:** `v2.4 TEST-PASSED / NOT LOCKED` — `releases/v2.4/` ve branch `agent/v2.4-acilis-ve-kilit-duzeltmeleri`.
- Otomatik "en yeni LOCKED/STABLE" çalışma protokolü, v2.4 kilitlenene kadar **v2.3'ü** seçmelidir.
- v2.3 yerinde değiştirilmez. v2.4 PDF/kart/preflight kapıları tamamlanmadan stable/locked yapılmaz.

## Her yeni çalışma oturumunda

1. `AI_HANDOFF.md` ve `PROJECT_STATE.md` dosyalarını oku.
2. Stabil referans için `releases/v2.3/README_RELEASE_v2.3.md` ve manifestini kontrol et.
3. Aktif geliştirme devam edecekse `releases/v2.4/README_RELEASE_v2.4.md`, `V24_RULE_PATCH.md`, `V24_TEST_REPORT.md`, `V24_DEV_MANIFEST.json` ve `SOURCE_PACKAGE.md` dosyalarını oku.
4. v2.4 rota sözleşmesini yeniden doğrulamak için `python releases/v2.4/validate_release_v2_4.py` çalıştır. Bu doğrulayıcı geometri ve relocation auditini yeniden hesaplar; yalnız kaydedilmiş PASS değerine güvenmez.
5. Tam v2.4 insan kuralı, tam JSON/spec, self-contained simülasyon ve ham sonuçlar gerekiyorsa `SOURCE_PACKAGE.md` içindeki Library ZIP'ini kullan ve SHA-256 değerini doğrula.
6. Son commit/PR/issue durumunu incele.
7. Yeni bir değişiklik v2.4 adayına aitse aynı geliştirme hattında test et; v2.3'e geri yazma.

## v2.4 test-passed omurgası

- Gemi alt kenardaki seçilmiş sütun hizasında gerçek, geri dönülebilir **Kalkış Limanı** kurulum alanında başlar; üst sıradaki varış noktası **Hedef Liman**dır.
- İlk gün yalnız Kaptan seçimi yapılır; rota, Suçlama ve İsyan yoktur.
- İlk tarafsız gecede Kaptan, Sadakatini bilmeden tam **1 yasal Yakın Ufuk** kartına gizlice bakar; kart kapalı kalır.
- Sadakatler ertesi sabah dağıtılır.
- İlk gerçek rota normal eşzamanlı rota oylamasıdır; Kaptanın rota oyu 2 sayar.
- Kaptan makamı daha sonraki gecelerde otomatik Ufuk bilgisi vermez.
- Kamusal olarak açılan Harita kartı tekrar kapanmaz. Açık fakat ziyaret edilmemiş kartın olayı ilk gerçek girişe kadar çözülmez.
- Kamusal açılan Geçilmez Kayalık anında bilinen fiziksel engel olur ve rota/Ufuk hedefi değildir; gizli bakışlar kartı açmaz.
- Acil geri dönüş ziyaret yolunu Kalkış Limanına kadar geri izleyebilir; çözülmüş olay tekrar çalışmaz ve bilinen çıkmaza başka seçenek varken yeniden girilmez.
- Harita yer değiştirme bütün gerçek Kalkış Limanı→Hedef Liman yollarını yok edecekse değişiklik iptal edilir/geri alınır; Moderatör nedenini açıklamaz.
- Kaptan seçimi ilk beraberlikte bir kez tekrarlanır; ikinci beraberlikte eşit adaylar Kader Zarıyla kesin sonuca gider.
- Başlangıç Gövdesi 2; 20 Karakter / 30 Güç / 15 Sadakat / 52 Harita / 12 Kayalık / 118 ana kart kimliği korunur.
- `HAR-KY-01` ve `HAR-KY-03` gizli Geçilmez Kayalık olarak kalır.

## v2.4 doğrulama özeti

- Regresyon: **8/8 PASS**.
- Geometri: **51.204 teorik / 51.102 legal / 102 rejected**; Kalkış Limanı ile kalıcı ilk-kol kilidi **0**.
- Near-Horizon relocation exhaustive audit: **1.667.231** transition; unsafe **20** işlem rollback; guard sonrası kabul edilen kalıcı kilit **0**.
- Self-contained rota/sosyal-proxy: **9.000 oyun**, setup error **0**, hard route lock **0**, Hedef Limana ulaşma **%100**.
- Bu 9.000 oyun tam Tayfa/Hain kazanma dengesi değildir; rota ve state-machine regresyon proxy'sidir.

## Tam v2.4 kaynak paketi

Library: `/Oyun-GitHub/OYUN_SIMULASYON_PAKETI_v2.4-dev.zip`  
SHA-256: `b6a9262bf7212b77a3ca9fc6a718048de53d2bcb9060fdfc1bfe4518641f32f2`  
Boyut: `54521` byte.

## Stabil kilit için kalan kapılar

- v2.4 kural kitabı PDF'sini üret ve kaynakla çapraz doğrula.
- Etkilenen kart metinleriyle v2.4 kart PDF'sini üret.
- İki PDF için görsel/preflight taraması yap.
- Binary hash ve nihai release manifestini üret.
- Tüm kapılar PASS olmadan v2.4'e `STABLE / LOCKED` etiketi verme.

## Kısa devam komutu

> GitHub'daki Açık Deniz oyun reposunu aç; `AI_HANDOFF.md` ve `PROJECT_STATE.md` dosyalarını oku. Son kilitli sürümü ayrı tut, aktif v2.4 test-passed geliştirme adayını `releases/v2.4/` üzerinden devam ettir.
