# AI Handoff Protocol

Bu dosya farklı ChatGPT oturumları/model sürümleri arasında oyunun kanonik durumunu yeniden kurmak için zorunlu protokoldür.

## Sürüm durumu

- **Son kilitli stabil sürüm:** `v2.4 STABLE / LOCKED` — `releases/v2.4/`.
- **Önceki stabil geri dönüş:** `v2.3 STABLE / LOCKED` — `releases/v2.3/`.
- Otomatik “en yeni LOCKED/STABLE” çalışma protokolü artık **v2.4'ü** seçmelidir.
- `releases/v2.4/` yerinde değiştirilmez; sonraki tasarım değişiklikleri **v2.5+** hattında açılır.

## Her yeni çalışma oturumunda

1. `AI_HANDOFF.md` ve `PROJECT_STATE.md` dosyalarını oku.
2. En yeni kilitli release için `releases/v2.4/README_RELEASE_v2.4.md`, `V24_RELEASE_MANIFEST.json`, `SOURCE_PACKAGE.md`, `BINARY_ARTIFACTS.md` ve `V24_TEST_REPORT.md` dosyalarını kontrol et.
3. Rota sözleşmesini yeniden doğrulamak gerekirse `python releases/v2.4/validate_release_v2_4.py` çalıştır. Doğrulayıcı geometri ve relocation sonuçlarını yeniden hesaplar.
4. Tam insan kuralı, tam JSON/spec, self-contained simülasyon, ham sonuçlar ve final PDF'ler gerekiyorsa `SOURCE_PACKAGE.md` içindeki kilitli Library ZIP'ini kullan ve SHA-256 ile doğrula.
5. Son commit/PR/issue durumunu incele.
6. Yeni tasarım değişikliğini v2.4'e yerinde yazma; **v2.5+** çalışma hattı aç.

## v2.4 kilitli omurga

- Gemi alt kenarda seçilmiş sütun hizasındaki fiziksel **Kalkış Limanı** kurulum kartında (`SET-KL-01`) başlar; üst sıradaki varış noktası **Hedef Liman**dır.
- `SET-KL-01`, 52 Harita / 118 ana kart kimliğinin dışında tek kurulum bileşenidir.
- İlk gün yalnız Kaptan seçimi yapılır; rota, Suçlama ve İsyan yoktur.
- İlk tarafsız gecede Kaptan, Sadakatini bilmeden tam **1 yasal Yakın Ufuk** kartına gizlice bakar; kart kapalı kalır.
- Sadakatler ertesi sabah dağıtılır.
- İlk gerçek rota normal eşzamanlı rota oylamasıdır; Kaptanın rota oyu 2 sayar.
- Kaptan makamı daha sonraki gecelerde otomatik Ufuk bilgisi vermez.
- Kamusal açılan Harita kartı tekrar kapanmaz; açık fakat ziyaret edilmemiş kartın olayı ilk gerçek girişe kadar çözülmez.
- Kamusal açılan Geçilmez anında bilinen fiziksel engeldir ve rota/Ufuk hedefi değildir; gizli bakışlar kartı açmaz.
- Acil geri dönüş ziyaret yolunu **Kalkış Limanına kadar** geriye izleyebilir; her geri adım tam gün/hareket tüketir ve çözülmüş olay tekrar çalışmaz.
- Başka yasal seçenek varken bilinen çıkmaz kola yeniden girilmez.
- Harita yer değiştirmesi bütün gerçek Kalkış Limanı→Hedef Liman yollarını yok edecekse işlem iptal edilir/geri alınır; Moderatör nedenini açıklamaz.
- Kaptan seçiminde ilk beraberlikte bir yeniden oy; ikinci beraberlikte eşit adaylar arasında Kader Zarı uygulanır.
- Başlangıç Gövdesi 2; 20 Karakter / 30 Güç / 15 Sadakat / 52 Harita / 12 Kayalık / 118 ana kart kimliği korunur.
- `HAR-KY-01` ve `HAR-KY-03` gizli Geçilmez Kayalık olarak kalır.

## v2.4 doğrulama özeti

- Regresyon: **8/8 PASS**.
- Geometri: **51.204 teorik / 51.102 legal / 102 rejected**; kalıcı ilk-kol kilidi **0**.
- Near-Horizon relocation: **1.667.231** transition; unsafe **20** işlem rollback; guard sonrası kalıcı kilit **0**.
- Self-contained rota/sosyal-proxy: **9.000 oyun / 0 setup error / 0 hard-lock / %100 Hedef Limana ulaşma**.
- Kural PDF: **27 sayfa A4**, preflight/görsel tarama PASS.
- Kart PDF: **32 sayfa A4**, 63,5×88,9 mm, uzun kenardan çift taraflı; preflight/görsel tarama PASS.
- 118 ana kart kimliği eksiksiz; `SET-KL-01` ayrıca fiziksel kurulum bileşenidir.
- 12 Kayalık arka yüzü normalize iç kırpımlarda piksel düzeyinde özdeştir; gizli Geçilmez sızıntısı **0**.

## Kilitli artefaktlar

- Full ZIP: `/Oyun-GitHub/OYUN_SIMULASYON_PAKETI_v2.4.zip`  
  SHA-256: `9edbef118561632c9c37a3c854d6c67f55c30ca99771d87e64d77b6c38454561`
- Kural PDF: `/Oyun-GitHub/v2.4/OYUN_Kural_Kitabi_v2.4.pdf`  
  SHA-256: `beae69144b6af5e7ed7a16d6c5f30c262f63af9b92826abc78c61c0493011216`
- Kart PDF: `/Oyun-GitHub/v2.4/OYUN_Kartlar_A4_Prototip_v2.4.pdf`  
  SHA-256: `5fb4a0c42bb9eaedfb7434ae9eb3a540eade6f5f9df7c34a6720f376cd32e9d1`

## Kısa devam komutu

> GitHub'daki Açık Deniz oyun reposunu aç; `AI_HANDOFF.md`, `PROJECT_STATE.md` ve `releases/v2.4/README_RELEASE_v2.4.md` dosyalarını okuyup en son kilitli v2.4 sürümünden devam et. Yeni tasarım değişikliklerini v2.5+ hattında yap.
