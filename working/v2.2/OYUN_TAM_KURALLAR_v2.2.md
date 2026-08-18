# OYUN - Tam Kural Seti v2.2

**Tarih:** 18 Ağustos 2026  
**Durum:** v2.2 geliştirme sürümü. v2.1 stabil temelinden türetilmiştir. Geçilmez Kayalık + acil geri dönüş teknik testi PASS; tam v2.2 regresyonu ve baskı çıktıları tamamlanmadan stabil sayılmaz.  
**Amaç:** v2.2 için ayrıntılı insan kural kaynağı; JSON/spec ve doğrulayıcıyla eşleşmesi gereken kanonik geliştirme metni.

> Bu dosya v2.2 geliştirme hattının ayrıntılı insan kural kaynağıdır. `releases/v2.1/` değiştirilemez geri dönüş temelidir. Eski v1.0/v2.0 simülasyon sonuçları v2.2 sonucu sayılmaz; Geçilmez Kayalık için yapılan hedefli teknik test yalnız ilgili mekanik için kanıttır.

## 1. Bu sürümde kilitlenen ana kararlar

1. Kurulum sırası **Karakter -> Kaptan seçimi -> Güç/Erzak -> İskorbüt -> tanışma gecesi -> Sadakat -> ilk oyun günü** şeklindedir.
2. Kaptan seçilirken hiç kimse Güç veya Sadakat kartını bilmez.
3. **Kaptan rolü oyunun kalıcı omurgasıdır ve kaldırılmaz.** İlk rotayı Kaptan tek başına ve olay bilgisi olmadan seçer. Başarılı İsyan, Kaptanın ölümü veya görev yapamayacağı mevcut durumlarda yeni Kaptan seçilir.
4. Kaptan gece ayrıca uyanmaz; makamı otomatik Yakın/Uzak Ufuk bilgisi vermez.
5. Güç kartları gizlidir; başlangıçta yalnız **Çürümüş Erzak — İskorbüt Tehlikesi** zorunlu açılır.
6. Sadakat kartları ayrı destedir ve kalkış öncesi tanışma gecesinin sabahında dağıtılır.
7. Her Haritada en az iki Ada vardır. İskorbüt etkinse gemi Limandan önce en az bir Adaya girmek zorundadır.
8. **Gemi bütün Harita boylarında 2 Gövdeyle başlar.**
9. Gemi Haritanın alt kenarının hemen dışında **herhangi bir sütun hizasında** başlayabilir. Sabit merkez/sağ-orta başlangıç kaldırılmıştır.
10. İlk Yakın Ufuk, seçilen başlangıç sütununa göre dinamik hesaplanır; kenar veya Liman erişimi nedeniyle 1, 2 veya 3 yasal ilk rota bulunabilir. Bu yasal ilk rotaların hiçbirinde Sis olamaz.
11. Her oyunda Geçilmez Kayalık bulunur: `5×5`, `5×6`, `6×5` için **1**; `5×7`, `6×6`, `6×7` için **2**.
12. Geçilmez Kayalık prototipte Harita kartının üstüne konan ayrı bir **işarettir**; 52 Harita kartı ve 118 kart kimliği değişmez. İşaretli kareye Gemi giremez.
13. Geçilmez Kayalık Limanın hemen kıçındaki son Harita/Ufuk hattına konulamaz. Kurulum baştan çözümsüz olamaz; başlangıçtan erişilebilir en az bir Ada üzerinden seçilmiş Limana en az bir ileri yol kalmalıdır.
14. Gemi normalde yalnız ileri gider. Ancak bütün normal çözüm adımlarından sonra hiç yasal ileri rota kalmamışsa ve Geçilmez Kayalıklar yok sayıldığında en az bir ileri rota doğuyorsa **acil geri dönüş** açılır: Gemi geldiği bir önceki kareye bir adım geri gider, o günün hareketini tüketir ve dönülen kartın olayı tekrar çalışmaz.
15. Çıkmaz sürerse sonraki normal günde bir kare daha geri dönülebilir. Bilinen çıkmaz kola başka yasal seçenek varken yeniden girilemez.
16. Girdap veya başka bir zorunlu ek hareket Geçilmez Kayalık yüzünden yasal hedef bulamazsa yalnız o ek hareket boşa düşer; aynı gün acil geri dönüş tetiklenmez. Sonraki normal rota gününde hâlâ çıkmaz varsa geri dönüş uygulanabilir.
17. Liman sabit orta kare değildir; Moderatör üst sıradan bir Liman karesi seçer ve bütün rota yasallığı bu kareye göre hesaplanır.
18. Yakın Ufuk bir sıra ilerideki yasal İskele/Pruva/Sancak karşılıkları; Uzak Ufuk ise iki sıra ilerideki karşılıklarıdır ve Geçilmez Kayalık hedefleri Ufuk sayılmaz.
19. Kayıkçı Karakteri kalır. İşaret Fişeği ve Son Sandal çıkar; iki amaçlı **Pusula** kuralı korunur.
20. Girdap ve Ters Akıntı kalır; hiçbir Ada kartının çevresindeki sekiz bitişik kareye yerleştirilemez.

## 2. Oyunun kimliği

- **Oyuncu sayısı:** 6–15 oyuncu + 1 tarafsız Moderatör.
- **Hedef süre:** yaklaşık 25–45 dakika; insan testiyle yeniden ölçülecek.
- **Tür:** sosyal çıkarım + rota seçimi + yarı işbirliği.
- Karakter ile Sadakat ayrıdır. Her Karakter Tayfa veya Hain olabilir.
- Harita kategorisi açıktır; olay yüzü kapalıdır.
- Liman baştan görünür ve Moderatörün üst sırada seçtiği tek karedir. Gemi **normalde** yalnız ileri gider ve bekleyemez; yalnız Geçilmez Kayalık kaynaklı tam çıkmazda yazılı acil geri dönüş istisnası uygulanabilir.
- Rota oyları eşzamanlı açılır ve kamusal iz bırakır.
- Hainler gemiye doğrudan Gövde hasarı veremez. Bildikleri tehlikeli rotayı seçtirmeye çalışırlar.
- Kart göstermek masumiyet kanıtı değildir. Kart yalnız yazılı kullanım penceresinde açılabilir.

Oyunun hedef duygusu:

> Bilgiye ihtiyacın var. Bilginin sahibine güvenemiyorsun. Yine de birine güvenmeden rota seçemiyorsun.

## 3. Kazanma koşulları

### Tayfa kazanır

Gemi Liman Gecesini sağ çıkarır, etkin İskorbüt temizlenmiş olur ve şafakta en az bir Tayfa hayattaysa **Tayfa kazanır**.

### Hainler kazanır

Hainler aşağıdaki durumlardan biri gerçekleştiğinde kazanır:

1. Gemi `0 Gövdeye` düşüp batar.
2. Limana girilmeden önce bütün Tayfa oyuncuları ölür.
3. İskorbüt etkin olduğu hâlde gemi hiçbir Adaya uğramadan Liman Gecesine ulaşır.

İskorbüt zaferinde gemideki herkes ölmüş sayılır; Hainler de ölse yük Limana ulaşmadığı için Hain takımı kazanır.

Adada mahsur bir Tayfa hayattadır ve “bütün Tayfa öldü” koşulunu engeller.

Şunlar yoktur: Limanda taraf sayımı, son Liman oylaması, Hain–Tayfa eşitliğiyle zafer veya oyunu kilitleyerek kazanma.

## 4. Bileşenler

- 20 Karakter kartı
- 30 gerçek Güç kartı
- 1 özel başlangıç kartı: **Çürümüş Erzak — İskorbüt Tehlikesi**
- Tayfa ve Hain Sadakat kartları
- 52 Harita kartı
- 1 Gemi piyonu
- 1 Liman işareti
- 1 Kaptan işareti
- 2 Gövde işareti veya `2–1–0` Gövde göstergesi
- 2 Kamara işareti
- 15 Bir Kez Mahkûm işareti
- 1 Mahsur işareti
- 1 Kayıkçı Seferde işareti
- İskorbüt işareti olarak kullanılabilen Çürümüş Erzak kartı
- 1 adet on iki yüzlü **Kader Zarı (d12)**; prototipte aynı tür dijital zar da kullanılabilir
- **2 Geçilmez Kayalık işareti**; Harita boyuna göre 1 veya 2 kullanılır. Bunlar Harita kartı değildir ve 52 kartlık havuza eklenmez.
- Güvercin Mektubu için küçük kâğıtlar ve kalem

Çürümüş Erzak kartı gerçek bir Güç değildir; Güç destesinin 30 kartına dâhil değildir.

## 5. Kurulum

### 5.1 Moderatörün gizli hazırlığı

1. Oyuncu sayısına göre Hain sayısını, Karakter yoğunluğunu, Harita boyunu ve hasar kotasını belirle.
2. Limanı Haritanın en üst satırındaki istediğin tek kareye açık yerleştir.
3. Gemi için Haritanın alt kenarının dışında bir başlangıç sütunu belirle. Kural açısından bütün sütunlar yasaldır; Moderatör seçebilir veya tarafsız bir rastgele yöntem kullanabilir.
4. Haritada en az iki Ada bulunduğunu doğrula.
5. Girdap ve Ters Akıntı olaylarını hiçbir Ada kartının yatay, dikey veya çapraz bitişiğine koyma.
6. Harita boyuna göre Geçilmez Kayalık işaretlerini yerleştir: `5×5`, `5×6`, `6×5` = 1; `5×7`, `6×6`, `6×7` = 2.
7. Geçilmez Kayalığı en üstteki son Harita/Ufuk hattına koyma. İşaretli kare Gemi için tamamen geçilemezdir.
8. Seçilen başlangıçtan, Geçilmez Kayalıklar hesaba katıldığında, en az bir erişilebilir Adaya ve oradan seçilmiş Limana normal ileri hareketlerle ulaşan en az bir yasal yol kaldığını doğrula. İlk hareket tamamen kapalı olamaz.
9. Seçilen başlangıçtan doğan bütün **yasal ve Geçilmez Kayalık olmayan ilk Yakın Ufuk** kartlarında Sis bulunmadığını doğrula.
10. Harita olay yüzlerini oyunculara göstermeden kategorileri açık biçimde yerleştir; Geçilmez Kayalık işaretleri oyuncular tarafından baştan görülür.

### 5.2 Kart dağıtımının kesin sırası

#### A. Karakterler

Her oyuncuya bir kapalı Karakter kartı dağıtılır.

- Herkes yalnız kendi Karakterine bakar.
- Karakter kartı, yazılı açık yetenek kullanımı dışında başka oyuncuya gösterilemez.
- Oyuncu Karakteri hakkında doğru veya yanlış konuşabilir.
- Karakter, Sadakati göstermez.

#### B. Kör Kaptan seçimi

Oyuncular açık oylamayla Kaptanı seçer.

- Bu sırada hiç kimse Güç veya Sadakat kartını bilmez.
- Oyuncular yalnız gördükleri kendi Karakterlerinden ve masa konuşmasından hareket eder.
- Beraberlik olursa yalnız berabere adaylar arasında yeniden oylanır.

#### C. Başlangıç Güçleri ve Çürümüş Erzak

1. Başlangıca uygun 28 gerçek Güç kartını karıştır. Kaderi Yeniden Yaz ve Seyir Zabtı başlangıç havuzuna girmez.
2. `N` oyuncu için `N−1` gerçek Güç ile 1 Çürümüş Erzak kartını aynı arkalı başlangıç paketi olarak karıştır.
3. Her oyuncuya bir kart dağıt.
4. Herkes aynı anda kartına gizlice bakar.
5. Gerçek Güç alanlar kartlarını açıklamaz ve göstermez.
6. Çürümüş Erzak alan oyuncu kartı **hemen ve zorunlu olarak** açar.
7. Çürümüş Erzak sahibi, kalan başlangıç havuzundan bir gerçek Güç çeker ve yalnız kendisi bakar.
8. Dağıtılmayan başlangıç Güçleriyle başlangıca kapalı iki olağanüstü kartı karıştır; yolculuk Güç destesini oluştur.

Sonuçta herkes tam bir gerçek Güçle başlar. Kimse hangi gerçek Gücün kimde olduğunu açıklamak zorunda değildir.

#### D. İskorbüt sonucunun belirlenmesi

- Çürümüş Erzak sahibi o anda Kaptansa kart atılır ve İskorbüt etkinleşmez.
- Çürümüş Erzak sahibi Kaptan değilse kart Haritanın yanına açık konur; İskorbüt etkindir.
- Daha sonra Kaptanın değişmesi bu sonucu değiştirmez.

#### E. Kalkış öncesi ilk tanışma gecesi

1. Gemi henüz karadan ayrılmamıştır ve başlangıç konumundadır.
2. Bütün oyuncular Sadakat taraflarından bağımsız biçimde **mürettebat** olarak tanışır. Buradaki mürettebat sözcüğü Tayfa Sadakatini değil, oyundaki bütün oyuncuları ifade eder.
3. Moderatör oyun dünyasını, gemiyi ve yolculuğun başlangıç durumunu tanıtır.
4. Bu gece Karakter, Güç, Harita veya Hain eylemi yapılmaz.
5. Sadakatler henüz dağıtılmadığı için Tayfa ve Hain tarafları oluşmamıştır.
6. Kaptan ayrıca uyanmaz; makamı ona Ufuk kartına bakma hakkı vermez.

#### F. İlk sabah Sadakatlerin dağıtılması

Tanışma gecesinin sabahında Sadakat kartları dağıtılır. `N` oyuncu için aşağıdaki tablodan tam Hain sayısı alınır; kalan `N − Hain` kart Tayfa olur. Böylece toplam tam `N` Sadakat kartı hazırlanır, karıştırılır ve herkese birer kart dağıtılır. Kullanılmayan Sadakatler görülmeden oyun dışında kalır. Sadakatler görüldükten sonra ilk oyun günü başlar.

| Oyuncu | Hain | Tayfa |
|---:|---:|---:|
| 6 | 1 | 5 |
| 7 | 2 | 5 |
| 8 | 3 | 5 |
| 9 | 3 | 6 |
| 10 | 3 | 7 |
| 11 | 4 | 7 |
| 12 | 4 | 8 |
| 13 | 4 | 9 |
| 14 | 5 | 9 |
| 15 | 5 | 10 |

- Herkes yalnız kendi Sadakatine bakar.
- Sadakat kartı yüzü kapalı biçimde oyuncunun önünde kalır.
- Sadakat kartı Güç eli değildir; kaybedilemez, çalınamaz ve el sınırına girmez.
- Sadakat oyun sırasında gösterilemez; ölen oyuncunun Sadakati de açıklanmaz.
- Hainler birbirini Sadakatlerin dağıtılmasından sonraki ilk yolculuk gecesinde tanır.

Bu düzenin amacı, Kaptan seçimini, Çürümüş Erzak açılışını ve kalkış öncesi tanışmayı kimse Hain veya Tayfa olduğunu bilmeden tamamlamaktır.

## 6. İskorbüt kuralı

Yolculuk Haritası, uzun bir deniz seferinin son bölümüdür. Tayfanın taze erzağa ihtiyacı vardır.

1. İskorbüt etkin değilse Ada ziyareti zorunlu değildir.
2. İskorbüt etkinse gemi Liman Gecesinden önce Haritadaki herhangi bir Ada kartına girmek zorundadır.
3. Gemi ilk kez bir Adaya girdiği anda, Ada olayı çözülmeden önce İskorbüt temizlenir ve Çürümüş Erzak kartı atılır.
4. Liman Gecesi başlarken kart hâlâ açıksa herkes İskorbütten ölür ve Hainler kazanır.

Ada kartına giriş İskorbüt bakımından anlık ve kalıcıdır. Ada olayı uygulanmadan **Kaderi Yeniden Yaz** kullanılıp gemi önceki konumuna dönse bile İskorbüt yeniden etkinleşmez; yalnız Ada olayının uygulanması engellenir.

İskorbüt kartının ilk sahibi ölse, mahsur kalsa veya Kamaraya girse bile ortak zorunluluk devam eder.

## 7. Harita kurulumu

### 7.1 Harita boyu ve kategori kotası

`Genişlik × yükseklik` kullanılır.

| Süre | 6–10 kişi | Kategori | 11–15 kişi | Kategori |
|---|---|---|---|---|
| Hızlı | 5×5 | 15 Deniz / 6 Kayalık / 2 Ada / 2 Fener | 6×5 | 18 / 7 / 3 / 2 |
| Standart | 5×6 | 18 / 7 / 3 / 2 | 6×6 | 21 / 8 / 4 / 3 |
| Uzun | 5×7 | 21 / 8 / 4 / 2 | 6×7 | 25 / 10 / 4 / 3 |

Her kurulumda en az iki Ada bulunması bu tabloyla zaten garanti edilir.

### 7.2 Gizli doğrudan Gövde-hasarı kotası

| Oyuncu | Hızlı / Standart Deniz + Kayalık | Uzun Deniz + Kayalık |
|---:|---:|---:|
| 6 | 6 + 4 = **10** | 5 + 4 = **9** |
| 7–9 | 5 + 4 = **9** | 4 + 4 = **8** |
| 10 | 6 + 4 = **10** | 5 + 4 = **9** |
| 11–12 | 7 + 5 = **12** | 6 + 5 = **11** |
| 13–15 | 9 + 5 = **14** | 8 + 5 = **13** |

Kartların olay yüzünde yalnız Moderatörün göreceği küçük bir Gövde çatlağı kurulum simgesi bulunmalıdır.

### 7.3 Havuzun toplamı

| Kategori | Toplam | Doğrudan Gövde hasarı | Doğrudan Gövde hasarı yok |
|---|---:|---:|---:|
| Açık Deniz | 30 | 9 | 21 |
| Kayalık | 12 | 5 | 7 |
| Ada | 6 | 0 | 6 |
| Deniz Feneri | 4 | 0 | 4 |
| **Toplam** | **52** | **14** | **38** |

### 7.4 Ada çevresi güvenlik kuralı

Bir Ada kartının çevresindeki sekiz bitişik karede Girdap veya Ters Akıntı olamaz.

Moderatör pratikte şu sırayı kullanır:

1. Ada yerlerini belirler.
2. Her Adanın yatay, dikey ve çapraz komşularını yasaklı bölge olarak işaretler.
3. Seçilen Girdap ve Ters Akıntı kartlarını bu bölgenin dışında yerleştirir.
4. Kalan kartları normal biçimde doldurur.

Bu yerleşim bilgisi oyunculara açıklanmaz; onlar yalnız kategori yüzlerini görür.

### 7.5 Liman karesi ve başlangıç Sis yasağı

- Liman sabit olarak ortada değildir. Moderatör 5 veya 6 sütunlu Haritanın en üst satırındaki istediği tek kareyi Liman olarak işaretler.
- Liman seçildikten sonra bütün rota yasallığı o kareye göre hesaplanır.
- Başlangıç sütunu da kurulumda seçilir; sabit merkez başlangıcı yoktur.
- Geçilmez Kayalıklar hesaba katıldığında başlangıçtan en az bir erişilebilir Adaya, oradan seçilmiş Limana normal ileri hareketlerle ulaşan en az bir yol zorunludur.
- Kalan normal hamle sayısıyla seçilmiş Limana ulaşmayı imkânsız hâle getiren kare yasal rota değildir.
- İlk gün Kaptanın seçebileceği **bütün yasal ilk Yakın Ufuk** kartlarında Sis bulunamaz. Başlangıcın kenarda veya Limanın uzak konumda olması nedeniyle ilk seçenek sayısı 1, 2 veya 3 olabilir.

### 7.6 Dinamik başlangıç geometrisi

Sütunlar oyuncuların baktığı yönde soldan sağa, `1` ile Harita genişliği arasında sayılır. Gemi Haritanın en alt satırının hemen dışında başlar.

- 5 sütunlu Haritada başlangıç sütunu `1–5` arasındaki herhangi bir sütundur.
- 6 sütunlu Haritada başlangıç sütunu `1–6` arasındaki herhangi bir sütundur.
- Moderatör başlangıç sütununu seçebilir veya tarafsız bir rastgele yöntem kullanabilir; kural açısından sabit bir merkez sütunu yoktur.
- İlk Yakın Ufuk adayları başlangıç sütununun bir sol, aynı ve bir sağ karşılıklarıdır. Harita dışı, seçilmiş Limana kalan adımlarla erişemeyen veya Geçilmez Kayalık olan hedefler elenir.
- Bu nedenle ilk rota sayısı her zaman üç olmak zorunda değildir. Yalnız kalan yasal seçenekler Kaptanın kör ilk rota seçiminde kullanılabilir.

### 7.7 Geçilmez Kayalık kurulumu

Geçilmez Kayalık, 52 Harita kartından ayrı bir kurulum işaretidir. İşaret bir Harita karesinin üzerine konur ve alttaki kartın kategori/olay kimliğini değiştirmez; fakat Gemi o kareye hiçbir normal, zorunlu veya isteğe bağlı hareketle giremez.

| Harita | Geçilmez Kayalık |
|---|---:|
| 5×5 | 1 |
| 5×6 | 1 |
| 6×5 | 1 |
| 5×7 | 2 |
| 6×6 | 2 |
| 6×7 | 2 |

Yerleşim hükümleri:

1. Geçilmez Kayalık en üstteki son Harita/Ufuk hattına konulamaz.
2. Başlangıçtaki bütün yasal ilk rotaları kapatamaz.
3. Kurulum sonunda seçilen başlangıçtan en az bir erişilebilir Ada üzerinden seçilmiş Limana en az bir normal ileri yol kalmalıdır.
4. Geçilmez Kayalık oyuncular tarafından baştan görülür; gizli olay değildir.
5. İşaretli kare Ufuk hedefi değildir ve rota oylamasına girmez.
6. Geçilmez Kayalık alttaki Harita kartını açmaz ve olayını çözmez.

Bu kurulum kontrolü, acil geri dönüş kuralına rağmen zorunludur. Acil geri dönüş, **oyuncuların yolculuk sırasında seçtiği bir kolun sonradan Geçilmez Kayalık yüzünden çıkmaza dönüşmesi** için vardır; Moderatörün baştan matematiksel olarak çözümsüz Harita kurmasına izin vermez.

### 7.8 Moderatör hızlı Ufuk referansı

- **Yakın Ufuk:** Geminin bir sonraki normal harekette gidebileceği, bir sıra ilerideki İskele önü, Pruva önü ve Sancak önü kartlarıdır.
- **Uzak Ufuk:** Bu üç geometrik karşılığın hemen arkasında, gemiden iki sıra ileride bulunan karşılık gelen kartlardır; iki hamlede erişilebilecek bütün kartlar değildir.
- Bir kart ancak Harita içinde bulunuyor, seçilmiş Limana kalan hamlelerle erişimi koruyor, **Geçilmez Kayalıkla kapalı değil** ve o anda geçerli diğer hareket/yasallık kısıtlarını sağlıyorsa Ufuk hedefidir.
- Yakın Ufuk hedefi bir sonraki normal hareketle doğrudan yasal biçimde erişilebilir olmalıdır.
- Uzak Ufuk hedefi, karşılık gelen konumda olmasının yanında mevcut yasal Yakın Ufuklardan en az biri üzerinden iki normal hareketlik yasal bir yola sahip olmalıdır.
- Liman üst sırada seçilmiş tek karedir; rota yasallığı yalnız bu gerçek hedefe göre hesaplanır.
- Başlangıçtaki yasal Yakın Ufuk kartlarında Sis bulunmaz; sonraki sıralarda Sis normal kullanılabilir.

## 8. 52 Harita kartı

Geçilmez Kayalık işaretleri bu 52 karta dâhil değildir; alttaki kartın kimliği değişmez ve kart havuzu **118 toplam kart kimliğinde** kalır.


### 8.1 Açık Deniz — 30 kart

| Kart | Adet | Etki |
|---|---:|---|
| Sakin Deniz | 3 | Hiçbir şey olmaz. |
| Sis | 5 | Bu gece Sis kuralı uygulanır. İlk Hain uyanışında saldırı yine yoktur. |
| Girdap | 2 | Gemi hemen rastgele bir yasal Yakın Ufka zorunlu ek hareket yapar; yeni kart da çözülür. Geçilmez Kayalık nedeniyle hiç yasal ek hedef yoksa yalnız hareket kısmı boşa düşer; aynı gün acil geri dönüş yapılmaz. |
| Fırtına | 2 | Gemi 1 Gövde kaybeder. |
| Kraken | 1 | Gemi 1 Gövde kaybeder. Yama Tahtası işlemez; Zıpkın Sandığı veya Tahtakakan işleyebilir. |
| Adam Denize! | 2 | Kader Zarıyla seçilen bir serbest gemi oyuncusu denize düşer; hemen kurtarılmazsa ölür. |
| Durgun Deniz | 1 | Bir sonraki rota seçiminde yalnız Pruva önü kullanılabilir. Bu seçenek yasal değilse kısıt boşa düşer. |
| Uygun Rüzgâr | 1 | Gemi isterse olaydan sonra bir ek normal hareket yapar; yeni kart da çözülür. |
| Sürüklenen Sandık | 2 | Tayfa 1 Güç kartı kazanır. |
| Hayalet Işıkları | 1 | İki dış Yakın Ufuk kartının yeri, olay yüzlerine bakılmadan değiştirilir. |
| Ters Akıntı | 1 | Bir sonraki rota seçiminde yasal yönlerden biri Kader Zarıyla kapanır; bütün yolları kapatamaz. |
| Tuzlu Sağanak | 1 | Gücü olan oyuncular arasından Kader Zarıyla seçilen bir kişi rastgele 1 Güç kaybeder. |
| Uçan Balık Yağmuru | 1 | Mekanik etki yoktur. |
| Güverteyi Yalayan Dalga | 1 | Gücü olan oyuncular arasından Kader Zarıyla seçilen iki kişi rastgele birer Güç kaybeder. |
| Direk Çatlatan Bora | 1 | Gemi 1 Gövde kaybeder. |
| Mizanayı Döven Dalga | 1 | Gemi 1 Gövde kaybeder. |
| Karayel Tokadı | 1 | Gemi 1 Gövde kaybeder. |
| Kırkikindi Açıkta Yakaladı | 1 | Gemi 1 Gövde kaybeder. |
| Alabora Olmadık Sayılır | 1 | Gemi 1 Gövde kaybeder. |
| Bir Bulutun Kişisel Meselesi | 1 | Gemi 1 Gövde kaybeder. |

### 8.2 Kayalık — 12 kart

| Kart | Adet | Etki |
|---|---:|---|
| Ufak Kayalık | 1 | Hasar olmaz. |
| Batık Kalyon | 2 | Tayfa 1 Güç kazanır; Dipgören kullanılırsa 1 ek Güç kazanır. |
| Sivri Kayalık | 2 | Gemi 1 Gövde kaybeder. |
| Dar Resif | 1 | Gemi 1 Gövde kaybeder; ardından isterse bir ek normal hareket yapar. |
| Gizli Geçit | 1 | Gemi isterse bir ek normal hareket yapar. |
| Kaçakçı Oyuğu | 1 | Tayfa 1 Güç kazanır. |
| Kırılan Sandıklar | 1 | Gücü olan oyuncular arasından Kader Zarıyla seçilen bir kişi rastgele 1 Güç kaybeder. |
| İki Taraftan Sıyırdık | 1 | Gücü olan oyuncular arasından Kader Zarıyla seçilen iki kişi rastgele birer Güç kaybeder. |
| Suyun Altındaki Diş | 1 | Gemi 1 Gövde kaybeder. |
| Haritada İnce Çizgi | 1 | Gemi 1 Gövde kaybeder. |

Kayalık kategorisinde denize düşme olayı yoktur.

### 8.3 Ada — 6 kart

İskorbüt etkinse gemi bir Ada kartına girer girmez önce İskorbüt temizlenir, sonra aşağıdaki olay çözülür.

| Kart | Adet | Etki |
|---|---:|---|
| Erzak Adası | 1 | Tayfa 2 Güç kazanır; iki farklı oyuncuya verilir. |
| Terk Edilmiş Karakol | 1 | Tayfa 1 Güç kazanır; Kaptan mevcut kapalı Yakın veya Uzak Ufuktan birini seçer, kart herkese gösterilip yeniden kapatılır. |
| Rehin Adası | 1 | Kader Zarıyla seçilen bir serbest gemi oyuncusu zorunlu olarak adada bırakılır. Güç ödeme seçeneği yoktur. |
| Tersane Koyu | 1 | Gemi en fazla başlangıç değeri olan 2 Gövdeye kadar 1 Gövde onarır. |
| Korsanların Mola Yeri | 1 | Gücü olan oyuncular arasından Kader Zarıyla seçilen iki kişi bütün Güçlerini kaybeder. |
| Gümrükçünün Tek Yaşadığı Ada | 1 | Gemideki herkes en fazla bir Güç tutar; fazlasını yüzü kapalı atar. |

### 8.4 Deniz Feneri — 4 kart

| Kart | Adet | Etki |
|---|---:|---|
| Çalışan Deniz Feneri | 1 | Kaptan mevcut kapalı Yakın veya Uzak Ufuktan birini seçer; kart herkese gösterilip yeniden kapatılır. |
| Terk Edilmiş Deniz Feneri | 1 | Tayfa 1 Güç kazanır. |
| Fenercinin Zulası | 1 | Tayfa 2 Güç kazanır. |
| Sahte Deniz Feneri | 1 | Bir sonraki seçilmiş rota, mümkünse komşu başka bir yasal Yakın Ufka rastgele sapar. |

## 9. Kader Zarıyla oyuncu seçimi

### 9.1 Genel yöntem

1. Olayın uygun hedefleri belirlenir.
2. Her uygun oyuncu bir d12 atar.
3. En düşük sonucu atan oyuncu hedef olur.
4. En düşükte eşitlik varsa yalnız eşit kalanlar yeniden atar.
5. İki hedef gerekiyorsa en düşük iki farklı oyuncu seçilir. İkinci sıra sınırında eşitlik varsa yalnız o eşit grup, kalan yer için yeniden atar.
6. Uygun oyuncu sayısı etkiden azsa yalnız mevcut uygun oyuncular etkilenir.

### 9.2 Uygun hedefler

- **Güç kaybı:** yaşayan, gemide, Kamarada olmayan ve en az bir gerçek Gücü bulunan oyuncular.
- **Rehin Adası:** yaşayan, gemide ve Kamarada olmayan oyuncular. Kaptan da zar atar.
- **Adam Denize!:** yaşayan, gemide ve Kamarada olmayan oyuncular.
- Bir etki gemide hiç oyuncu bırakacaksa son gemi oyuncusu uygun hedef değildir.

### 9.3 Hangi Güç kaybolur?

Harita olayı “rastgele bir Güç kaybet” diyorsa hedef, Güçlerini yüzü kapalı karıştırır; Moderatör bakmadan birini kapalı atık destesine koyar.

Karakter ve Sadakat kartları hiçbir zaman bu seçime girmez.

Şüpheli Martı ilk hedefi belirleyerek zarı geçersiz kılabilir. Uğurlu Altın tamamlanmış seçimi bir kez yeniden yaptırabilir; ikinci sonuç kesindir.

## 10. Gemi, hareket ve Kaptan

- Gemi **2 Gövdeyle** başlar: `2 sağlam`, `1 su alıyor`, `0 battı`.
- Gemi yukarı, seçilmiş Liman yönünde ilerler.
- **Yakın Ufuk**, geminin bir sonraki normal harekette gidebileceği bir sıra ilerideki İskele önü, Pruva önü ve Sancak önü kartlarıdır.
- **Uzak Ufuk**, bu üç geometrik karşılığın hemen arkasında, gemiden iki sıra ileride bulunan karşılık gelen kartlardır. İki hamlede erişilebilecek bütün kartlar Uzak Ufuk sayılmaz.
- Harita sınırı dışındaki, seçilmiş Limana kalan hamlelerle erişimi kaybettiren, Geçilmez Kayalıkla kapalı veya o anda geçerli başka bir yasallık kısıtı nedeniyle erişilemeyen kart Ufuk hedefi değildir.
- Yakın Ufuk doğrudan bir sonraki normal hareketle erişilebilir olmalıdır. Uzak Ufuk ise mevcut yasal Yakın Ufuklardan en az biri üzerinden iki normal hareketlik yasal bir yola sahip olmalıdır.
- **Normal hareket yalnız bir sonraki satıra doğrudur.** Gemi normalde geri gidemez ve bekleyemez. Tek geri hareket istisnası aşağıdaki Geçilmez Kayalık acil geri dönüşüdür.
- Kalan normal hamle sayısıyla Moderatörün seçtiği Liman karesine ulaşmayı imkânsız kılan kare yasal rota değildir.
- Geçilmez Kayalık işaretli kare hiçbir koşulda normal rota hedefi olmaz.
- Harita sınırı, seçilmiş Limana erişim, Geçilmez Kayalık ve ziyaret edilmiş kart durumu temel yasallığı belirler. Aktif **mutlak olmayan** rota kısıtları oluşma sırasıyla uygulanır; ardından yazılı iptal/kaldırma ve rota açma etkileri çözülür. Sıfır rota kalırsa en son mutlak olmayan kısıtlar en az bir rota kalana kadar yok sayılır. Harita sınırı, Limana geometrik erişim ve Geçilmez Kayalık hiçbir zaman yok sayılmaz.
- Açılmış ve olayı çözülmüş karta yeniden girilirse olay ikinci kez çalışmaz.
- Zorunlu veya ek hareket yeni kapalı karta götürürse yeni olay da çözülür.
- Kaptanın rota oyu 2, Suçlama ve İsyan oyu 1’dir.
- Rota beraberliğini Kaptan yalnız berabere seçenekler arasından bozar.
- **Kaptan rolü kalıcıdır ve kaldırılamaz.** Kaptan ölür, Kamaraya girer, mahsur kalır, Kayıkçı olarak kurtarmaya gider veya başarılı İsyanla görevden düşerse hemen yeni Kaptan seçilir.

### Geçilmez Kayalık kaynaklı acil geri dönüş

Acil geri dönüş yalnız şu kesin sırayla uygulanır:

1. Önce normal rota yasallığı ve bütün mutlak olmayan kısıtların sıfır-rota geri düşümü çözülür.
2. Hâlâ **hiç yasal ileri rota yoksa**, Moderatör yalnız Geçilmez Kayalıkları geçici olarak yok sayarak aynı konumdaki ileri rotaları yeniden hesaplar.
3. Kayalıklar yok sayıldığında en az bir ileri rota doğuyorsa çıkmazın nedeni Geçilmez Kayalıktır ve acil geri dönüş açılır.
4. Gemi Harita üzerinde daha önce bulunduğu **bir önceki kareye** geri döner. Bu rota oylaması değildir; tek mümkün geri çekilmedir.
5. Geri dönüş o günün normal hareketini tamamen tüketir. Dönülen kart daha önce çözülmüşse olay tekrar çalışmaz. Ardından o günün normal gece sırası oynanır.
6. Geri dönülen noktada sonraki normal gün yine hiçbir ileri rota yoksa aynı koşullar tekrar kontrol edilir ve gerekirse bir kare daha geri dönülebilir.
7. Bir kolun Geçilmez Kayalık nedeniyle çıkmaz olduğu açıkça öğrenildiyse, başka yasal seçenek varken aynı bilinen çıkmaz kola tekrar girilemez. Böylece Hainler veya Tayfa sonsuz ileri-geri döngüsü yaratamaz.
8. Girdap/isteğe bağlı ek hareket gibi **olay içi ek hareket** Geçilmez Kayalık yüzünden hedef bulamazsa ek hareket boşa düşer; bu madde aynı olay çözümü içinde geri dönüş başlatmaz. Acil geri dönüş ancak sonraki normal rota gününde değerlendirilir.

Kurulumun ilk hareketi baştan tamamen kapalı olamayacağı için Gemi Harita dışındaki başlangıç noktasına acil geri dönüş yapmaz.

### Kaptan seçiminin aday ve seçmenleri

- Yaşayan, gemide bulunan ve Kamarada olmayan her oyuncu aday olabilir ve oy verebilir; kendine oy vermek serbesttir.
- Mahsur, ölü, Kamarada veya Kayıkçı seferinde olan oyuncu aday veya seçmen olamaz.
- Beraberlik yalnız berabere adaylar arasında sonuç çıkana kadar yeniden oylanır.
- Kaptan gece ayrıca uyanmaz ve makamı kendiliğinden Yakın veya Uzak Ufka bakma hakkı vermez.

## 11. Gün ve gece akışı

### 11.1 Kalkış öncesi tanışma gecesi

Gemi başlangıç konumundadır. Bütün oyuncular tarafsız anlamda mürettebat olarak tanışır; Moderatör dünyayı ve yolculuğu tanıtır. Karakter, Güç, Harita ve Hain eylemi yoktur. Sadakatler henüz dağıtılmamıştır. Kaptan uyanmaz ve Ufka bakmaz.

### 11.2 İlk gün

1. Sadakatler dağıtılır.
2. Serbest tartışma yapılır.
3. İlk rota öncesinde rota bilgisi veren veya rota kartlarının yerini/yasallığını değiştiren isteğe bağlı Karakter ve Güçler kullanılamaz. Buna Pusula, Kırık Dürbün, Islak Deniz Haritası, Eski Seyir Defteri ve benzerleri dâhildir.
4. İlk rotayı Kaptan tek başına, seçilen başlangıç konumundan doğan **yasal Yakın Ufuklar arasından** ve olay yüzlerini bilmeden seçer. Yasal ilk seçenek sayısı 1, 2 veya 3 olabilir.
5. Hareket ve Harita olayı çözülür.
6. İlk olayın tepki pencerelerinde Hemen, Hasardan önce veya Olay açılınca yazan kartlar normal biçimde kullanılabilir. Bu, Kaptanın ilk rota seçimini bilgiyle yaptığı anlamına gelmez.
7. İlk gün Suçlama veya İsyan yapılamaz.
8. Sadakatlerin dağıtılmasından sonraki ilk yolculuk gecesi oynanır.

### 11.3 Sonraki günler

1. Şafak ve gece sonucu
2. Kamaradan çıkışlar ve Kaptan kontrolü
3. Serbest tartışma
4. Gündüz bilgi, açık Karakter ve Güç pencereleri
5. Eşzamanlı ve açık rota oyu
6. Hareket
7. Harita olayını çevirme ve çözme
8. En fazla bir Suçlama veya İsyan
9. Gece

### 11.4 Kartların zaman ve görünürlük ilkesi

- Seçime bağlı Güç ve açık Karakter kullanımları kural olarak gündüz yapılır.
- Pusula yalnız gündüz kullanılabilir veya açıkça devredilebilir.
- Kartında “hemen”, “hasardan önce”, “oylar açılınca” veya benzeri bir tepki penceresi yazan kart yalnız o anda açılır. Bu kullanım yeni bir gizli gece eylemi sayılmaz.
- Uzakgören ve Kıyıçizen gibi yazılı gizli roller gece çalışır.
- Kart metninde açıkça yazmayan hiçbir gizli gece kullanımı yoktur.
- Metninde **gizlice** yazan veya gece Ufka bakan Karakter, kullanıldığında açılmaz ve kapalı kalır; Moderatör etkisini gizlice yürütür.
- Kamusal bir durumu, hedefi, oyu, kurtarmayı, hasarı veya kart dağıtımını değiştiren Karakter kullanılırken açılır ve oyunun sonuna kadar açık kalır.
- Tek kullanımlık gizli yeteneklerin harcandığını Moderatör gizlice kaydeder; açık yeteneklerin harcandığı kartın üzerinde görünür işaretle tutulur.

### 11.5 İkinci geceden itibaren kesin gece sırası

Tanışma gecesinden sonraki her yolculuk gecesinde Moderatör şu sırayı kullanır:

1. Yakın Ufka bakma yeteneği olan Karakter çalışır.
2. Uzak Ufka bakma yeteneği olan Karakter çalışır.
3. O gece tetiklenen diğer Karakter, Güç veya özel etkileşimler çözülür.
4. En son Hainler uyanır.

### 11.6 Hainlerin gece eylemi

- Hainlerin ilk uyanışı Sadakatlerin dağıtılmasından sonraki ilk yolculuk gecesidir. Bu uyanışta birbirlerini tanır, takım olarak bir Yakın Ufuk kartına bakar ve saldırı yapamazlar.
- Sonraki normal gecelerde takım ya bir Yakın Ufka bakar ya da gemide ve Kamarada olmayan bir Tayfayı denize atmaya çalışır.
- Sisli gecede önce bir Yakın Ufka bakabilir, sonra ayrıca bir Tayfaya saldırabilir.
- Fırtına Feneri Sis saldırısını kapatır; bilgi eylemi kalır.
- Hain sayısından bağımsız olarak takımın toplam saldırısı birdir.
- Kamarada, adada veya Kayıkçı seferinde olan Hain takım eylemine katılamaz.
- Hainler süre içinde anlaşamazsa eylem boşa düşer; Moderatör onlar adına seçim yapmaz.

## 12. Suçlama, İsyan ve Kamara

Gemide ve Kamarada olmayan yaşayan oyuncuların salt çoğunluğu gerekir. Oylar aynı anda açılır.

### Suçlama

- Aynı gün birden fazla geçerli hedef önerilirse uygun seçmenler önerilen hedeflerden birini aynı anda işaretler. En çok işaret alan hedef o günün tek resmî Suçlama hedefi olur; eşitliği Kaptan bozar. Bu hedef belirleme işlemi resmî oylama değildir ve oylama Güçlerini tetiklemez.
- İlk başarılı Suçlama: hedef Kamaraya girer, bir gece kalır ve kalıcı **Bir Kez Mahkûm** işareti alır.
- Aynı oyuncuya karşı ikinci başarılı Suçlama: oyuncu denize atılır, ölür ve kurtarılamaz.
- Sadakati açıklanmaz.

### İsyan

- Yalnız Kaptana karşı yapılır ve o günün siyasi işlemini tüketir.
- Başarılıysa eski Kaptan bir gece Kamaraya girer fakat Bir Kez Mahkûm işareti almaz.
- Yeni Kaptan hemen açık oylamayla seçilir.

### Resmî oylama ve Bir Daha Say

- Rota oylaması, Kaptan seçimi, Suçlama, İsyan ve kuralların resmî oylama dediği diğer bütün oylamalar bu kapsamdadır.
- Resmî sonuç tam 1 oy farkıyla bittiyse **Bir Daha Say** açılabilir; oylama bir kez bütünüyle tekrarlanır.
- İkinci sonuç kesindir. Bir Daha Say kullanıldıktan sonra kapalı Güç atık destesine gider.

### Kamarada konuşma

- Kaptan, oyuncu Kamaraya girdiği anda onun konuşup konuşamayacağını açıkça söyler.
- İzin verilmezse mahkûm konuşamaz, fısıldayamaz veya işaretle görüş bildiremez.
- İzin verilirse konuşabilir; fakat oy veremez, makam taşıyamaz, Karakter/Güç kullanamaz ve gece eylemine katılamaz.
- **Anahtar Deliği**, kendi yazılı metniyle Güç kullanma yasağının tek istisnasıdır. Konuşma izni yoksa öğrendiği bilgiyi o gün aktaramaz.
- Kamaradaki oyuncu Hain saldırısının hedefi olamaz.

## 13. Ölüm, denize düşme ve mahsur kalma

### 13.1 Ölüm

- Ölen oyuncu oyundan elenir ve oyun hakkında konuşamaz.
- Oy veremez, aday olamaz, kart veya yetenek kullanamaz ve gece gözünü açmaz.
- Sadakati oyun sonuna kadar açıklanmaz.
- Takımı sonradan kazanırsa ölü oyuncu da takımıyla kazanır.

### 13.2 Denize düşme

- Harita veya Hain saldırısıyla denize düşen oyuncu uygun Can Simidi, Kancalı Halat veya Canhalatıyla hemen kurtarılabilir.
- Hemen kurtarılmazsa ölür.
- Sosyal oylamayla denize atılan oyuncu hiçbir kurtarma etkisiyle kurtarılamaz.
- Kayalık kategorisinde oyuncuyu denize düşüren bir çekirdek kart yoktur.

### 13.3 Adada mahsur kalma

Mahsur oyuncu hayattadır; fakat gemiye dönene kadar:

- konuşamaz veya işaretle görüş bildiremez;
- oy veremez;
- Kaptan olamaz;
- Karakter veya Güç kullanamaz;
- gemideki olayların hedefi olamaz.

Tek istisna: Mahsur oyuncu elinde Pusula varsa gündüz Pusula penceresinde kartı sessizce açarak kurtarma için hazır edebilir.

### 13.4 Güvercin Mektubu

- Gemidekiler her gün toplam en fazla bir mahsur oyuncuya bir Güvercin gönderebilir.
- Tek ve açık bir soru yüksek sesle sorulur. Birden fazla öneri varsa son soruyu Kaptan belirler.
- Mahsur oyuncu cevabını hemen kâğıda, en fazla bir cümle olarak yazar ve Moderatöre verir.
- Çizim, şifre, ikinci mesaj veya sözlü açıklama kullanamaz.
- Moderatör cevabı bir sonraki şafakta okur veya kâğıdı gemiye verir.
- Mahsur oyuncu mektupta doğruyu söylemek zorunda değildir.

## 14. Pusula ve Kayıkçı

### 14.1 Pusulanın iki modu

Pusula tek kullanımlık bir Güç kartıdır ve yalnız gündüz kullanılır.

#### A. Ufuk modu

1. Mevcut yasal Yakın Ufuk kartlarından biri seçilir.
2. Olay yüzü bütün oyunculara gösterilir.
3. Kart yeniden kapatılır; ziyaret edilmiş veya çözülmüş sayılmaz.
4. Pusula atılır.

#### B. Kurtarma modu

1. Pusula sahibi kartı açıkça Kayıkçıya verir veya mahsur oyuncunun önüne açık koyar.
2. Mahsur oyuncu zaten Pusulaya sahipse kartı sessizce açabilir.
3. Kayıkçı hayatta, gemide ve Kamarada değilse Karakterini açıp kurtarma seferini başlatmayı seçebilir.
4. Kayıkçı kabul ederse sefer başlar; Pusula kapalı Güç atık destesine gider ve Kayıkçının tek kullanımlık Karakter yeteneği harcanır.
5. Kayıkçı reddederse Pusula harcanmış sayılır ve kapalı Güç atık destesine gider; sefer başlamaz, mahsur adada kalır ve Kayıkçının tek kullanımlık yeteneği harcanmaz. Oyun başka işlem yapılmadan normal sürer.
6. Pusulayı mahsur oyuncu açmış olsa bile Kayıkçı reddederse aynı hüküm uygulanır.

Pusulanın açıkça Kayıkçıya veya mahsur oyuncuya verilmesi kartın özel kuralıdır; başka Güçler bu yolla devredilemez.

### 14.2 Kurtarma süresi

- Kayıkçı gündüz, rota oylamasından önce gemiden ayrılır.
- O günün rota oylaması, Harita olayı ve gecesi boyunca oyunda değildir.
- Konuşamaz, oy veremez, hedef olamaz ve başka kart/yetenek kullanamaz.
- Mahsur oyuncu aynı süre boyunca adada kalır.
- Kayıkçı ve kurtardığı tek oyuncu bir sonraki şafakta gemiye döner.
- Kayıkçı Kaptansa ayrılmadan önce yeni Kaptan seçilir; dönüşte makamı otomatik geri almaz.
- Gemi sefer sırasında batarsa kurtarma tamamlanmaz.

Kayıkçı kendi mahsur kaldıysa kendisini kurtaramaz; seferi başlatacak Kayıkçının gemide olması gerekir.

## 15. Kart gizliliği, Güç kazanma ve el sınırı

- Karakter, Güç ve Sadakat kartları birbirinden ayrı tutulur.
- Güç kartlarının adları ve metinleri gizlidir; kart sayısı kamusaldır.
- Oyuncu Gücü hakkında yalan söyleyebilir fakat ispat için gösteremez.
- Güç yalnız yazılı kullanım penceresinde açılır.
- Kullanılan Güç, metni başka bir yerde kalmasını söylemiyorsa atılır.
- Oyuncu en fazla iki kullanılabilir Güç tutar. Üçüncüyü alınca birini yüzü kapalı atar.
- **Islak Çorap** bu iki Güçlük el sınırına dâhildir.
- Sadakat ve Karakter kartları Güç kaybından etkilenmez.

### Islak Çorap çözüm sırası

1. Harita veya başka bir etki Güç alıcısını belirler; kazanılan kart henüz açıklanmaz.
2. Islak Çorap sahibi kartı açarsa kazanılan yeni Güç doğrudan ona gider; Islak Çorap asıl alıcıya geçer.
3. Yeni alıcı kendi kartına baktıktan sonra iki oyuncu da ayrı ayrı iki Güçlük el sınırını kontrol eder.
4. Sınırı aşan oyuncu kendi Güçlerinden birini yüzü kapalı atar. Islak Çorap da bu seçimde normal bir Güç sayılır.

### Güç destesinin tükenmesi

- Yolculuk Güç destesi biterse uygun kartlardan oluşan kapalı Güç atık destesi karıştırılır ve yeni yolculuk Güç destesi yapılır.
- Bir ödül sırasında deste yetmezse mevcut kartlar çekilir; uygun atıklar karıştırılır ve eksik çekim tamamlanır.
- **Kaderi Yeniden Yaz** ve **Seyir Zabtı** kullanıldıktan sonra oyun dışına çıkar; Güç destesine yeniden karıştırılmaz. Kesin dönüş-dışı liste yalnız bu iki karttır.
- Bir Daha Say, Pusula ve diğer normal Güçler kendi metinleri uyarınca atığa gittiklerinde yeniden karıştırılmaya uygundur.
- Oyun dışındaki kartlar, oyuncuların elleri, masada bağlı duran Güçler ve henüz çözülmemiş Şüpheli Martı/Islak Çorap atık destesine katılmaz.

### Haritadan Güç kazanma

- Harita Güç kazandırdığında kartlar görülmeden önce alıcıyı Kaptan belirler.
- Aynı olay iki kart veriyorsa, kart metni aksini söylemedikçe iki farklı alıcı seçilir.
- İskele Sıçanı kullanılırsa bir kartın alıcısını Kaptandan önce ve kart görülmeden belirler.
- Alıcı kartı yalnız kendisi görür.

## 16. 20 Karakter kartı

| # | Karakter | Etki | Kullanım biçimi |
|---:|---|---|---|
| 1 | **Uzakgören — Gözcü +2** | Tanışma gecesi hariç her gece bir Yakın Ufuk olayına gizlice bakar; Sis engellemez. | Gizli; kart kapalı kalır. |
| 2 | **Kıyıçizen — Haritacı +2** | Tanışma gecesi hariç, Sis olmayan her gece bir Uzak Ufuk olayına gizlice bakar. | Gizli; kart kapalı kalır. |
| 3 | **Dümenkurdu — Serdümen +2** | Tek kullanım; bir Harita olayının zorunlu hareket veya rota kilidi etkisini iptal eder. | Açılır ve açık kalır. |
| 4 | **Canhalatı — Palamarcı +2** | Tek kullanım; Harita veya Hain saldırısıyla düşeni hemen kurtarır. Oylamaya işlemez. | Açılır ve açık kalır. |
| 5 | **Tahtakakan — Kalafatçı +2** | Tek kullanım; geminin alacağı 1 Gövde hasarını engeller; Kraken'e de işler. | Açılır ve açık kalır. |
| 6 | **Dipgören — Dalgıç +1** | Batık Kalyonda bir kez 1 ek Güç kazandırır. | Açılır ve açık kalır. |
| 7 | **Rüzgârkoklayan — Yelkenci +1** | Bir kez Durgun Deniz veya rüzgâr kaynaklı rota kısıtını gizlice kaldırır. | Gizli; Moderatör harcandığını kaydeder. |
| 8 | **Kırık Kürek — Kayıkçı +1** | Pusula sunulunca kabul ederse bir tam vardiyalık kurtarma seferine çıkar; reddederse Pusula atılır, sefer başlamaz ve yeteneği harcanmaz. | Kabulde açılır ve açık kalır. |
| 9 | **Üç Anahtar — Levazımcı +1** | Tek kullanım; Güç kazanılırken bir fazla karta bakılır, sonra bir kart kapalı atılır. Kazanç sayısı artmaz. | Açılır ve açık kalır. |
| 10 | **Güvertebaşı — Lostromo +1** | Tek kullanım; Harita Güç kaybettirecekken seçilen oyuncunun bir kartlık kaybını engeller. | Açılır ve açık kalır. |
| 11 | **İskele Sıçanı +1** | Ada/Fenerden Güç kazanılırken bir kartın alıcısını, karta bakılmadan belirler. | Açılır ve açık kalır. |
| 12 | **Karga Yuvası +1** | Tek kullanım; rota öncesi bir Yakın Ufku işaretler, o rota en az bir oy alırsa toplamına +1 eklenir. | Açılır ve açık kalır. |
| 13 | **Kazanbaşı — Aşçı** | Özel mekanik yoktur. | Yeteneksiz; kart kapalı kalabilir. |
| 14 | **Fare Nazırı** | Özel mekanik yoktur. | Yeteneksiz; kart kapalı kalabilir. |
| 15 | **Papağan Mütercimi** | Özel mekanik yoktur. | Yeteneksiz; kart kapalı kalabilir. |
| 16 | **Fıçı Bekçisi** | Özel mekanik yoktur. | Yeteneksiz; kart kapalı kalabilir. |
| 17 | **Kafiye Belası — Gemi Şairi** | Özel mekanik yoktur. | Yeteneksiz; kart kapalı kalabilir. |
| 18 | **Karayı Özleyen — Acemi Gemici** | Özel mekanik yoktur. | Yeteneksiz; kart kapalı kalabilir. |
| 19 | **Yastıkçı — Kamarot** | Özel mekanik yoktur. | Yeteneksiz; kart kapalı kalabilir. |
| 20 | **Tahtaya Vuran — Hurafeci** | Özel mekanik yoktur. | Yeteneksiz; kart kapalı kalabilir. |

### Karakter kurulum yoğunluğu

| Oyuncu | Toplam Etki | En fazla +2 Karakter | Ek kural |
|---:|---:|---:|---|
| 6–7 | 4–5 | 2 | Uzakgören ve Kıyıçizen birlikte seçilmez. |
| 8–10 | 6–8 | 3 | — |
| 11–12 | 8–10 | 4 | — |
| 13–15 | 10–12 | 5 | — |

## 17. 30 Güç kartı

| # | Kart | Adet | Zaman | Kesin etki |
|---:|---|---:|---|---|
| 1 | **Can Simidi** | 2 | Hemen | Harita veya Hain saldırısıyla düşen bir oyuncuyu kurtarır; oylamaya işlemez. |
| 2 | **Kancalı Halat** | 2 | Hemen | Yalnız Harita olayıyla düşen bir oyuncuyu kurtarır. |
| 3 | **Pusula** | 1 | Gündüz | Bir yasal Yakın Ufku herkese gösterir veya Kayıkçıya kurtarma sunar. Kayıkçı reddederse Pusula atılır; sefer başlamaz, mahsur kalır ve Kayıkçı yeteneği harcanmaz. |
| 4 | **Güverte Araması** | 1 | Gündüz, rota öncesi | En az iki Gücü olan bir gemi oyuncusu seçilir; hedef seçtiği bir Gücü kapalı atar. Son Gücü aldıramaz. |
| 5 | **Yama Tahtası** | 1 | Hasardan önce | Kraken dışındaki 1 Gövde hasarını engeller. |
| 6 | **Zıpkın Sandığı** | 1 | Hasardan önce | Kraken’in 1 Gövde hasarını engeller. |
| 7 | **Geçici Yeke** | 1 | Rota öncesi | Bir etki rotayı tek yasal seçeneğe indirdiyse ikinci bir yasal Yakın Ufku açar. |
| 8 | **Kerteriz Pergeli** | 1 | Girdap/Akıntı çözülürken | Girdabın yasal varışını veya Ters Akıntının kapatacağı yasal yönü rastgelelik yerine sahibi seçer. |
| 9 | **Kurşun Ağırlık** | 1 | Girdap çözülürken | Girdabın zorunlu ek hareketini tamamen iptal eder. |
| 10 | **Yedek Yelken** | 1 | Rota öncesi | Durgun Deniz veya rüzgâr kaynaklı rota kısıtını kaldırır. |
| 11 | **Islak Deniz Haritası** | 1 | Gündüz, rota öncesi | İki Yakın Ufuk kartının yerini olaylara bakmadan değiştirir. |
| 12 | **Kırık Dürbün** | 1 | Gündüz, rota öncesi | Bir Yakın Ufuk olayına gizlice bakar. |
| 13 | **Eski Seyir Defteri** | 1 | Sis olmayan gündüz | Bir Uzak Ufuk için Moderatör yalnız “Gövde hasarı verebilir/vermez” der. |
| 14 | **Anahtar Deliği** | 1 | Gündüz, yalnız Kamarada | Bir Yakın Ufuk olayına gizlice bakar; Kamara Güç yasağının yazılı istisnasıdır. |
| 15 | **Kaptanın Eski Şapkası** | 1 | Rota oylaması | Sahibinin rota oyuna +1 ekler. |
| 16 | **İsyan Bildirisi** | 1 | İsyan | Sahibinin İsyan oyunu 2 sayar. |
| 17 | **Papağanın İfadesi** | 1 | Rota öncesi | Hedef rota tavsiyesini açık söyler; başka rotaya oy verirse oyu 0 sayılır. |
| 18 | **Mühürlü Emir** | 1 | Rota beraberliği | Kaptan çözmeden önce berabere rotalardan kazananı seçer. |
| 19 | **Kaçak Rom** | 1 | Rota öncesi | Hedef diğer açık oyları gördükten sonra en son ve açık oy verir. |
| 20 | **Bir Daha Say** | 1 | Oylar açılınca | Tam 1 oy farkıyla biten herhangi bir resmî oylamayı bir kez tekrar ettirir; ikinci sonuç kesindir ve kart atılır. |
| 21 | **Uğurlu Altın** | 1 | Kader Zarı sonucu sonrası | Tamamlanmış rastgele hedef seçimini bir kez yeniden yaptırır; ikinci sonuç kesindir. |
| 22 | **Kaptanın Çatlak Kupası** | 1 | Rota oylaması | Kaptanın o oylamadaki 2 oyunu 1’e indirir. |
| 23 | **Bayat Peksimet** | 1 | Gündüz, rota öncesi | Hedef ya bir Gücünü kapalı atar ya da rota sonucu açıklanana kadar konuşamaz. Gücü yoksa susmayı seçmek zorundadır. |
| 24 | **Islak Çorap** | 1 | Başkası Güç kazanırken | Kazanç açıklanmadan yeni Gücü sahibi alır, Çorap asıl alıcıya geçer; sonra iki oyuncu da iki Güç sınırını uygular. Çorap bir Güç sayılır. |
| 25 | **Şüpheli Martı** | 1 | Gündüz | Bir oyuncının önüne konur; sonraki rastgele oyuncu hedefli Harita olayının ilk hedefi olur, sonra Martı atılır. |
| 26 | **Fırtına Feneri** | 1 | Sis açıldığında | O gece Sis saldırısını kapatır; Hainlerin bir Yakın Ufuk bilgisi kalır. |
| 27 | **Kaderi Yeniden Yaz ★** | 1 | Olay açılınca, etkiden önce | Gemi önceki yere döner ve başka yasal Yakın Ufka gider. İlk kart açık ve ziyaret edilmiş kalır, olayı yeniden çalışmaz; Ada İskorbütü kalıcı temizler. Kullanıldıktan sonra oyun dışına çıkar. |
| 28 | **Seyir Zabtı ★** | 1 | Zararlı rota çözüldükten sonra | Zararlı rotaya oy veren bir oyuncuyu Sadakat açmadan bir gece Kamaraya yollar; Bir Kez Mahkûm sayılmaz. Kullanıldıktan sonra oyun dışına çıkar. |

Fiziksel toplam: `Can Simidi ×2 + Kancalı Halat ×2 + 26 tekil kart = 30`.

### Bu sürümde Güç değişiklikleri

- İşaret Fişeği çıkarıldı; fiziksel yerini Pusula aldı.
- Son Sandal çıkarıldı; fiziksel yerini Güverte Araması aldı.
- Eski Demir Pusulanın işlevi korundu fakat yeni Pusulayla karışmaması için adı Kerteriz Pergeli oldu.
- Bayat Peksimetin eski “2 Güç maliyeti” işlevi, Rehin Adası ödemesi kalktığı için silindi; etkileşim kartına dönüştü.
- Güvertebaşı’nın eski maliyet azaltma yeteneği aynı nedenle Güç kaybını önleyen yeteneğe dönüştü.

### Seyir Zabtı için zararlı rota tanımı

Bir rota, bütün önleme ve değiştirmeler çözüldükten sonra aşağıdakilerden en az birini gerçekten doğurmuşsa **zararlı rota** sayılır:

1. Gemi en az 1 Gövde kaybeder.
2. Bir oyuncu ölür, denize düşer veya mahsur kalır.
3. En az bir gerçek Güç kaybolur.
4. Gemi zorunlu ek harekete/sapmaya girer veya sonraki rota seçimi kısıtlanır.

Etki bütünüyle önlenmişse rota yalnız kart adından veya prototip Denge etiketinden dolayı zararlı sayılmaz. Seyir Zabtıyla verilen bir gecelik Kamara **Bir Kez Mahkûm** sayılmaz.

## 18. Liman Gecesi

1. Gemi üst sırada Moderatörün önceden seçtiği tek Liman karesine girer.
2. Liman karesindeki Harita olayı normal çözülür. Girdap veya isteğe bağlı ek hareket içeriyorsa hareket bölümü Limandan çıkamaz; gemi Limanda kalır.
3. Gemi batmadıysa İskorbüt kontrol edilir.
4. İskorbüt hâlâ etkinse herkes ölür ve Hainler kazanır.
5. İskorbüt temizlenmişse normal Liman Gecesi oynanır; son kart Sis ise Sis kuralı geçerlidir.
6. Şafakta Gövde 0 ise Hainler, bütün Tayfa ölmüşse Hainler, aksi hâlde Tayfa kazanır.
7. Liman Gecesinde yeni Suçlama veya İsyan yapılmaz.

## 19. Kesin kenar hükümleri

| Durum | Hüküm |
|---|---|
| Çürümüş Erzak sahibinin sonradan Kaptan olması | İskorbüt iptal olmaz. Yalnız kart açıldığı andaki Kaptanlık sayılır. |
| Çürümüş Erzak sahibinin ölmesi/mahsur kalması | Ortak Ada zorunluluğu devam eder. |
| İlk ziyaret edilen Ada Rehin Adasıysa | Önce İskorbüt temizlenir, sonra zarla biri adada bırakılır. |
| Ada girişinde Kaderi Yeniden Yaz kullanılırsa | İskorbüt kalıcı olarak temizlenir; yalnız Ada olayı uygulanmaz. |
| Kaderi Yeniden Yaz ile terk edilen kart | Olay yüzü açık ve ziyaret edilmiş kalır; daha sonra girilirse olayı çalışmaz. |
| Pusula Ufuk için kullanıldıysa | Aynı Pusula daha sonra kurtarmada kullanılamaz. |
| Pusula mahsur oyuncudaysa | Yalnız kartı sessizce açabilir; başka Güç kullanamaz. |
| Kayıkçı kurtarmayı reddederse | Pusula atılır; sefer başlamaz, mahsur kalır, Kayıkçı yeteneği harcanmaz. |
| Kayıkçı Pusulasızsa | Kurtarma seferi başlatamaz. |
| Kayıkçı Kaptansa | Ayrılmadan önce yeni Kaptan seçilir. |
| Kayıkçı mahsursa | Kendisini kurtaramaz. |
| Güç kaybı için Gücü olan kimse yoksa | Etkinin Güç kaybı kısmı boşa düşer. |
| İki Güç kaybı hedefi ama yalnız bir uygun oyuncu varsa | Yalnız o oyuncu etkilenir; aynı olay onu iki kez hedeflemez. |
| Güvertebaşı “bütün Güçlerini kaybet” olayında kullanılırsa | Seçilen oyuncunun bir Gücü korunur; diğerleri kaybolur. |
| Açılmış ve çözülmüş Harita kartına yeniden giriş | Olay ikinci kez çözülmez. |
| Pusulayla gösterilip yeniden kapatılan karta giriş | Kart henüz çözülmediği için olay normal çözülür. |
| Geçilmez Kayalık rota hedefiyse | Hedef yasal değildir; Ufuk sayılmaz ve oylamaya girmez. |
| Normal rota gününde hiç ileri rota yoksa | Önce mutlak olmayan kısıtların sıfır-rota geri düşümü uygulanır. Hâlâ sıfırsa Kayalıklar yok sayılarak nedensellik kontrol edilir; yalnız Kayalık kaynaklıysa acil geri dönüş açılır. |
| Acil geri dönüş | Gemi geldiği bir önceki Harita karesine döner; bir tam hareket/gün tüketir, çözülmüş olay tekrar çalışmaz ve gece normal oynanır. |
| Çıkmaz birden fazla kare geri çekilmeyi gerektiriyorsa | Her normal günde koşullar yeniden sağlanıyorsa yalnız bir kare geri dönülür. |
| Bilinen Kayalık çıkmaz koluna tekrar giriş | Başka yasal seçenek varken yasaktır. |
| İlk rota Geçilmez Kayalıklarla kapanıyorsa | Kurulum geçersizdir; Moderatör Kayalık yerleşimini değiştirir. |
| Girdap/ek hareket yalnız Geçilmez Kayalık yüzünden hedef bulamazsa | Olay içi hareket kısmı boşa düşer; aynı olay içinde geri dönüş yapılmaz. Sonraki normal rota gününde çıkmaz sürüyorsa acil geri dönüş değerlendirilebilir. |
| Girdap yeni kapalı karta sokarsa | Yeni kart çevrilir ve çözülür. |
| Girdap/ek hareket seçilmiş Limanda tetiklenirse | Harita dışına veya Limandan uzağa hareket edilmez; oyun Liman karesinde sürer. |
| Ek hareket için yasal hedef yoksa | İsteğe bağlı hareket kullanılamaz; zorunlu hareketin hareket kısmı boşa düşer. |
| Aynı hareket içinde Gövde 0 olursa | Limana yakınlık fark etmeksizin Hainler hemen kazanır. |
| Oylamayla denize atılma | Hiçbir kurtarma kartı veya Karakteri işlemez. |
| Son gemi oyuncusunu düşürme/mahsur bırakma | Oyuncu hedef havuzuna girmez; başka hedef yoksa etki boşa düşer. |
| Bütün Hainler ölürse | Oyun bitmez; Tayfa yine Limana ulaşmalıdır. |
| Kaptan Kamaraya, ölüme, Adaya veya Kayıkçı seferine giderse | Hemen yeni Kaptan seçilir. |
| Birden fazla rota kısıtı varsa | Temel yasallık; kısıtlar oluşma sırasıyla; iptal/kaldırma; rota açma sırasıyla çözülür. Hâlâ sıfır rota varsa en son mutlak olmayan kısıtlar bir rota kalana kadar yok sayılır. Harita sınırı ve Limana erişim yok sayılamaz. |
| Ufuk etkisi yeterli hedef bulamazsa | Harita dışındaki kart yerine konmaz; mevcut uygun hedefler kadar çözülür, hiç hedef yoksa bilgi kısmı boşa düşer. |
| Kart yalnız “Ufuk” diyorsa | Kaptan mevcut kapalı Yakın veya Uzak Ufuktan birini seçer. |
| İlk rota öncesi bilgi/değişiklik Gücü | Kullanılamaz; ilk rota kör seçilir. Yazılı tepki kartları ilk olay sırasında kullanılabilir. |
| Islak Çorap aktarımı | Önce yeni Güç ve Çorap yer değiştirir, sonra iki oyuncu ayrı ayrı iki Güç sınırını uygular. |
| Seyir Zabtı Kamarası | Bir gece sürer ve Bir Kez Mahkûm sayılmaz. |
| Güç destesi biterse | Uygun kapalı atıklar karıştırılır; Kaderi Yeniden Yaz ve Seyir Zabtı geri dönmez. |

## 20. v2.2 doğrulama kapsamı

v2.2 geliştirme doğrulayıcısı tam bir sosyal denge simülatörü değildir. Aşağıdaki yapısal kontrolleri yapar:

1. Oyuncu, Hain, Karakter, Güç, Sadakat ve 52 Harita kartı adetlerinin korunması; toplam kart kimliğinin 118 kalması.
2. Başlangıç Gövdesinin bütün Haritalarda 2 kalması.
3. 6-7 kişilik Karakter setinde Uzakgören ile Kıyıçizenin birlikte bulunmaması.
4. Dinamik alt-kenar başlangıcının 5 ve 6 sütundaki bütün sütunları kabul etmesi.
5. İlk Yakın Ufkun seçilen başlangıç, Liman erişimi ve Geçilmez Kayalığa göre dinamik türetilmesi; yasal ilk rotalarda Sis bulunmaması.
6. Harita boyuna göre Geçilmez Kayalık sayısının `1/1/1/2/2/2` tablosuyla uyuşması ve son Liman/Ufuk hattına işaret konulamaması.
7. Seçilen başlangıçtan erişilebilir bir Ada üzerinden seçilmiş Limana, Geçilmez Kayalıklar hesaba katıldığında en az bir ileri yol bulunması.
8. Geçilmez Kayalık hedeflerinin Yakın/Uzak Ufuktan ve normal hareketten elenmesi.
9. Acil geri dönüşün yalnız `sıfır ileri rota + Kayalıklar yok sayıldığında rota var` koşulunda açılması.
10. Kaptanın kalıcı olması; ilk rotayı tek başına seçmesi; ölüm/Kamara/mahsur/Kayıkçı/başarılı İsyan durumlarında yeni Kaptan seçilmesi; gece uyanışı ve otomatik Ufuk bilgisinin kapalı kalması.
11. Girdap/ek hareketin Kayalık yüzünden hedef bulamamasının aynı gün geri dönüş başlatmaması.
12. Kart metni karmasının v2.1 kart havuzuyla aynı kalması; Geçilmez Kayalık işaretlerinin kart kimliği sayılmaması.

Geçilmez Kayalık + acil geri dönüş için ayrı hedefli teknik testte 51.204 geometri yerleşimi, 15.000 yeni-kural davranışsal oyunu ve 6.000 kontrol oyunu çalıştırılmış; kalıcı kilit ve kurulum hatası görülmemiştir. Bu sonuç insan masa testinin yerini tutmaz.

## 21. v2.2 değişiklik kaydı

- v2.1 stabil temel olarak korunur; v2.2 ayrı geliştirme hattıdır.
- Gemi başlangıcı sabit merkez/sağ-orta sütundan çıkarılıp alt kenardaki herhangi bir sütuna açıldı.
- İlk Yakın Ufuk ve ilk Sis yasağı seçilen başlangıca göre dinamikleştirildi.
- Kaptanın oyunun kalıcı omurgası olduğu açıkça kilitlendi; ilk rotayı Kaptan tek başına seçmeye devam eder.
- Başarılı İsyan, Kaptanın ölümü ve mevcut görev dışı durumlarında yeni Kaptan seçimi korunmuştur.
- Kaptanın gece ayrıca uyanmaması ve makamın otomatik Ufuk bilgisi vermemesi korunmuştur.
- Gövde bütün Harita boylarında 2 olarak kilitlendi; 3 Gövde adayı reddedildi.
- 52 Harita kartını değiştirmeden, Harita üstü ayrı işaret olarak Geçilmez Kayalık eklendi.
- 30 kareye kadar 1; 35+ karede 2 Geçilmez Kayalık kullanımı kilitlendi.
- Geçilmez Kayalık son Liman/Ufuk hattında yasaklandı ve kurulumda başlangıç-Ada-Liman erişimi zorunlu tutuldu.
- Yalnız Geçilmez Kayalık kaynaklı tam çıkmazda bir karelik, gün tüketen acil geri dönüş eklendi.
- Geri dönülen çözülmüş kartın olayının tekrar çalışmaması ve bilinen çıkmaz kola alternatif varken yeniden girilememesi kesinleştirildi.
- Girdap/ek hareket Kayalık yüzünden hedef bulamazsa hareket kısmının boşa düşmesi, aynı gün geri dönüş başlamaması kesinleştirildi.

## 22. Simülasyon notu

v2.2 için Geçilmez Kayalık mekanizmasına yönelik hedefli teknik/duyarlılık testi yapılmıştır; bu, oyunun bütün sosyal ve stratejik katmanlarını kapsayan tam denge simülasyonu değildir. Konuşma, blöf, güven, gerçek Kaptan becerisi, masa eğlencesi ve insan oylama davranışı yalnız insan testleriyle değerlendirilebilir.
