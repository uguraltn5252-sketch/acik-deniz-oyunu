# Project State

**Son güncelleme:** 2026-08-18  
**Son stabil prototip:** **v2.4 STABLE / LOCKED**  
**Kanonik kaynak:** `releases/v2.4/`  
**Önceki stabil geri dönüş:** `releases/v2.3/`  
**Durum:** **v2.4 STABLE / LOCKED.** Sonraki tasarım değişiklikleri v2.5+ olarak açılmalıdır.

## v2.4 kesin omurga

- Gemi, Moderatörün alt kenarda seçtiği sütun hizasındaki fiziksel **Kalkış Limanı** (`SET-KL-01`) kurulum kartında başlar.
- Kalkış Limanı 52 Harita ve 118 ana kart kimliği dışındaki tek kurulum bileşenidir; üst sıradaki varış noktası Hedef Limandır.
- İlk gün yalnız Kaptan seçilir; rota, Suçlama ve İsyan yoktur.
- İlk tarafsız gecede Kaptan Sadakatini bilmeden yalnız bir kez uyanır ve tam **1 yasal Yakın Ufuk** kartına gizlice bakar; kart kapalı kalır.
- Sadakatler ertesi sabah dağıtılır.
- İlk gerçek rota normal eşzamanlı rota oylamasıdır; Kaptanın rota oyu 2 sayar.
- Kaptan makamı daha sonraki gecelerde otomatik Ufuk bilgisi vermez.
- Kamusal açılan/gösterilen Harita kartı tekrar kapanmaz. Açık ama ziyaret edilmemiş kartın olayı ilk gerçek girişe kadar çözülmez.
- Kamusal açılan Geçilmez anında bilinen engel olur ve rota/Ufuk hedefi değildir; gizli bakışlar kamusal durumu değiştirmez.
- Acil geri dönüş ziyaret yolunu Kalkış Limanına kadar izleyebilir; her geri adım normal gün/hareket tüketir, çözülmüş olay yeniden çalışmaz.
- Başka yasal seçenek varken bilinen çıkmaz kola yeniden girilemez.
- Harita yer değiştirmesi bütün gerçek Kalkış Limanı→Hedef Liman yollarını yok edecekse işlem iptal edilir/geri alınır; neden açıklanmaz.
- Kaptan seçiminde ilk beraberlikte bir yeniden oy; ikinci beraberlikte eşit adaylar Kader Zarıyla çözülür.
- Kaptan rolü kalıcıdır. Başlangıç Gövdesi **2**.
- 20 Karakter / 30 Güç / 15 Sadakat / 52 Harita / 12 Kayalık / 118 ana kart kimliği korunur.
- `HAR-KY-01` ve `HAR-KY-03` gizli Geçilmez Kayalık olarak kalır; küçük Haritalarda 1, büyük Haritalarda 2 Geçilmez kullanılır.

## v2.4 doğrulama ve fiziksel release

- Regresyon: **8/8 PASS**.
- Geometri: **51.204 / 51.102 legal / 102 rejected**; kalıcı ilk-dal kilidi **0**.
- Exhaustive relocation: **1.667.231** transition; **20** unsafe rollback; guard sonrası kalıcı kilit **0**.
- Self-contained rota/sosyal-proxy: **9.000 oyun**, setup error **0**, hard-lock **0**, Hedef Limana ulaşma **%100**.
- Kural PDF: **27 sayfa A4**, preflight + render taraması PASS.
- Kart PDF: **32 sayfa A4**, 63,5×88,9 mm uzun-kenar duplex, preflight + render taraması PASS.
- 118 ana kart kimliği kart PDF'sinde eksiksiz; `SET-KL-01` ayrıca fiziksel kurulum kartıdır.
- 12 Kayalık arka yüzü piksel düzeyinde özdeştir; gizli Geçilmez bilgi sızıntısı yoktur.

## Kilitli paket

- Library: `/Oyun-GitHub/OYUN_SIMULASYON_PAKETI_v2.4.zip`
- SHA-256: `9edbef118561632c9c37a3c854d6c67f55c30ca99771d87e64d77b6c38454561`
- Kural PDF SHA-256: `beae69144b6af5e7ed7a16d6c5f30c262f63af9b92826abc78c61c0493011216`
- Kart PDF SHA-256: `5fb4a0c42bb9eaedfb7434ae9eb3a540eade6f5f9df7c34a6720f376cd32e9d1`

`releases/v2.4/` bundan sonra yerinde düzenlenmez. Otomatik “en yeni kilitli sürüm” seçimi **v2.4** olmalıdır.
