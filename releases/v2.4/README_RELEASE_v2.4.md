# OYUN v2.4 — STABLE / LOCKED

**Taban:** v2.3 STABLE / LOCKED  
**Durum:** **STABLE / LOCKED**  
**Tarih:** 18 Ağustos 2026

v2.4, v2.3 kapsamlı kırma testinde bulunan rota kilitleri, kamusal Harita görünürlüğü belirsizliği, Kaptan açılış akışı, seçim beraberliği ve eksik simülasyon bağımlılığı sorunlarını düzeltir. v2.3 yerinde değiştirilmemiştir ve önceki geri dönüş sürümü olarak korunur. Sonraki tasarım değişiklikleri v2.5+ olarak açılmalıdır.

## v2.4 ana değişiklikleri

- Gemi, Haritanın alt kenarında seçilen sütun hizasındaki fiziksel **Kalkış Limanı** kurulum kartında başlar. Bu kart 52 Harita ve 118 ana kart kimliğinin dışındadır.
- Acil geri dönüş ilk Harita satırından Kalkış Limanına kadar uzanabilir.
- İlk gün yalnız Kaptan seçilir.
- İlk tarafsız gecede Kaptan Sadakatini bilmeden yalnız **1 yasal Yakın Ufuk** kartına gizlice bakar; kart kapalı kalır.
- Sadakatler ertesi sabah dağıtılır.
- İlk gerçek rota normal eşzamanlı rota oylamasıdır; Kaptanın rota oyu 2 sayar.
- Kamusal açılan Harita kartı tekrar kapanmaz; açık ama ziyaret edilmemiş kartın olayı ilk gerçek girişe kadar çözülmez.
- Kamusal açılan Geçilmez anında bilinen fiziksel engel olur.
- Harita yer değiştirmesi bütün gerçek Kalkış Limanı→Hedef Liman yollarını yok edecekse işlem iptal edilir/geri alınır.
- Kaptan seçimi ikinci beraberlikte Kader Zarıyla kesin sonuca gider.
- Rota/sosyal-proxy motoru self-contained'dir; proje-içi Python bağımlılığı yoktur.

## Doğrulama

- Regresyon: **8/8 PASS**.
- Geometri: **51.204 teorik / 51.102 legal / 102 rejected**.
- Kalıcı ilk-kol kilidi: **0**.
- Exhaustive Near-Horizon relocation: **1.667.231** transition; unsafe **20** işlem rollback; guard sonrası kalıcı kilit **0**.
- Self-contained rota/sosyal-proxy: **9.000 oyun / 0 setup error / 0 hard-lock / %100 Hedef Limana ulaşma**.
- Kural PDF: **27 sayfa A4**, preflight/görsel tarama PASS.
- Kart PDF: **32 sayfa A4**, 63,5×88,9 mm, uzun kenardan çift taraflı; preflight/görsel tarama PASS.
- 118 ana kart kimliği kart PDF'sinde eksiksiz; ayrıca `SET-KL-01` Kalkış Limanı kurulum kartı eklenmiştir.
- 12 Kayalık arka yüzü piksel düzeyinde özdeştir; gizli Geçilmez kimliği arka yüzden sızmaz.

## Kilit kuralı

`releases/v2.4/` bundan sonra yerinde değiştirilmez. Yeni tasarım değişiklikleri **v2.5+** hattında yapılır.
