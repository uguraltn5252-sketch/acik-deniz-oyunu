# OYUN v2.4 — Kural Düzeltme Sözleşmesi

**Taban:** v2.3 STABLE / LOCKED  
**Durum:** TEST-PASSED DEVELOPMENT CANDIDATE / NOT LOCKED

Bu dosya yalnız v2.3 üzerine gelen v2.4 değişikliklerini tanımlar. Değişmeyen bütün kurallar v2.3'ten devralınır.

## 1. Kalkış Limanı

- Gemi soyut Harita-dışı konumda başlamaz. Moderatör alt kenarda istediği sütun hizasında bir **Kalkış Limanı** kurulum kartı/alanı belirler.
- Kalkış Limanı 52 Harita kartının ve 118 ana kart kimliğinin dışında bir kurulum bileşenidir.
- Hedef Liman üst sıradaki seçilmiş Liman olarak kalır.
- Gemi çıkmazda ziyaret yolunu geriye doğru izleyerek Kalkış Limanına kadar dönebilir. Her geri adım bir normal gün/hareket tüketir; çözülmüş olay tekrar çalışmaz.
- Bilinen çıkmaz kola başka yasal seçenek varken yeniden girilemez.

## 2. Açılış ve Kaptan

- İlk gün yalnız Kaptan seçimi yapılır; rota, Suçlama ve İsyan yoktur.
- İlk tarafsız gecede Kaptan makamı nedeniyle **yalnız bir kez** uyanır.
- Kaptan, Kalkış Limanından o anda yasal olan **Yakın Ufuk kartlarından tam 1 tanesine** gizlice bakar.
- Bu gizli bakışta kart açık kalmaz; yalnız Kaptan görür.
- Kaptan bu sırada Sadakatini bilmez.
- Sadakatler ertesi sabah dağıtılır.
- İlk gerçek rota Kaptanın tek başına kararı değildir; normal eşzamanlı rota oylaması yapılır. Kaptanın rota oyu 2 sayar.
- Kaptan makamı daha sonraki gecelerde otomatik uyanış veya Ufuk bilgisi vermez.

## 3. Kamusal Harita bilgisi

- **Kamusal olarak açılan/gösterilen Harita kartı tekrar kapanmaz.**
- Kamusal açık ama ziyaret edilmemiş kartın olayı henüz çözülmüş sayılmaz; Gemi ilk kez gerçekten girince olay çözülür.
- Kamusal açılan Geçilmez Kayalık anında bilinen fiziksel engeldir ve rota/Ufuk hedefi değildir.
- Pusula ve herkese gösteren Deniz Feneri/Karakol etkileri bu kamusal-açık kuralını izler.
- Gizli bakışlar (Kaptanın açılış bakışı, Kırık Dürbün, Hain/Karakter gizli bilgisi vb.) kartın kamusal durumunu değiştirmez; kart kapalı kalır.

## 4. Rota güvenliği

- Kurulumda Kalkış Limanından en az bir gerçek ilk rota bulunmalı ve en az bir erişilebilir Ada üzerinden Hedef Limana gerçek yol kalmalıdır.
- Başlangıç Yakın Ufku toplam kilit olamaz.
- Geçilmez nedeniyle seçilen bir kol sonradan çıkmazsa acil geri dönüş Kalkış Limanına kadar çalışabilir; bu bir hata değil, zaman/rota maliyetidir.
- `Islak Deniz Haritası`, `Hayalet Işıkları` veya başka bir yer değiştirme, **Kalkış Limanı→Hedef Liman bütün gerçek yollarını yok edecekse** uygulanmaz veya anında geri alınır. Moderatör bunun nedenini açıklamaz.

## 5. Kaptan seçimi beraberliği

- İlk eşitlikte yalnız eşit adaylar arasında bir kez yeniden oylanır.
- İkinci kez yine eşitlik varsa yalnız eşit adaylar Kader Zarı atar; en yüksek sonuç Kaptan olur. En yüksek sonuçta eşitlik varsa yalnız eşitler yeniden atar.
- Böylece Kaptan seçimi sonsuz döngüye giremez.

## 6. Değişmeyen kilitler

- Başlangıç Gövdesi: **2**.
- Kaptan rolü kalıcıdır.
- 20 Karakter / 30 Güç / 15 Sadakat / 52 Harita / 12 Kayalık / 118 ana kart kimliği korunur.
- `HAR-KY-01` ve `HAR-KY-03` gizli Geçilmez Kayalık olarak kalır.
- Küçük Haritalarda 1, büyük Haritalarda 2 Geçilmez kotası korunur.

## 7. Release durumu

v2.4 bu sözleşmeyle test-passed geliştirme adayıdır. Kural PDF'si, kart PDF'si ve görsel preflight tamamlanmadan **STABLE / LOCKED** yapılamaz.
