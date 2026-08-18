# OYUN v2.5 — Kural Düzeltme Sözleşmesi

**Taban:** v2.4 STABLE / LOCKED  
**Durum:** v2.5 STABLE / LOCKED

Değişmeyen bütün v2.4 kuralları korunur. v2.5 yalnız aşağıdaki kesin farkları ekler.

## 1. İskorbüt-aware relocation

- İskorbüt aktif ve henüz temizlenmemişse herhangi bir Harita kartı yer değiştirmesi sonrasında Kalkış Limanından başlayarak en az bir **Ada üzerinden Hedef Limana kazanılabilir yol** kalmalıdır.
- İskorbüt temizlenmiş veya hiç etkinleşmemişse en az bir gerçek Kalkış Limanı→Hedef Liman yolu kalmalıdır.
- Şart bozulacaksa işlem uygulanmaz veya anında geri alınır. Moderatör nedenini açıklamaz.

## 2. Ada çevresi oyun-boyu invariantı

- Girdap ve Ters Akıntı hiçbir Ada kartının yatay, dikey veya çapraz komşuluğunda bulunamaz.
- Bu yalnız kurulum kuralı değildir; oyun boyunca geçerlidir.
- Islak Deniz Haritası, Hayalet Işıkları veya başka bir fiziksel Harita yer değiştirmesi bu invariantı bozacaksa işlem rollback edilir.

## 3. Kaderi Yeniden Yaz × Geçilmez

- Geçilmez Kayalık açıldıktan sonra Kaderi Yeniden Yaz kullanılabilir.
- Gemi Geçilmez kareye girmiş veya o kareyi ziyaret etmiş sayılmaz.
- Geçilmez açık ve kamusal blocker olarak kalır.
- Aynı hareket penceresinde başka yasal Yakın Ufka yönlenilir.
- İlk kart gerçek bir Ada ise Ada'ya giriş İskorbütü olay çözülmeden önce temizler; ardından Kaderi başka yasal Yakın Ufka yönlendirebilir.

## 4. Çürümüş Erzak fiziksel kart sözleşmesi

- Başlangıç paketi `N-1 gerçek Güç + 1 Çürümüş Erzak` kartıdır.
- Çürümüş Erzak sahibi İskorbüt sonucu belirlendikten sonra yolculuk Güç destesinden **1 gerçek Güç çeker**.
- Böylece ilk yolculuk gününe her oyuncu 1 gerçek Güçle başlar.

## 5. Release bütünlüğü

- Hain tablosu, oyuncu×süre Gövde-hasarı kotaları, PDF/binary release gate'leri machine spec'te açıkça bulunur.
- Stable pakette stale `DEV_MANIFEST`, boş regresyon çıktısı veya simülatör hatasıyla üretilmiş erken denge verisi kanonik kanıt olarak tutulmaz.
- v2.5 full ZIP içindeki her dosya `SHA256SUMS.txt` ile doğrulanır.

## 6. Değişmeyen kilitler

- Gövde 2.
- Kaptan kalıcı; ilk tarafsız gece tek gizli Yakın Ufuk bakışı.
- İlk gerçek rota normal eşzamanlı oy; Kaptan oyu 2.
- Kamusal açılan Harita kapanmaz; ziyaret edilmeden olay çözülmez.
- Kalkış Limanına acil geri dönüş korunur.
- 20 Karakter / 30 Güç / 1 Çürümüş Erzak / 15 Sadakat / 52 Harita / 12 Kayalık / 118 ana kimlik.
- `HAR-KY-01` ve `HAR-KY-03` gizli Geçilmez olarak kalır.
