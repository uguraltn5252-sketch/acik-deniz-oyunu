# FOULWAKE 7 BACK BRIEFS v2.7

Status: BRIEF — arka yüz sanat fikri ve risk analizi; final görsel/render/PDF değildir.  
Source branch: work/v2.7-art-direction  
Chief Editor source: v2.7-design@29da7e35c4d940e1836bc3852a67d0cc7a5904a1  
Baseline: v2.6 STABLE / LOCKED  
Decision gate: PROJECT OWNER + CHIEF EDITOR  
Production owner after approval: Görsel Tasarım

## 1. Bağlayıcı topoloji

| Binary | Adet | Ön yüz kapsamı |
|---|---:|---|
| BACK_CHARACTER | 20 | KAR-01…KAR-20 |
| BACK_POWER | 31 | 30 Güç + ERZ-01 Çürümüş Erzak |
| BACK_LOYALTY | 15 | 10 Tayfa + 5 Hain |
| BACK_SEA_ROCK | 42 | 30 Açık Deniz + 12 Kayalık |
| BACK_ISLAND | 6 | 6 Ada |
| BACK_LIGHTHOUSE | 4 | 4 Deniz Feneri |
| BACK_SUPPORT | 3 | 2 Liman + Kaptan Makamı |
| Toplam | 121 | Yedi exact binary |

Topoloji notu: v2.6 STABLE / LOCKED, Kayalık arkasını Açık Denizden ayrı tutar. Exact v2.7 iş emri yedi binary içinde BACK_SEA_ROCK ortak arkasını ister. Bu brief v2.6’yı değiştirmez ve v2.7’yi kilitlemez; yeni ortak arka yüz yalnız DRAFT öneridir ve proje sahibi + Baş Editör dispozisyonu gerektirir.

## 2. Bütün arka yüzler için ortak kurallar

### 2.1 İçerik

- Okunabilir yazı, logo, oyun adı, kart tür etiketi, sayı, harf, yön oku, pusula harfi, arma ve slogan yok.
- Ön yüzün kart adı, karakteri, nesnesi, olayı, ahlak durumu veya mekaniği arka yüzde görünmez.
- Aile içindeki bütün fiziksel kopyalar bit-bit exact aynı master dosyayı kullanır; kart başına farklı eskitme, leke veya renk varyantı yok.
- Kâğıt, katran, tuz, kenevir, oksit ve eski baskı çizgisi ön yüzlerle aynı dünyadadır. Arka yüz ayrı bir “marka logosu” katmanı değildir.
- Ekli KAPTAN STYLE_ONLY referansından yüz, şapka, kuş, gemi, çerçeve, kompozisyon, nesne veya çizgi alınmaz.
- Reddedilmiş e91581 arka yüzleri sanat girdisi değildir; yalnız teknik tarih olarak dışlanır.

### 2.2 Exact 180 derece güvenliği

Arka yüz “yaklaşık simetrik” olmayacaktır. Görsel Tasarım master üretiminde:

1. Ana motif yarım dönüş eşli çiftler veya merkezi 180 derece invariant geometriyle kurulur.
2. El çizgisi sıcaklığı korunur; ancak bir yarıdaki çizgi grubu 180 derece eşine bağlanır.
3. Eskitme, kâğıt lifi, çizik, pas, kurum ve baskı kayması en son rastgele filtreyle eklenmez. Bunlar da dönüş eşli master içinde yer alır.
4. Flatten edilmiş master 180 derece döndürülüp aynı piksel ızgarasına oturtulduğunda trim + bleed alanında fark sıfır olmalıdır; renk yönetiminin yuvarlama farkları hariç tutulmaz, aynı dosya test edilir.
5. Kare ve dikey kartlar için ayrı fiziksel oran uygulanabilir; fakat ilgili binary içindeki bütün kartlar aynı ratio/master dosyayı paylaşır.
6. Üst/altı ele veren tekil lamba, damla, gölge, ufuk, ip ucu, insan başı veya açık sayfa yoktur.
7. Motif 90 derece simetrik olmak zorunda değildir; 180 derece exact güvenlik zorunludur.

### 2.3 Kesim, kenar ve parlaklık

- Ana motif trim kenarından en az 3 mm, küçük/ayırt edici detay en az 4 mm içeride tutulur; gerçek baskı şablonunun bleed/safe değerleri daha büyükse şablon kazanır.
- Dört köşenin ve karşılıklı kenarların ortalama açık/koyu değeri dengelenir. Bir kenardaki tek koyu leke kart yönünü veya belirli kopyayı ele veremez.
- İnce çift çerçeve varsa kesim sapmasını “yamuk kart” gibi büyütmemeli; dıştan içe geniş, organik ama exact eşli değer bandı tercih edilir.
- Spot UV, metalik folyo, yönlü vernik, kabartma veya yalnız bir motifte parlak kaplama yok. Mat yüzey bütün binarylerde aynı baskı süreciyle yürür.
- Lif veya tarama baskı yönü üst/alt ayrımı üretmemeli. Vernik/laminasyon makine yönü test kartlarında karıştırılarak kör kontrol edilir.
- Bir kartın arkasındaki üretim kiri, çizik veya ton farkı tanınabilir hale gelirse deste reddedilir; “eski baskı” tasarlanmış master dokusudur, kontrolsüz kusur değildir.

### 2.4 Bilgi sızıntısı testleri

Her binary için Görsel Tasarım daha sonra şu kanıtları üretmelidir; bu belge kanıt dosyalarını üretmez:

- Düz/ters karışık 20 kart kör masa testi: yön tahmini şanstan anlamlı biçimde sapmamalı.
- Aile içi kopya testi: tek kart tonu/kenarı/lekesiyle tanınmamalı.
- BACK_LOYALTY: Tayfa/Hain tahmini yalnız arka yüze bakarak yapılamamalı.
- BACK_SEA_ROCK: Açık Deniz/Kayalık tahmini yalnız arka yüze bakarak yapılamamalı.
- BACK_POWER: ERZ-01 diğer 30 Güçten ayırt edilememeli.
- 180 derece rotate/difference testi: flattened master exact eşleşmeli.
- Küçük baskı testi: mikro tarama moiré veya koyu çamur oluşturmamalı.
- Parlaklık testi: eğik ışıkta aile/kopya/yön sızdıran vernik farkı olmamalı.

## 3. BACK_CHARACTER — 20

### Sanat fikri: “İşin bıraktığı çift iz”

Merkezde insan yüzü veya portresi yoktur. İki karşıt yönden gelen, birbirinin 180 derece eşi olan iki geniş kenevir halat kıvrımı; aralarında dört farklı meslek malzemesinin yalnız dokusal izini taşıyan kapalı bir bez oval oluşturur: kurum, tuz, balmumu ve ahşap sürtünmesi. Nesnelerin kendisi resmedilmez; izler karakterlerin kişiden önce iş tarafından biçimlendiğini söyler.

Motif uzaktan merkezi koyu bir oval ve iki açık halat S’i olarak okunur. Yakından bezde farklı el basıncı/aşınma izleri vardır; gerçek el silueti veya parmak izi yoktur. Böylece belirli yaş, cinsiyet, ten, rol ya da karakter kimliği sızmaz.

### Çizgi ve palet

- Halatta dönüşlü çift çizgi; bezde seyrek çapraz; kurum alanında kontrollü koyu.
- Kâğıt/kemik, tar, solmuş indigo ve çok küçük pas kahvesi.
- Hardal/kırmızı vurgu yok; belirli rol/rütbe hissi doğurmasın.
- İnsan yüzü, şapka, silah, kuş, gemi veya meslek ikonu yok.

### 180 derece yapısı

İki halat kıvrımı aynı vektör/çizgi grubunun 180 derece eşidir. Bez ovalin üst ve alt dikişi aynı yarım dönüş çiftidir. Dört aşınma izi iki eşli çift halinde yerleştirilir; tekil leke yoktur.

### Risk analizi

- Yüz benzeri pareidolia: oval + iki koyu nokta göz gibi görünmemeli.
- Sadakat arkasına benzer “gizli kişi” hissi: bez açık ve iş malzemeli; mühür/kapalı zarf kullanılmaz.
- Karakter rol sızıntısı: kılıç, dümen, iğne, anahtar gibi tanınır nesne yok.
- Üst/alt sızıntısı: halat liflerinin uçları kapanır; tek serbest uç yok.
- Kesim: dış halat hiçbir köşeye diğerinden daha yakın değildir.

### Kabul ölçütü

Kartı gören “insan emeği / karakter ailesi” hissi alabilir; fakat herhangi bir Karakteri, rolü, cinsiyeti veya yönü tahmin edemez.

## 4. BACK_POWER — 31

### Sanat fikri: “Kapalı donanım rulosu”

Merkezde iki uçtan karşılıklı sarılmış, exact 180 güvenli yağlı bez donanım rulosu bulunur. Rulo kapalıdır; içindeki Güç veya erzak görünmez. İki simetrik kenevir bağ, ortada dört kollu ama logo gibi olmayan basit düğüm baskısı kurar. Çevredeki mat metal sürtünme izleri araç ihtimalini taşır, belirli bir karta işaret etmez.

ERZ-01 bu arka yüzü paylaşır. Bu nedenle yiyecek, fıçı, küf, peksimet, koku çizgisi, böcek veya yeşil leke kesinlikle yoktur. Rulo “her türlü taşınabilir gemi kaynağı” olarak nötr kalır.

### Çizgi ve palet

- Yağlı bezde geniş açık alan + kat yerlerinde kısa çapraz.
- Bağlarda kenevir lif çizgisi, metal sürtünmede pas kahvesi.
- Tar, ıslak meşe, kemik, soluk indigo; küçük pas vurgu.
- Alev, altın, parıltı, silah ucu veya kart ikonu yok.

### 180 derece yapısı

Rulonun iki ucu aynı çizgi grubunun 180 derece eşidir. Düğümler çift; ortadaki boşluk dönüş merkezidir. Bezdeki bütün yama ve leke eşli çiftlenir. Bir ucun daha sıkı, daha koyu veya daha aşınmış görünmesine izin verilmez.

### Risk analizi

- ERZ sızıntısı: renk/lekede küf-zeytin kullanılmaz.
- Belirli Güç sızıntısı: kanca, para, kupa, fener, şapka, peksimet veya zıpkın görülmez.
- SUPPORT ile karışma: bürokratik mühür, kayıt tahtası ve anahtar yok.
- Parlaklık: metal sürtünme noktaları spot vernik gibi parlamaz.
- Kesim: rulo ucu trim alanına girip yön işareti üretmez.

### Kabul ölçütü

Arka yüz “kapalı, taşınabilir kaynak” hissi vermeli; 31 kart arasında ERZ-01 dahil hiçbir ön kimlik veya yön tahmin edilememelidir.

## 5. BACK_LOYALTY — 15

### Sanat fikri: “İki yüzü de kapalı bağ”

Merkezde iki karşıt yönden katlanmış tek koyu keten parça ve onu eşit baskıyla tutan çift düğüm vardır. Düğümün ortası açık değil, mat ve nötrdür; iyi/kötü, aydınlık/karanlık, kırmızı/siyah gibi ikili ahlak kodu kurulmaz. Kumaşın altında insan, silah, mektup veya simge görünmez.

Görselin ana duygusu kapalı niyet ve taşınan yük olmalıdır. Tayfa ile Hain aynı exact masterı kullanır; kart başına eskitme/ton değişimi yoktur.

### Çizgi ve palet

- Keten katlarında formu izleyen seyrek çapraz; düğümde sık kenevir çizgisi.
- Koyu indigo, tar, kemik ve çok az soğuk gri.
- Kırmızı/yeşil, beyaz/siyah yarılma, altın mühür ve kan lekesi yok.
- İnsan gözü, maske, hançer, el sıkışma veya zincir ikonu yok.

### 180 derece yapısı

Kat izleri, düğüm ve dört köşe aşınması yarım dönüş eşli. Merkezde bir “üst kapak” veya açılma yönü bulunmaz. Keten dokusunun atkı yönü dahi iki yönde dengelenir.

### Risk analizi

- En kritik risk Tayfa/Hain sızıntısıdır: hiçbir baskı varyantı, leke, renk veya koyuluk alt gruplara atanamaz.
- Yüz pareidoliası: iki düğüm göz, kat çizgisi ağız görünmemeli.
- “Hain daha koyu” üretim yanlılığı: baskı lotları karıştırılmalı, aynı dosya/hash kullanılmalı.
- POWER ile karışma: rulo/alet hissi değil kapalı niyet hissi; metal/pas minimum.
- Kesim/parlaklık: düğüm gölgesi iki yönde exact eşli; yönlü kumaş parlaklığı yok.

### Kabul ölçütü

Arka yüze bakarak Tayfa/Hain tahmin doğruluğu şans düzeyini aşmamalı; kart düz veya tersken açılma yönü okunmamalıdır.

## 6. BACK_SEA_ROCK — 42

### Sanat fikri: “Keşfedilmemiş su yüzeyi”

Ne belirgin dalga ne belirgin kaya: merkezde dört yönden birbirine giren düşük kontrastlı gelgit çizgileri, aralarında tuzla kabarmış koyu bir su lekesi. Kıyı çizgisi, ada, kayalık sivri, gemi, fener, pusula ve ufuk yoktur. Doku “henüz açılmamış coğrafya”yı taşır; Açık Deniz veya Kayalık sonucunu önceden söylemez.

Su çizgileri tek yönde akan rota gibi değil, iki 180 derece eşli karşı akış halinde kurulur. Ortadaki koyu leke kaya silueti veya ada konturu gibi okunmayacak düzensiz fakat dönüş güvenli bir dörtlü formdur.

### Çizgi ve palet

- İnce fakat baskıda kapanmayacak yatay/kavisli akıntı çizgileri.
- Deniz indigosu, tuz mavi-grisi, tar ve kemik rezerv.
- Pas/hardal/kırmızı yok; kıyı veya insan yapısı çağrıştırmasın.
- Gradient su, fotoğraf dalga köpüğü, harita ızgarası, yön oku veya koordinat yok.

### 180 derece yapısı

Akıntı çizgilerinin her grubu dönüş eşine sahiptir; tek “yukarı akış” yok. Merkez lekesi iki döndürülmüş alt grubun birleşimidir. Dış çerçevede dört karşılıklı kenar aynı ortalama değerdedir.

### Risk analizi

- En kritik risk Açık Deniz/Kayalık sızıntısıdır: keskin taş konturu, köpüren sığlık veya açık ufuk kullanılamaz.
- v2.6 ayrımının yanlışlıkla kilitlenmiş gibi sunulması: bu arka yüz DRAFT’tır; ayrı v2.6 dosyaları değiştirilmez.
- Kare kartta 90 derece döndürme davranışı: zorunlu olan 180’dir, fakat 90’da da bariz yön oku oluşmaması tercih edilir.
- Baskı banding’i: geniş koyu su alanı mat baskıda lot farkı göstermemeli.
- Çerçeve kesimi: tek bir koyu köşe Açık Deniz/Kayalık kopyasını tanıtmamalı.

### Kabul ölçütü

42 kapalı kart içinde hiçbir kartın Açık Deniz mi Kayalık mı olduğu arka yüzden tahmin edilemez; motif düz/ters aynı, henüz keşfedilmemiş deniz hissinde kalır.

## 7. BACK_ISLAND — 6

### Sanat fikri: “Dört kollu gelgit halkası”

Üstten görülen belirli bir ada silueti yerine, merkezde düz ve adsız küçük bir kara lekesini dört yönden eşit aşındıran gelgit halkaları. Kara lekesi tam bir harita şekli değildir; kıyı yaşamı, bina, palmiye, liman veya ürün göstermez. Çevrede iki karşıt kenevir bağ izi, kartın masa üzerindeki fiziksel obje hissini ön yüz dünyasına bağlar.

### Çizgi ve palet

- Kıyıda kısa kırık çizgi, gelgitte geniş aralıklı halkalar.
- Taş zeytin-grisi, ıslak meşe kahvesi, indigo, kemik.
- Tropik yeşil, parlak kum, turkuaz, kırmızı bayrak yok.
- Ada üzerinde ikon, bina, insan, ağaç veya hazine işareti yok.

### 180 derece yapısı

Kara lekesi iki yarım dönüş eşli formdan kurulur; gelgit halkaları tam merkezi. İki bağ izi aynı çizginin 180 derece eşi. Tek burun, koy veya kıyı açıklığı yön göstermez.

### Risk analizi

- Belirli Ada sızıntısı: gümrük kulübesi, karakol, tersane, korsan kampı, erzak veya insan yok.
- SEA_ROCK ile karışma: merkezde kara hissi var, fakat belirli şekil yok; palet biraz daha meşe/zeytin.
- Yön sızıntısı: uzun ada formu üst/alt göstermemeli; ana kütle merkezi ve dengeli.
- Kesim: dış gelgit halkaları köşede kesilse dahi karşı köşe aynı davranır.
- Parlaklık: “su” halkalarında spot parlaklık yok.

### Kabul ölçütü

Aile Ada olarak hissedilir; altı Ada kartından hangisi olduğu ve kart yönü öğrenilemez.

## 8. BACK_LIGHTHOUSE — 4

### Sanat fikri: “Fener odasının üstten halkası”

Dikey kule veya tek yönlü ışın arka yüzde yön sızdırır. Bunun yerine fener odasının tam üstten, radyal ama logo olmayan yapısal halkası kullanılır: merkezde küçük mat yağ haznesi; çevrede dört eşit panjur/metal reflektör parçası ve taş duvar halkası. Işık huzmesi yoktur; taramanın azaldığı dört eşit açıklık yalnız malzeme düzenini verir.

### Çizgi ve palet

- Metalde kısa paralel, taş halkada düzensiz kırık, kurumda mat çapraz.
- Kurum, taş grisi, kemik ve çok küçük donuk hardal.
- Elektrik sarısı, Fresnel prizması, parlayan halo, kule silueti yok.
- Logo/arma gibi kusursuz geometrik rozet görünümü kırık el çizgisiyle önlenir; exact dönüş yine master yapısından gelir.

### 180 derece yapısı

Dört panjurdan karşılıklı ikiler exact yarım dönüş eşidir; yağ haznesi merkezde. Kurum ve aşınma iki eşli çift halinde. “Alevin üstü” yok; alev doğrudan çizilmez.

### Risk analizi

- Dikey yön sızıntısı: kule, merdiven, ışın ve ufuk yasak.
- POWER’daki Fırtına Feneri ile karışma: elde taşınır fener değil mimari halka; dış çerçeve taş.
- SUPPORT ile kurumsal rozet benzerliği: merkezde mühür/anahtar yok, ışık mekanizması malzemesi belirgin.
- Anakronizm: Fresnel lensi, elektrik ampulü ve modern beacon yok.
- Parlaklık: hardal alan vernikle parlamaz; baskı lotunda dört kart eşit.

### Kabul ölçütü

Dört kart fener ailesi olarak okunur fakat belirli kule, yön, açık/kapalı ışık veya ön kart kimliği sızdırmaz.

## 9. BACK_SUPPORT — 3

### Sanat fikri: “İki rıhtım, bir boş merkez”

İki karşıt yönde exact eşli taş rıhtım babası ve aralarında merkezi boş bırakan tek kenevir palamar halkası. Merkezde kişi, sandalye, liman adı, anahtar veya mühür yoktur. Bu boşluk Kalkış, Varış ve Kaptan Makamı için ortak olan “işlevin insan/yer değişse de kalması” fikrini taşır.

Rıhtım babaları belirli bir limanı anlatmaz; taş/ahşap karışımı nötr gemi altyapısıdır. Palamar iki yönü bağlar ama ok veya rota değildir.

### Çizgi ve palet

- Taşta kısa kırık, halatta çift sarmal, merkezde kâğıt rezervi.
- Islak meşe, taş grisi, indigo, tar; küçük pas bağlantı.
- Liman manzarası, şehir, gemi, Kaptan şapkası, sandalye, arma, harita veya yazı yok.

### 180 derece yapısı

İki baba ve palamar halkasının üst/alt yarısı aynı çizgi grubunun 180 derece eşidir. Halatın serbest ucu yoktur. Merkez boşluk tam dönüşte değişmez; taş aşınmaları eşli çiftlenir.

### Risk analizi

- Üç destek kartından birini ele verme: Kalkış için koyu, Varış için açık, Kaptan için anahtar/şapka varyantı kesinlikle yok.
- CHARACTER ile insan emeği izine, POWER ile donanım rulosuna benzerlik: merkez bez/alet değil açık kurumsal boşluk.
- “Logo” riski: palamar halkası kusursuz amblem gibi çizilmez; malzeme düzensizliği korunur.
- Kesim: iki baba karşı kenarlara fazla yaklaşmaz; birinin kesilmesi yön sızıntısı yaratmaz.
- Parlaklık: ıslak rıhtım efekti gradient/vernik değil, çizgi/değerle kurulur.

### Kabul ölçütü

Üç kart aynı kurumsal destek ailesi olarak hissedilir; Kalkış, Varış veya Kaptan Makamı ayrımı ve yönü arka yüzden öğrenilemez.

## 10. Binaryler arası çakışma kontrolü

| Binary | Uzakta büyük biçim | Yakında maddi imza | Kaçınacağı komşu |
|---|---|---|---|
| CHARACTER | Bez oval + çift halat S | İş aşınması izleri | LOYALTY’nin kapalı düğümü |
| POWER | İki uçtan kapalı rulo | Yağlı bez + pas | SUPPORT’ın açık merkezi |
| LOYALTY | Kapalı koyu keten + çift bağ | Nötr düğüm | CHARACTER’ın iş izleri |
| SEA_ROCK | Merkezi karşı akıntı alanı | Tuz/su çizgisi | ISLAND’ın kara merkezi |
| ISLAND | Kara lekesi + gelgit halkası | Kıyı kırığı | SEA_ROCK’ın karasız yüzeyi |
| LIGHTHOUSE | Radyal taş/metal halka | Kurum + panjur | Logo/rozet görünümü |
| SUPPORT | İki rıhtım babası + boş merkez | Taş + palamar | POWER’ın kapalı rulosu |

Yedi arka yüz aynı mat kâğıt, ana mürekkep ve el çizgisi ailesini paylaşır. Ayrım yalnız motif ve malzeme oranından gelir; her binary için farklı doygun “renk kodu” yapılmaz. Renk körlüğü ve mat baskı koşulunda aileler büyük biçimle ayrılmalıdır.

## 11. Üretim ve hash disiplini

Onaydan sonra Görsel Tasarım her binary için tek master üretir ve:

- dosya adını binary kimliğiyle eşler;
- her fiziksel kopyayı aynı masterdan türetir;
- flattened dosya hashini manifestte bir kez kaydeder;
- 180 rotate/difference kanıtını saklar;
- baskı lotu, kâğıt ve vernik bilgisini ayrı teknik raporda tutar;
- hiçbir karta kart-başına random distress eklemez;
- test baskısı başarısızsa sanat dosyasını revize eder, kart kopyalarını ayrı ayrı “düzeltmez”.

Bu iş emri dosya formatı, DPI, bleed veya ICC profilini kilitlemez; bunlar Görsel Tasarımın teknik üretim ve Baş Editör entegrasyon alanıdır. Sanat fikri ve sızıntı riskleri bağlayıcı brief olarak sunulur.

## 12. Dispozisyon

ART_DIRECTION_STAGE: BRIEF  
CREATIVE_VERDICT: SEVEN_BACK_BRIEFS_READY / PENDING_PROJECT_OWNER_AND_CHIEF_EDITOR_REVIEW  
PROJECT_OWNER_DECISION_REQUIRED: YES  
FINAL_VISUAL_AND_PDF_OWNER: Görsel Tasarım  
INTEGRATION_AND_DISPOSITION: Baş Editör  
LOCK_REQUESTED: NO
