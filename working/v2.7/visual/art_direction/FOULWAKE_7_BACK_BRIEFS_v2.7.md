# FOULWAKE 7 BACK BRIEFS v2.7

Status: OWNER RESET / THREE BACKS REWORK_REQUIRED / OTHER FOUR HOLD  
Current authority: governance/CURRENT_STAGE.json  
Rejected input: work/v2.7-visual@23c062f6de06c32eab224b3440c8474725d4fe9e  
Project Owner: BACK_SEA_ROCK matte; BACK_ISLAND FULL REDRAW; BACK_LIGHTHOUSE larger and no forced long ridge  
Framing gate: independent Art Direction review required  
Visual production authorized: NO  
Source branch: work/v2.7-art-direction  
Baseline: v2.6 STABLE / LOCKED  
Decision gate: PROJECT OWNER + CHIEF EDITOR  
Production owner after a new exact order: Görsel Tasarım  
Target scope: three rejected map backs; CHARACTER / POWER / LOYALTY / SUPPORT remain HOLD, not owner-accepted.

## 1. Bağlayıcı topoloji

| Binary | Adet | Ön yüz kapsamı |
|---|---:|---|
| BACK_CHARACTER | 20 | KAR-01…KAR-20 |
| BACK_POWER | 31 | 30 Güç + ERZ-01 Çürümüş Erzak |
| BACK_LOYALTY | 15 | 10 Tayfa + 5 Hain |
| BACK_SEA_ROCK | 42 | 30 Açık Deniz + 12 Kayalık |
| BACK_ISLAND | 6 | 6 Ada |
| BACK_LIGHTHOUSE | 4 | 4 Deniz Feneri |
| BACK_SUPPORT | 3 | 2 Liman + KAPTAN |
| Toplam | 121 | Yedi exact binary |

Topoloji notu: v2.6 STABLE / LOCKED, Kayalık arkasını Açık Denizden ayrı tutar. Exact v2.7 iş emri yedi binary içinde BACK_SEA_ROCK ortak arkasını ister. Bu brief v2.6’yı değiştirmez ve v2.7’yi kilitlemez; yeni ortak arka yüz yalnız DRAFT öneridir ve proje sahibi + Baş Editör dispozisyonu gerektirir.

## 2. Bütün arka yüzler için ortak kurallar

### 2.1 Kapalı kartların sanatsal görevi

Arka yüzler yedi ayrı logo değildir. Masada yüzü kapalı duran kart, FOULWAKE’ın temel hâlini taşır: **bilgi vardır, fakat henüz kimse ona sahip değildir.** Bu nedenle arka yüzün güzelliği “gizemli simge”den değil, tutulmuş ve kullanılmış bir nesnenin sessiz ağırlığından doğar.

- Aile farkı kart-sırtı logosuyla kurulmaz. Harita ailelerinde BACK_ISLAND genel kara unsuru ve BACK_LIGHTHOUSE genel dönem feneriyle açıkça görünür; bu öğeler ortak denizin doğal coğrafyasıdır. Diğer ailelerde emek izi, kapalı kaynak, kapalı niyet ve kamusal düzen maddi hâlle kurulur.
- Motifler antik mühür, tarikat logosu, oyun amblemi veya koleksiyon serisi rozeti gibi davranmaz.
- Eski baskı dili rastgele kir değil; aynı masterda, aynı 180 derece düzen içinde tasarlanmış kullanım hafızasıdır.
- Kapalı deniz alanı “tehlike” diye bağırmaz; oyuncuyu seçim öncesi sessizliğe sokar.
- Ön yüzlerin özel adları, çalışma lore’u ve siyah balmumu ihtimali arka yüzlere taşınmaz. Adlar değişse bile aile işlevi ve masa güvenliği aynen kalır.
- Arka yüz sanatçısı güvenlik yüzünden yalnız teknisyen değildir. Çizgi ritmi, yüzeyin nefesi ve maddi ağırlık onun yorumudur; ancak bu yorum exact master, 180 derece ve bilgi sızıntısı sınırlarını aşamaz.

### 2.2 İçerik

- Okunabilir yazı, logo, oyun adı, kart tür etiketi, sayı, harf, yön oku, pusula harfi, arma ve slogan yok.
- Ön yüzün exact kart adı, özel karakteri, özel nesnesi, olayı, sonucu, ahlak durumu veya mekaniği arka yüzde görünmez. Proje sahibi kararı yalnız genel ada ve genel dönem feneriyle aile bilgisini görünür kılar; belirli ön karta ait hiçbir ayrıntıya izin vermez.
- Siyah balmumu ve Siyah Mühür hiçbir arka yüzde motif, logo, renk kodu veya kanıt izi değildir; özellikle BACK_LOYALTY’de Tayfa/Hain sızıntısı yaratacak koyu varyant bulunmaz.
- Aile içindeki bütün fiziksel kopyalar bit-bit exact aynı master dosyayı kullanır; kart başına farklı eskitme, leke veya renk varyantı yok.
- v2.7 anlatısal görsel omurga arka yüzlere taşınmaz: tiryak sandığı, Gusto eşyası, Siyah Mühür ve Veyr izi binary tasarımına girmez.
- Kâğıt, katran, tuz, kenevir, oksit ve eski baskı çizgisi ön yüzlerle aynı dünyadadır. Arka yüz ayrı bir “marka logosu” katmanı değildir.
- Yüklenen KAPTAN kartı SET-KP-01 için görsel/copy kaynağı ve deste için
  mürekkep–gravür–kâğıt–mat palet dilidir. KAPTAN figürü arka yüzlere
  kopyalanmaz; gemi ve martı zorunlu motif değildir.
- Reddedilmiş e91581 arka yüzleri sanat girdisi değildir; yalnız teknik tarih olarak dışlanır.

### 2.3 Exact 180 derece güvenliği

Arka yüz “yaklaşık simetrik” olmayacaktır. Görsel Tasarım master üretiminde:

1. Ana motif yarım dönüş eşli çiftler veya merkezi 180 derece invariant geometriyle kurulur.
2. El çizgisi sıcaklığı korunur; ancak bir yarıdaki çizgi grubu 180 derece eşine bağlanır.
3. Eskitme, kâğıt lifi, çizik, pas, kurum ve baskı kayması en son rastgele filtreyle eklenmez. Bunlar da dönüş eşli master içinde yer alır.
4. Flatten edilmiş master 180 derece döndürülüp aynı piksel ızgarasına oturtulduğunda trim + bleed alanında fark sıfır olmalıdır; renk yönetiminin yuvarlama farkları hariç tutulmaz, aynı dosya test edilir.
5. Kare ve dikey kartlar için ayrı fiziksel oran uygulanabilir; fakat ilgili binary içindeki bütün kartlar aynı ratio/master dosyayı paylaşır.
6. Üst/altı ele veren tekil lamba, damla, gölge, ufuk, ip ucu, insan başı veya açık sayfa yoktur.
7. Motif 90 derece simetrik olmak zorunda değildir; 180 derece exact güvenlik zorunludur.

### 2.4 Kesim, kenar ve parlaklık

- Ana motif trim kenarından en az 3 mm, küçük/ayırt edici detay en az 4 mm içeride tutulur; gerçek baskı şablonunun bleed/safe değerleri daha büyükse şablon kazanır.
- Dört köşenin ve karşılıklı kenarların ortalama açık/koyu değeri dengelenir. Bir kenardaki tek koyu leke kart yönünü veya belirli kopyayı ele veremez.
- İnce çift çerçeve varsa kesim sapmasını “yamuk kart” gibi büyütmemeli; dıştan içe geniş, organik ama exact eşli değer bandı tercih edilir.
- Spot UV, metalik folyo, yönlü vernik, kabartma veya yalnız bir motifte parlak kaplama yok. Mat yüzey bütün binarylerde aynı baskı süreciyle yürür.
- Lif veya tarama baskı yönü üst/alt ayrımı üretmemeli. Vernik/laminasyon makine yönü test kartlarında karıştırılarak kör kontrol edilir.
- Bir kartın arkasındaki üretim kiri, çizik veya ton farkı tanınabilir hale gelirse deste reddedilir; “eski baskı” tasarlanmış master dokusudur, kontrolsüz kusur değildir.

### 2.5 Bilgi sızıntısı testleri

Her binary için Görsel Tasarım daha sonra şu kanıtları üretmelidir; bu belge kanıt dosyalarını üretmez:

- Düz/ters karışık 20 kart kör masa testi: yön tahmini şanstan anlamlı biçimde sapmamalı.
- Aile içi kopya testi: tek kart tonu/kenarı/lekesiyle tanınmamalı.
- BACK_LOYALTY: Tayfa/Hain tahmini yalnız arka yüze bakarak yapılamamalı.
- BACK_SEA_ROCK: Açık Deniz/Kayalık tahmini yalnız arka yüze bakarak yapılamamalı.
- BACK_POWER: ERZ-01 diğer 30 Güçten ayırt edilememeli.
- 180 derece rotate/difference testi: flattened master exact eşleşmeli.
- Küçük baskı testi: mikro tarama moiré veya koyu çamur oluşturmamalı.
- Parlaklık testi: eğik ışıkta aile/kopya/yön sızdıran vernik farkı olmamalı.

## 2A. COMMON_MAP_BACK_VISUAL_SYSTEM

### Referans sınıflandırması

Ekli masa örneği MAP_TABLE_REFERENCE: TABLE_READ_ONLY / COMPOSITION_PRINCIPLE_ONLY olarak sınıflandırılır. Ondan yalnız “kapalı kartlar birlikte tek bir keşfedilmemiş deniz/oyun alanı okur” ilkesi alınır. Örneğin 5×5 kart sayısı, sabit grid, satır/sütun, dalga çizgileri, renkleri, çerçevesi, kart yüzleri ve yerleşimi kopyalanmaz veya üretim şartı yapılmaz. KAPTAN, SET-KP-01 görsel/copy kaynağı ve deste sanat dili anahtarıdır;
harita-masası referansı KAPTANın, KAPTAN da harita-masası referansının yetkisini
genişletmez.

### Bağlayıcı aile görünürlüğü ve bilgi sınırı

| Binary | Oyuncunun arka yüzden bilebileceği | Oyuncunun arka yüzden bilemeyeceği |
|---|---|---|
| BACK_SEA_ROCK | Kartın 42 kartlık Açık Deniz/Kayalık ortak ailesinde olduğu | Açık Deniz mi Kayalık mı olduğu; exact ön kimlik, olay veya sonuç |
| BACK_ISLAND | Kartın Ada ailesinde olduğu; genel ada açıkça görünür | Altı ön adadan hangisi olduğu; özel kıyı, yerleşim, ürün, kişi veya sonuç |
| BACK_LIGHTHOUSE | Kartın Deniz Feneri ailesinde olduğu; genel fener açıkça görünür | Dört ön fenerden hangisi olduğu; özel mimari, ışık davranışı, hasar, paket, kıyı veya sonuç |

Aile görünürlüğü bu projede sızıntı değildir. Aile bilgisini alt tür, exact ön kart, sonuç, güven/tehdit veya kart yönü tahminine dönüştüren her ayrıntı sızıntıdır. Kart adı; effect veya flavor içeriği; olumlu/olumsuz sonuç; ön yüzdeki özel mekân, karakter, nesne veya sahne kesinlikle gösterilemez.

### Birincil kompozisyon birimi: değişken harita

Sanatın birincil kompozisyon birimi tek kart veya sabit bir 5×5 değildir; oyun sırasında kurallara uygun biçimde oluşan değişken harita alanıdır.

- Sistem belirli grid, satır, sütun, kart sayısı veya dizilime bağlanmaz.
- Kompakt, genişleyen, uzayan ve komşuluğu değişen geçerli düzenlerde aynı deniz hissini taşır.
- Üç aile normal masa mesafesinde seçilebilir; fakat deniz, ada ve fener ayrı marka fayanslarına dönüşmez.
- Literal bir dalga çizgisinin komşu kartta devam etmesi gerekmez. Birlik; ortak ölçek, hava, değer, kâğıt ve kenar ritmiyle kurulur.
- Görsel düzen hiçbir yeni kurulum, yön, rota, komşuluk veya harita mekaniği üretmez.

### Ortak deniz, çizgi ve mat malzeme grameri

- Üç aile aynı ana çizgi kalınlığı, üçlü mikro-ölçek merdiveni ve ortalama değer zarfını kullanır.
- Deniz, farklı uzunluk ve aralıklardaki kısa/kırık su çizgileri, seyrek kısa çapraz tarama ve kemik kâğıt rezerviyle kurulur.
- Hacim boya gradyanı, airbrush, glow veya dijital noise ile değil; çizgi aralığı, kesinti, kontur basıncı ve kâğıt rezerviyle kurulur.
- Palet omurgası kurum indigosu, tuz mavi-grisi, tar grisi ve kemik kâğıttır. Ada toprağı ve fener taşı bu zarfın içinde, düşük doygunluklu küçük değer farklarıyla ayrılır.
- Büyük S, dört kollu akıntı, koyu göbek, imza dalga, renk rozeti veya kolay ezberlenen su lekesi yoktur.
- Deniz her üç ailede trim/bleed’e kadar gider; ada veya fener çevresinde başka bir zemin, halo ya da grafik plaka oluşmaz.

### Ortak kenar ritmi ve yerleşim bağımsızlığı

- Trim çevresindeki kenar zarfı üç ailede aynı dalga ölçeği, ortalama yoğunluk ve değer aralığında kalır.
- Uzun, yüksek kontrastlı çizgi trimde kesilip sahte rota veya “yanlış komşu” hissi üretmez.
- Rastgele komşulukta literal çizgi uçları değil, istatistiksel dikiş aranır: aynı çizgi ölçüsü, hava, matlık ve kâğıt nefesi.
- Teknik keyline gerekiyorsa üç ailede exact aynı, ince, süssüz ve dalga çizgisinden daha düşük kontrastlıdır.
- Kara veya kule unsuru kenara taşarak belirli komşu gerektirmez; deniz zarfı dört kenarın tamamında ortak sistemi sürdürür.
- Kartların rastgele 180 derece çevrilmesi kenar değerini, dalga ritmini veya aile okumasını değiştirmez.

### Aile görünürlüğünü ikonlaştırmadan kurma

**BACK_SEA_ROCK:** Ortak denizin nötr baseline’ıdır. Hiçbir kaya, sığlık, resif, köpüren kırıcı dalga veya jeolojik renk bulunmaz. Aile bilgisi yalnız genel deniz yüzeyidir; Açık Deniz/Kayalık alt türü tamamen kördür.

**BACK_ISLAND:** Aynı deniz içinde dik kuşbakışında tek, alçak ve anonim bir ada görülür. Ada; karşıt iki burunla uzayan, kusursuz oval olmayan doğal bir kara kütlesidir. Deniz halkası, kontur madalyonu, renk diski veya etiket alanı yoktur; deniz dört kenara kadar sürer. Anonim taş, düşük çalı ve aşınmış toprak dışında yerleşim, gümrük, kamp, tersane, erzak, özel palmiye dizisi, bayrak, insan, ürün veya belirli kıyı işareti yoktur.

**BACK_LIGHTHOUSE:** Aynı deniz içinde çok dik kuşbakışında, alçak ve anonim kaya sırtına oturan küçük, sade yığma taş fener görülür. Kule etrafında halka, ışık halesi, ışın, rozet, pusula geometrisi veya boş grafik disk yoktur. Kaya ve bakım aşınması kuleyi suya yapıştırılmış ikondan çıkarıp fiziksel seyir unsuruna dönüştürür. Yanıltıcı ışık, özel ateş, gizli paket, belirli hasar, özel kıyı ve ön karta bağlı olay izi yoktur.

### Exact 180 dereceyi sahnenin içinde kurma

- BACK_SEA_ROCK çizgi mikro-kümeleri uzak yarım-dönüş eşleriyle dağılır; dönüş merkezi sıradan sudur.
- BACK_ISLAND tek gövde olarak dönüş merkezinden geçen doğal uzun bir eksene sahiptir. İki burun, küçük koylar, taş/çalı kümeleri ve kıyı kırıkları yarım-dönüş eşlidir; sağ-sol ayna, kusursuz oval veya dijital rozet değildir.
- BACK_LIGHTHOUSE tek kuleyi exact dönüş noktasında kullanır; bu bir logo merkezi değil, yön-güvenli fiziksel sahne çözümüdür. Sade çokgen kule planı, fener üst yapısı, iki yana uzayan kaya sırtı, su yarıkları ve aşınmalar yarım-dönüş eşlidir. Kuleyi çevreleyen halka/radyal boşluk yoktur.
- Ufuk, tek yönlü gölge, üst/alt hava farkı, tek tarafta köpük, serbest ip/kapı yönü veya rüzgâr oku kullanılmaz.
- Eskitme ve kâğıt lifi rastgele son filtre değildir; exact dönüş eşli masterın içindedir.
- Flattened master 180 derece rotate/difference testinde piksel düzeyinde eşleşmelidir.

### Exact master tekrarını duvar kâğıdından ayırma

Aile içinde exact aynı master zorunludur. Tekrarı masa üzerinde düşük görünürlüklü tutmak için:

1. BACK_SEA_ROCK’ta büyük odak, merkez koyuluğu ve tek imza dalga yoktur.
2. Ada ve fener çevresindeki deniz, diğer ailelerin kenar zarfıyla aynı ritmi sürdürür.
3. Yatay dalga satırı, dama, zincir, eşit aralıklı fayans ritmi veya kart-başına aynı koyu köşe yoktur.
4. Küçük su kümeleri çok sayıda ve düşük baskılıdır; tek hatırlanabilir su lekesi bırakılmaz.
5. Ada ve fener aile görünürlüğü kasıtlıdır; buna karşılık belirli ön kartı ele verecek ikinci bir landmark bulunmaz.
6. Farklı geçerli düzenlerde ve rastgele dönüşlerde tekrar, ayrı kart çerçevelerinden önce ortak deniz kadansına dönüşmelidir.

### Ön yüzlerle ilişki

Kapalı deniz zemini kabul edilmiş ön-yüz illüstrasyonlarının çizgi, tarama ve mat malzeme dünyasına aittir. Ada ve fener, ön yüz ikonlarının küçültülmüş kopyaları değildir; yalnız anonim aile coğrafyasıdır. Birkaç kart açıldığında ön yüzler ortak denizde keşfedilmiş olay/coğrafya parçaları gibi yükselir. Bu brief ön-yüz sanatını veya kompozisyonunu değiştirmez.

## 3. BACK_CHARACTER — 20

### Sanat fikri: “İşin bıraktığı çift iz”

Merkezde insan yüzü veya portresi yoktur. İki karşıt yönden gelen, birbirinin 180 derece eşi olan iki geniş kenevir halat kıvrımı; aralarında dört farklı meslek malzemesinin yalnız dokusal izini taşıyan kapalı bir bez oval oluşturur: kurum, tuz, balmumu ve ahşap sürtünmesi. Nesnelerin kendisi resmedilmez; izler karakterlerin kişiden önce iş tarafından biçimlendiğini söyler.

Motif uzaktan merkezi koyu bir oval ve iki açık halat S’i olarak okunur. Yakından bezde farklı el basıncı/aşınma izleri vardır; gerçek el silueti veya parmak izi yoktur. Böylece belirli yaş, cinsiyet, ten, rol ya da karakter kimliği sızmaz.

### Korunacak duygu ve sanatçı payı

**Korunacak duygu:** İnsan görünmeden emek; yüz kapalıyken bile bir hayatın malzemeyle sürtünmüş olması.

**Açık karar alanı:** Halat/bez önerisi starting vector’dür. Yüz, el, rol nesnesi veya tanınır meslek ikonu üretmeden aynı emek izini daha canlı taşıyan 180-güvenli dönem malzemesi önerilebilir.

**İlk eleştiri sorusu:** Bu arka yüz belirli bir kişiyi ele vermeden ‘bedeni iş biçimlendirdi’ duygusu taşıyor mu, yoksa yalnız dekoratif tekstil mi?

Özel isim, baş harf, logo, arma ve çalışma lore’u bu çözümü taşıyamaz. Sanatçı önerisi önce siyah-beyaz küçük eskizde, sonra 180 derece rotate/difference ve kör masa testinde değerlendirilir; yüzey cilası bu iki kapıdan sonra gelir.

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

### Korunacak duygu ve sanatçı payı

**Korunacak duygu:** Kapalı potansiyel ve taşınan ağırlık; içerik bilinmez, müdahale ihtimali hissedilir.

**Açık karar alanı:** Yağlı rulo starting vector’dür. Güç/ERZ kimliği sızdırmayan, kapalı kaynak hissini koruyan 180-güvenli başka bir donanım hâli önerilebilir.

**İlk eleştiri sorusu:** Kart bir büyü destesi veya ganimet sandığına dönmeden ‘elde tutulan fakat henüz açılmamış imkân’ hissi veriyor mu?

Özel isim, baş harf, logo, arma ve çalışma lore’u bu çözümü taşıyamaz. Sanatçı önerisi önce siyah-beyaz küçük eskizde, sonra 180 derece rotate/difference ve kör masa testinde değerlendirilir; yüzey cilası bu iki kapıdan sonra gelir.

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

### Korunacak duygu ve sanatçı payı

**Korunacak duygu:** Kapalı niyet; aydınlık/karanlık, temiz/kirli veya iyi/kötü ikiliğine düşmeyen insan belirsizliği.

**Açık karar alanı:** Katlı keten ve düğüm starting vector’dür. Tayfa/Hain ayrımı üretecek renk, simge veya aşınma olmadan kapalı niyeti taşıyan başka bir 180-güvenli kumaş/bağ çözümü önerilebilir.

**İlk eleştiri sorusu:** Görsel gizemi ahlaki bir renge çevirmeden kapalı niyetin ağırlığını taşıyor mu?

Özel isim, baş harf, logo, arma ve çalışma lore’u bu çözümü taşıyamaz. Sanatçı önerisi önce siyah-beyaz küçük eskizde, sonra 180 derece rotate/difference ve kör masa testinde değerlendirilir; yüzey cilası bu iki kapıdan sonra gelir.

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

### Sanat fikri: “Mat ve ışıldamayan isimsiz açık su”

BACK_SEA_ROCK, COMMON_MAP_BACK_VISUAL_SYSTEM’in nötr, mat ve ışıldamayan deniz
baseline’ıdır. Önceki beyaz parlama pulları, krom/specular etki, düzenli
parlak dalga tepesi, bloom ve plastik AI cilası yeniden kullanılamaz. Oyuncu arka yüzden kartın Açık Deniz/Kayalık ortak ailesinde olduğunu bilir; fakat su yüzeyinde hangi alt türün geleceğine dair hiçbir ipucu bulamaz. Kartın tamamına yayılan kısa/kırık çizgiler, kâğıt rezervi ve seyrek tarama dışında ayrı motif yoktur.

Bu master 30 Açık Deniz ve 12 Kayalık için bit-bit exact aynıdır. Kaya, sığlık, resif, köpüren kırıcı dalga, keskin jeolojik tarama, koyu dip lekesi veya “tehlikeli su” rengi kullanılmaz.

### Korunacak duygu ve sanatçı payı

**Korunacak duygu:** Henüz okunmamış, geniş ve tarafsız su; ön yüzde rahatlık da tehdit de çıkabilir.

**Açık karar alanı:** Sanatçı kısa su çizgilerinin el ritmini, kesintisini ve mikro-aralıklarını kurabilir. Büyük yön, merkez motifi, ayrı leke, resif çağrışımı veya tekrarda tanınacak imza çizgi kuramaz.

**İlk eleştiri sorusu:** Bu arka yüz genel bir FOULWAKE denizi olarak açıkça okunurken Açık Deniz/Kayalık tahmini tamamen kör kalıyor mu?

### Çizgi, palet ve kenar

- Orta aralıklı kısa/kırık su çizgileri ortak üç mikro ölçekte dolaşır.
- Kurum indigosu, tuz mavi-grisi, tar grisi ve kemik rezerv ortak baseline’dır.
- Deniz dört kenarda aynı istatistiksel zarfla bleed’e kadar gider; dekoratif çerçeve yoktur.
- Uzun rota çizgisi, ufuk, gemi, kaya, köpük, sığlık, koordinat ve pusula yoktur.
- Pas, hardal, kırmızı, kara tonu, parlak vurgu ve gradient su yoktur.
- Sahne belirli sıra, sütun, grid veya komşu kart gerektirmez.

### 180 derece ve tekrar yapısı

Çok sayıdaki küçük çizgi kümesi yüzeyin uzak bölgelerindeki yarım-dönüş eşleriyle exact dengelenir. Dönüş merkezi sıradan sudur. Radyal karşı-akıntı, dört kollu kesişim veya merkez lekesi kullanılmaz. Exact master tekrarında tanınacak tekil koyu/açık landmark bulunmaz.

### Risk analizi

- **Açık Deniz/Kayalık sızıntısı:** köpük, sivri kırıcı çizgi, sığlık rengi, taş taraması ve “sakin/tehlikeli” hava kodu reddedilir.
- **Fayans etkisi:** aynı dalga satırı, merkez koyuluğu veya hatırlanabilir leke her kopyada tekrar ederse master reddedilir.
- **Dikiş etkisi:** trimde kesilen uzun çizgi veya kenar değer sıçraması değişken haritayı karelere böler.
- **Yerleşim bağımlılığı:** yalnız belirli komşulukta çalışan literal dalga devamı FAIL’dir.
- **Yön sızıntısı:** baskın çapraz, üstte sakin/altta çalkantılı dağılım veya tek akış yönü yoktur.
- **v2.6 riski:** bu DRAFT v2.7 ortaklığı, kilitli v2.6 dosyalarını değiştirmez.

### Kabul ölçütü

42 kapalı kart içinde Açık Deniz/Kayalık tahmini şans düzeyini aşmaz. Farklı kurala uygun harita biçimlerinde ve rastgele 180 dönüşlerde merkez tekrarı, yön, koyu kare veya kenar kopması görülmeden ortak keşfedilmemiş deniz okunur.

## 7. BACK_ISLAND — 6

### Sanat fikri: “İsimsiz kara eşiği” — FULL REDRAW

BACK_ISLAND önceki reddedilmiş ada varlığından crop, paint-over, recolor,
trace veya türev almadan sıfırdan çizilir. BACK_ISLAND’da aile bilgisi
kasıtlı olarak görünür: ortak FOULWAKE denizinin içinde genel bir ada vardır. Bu ada altı ön yüzden hiçbirine ait değildir; belirli liman, ekonomi, insan topluluğu, ürün, olay veya kıyı kimliği taşımaz. Altı Ada kartının tamamı bit-bit exact aynı masterı kullanır.

Dik kuşbakışında görülen tek, alçak kara gövdesi karşıt iki burun ve aralarında aşınmış bir omurga taşır. Kusursuz oval, ortalanmış renk diski veya etrafı halka gibi boşaltılmış madalyon değildir. Deniz adanın çevresinde ve dört kart kenarında kesintisiz ortak zemini sürdürür.

### Korunacak duygu ve sanatçı payı

**Korunacak duygu:** Uzak denizde karaya rastlama; rahatlık ihtimali kadar bilinmezlik de taşıyan, henüz adı konmamış bir eşik.

**Açık karar alanı:** Sanatçı anonim kıyı kırıklarının el ritmini, düşük çalının ve taşın taramasını kurabilir. Coğrafyayı canlı gözlemle zenginleştirebilir; fakat altı ön adadan birini tanıtacak siluet, yapı veya nesne ekleyemez.

**İlk eleştiri sorusu:** Ada ailesi normal masa mesafesinde açıkça okunurken kara, suyun üzerine yapıştırılmış ikon/rozet gibi mi duruyor; yoksa aynı denizin doğal coğrafyası mı?

### Çizgi, palet ve kenar

- Deniz, BACK_SEA_ROCK ile aynı çizgi ölçeği, değer zarfı ve kenar ritmini taşır.
- Ada konturu tek kalın sticker çizgisi değildir; ıslak taş, aşınmış toprak ve su temasında değişen kontur basıncıyla kurulur.
- Kara düşük doygunluklu isli toprak, taş grisi ve kemik rezervle ayrılır; parlak yeşil/turkuaz aile kodu yoktur.
- İç ayrıntı anonim taş, alçak çalı ve çıplak toprakla sınırlıdır.
- Yerleşim, gümrük binası, korsan kampı, tersane, erzak, bayrak, insan, ürün, özel palmiye düzeni, liman ağzı veya belirli kıyı biçimi yoktur.
- Ada kenara taşmaz ve belirli komşu istemez; deniz dört kenarda ortak zarfı korur.

### 180 derece ve tekrar yapısı

Tek ada gövdesi dönüş merkezinden geçen doğal uzun bir eksenle kurulur. İki burun, iki küçük koy, taş/çalı kümeleri, kıyı girintileri ve baskı aşınmaları yarım-dönüş eşlidir. Sağ-sol ayna simetrisi, kusursuz oval veya dijital rozet yoktur. Flattened master 180 derece döndüğünde exact eşleşir; herhangi bir ufuk, tek yönlü gölge veya üst/alt kıyı hiyerarşisi oluşmaz.

### Risk analizi

- **Ön kimlik sızıntısı:** altı ön adanın özel kıyı, bina, ürün, kişi, bitki düzeni veya olay motifiyle benzerlik reddedilir.
- **Sonuç sızıntısı:** bereketli/çorak, güvenli/tehlikeli, zengin/yoksul gibi oyun sonucuna dönüşebilecek renk ve hava kodu yoktur.
- **İkon/madalyon riski:** halo, çevre halkası, kalın sticker konturu, merkezî renk diski ve simetrik boş alan yoktur.
- **Aile kaybı:** normal masa mesafesinde ada ailesi anlaşılmıyorsa kara-su değer ayrımı veya kıyı konturu ölçülü güçlendirilir; yazı, bayrak, ikon eklenmez.
- **Yerleşim bağımlılığı:** ada belirli komşu, sabit grid veya kart sayısına ihtiyaç duymaz.
- **Fayans etkisi:** aynı ada görünür biçimde tekrar edecektir; bu kasıtlı aile bilgisidir. Buna ikinci bir hatırlanabilir su lekesi veya köşe işareti eklenmez.

### Kabul ölçütü

Oyuncu kartın Ada ailesinde olduğunu normal masa mesafesinde anlayabilir; altı ön adadan hangisi olduğunu, sonucunu veya yönünü tahmin edemez. Ada, farklı geçerli komşuluklarda rozet değil ortak FOULWAKE denizinin anonim kara parçası gibi görünür.

## 8. BACK_LIGHTHOUSE — 4

### Sanat fikri: “Büyük ve adsız seyir nöbeti”

BACK_LIGHTHOUSE ortak FOULWAKE denizinde anonim, 1721’e uygun bir deniz
fenerini aile düzeyinde açıkça gösterir. Fener daha büyük ve normal kart, thumbnail ve masa mesafesinde ilk bakışta
okunur. Uzun kayalık sırt zorunlu değildir; kompakt kaya, kısa burun veya sade kıyı temeli kullanılabilir.

Kule dört exact ön fenerden hiçbirine ait özel mimari, hasar, saklı paket,
yanıltıcı ışık, sonuç veya kıyı kimliği taşımaz. Dört kart bit-bit exact aynı
masterı kullanır.

### Çizgi, palet ve kompozisyon

- Deniz BACK_SEA_ROCK ile aynı mat, ışıldamayan çizgi/değer/kenar zarfındadır.
- Ana kule yığma taş gövde ve sade üst seyir/ateş yapısıyla küçük ölçekte bile
  açıkça okunur; kaya kütlesi kuleyi yutamaz.
- Fener merkez rozet, hedef veya suya yapıştırılmış ikon gibi durmaz.
- Kompakt fiziksel temel kuleyi denize bağlar; uzun diyagonal kaya, iki yana
  uzanan eş sırt veya belirli komşu kart şartı yoktur.
- Taş grisi, kurum indigosu, tuz mavi-grisi, tar grisi ve kemik rezerv; parlak
  sarı beacon veya doygun aile rengi yoktur.
- Işın, glow, halo, lens, ayna/reflektör gösterisi, Argand, Fresnel, elektrik,
  modern beacon, pusula, hedef, rozet ve madalyon yoktur.

### Kadraj ve 180 derece

Kule ile kompakt temel exact yarım dönüş eşliği içinde kurulur. Simetri grafik
amblemden değil fiziksel taş/kıyı dağılımından gelir. Ufuk ve tek yönlü gölge
yoktur; dört kenarın deniz zarfı eşdeğerdir. 180° test pixel-exact yapılır.

Sanat Yönetmeni ayrıca kulenin kart içindeki ölçeğini, güvenli alanını, deniz
negatif alanını, kaya tarafından örtülmemesini ve normal masa-mesafesi
okunurluğunu değerlendirir. Görsel Tasarım self-PASS veremez.

### Risk analizi

- **Aile kaybı:** kule küçük veya kayaya gömülü okunuyorsa REFRAME_REQUIRED.
- **Ada/kayalık yanlış okuması:** insan yapımı kule ilk bakışta seçilmiyorsa FAIL.
- **Ön kimlik sızıntısı:** exact ön mimari, hasar, ışık davranışı veya sonuç yok.
- **İkon/rozet:** halo, halka, hedef, radyal çizgi ve grafik merkez diski yok.
- **Dönem:** gelişmiş optik ve modern beacon yok.
- **Yerleşim:** sabit grid, uzun sırt veya belirli komşu gerektirmez.

### Kabul ölçütü

Oyuncu Deniz Feneri ailesini normal mesafede anlayabilir; dört önden hangisi
olduğunu, sonucunu veya yönünü tahmin edemez. Fener daha büyük, fiziksel ve
dönemsel görünür; FRAMING_PASS ve exact 180° PASS olmadan KEEP verilmez.

## 9. BACK_SUPPORT — 3

### Sanat fikri: “İki rıhtım, bir boş merkez”

İki karşıt yönde exact eşli taş rıhtım babası ve aralarında merkezi boş bırakan tek kenevir palamar halkası. Merkezde kişi, sandalye, liman adı, anahtar veya mühür yoktur. Bu boşluk Kalkış, Varış ve KAPTAN için ortak olan “işlevin insan/yer değişse de kalması” fikrini taşır.

Rıhtım babaları belirli bir limanı anlatmaz; taş/ahşap karışımı nötr gemi altyapısıdır. Palamar iki yönü bağlar ama ok veya rota değildir.

### Korunacak duygu ve sanatçı payı

**Korunacak duygu:** Kişilerden uzun yaşayan kamusal düzen; iki liman ve devredilebilir makamın ortak eşiği.

**Açık karar alanı:** İki rıhtım ve boş merkez starting vector’dür. Liman adı/arması, Kaptan simgesi veya tekil mimari marka olmadan aynı kamusal düzeni taşıyan 180-güvenli çözüm önerilebilir.

**İlk eleştiri sorusu:** Görsel bir FOULWAKE logosuna dönüşmeden ‘kurulum ve makam insanlardan önce/sonra da kalır’ duygusunu taşıyor mu?

Özel isim, baş harf, logo, arma ve çalışma lore’u bu çözümü taşıyamaz. Sanatçı önerisi önce siyah-beyaz küçük eskizde, sonra 180 derece rotate/difference ve kör masa testinde değerlendirilir; yüzey cilası bu iki kapıdan sonra gelir.

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

Üç kart aynı kurumsal destek ailesi olarak hissedilir; Kalkış, Varış veya KAPTAN ayrımı ve yönü arka yüzden öğrenilemez.

## 9A. REPRESENTATIVE_VARIABLE_MAP_LAYOUT_QA — zorunlu kanıtlar

Bu brief mockup üretmez. Görsel üretim yetkisi verilirse Görsel Tasarım aşağıdaki on dört kanıtı birlikte teslim eder:

1. BACK_SEA_ROCK, BACK_ISLAND ve BACK_LIGHTHOUSE’ı birlikte gösteren, kural kitabına uygun tamamen kapalı temsilî harita düzenleri.
2. Aynı kartların rastgele 180 derece çevrildiği temsilî düzenler.
3. Bazı kartların açıldığı keşif-sonrası masa düzenleri.
4. Kuralların izin verdiği ölçüde daha kompakt ve daha geniş/uzayan harita düzenleri.
5. Ada, Fener ve Deniz/Kayalık ailelerinin farklı komşuluklarda bulunduğu örnekler.
6. BACK_SEA_ROCK için Açık Deniz/Kayalık kör ayrım testi; tahmin şans düzeyini aşmamalıdır.
7. Altı Ada ön kimliği için kör tahmin testi; arka yüzden belirli Ada seçilememelidir.
8. Dört Deniz Feneri ön kimliği için kör tahmin testi; arka yüzden belirli Fener seçilememelidir.
9. Ada ve Fener ailelerinin normal masa mesafesinde anlaşılabildiği kontrol.
10. Ada ve fener unsurlarının ikon, rozet veya madalyon gibi görünmediği sanat incelemesi.
11. Okunabilir yazı, sayı, rota, pusula, koordinat, yön işareti ve gereksiz dekoratif şekil kontrolü.
12. Kart kenarı, kesim, parlaklık, exact master ve yön sızıntısı kontrolü.
13. Farklı kurala uygun düzenlerde ortak deniz hissinin korunduğu kontrol.
14. Arka yüzlerin açılan ön yüzlerle aynı FOULWAKE sanat dünyasına ait göründüğü kontrol.

Ek değerlendirmeler:

- Sabit 5×5, grid, satır, sütun veya kart sayısı kabul şartı değildir; örnekler yalnız kurala uygun temsilî değişken düzenlerdir.
- Kompakt ve uzayan örnekler hem net hem hafif bulanık/squint görünümde incelenir; ortak deniz yerine koyu kart kareleri veya üç ayrı marka fayansı çıkmamalıdır.
- Düz ve 180 çevrilmiş örnekler yan yana gösterilir; bütünlük yalnız tek yönlü dizilimde çalışıyorsa sonuç FAIL’dir.
- Aile görünürlüğü amaçtır: Ada ve Fener normal masa mesafesinde ayırt edilemiyorsa FAIL’dir.
- Kimlik sızıntısı yasaktır: Açık Deniz/Kayalık, altı Ada ön kimliği veya dört Fener ön kimliği şansın üstünde tahmin edilebiliyorsa ilgili master FAIL’dir.
- Ada/fener aile ayrımı yazı, bayrak, logo, ışın, renk rozeti veya ön karta özgü landmarkla güçlendirilemez.
- Bir yerleşimde başarılı olup başka kurala uygun yerleşimde sert kenar/değer kopması üreten sistem FAIL’dir.

Kabul cümlesi: **Oyuncu kapalı kartın Deniz/Kayalık, Ada veya Fener ailesinden olduğunu anlayabilir; ancak kart çevrilmeden hangi ön kart olduğunu veya sonucunu tahmin edemez. Harita, belirli bir ölçü veya dizilimde değil, oyun sırasında oluşabilecek kurala uygun farklı masa düzenlerinde tek bir keşfedilmemiş FOULWAKE denizi gibi görünür.**

## 10. Binaryler arası çakışma kontrolü

| Binary | Uzakta algı / masa rolü | Yakında maddi imza | Kaçınacağı komşu |
|---|---|---|---|
| CHARACTER | Bez oval + çift halat S | İş aşınması izleri | LOYALTY’nin kapalı düğümü |
| POWER | İki uçtan kapalı rulo | Yağlı bez + pas | SUPPORT’ın açık merkezi |
| LOYALTY | Kapalı koyu keten + çift bağ | Nötr düğüm | CHARACTER’ın iş izleri |
| SEA_ROCK | Değişken haritanın genel deniz zemini | Orta aralıklı kırık su çizgisi; kaya/sığlık yok | ISLAND/LIGHTHOUSE coğrafyasının su kenar ritmini bozması |
| ISLAND | Ortak denizde açıkça görülen anonim kara | Düşük ada omurgası + doğal kıyı taraması | Ön adaya özgü siluet; ikon, halo ve renk madalyonu |
| LIGHTHOUSE | Ortak denizde açıkça görülen anonim seyir yapısı | Sade taş kule + alçak kaya sırtı | Ön fenere özgü ayrıntı; ışın, rozet ve dönem dışı optik |
| SUPPORT | İki rıhtım babası + boş merkez | Taş + palamar | POWER’ın kapalı rulosu |

Yedi arka yüz aynı mat kâğıt, ana mürekkep ve el çizgisi ailesini paylaşır. Karakter, Güç, Sadakat ve Yardımcı yönleri f0389711… kabulüyle korunur. Üç harita binarysinde aile farkı kasıtlı olarak görünürdür: genel deniz, genel ada ve genel dönem feneri. Bu görünürlük belirli ön kimlik veya sonuç taşımaz. Değişken masa birliği, aynı deniz çizgisi, değer zarfı, kâğıt ve kenar ritmiyle kurulur; sabit dizilim veya renk rozetiyle değil.

## 11. Üretim ve hash disiplini

Onaydan sonra Görsel Tasarım her binary için tek master üretir ve:

- dosya adını binary kimliğiyle eşler;
- her fiziksel kopyayı aynı masterdan türetir;
- flattened dosya hashini manifestte bir kez kaydeder;
- 180 rotate/difference kanıtını saklar;
- baskı lotu, kâğıt ve vernik bilgisini ayrı teknik raporda tutar;
- hiçbir karta kart-başına random distress eklemez;
- test baskısı başarısızsa sanat dosyasını revize eder, kart kopyalarını ayrı ayrı “düzeltmez”.

Üç harita masterı ayrı ayrı değil, aynı COMMON_MAP_BACK_VISUAL_SYSTEM sürümü altında birlikte teslim edilir. Teknik pakette üç hash ile birlikte REPRESENTATIVE_VARIABLE_MAP_LAYOUT_QA’nın tamamen kapalı, rastgele 180 çevrilmiş, keşif-sonrası, kompakt ve geniş/uzayan düzenleri; normal-mesafe/kenar incelemesi; aile tanıma ve ön-kart kör tahmin sonuçları aynı kanıt setinde bulunur. Aile masterları tek tek geçse bile değişken masa QA’sı başarısızsa harita arka-yüz paketi FAIL’dir.

Bu targeted rework dosya formatı, DPI, bleed veya ICC profilini kilitlemez; bunlar Görsel Tasarımın teknik üretim ve Baş Editör entegrasyon alanıdır. Sanat fikri, aile görünürlüğü, değişken masa bütünlüğü ve sızıntı riskleri bağlayıcı brief olarak sunulur.

## 12. Dispozisyon

ART_DIRECTION_STAGE: BRIEF  
INPUT_VISUAL_BRANCH: NONE — BRIEF STAGE  
INPUT_VISUAL_COMMIT: NONE — BRIEF STAGE  
INPUT_CONTACT_SHEETS: NONE — BRIEF STAGE  
PROJECT_OWNER_DECISION: OPTION_2 — FAMILY-VISIBLE MAP BACKS  
CREATIVE_VERDICT: FAMILY_VISIBLE_VARIABLE_LAYOUT_MAP_BACK_REWORK_DELIVERED / PENDING_PROJECT_OWNER_AND_CHIEF_EDITOR_REVIEW  
PROJECT_OWNER_DECISION_REQUIRED: YES — FINAL REWORK REVIEW  
VISUAL_PRODUCTION_AUTHORIZED: NO  
FINAL_VISUAL_AND_PDF_OWNER: Görsel Tasarım — NOT AUTHORIZED  
INTEGRATION_AND_DISPOSITION: Baş Editör  
TEMPORARY_SUBAGENTS: NONE  
LOCK_REQUESTED: NO
