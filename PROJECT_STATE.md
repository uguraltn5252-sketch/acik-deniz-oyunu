# Project State

**Son güncelleme:** 2026-08-18  
**Son stabil prototip:** **v2.3 STABLE / LOCKED**  
**Aktif geliştirme adayı:** **v2.4 TEST-PASSED / NOT LOCKED**  
**Stabil kanonik kaynak:** `releases/v2.3/`  
**Aktif geliştirme kaynağı:** `releases/v2.4/`  
**Geliştirme branch'i:** `agent/v2.4-acilis-ve-kilit-duzeltmeleri`

v2.3 yerinde değiştirilmez. v2.4, kapsamlı v2.3 kırma testinde bulunan sorunları ve son tasarım kararlarını uygular; PDF/kart/preflight kapıları tamamlanmadan yeni stabil sürüm değildir.

## v2.4 kesin geliştirme sözleşmesi

### Açılış

- Gemi soyut Harita-dışı noktada değil, Moderatörün alt kenarda seçtiği sütun hizasındaki **Kalkış Limanı** kurulum kartı/alanında başlar.
- Kalkış Limanı 52 Harita kartı ve 118 ana kart kimliği dışında bir kurulum bileşenidir.
- Üst sıradaki seçilmiş varış Limanı **Hedef Liman** olarak kalır.
- İlk gün yalnız Kaptan seçimi yapılır; rota, Suçlama ve İsyan yoktur.
- İlk tarafsız gecede Kaptan yalnız bir kez uyanır ve Sadakatini bilmeden **tam 1 yasal Yakın Ufuk** kartına gizlice bakar. Kart kapalı kalır.
- Sadakatler ertesi sabah dağıtılır.
- İlk gerçek rota normal eşzamanlı rota oylamasıdır; Kaptanın rota oyu 2 sayar.
- Kaptan makamı sonraki gecelerde otomatik uyanış veya Ufuk bilgisi vermez.

### Harita bilgi durumu

- Kamusal olarak açılan/gösterilen Harita kartı tekrar kapanmaz.
- Kamusal açık ama ziyaret edilmemiş kartın olayı henüz çözülmüş değildir; ilk gerçek girişte çözülür.
- Kamusal açılan Geçilmez Kayalık anında bilinen engel olur ve rota/Ufuk hedefi değildir.
- Gizli bakışlar kartın kamusal durumunu değiştirmez; kart kapalı kalır.

### Rota güvenliği

- Başlangıç Yakın Ufku toplam kilit olamaz; Kalkış Limanından en az bir gerçek ilk rota ve en az bir erişilebilir Ada üzerinden Hedef Limana gerçek yol bulunmalıdır.
- Geçilmez nedeniyle seçilmiş kol çıkmaza dönüşürse acil geri dönüş ziyaret yolunu geriye doğru **Kalkış Limanına kadar** izleyebilir. Her geri adım normal hareket/gün tüketir; çözülmüş olay tekrar çalışmaz.
- Başka yasal seçenek varken bilinen çıkmaz kola yeniden girilmez.
- `Islak Deniz Haritası`, `Hayalet Işıkları` veya başka bir Harita yer değiştirme bütün gerçek Kalkış Limanı→Hedef Liman yollarını yok edecekse işlem uygulanmaz veya anında geri alınır. Moderatör bunun nedenini açıklamaz.

### Kaptan beraberliği

- İlk seçim beraberliğinde yalnız eşit adaylar arasında bir kez yeniden oylanır.
- İkinci kez beraberlikte yalnız eşit adaylar Kader Zarı atar; en yüksek sonuç kazanır, en yüksek eşitse yalnız eşitler yeniden atar.

### Değişmeyen omurga

- Kaptan rolü kalıcıdır.
- Başlangıç Gövdesi **2**.
- 20 Karakter / 30 Güç / 15 Sadakat / 52 Harita / 12 Kayalık / 118 ana kart kimliği korunur.
- `HAR-KY-01` ve `HAR-KY-03` gizli Geçilmez Kayalık olarak kalır ve kapalıyken normal Kayalıktan ayırt edilemez.
- Küçük Haritalarda 1, büyük Haritalarda 2 Geçilmez kotası korunur.

## v2.4 test sonucu

- Regresyon testleri: **8/8 PASS**.
- Geometri: **51.204 teorik / 51.102 legal / 102 rejected**.
- Görünür ilk rota dalları: **135.430**.
- Sonradan çıkmaz olabilen fakat Kalkış Limanıyla geri kazanılabilen ilk dallar: **8.791**.
- Kalıcı ilk-dal kilidi: **0**.
- Exhaustive Near-Horizon relocation: **1.667.231** transition.
- Global yolu yok edeceği için rollback edilen relocation: **20**.
- Guard sonrası kabul edilen kalıcı relocation kilidi: **0**.
- Self-contained rota/sosyal-proxy: **9.000 oyun**, setup error **0**, hard route lock **0**, Hedef Limana ulaşma **%100**, ortalama yolculuk **6,21 gün**.
- Bu 9.000 oyun tam Tayfa/Hain denge ölçümü değildir.

## Release engineering

- v2.4 route/social-proxy simülatörü proje-içi başka Python modülüne bağımlı değildir; yalnız Python standart kütüphanesi ve v2.4 full JSON spec gerekir.
- Repo-side `releases/v2.4/validate_release_v2_4.py` geometri ve relocation auditini **yeniden hesaplar**; kayıtlı PASS sayısını tek başına kanıt saymaz.
- Tam kaynak paketi Library'de `/Oyun-GitHub/OYUN_SIMULASYON_PAKETI_v2.4-dev.zip` yolundadır.
- ZIP SHA-256: `b6a9262bf7212b77a3ca9fc6a718048de53d2bcb9060fdfc1bfe4518641f32f2`; boyut `54521` byte.

## v2.4'ü STABLE / LOCKED yapmadan önce kalanlar

1. v2.4 kural kitabı PDF'sini üretmek.
2. Etkilenen kart metinleriyle v2.4 kart PDF'sini üretmek.
3. Kural/spec/kart/PDF çapraz doğrulaması yapmak.
4. İki PDF'nin görsel ve baskı preflight'ını yapmak.
5. Nihai binary hashleri ve release manifestini üretmek.
6. Bu kapılar PASS olduktan sonra v2.4'ü ayrı bir stabil commit/release olarak kilitlemek.

O zamana kadar otomatik "en yeni kilitli sürüm" seçimi **v2.3** üzerinde kalmalıdır.
