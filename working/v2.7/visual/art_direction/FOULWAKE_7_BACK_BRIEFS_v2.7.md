# FOULWAKE 7 BACK BRIEFS v2.7

Status: TARGETED MAP-BACK TABLE-COHERENCE REWORK — arka yüz sanat fikri ve risk analizi; final görsel/render/PDF değildir.  
Accepted package baseline: work/v2.7-art-direction@f0389711ebefaad7170cbee7f1a0ab09cf128b15 — CHARACTER / POWER / LOYALTY / SUPPORT BACKS PROTECTED  
Chief Editor targeted disposition: TARGETED_REWORK_REQUIRED — MAP_BACK_TABLE_COHERENCE  
Project Owner direction: closed map cards must read first as one undiscovered FOULWAKE sea; no visual production.  
Visual production authorized: NO  
Source branch: work/v2.7-art-direction  
Chief Editor source: v2.7-design@29da7e35c4d940e1836bc3852a67d0cc7a5904a1  
Baseline: v2.6 STABLE / LOCKED  
Decision gate: PROJECT OWNER + CHIEF EDITOR  
Production owner after approval: Görsel Tasarım  
Targeted rework scope: BACK_SEA_ROCK / BACK_ISLAND / BACK_LIGHTHOUSE ortak masa sistemi; diğer dört arka-yüz yönü korunur.

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

### 2.1 Kapalı kartların sanatsal görevi

Arka yüzler yedi ayrı logo değildir. Masada yüzü kapalı duran kart, FOULWAKE’ın temel hâlini taşır: **bilgi vardır, fakat henüz kimse ona sahip değildir.** Bu nedenle arka yüzün güzelliği “gizemli simge”den değil, tutulmuş ve kullanılmış bir nesnenin sessiz ağırlığından doğar.

- Aile farkı ikonla değil, maddi hâlle kurulur: emek izi, kapalı kaynak, kapalı niyet, okunmamış coğrafya, kara eşiği, insan yapımı ışık bakımı, kamusal düzen.
- Motifler antik mühür, tarikat logosu, oyun amblemi veya koleksiyon serisi rozeti gibi davranmaz.
- Eski baskı dili rastgele kir değil; aynı masterda, aynı 180 derece düzen içinde tasarlanmış kullanım hafızasıdır.
- Kapalı deniz alanı “tehlike” diye bağırmaz; oyuncuyu seçim öncesi sessizliğe sokar.
- Ön yüzlerin özel adları, çalışma lore’u ve siyah balmumu ihtimali arka yüzlere taşınmaz. Adlar değişse bile aile işlevi ve masa güvenliği aynen kalır.
- Arka yüz sanatçısı güvenlik yüzünden yalnız teknisyen değildir. Çizgi ritmi, yüzeyin nefesi ve maddi ağırlık onun yorumudur; ancak bu yorum exact master, 180 derece ve bilgi sızıntısı sınırlarını aşamaz.

### 2.2 İçerik

- Okunabilir yazı, logo, oyun adı, kart tür etiketi, sayı, harf, yön oku, pusula harfi, arma ve slogan yok.
- Ön yüzün kart adı, karakteri, nesnesi, olayı, ahlak durumu veya mekaniği arka yüzde görünmez.
- Siyah balmumu ve Siyah Mühür hiçbir arka yüzde motif, logo, renk kodu veya kanıt izi değildir; özellikle BACK_LOYALTY’de Tayfa/Hain sızıntısı yaratacak koyu varyant bulunmaz.
- Aile içindeki bütün fiziksel kopyalar bit-bit exact aynı master dosyayı kullanır; kart başına farklı eskitme, leke veya renk varyantı yok.
- v2.7 anlatısal görsel omurga arka yüzlere taşınmaz: tiryak sandığı, Gusto eşyası, Siyah Mühür ve Veyr izi binary tasarımına girmez.
- Kâğıt, katran, tuz, kenevir, oksit ve eski baskı çizgisi ön yüzlerle aynı dünyadadır. Arka yüz ayrı bir “marka logosu” katmanı değildir.
- Ekli KAPTAN STYLE_ONLY referansından yüz, şapka, kuş, gemi, çerçeve, kompozisyon, nesne veya çizgi alınmaz.
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

Ekli 5×5 örnek MAP_TABLE_REFERENCE: TABLE_READ_ONLY / COMPOSITION_PRINCIPLE_ONLY olarak sınıflandırılır. Ondan yalnız “kapalı kartlar yan yana geldiğinde tek bir keşfedilmemiş deniz/oyun alanı okunur” ilkesi alınır. Örneğin dalga çizgileri, renkleri, çerçevesi, kart yüzleri, kart dizilimi ve yüzey düzeni kopyalanmaz. KAPTAN ayrı bir STYLE_ONLY referanstır; harita-masası referansı KAPTAN’ın, KAPTAN da harita-masası referansının yetkisini genişletmez.

### Birincil kompozisyon birimi

Üç harita binarysinde sanatın birincil kompozisyon birimi tek kart değil, kapalı 5×5 veya benzer masa alanıdır. Sistem iki mesafeli hiyerarşi kurar:

- **Uzak / normal masa mesafesi:** Tekil karttan önce tek, geniş, keşfedilmemiş FOULWAKE denizi okunur.
- **Yakın / elde kart mesafesi:** BACK_SEA_ROCK, BACK_ISLAND ve BACK_LIGHTHOUSE yalnız su davranışındaki mikro-farkla ayırt edilebilir; belirli ön kart, yön veya alt tür okunamaz.

Yakın aile kimliği uzak masa birliğini yenemez. Üç ayrı renk adası, desen fayansı veya aile rozeti oluşursa sistem başarısızdır.

### Ortak çizgi ve tarama grameri

- Deniz, kart yüzeyine eşit dağılmış kısa ve kırık gözlem çizgileriyle kurulur; merkez, köşe, eksen ve kenar “ana motif” bölgesi değildir.
- Aynı boyda paralel dalga sıraları yoktur. Üç küçük ölçekte dolaşan, farklı uzunluk ve aralıklardaki sığ yüzey çizgileri; aralarında seyrek kısa çapraz tarama ve kemik kâğıt rezervi bulunur.
- Tekil büyük S, halka, yıldız, dört kollu akıntı, koyu göbek, rozet veya kolay ezberlenen “imza dalga” yoktur.
- Hacim boya gradyanı, airbrush veya dijital noise ile değil; çizgi aralığı, kesinti, yön gerilimi ve kâğıt rezerviyle kurulur.
- El çizgisi canlı kalır; fakat bütün mikro-kümeler exact 180 derece eşleriyle master içinde dengelenir. Eşler yüzeyin karşı tarafına dağıtılır; merkezde radyal simetri kurulmaz.

### Ortak dalga ölçeği ve değer zarfı

- Üç binary aynı ana çizgi kalınlığı, üçlü mikro-ölçek merdiveni ve yaklaşık aynı ortalama koyu/açık değer alanını kullanır.
- Palet omurgası kurum indigosu, tuz mavi-grisi, tar grisi ve kemik kâğıttır. Aile farkı doygun renk kodu değildir.
- Her masterın merkez yüzde 35’lik alanı, dış alandan daha koyu veya daha ayrıntılı kurulmaz. Orta alan “bakılacak yer” değildir.
- Hiçbir tekil açık/koyu leke gerçek kart boyunda ilk odak olamaz; en yüksek yerel kontrast yüzeye dağılmış çoklu küçük karşılıklarla dengelenir.

### Ortak kenar ritmi ve rastgele komşuluk

- Deniz yüzeyi bleed’e kadar gider; dekoratif çerçeve kullanılmaz.
- Üretim keyline’ı zorunluysa üç map binarysinde exact aynı, ince, düşük kontrastlı ve süssüz teknik çizgi kullanılır. Keyline dalga/tarama çizgisinden baskın olamaz.
- Trim çevresindeki kenar zarfında çizgi ölçeği, ortalama yoğunluk ve değer üç ailede aynı aralıkta kalır.
- Uzun, yüksek kontrastlı çizgi trimde kesilmez; komşu kartta devam etmesi beklenen sahte rota veya büyük dalga yarısı bırakılmaz.
- Rastgele komşulukta literal çizgi uçlarının birleşmesi aranmaz. Devamlılık; aynı ölçek, değer, hava ve kenar yoğunluğunun “istatistiksel dikişi” ile kurulur.
- Köşeler arasında farklı koyu leke, parlak köpük, tortu adası veya tanınabilir çizgi takımyıldızı yoktur.

### Exact master tekrarını duvar kâğıdından ayırma

Aile içinde exact aynı master zorunludur; bu nedenle tekrar gizlenmez, düşük görünürlüklü hâle getirilir:

1. Büyük odak ve tekil landmark kullanılmaz.
2. Yatay satır, dama, zincir veya tekrar eden dalga koridoru kurulmaz.
3. Çizgi kümeleri çok sayıda, küçük, değişken aralıklı ve düşük görsel baskılıdır.
4. Her ayırt edici mikro-küme başka bölgelerde benzer ağırlıkta karşılık bulur; tek “hatırlanabilir leke” bırakılmaz.
5. 5×5 bulanıklaştırma/kısık-göz testinde kart merkezleri koyu düğme gibi tekrar etmez.
6. Rastgele 180 dönüş, ortak alan ritmini korur; düz/ters yön görsel olarak seçilemez.

### Sembolsüz aile farkı

| Binary | Baseline’a göre su davranışı | Yakından izinli fark | Masa mesafesinde şart |
|---|---|---|---|
| BACK_SEA_ROCK | Nötr ana deniz | Orta aralıklı kırık yüzey çizgisi; dengeli indigo/tuz grisi | Açık Deniz/Kayalık okunmaz; büyük biçim yok |
| BACK_ISLAND | Bir mikro-adım daha yavaş/tortulu aynı deniz | Biraz geniş çizgi aralığı ve bütün yüzeye yayılmış çok hafif sıcak tuz-grisi alt ton | Kara, sığlık lekesi veya ayrı renk karesi okunmaz |
| BACK_LIGHTHOUSE | Bir mikro-adım daha ince rüzgârla taranmış aynı deniz | Yüzeye eşit dağılmış ince çapraz-rüzgâr izi ve çok hafif daha soğuk/açık hava değeri | Işık, radyal düzen veya ayrı parlak kare okunmaz |

Aile farkı merkezde değil bütün yüzeye düşük şiddette yayılır. Üç masterın en az yüzde 85’i ortak çizgi/palet/kenar grameri gibi hissedilmelidir; kalan fark yalnız yakın aile teşhisine yetecek ölçüdedir.

### Ön yüzlerle ilişki

Kapalı deniz zemini, kabul edilmiş ön-yüz illüstrasyonlarının çizgi/mat malzeme dünyasına aittir; fakat onların olay, ada, kayalık veya fener ikonlarını küçültüp arka yüzde kullanmaz. Birkaç kart açıldığında ön yüzler ortak denizde keşfedilmiş parçalar gibi yükselir. Bu brief ön-yüz sanatını veya kompozisyonunu değiştirmez; kapalı zeminin onlarla yarışmamasını ister.


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

### Sanat fikri: “Odaksız ana deniz alanı”

BACK_SEA_ROCK, COMMON_MAP_BACK_VISUAL_SYSTEM’in nötr baseline’ıdır. Bütün yüzeye eşit dağılmış kırık su çizgileri ve seyrek kısa taramalar dışında ayrı motif yoktur. Kartın ortası kenarlardan daha koyu, daha boş veya daha düzenli değildir; gözün tutunacağı leke, dört yönlü akıntı, büyük dalga, kaya, köpük veya sığlık işareti bulunmaz.

Bu master hem 30 Açık Deniz hem 12 Kayalık için exact aynıdır. Ön yüzde ne çıkacağını sezdirecek su rengi, çizgi sertliği, kabarma, köpük veya jeolojik iz yoktur.

### Korunacak duygu ve sanatçı payı

**Korunacak duygu:** Henüz okunmamış, tarafsız ve geniş su; rota kararı verilmeden önceki sessiz alan.

**Açık karar alanı:** Sanatçı kısa su çizgilerinin kesin el hareketini ve mikro-aralıklarını yazabilir. Ancak büyük yön, merkez motifi, ayrı leke veya tekrarda tanınacak imza çizgi oluşturamaz.

**İlk eleştiri sorusu:** Tek karta bakınca “arka yüz tasarımı” değil su yüzeyi; 5×5’e bakınca 25 ayrı merkez değil tek deniz alanı okunuyor mu?

### Çizgi, palet ve kenar

- Orta aralıklı kısa/kırık su çizgileri; üç ortak mikro ölçekte dolaşır.
- Kurum indigosu, tuz mavi-grisi, tar grisi ve kemik rezerv; COMMON_MAP_BACK değer baseline’ı.
- Kenar zarfı ortak sistemle aynı; yüzey bleed’e kadar sürer, dekoratif çerçeve yoktur.
- Pas, hardal, kırmızı, kara tonu, parlak köpük ve gradient su yoktur.
- Harita ızgarası, rota, koordinat, ufuk, gemi, kaya ve pusula yoktur.

### 180 derece ve tekrar yapısı

Çok sayıdaki küçük çizgi kümesi yüzeyin uzak bölgelerindeki yarım-dönüş eşleriyle exact dengelenir. Dönüş merkezi sıradan su dokusudur. Radial karşı-akıntı, dört kollu kesişim veya merkez lekesi kullanılmaz. Master tekrarında tanınacak tekil koyu/açık landmark bulunmaz.

### Risk analizi

- **Açık Deniz/Kayalık sızıntısı:** köpük, sivri çizgi, kırıcı dalga, sığlık rengi ve taş taraması reddedilir.
- **Fayans etkisi:** aynı dalga sırası veya merkez koyuluğu her kartta tekrar ederse master reddedilir.
- **Dikiş etkisi:** trimde kesilen uzun çizgi veya kenar değer sıçraması 5×5’i karelere böler.
- **Yön sızıntısı:** baskın çapraz, üstte sakin/altta çalkantılı dağılım veya tek akış yönü yoktur.
- **v2.6 riski:** bu DRAFT v2.7 ortaklığı, kilitli v2.6 dosyalarını değiştirmez.

### Kabul ölçütü

42 kapalı kart içinde Açık Deniz/Kayalık tahmini şans düzeyini aşmaz. Rastgele 180 çevrilmiş 5×5 alanda merkez tekrarı, yön, koyu kare veya kenar kopması görülmeden tek keşfedilmemiş deniz okunur.

## 7. BACK_ISLAND — 6

### Sanat fikri: “Aynı denizin yavaşlayan nefesi”

BACK_ISLAND’da kara resmedilmez. COMMON_MAP_BACK ana denizi bütün yüzeye sürer; yalnız çizgi aralıkları bir mikro-adım genişler ve tuz-grisi alt ton bütün yüzeye çok hafif ısınır. Bu değişim lokal sığlık, merkezî tortu veya kıyı lekesi değildir. Yakında aile hissi yaratır; normal masa mesafesinde ayrı bir renk karesi oluşturmaz.

Ada ailesi “burada kara var” diye bağırmaz. Yalnız keşfedilmemiş denizin başka tür bir eşik ihtimali taşıdığını, sembolsüz ve düşük sesle söyler.

### Korunacak duygu ve sanatçı payı

**Korunacak duygu:** Rahatlama vaadi, gecikme ve kuşkunun henüz açılmamış denizde aynı anda bulunması.

**Açık karar alanı:** Sanatçı ortak su grameri içinde daha geniş nefesi ve hafif tortulu havayı çizgi aralığıyla kurabilir. Kara, sahil, sığlık konturu, renk adası veya merkezî yumuşama kullanamaz.

**İlk eleştiri sorusu:** Yakından Ada ailesi seçilebilirken 5×5’te kart, denizin içindeki ayrı bir madalyon veya “kara burada” işareti gibi görünüyor mu?

### Çizgi, palet ve kenar

- Ortak üçlü mikro-ölçek korunur; ana çizgiler baseline’dan yalnız biraz daha seyrek/geniş nefeslidir.
- Kurum indigosu ve tar grisi aynıdır; çok hafif sıcak tuz-grisi farkı bütün yüzeye eşit dağılır.
- Kenar zarfı BACK_SEA_ROCK ile aynı değer ve çizgi ölçeği aralığında kalır.
- Kara/zeytin kütlesi, kum, turkuaz, kıyı kırığı, gelgit halkası, palmiye, bina ve hazine yoktur.
- Merkez/köşe/kenar arasında “sığlık bölgesi” yaratılmaz.

### 180 derece ve tekrar yapısı

Seyrek çizgi mikro-kümeleri uzak yarım-dönüş eşleriyle exact dengelenir. Merkez sıradan su alanıdır. Çizgi aralığı değişimi bütün yüzeye yayıldığı için dönüşte yön, kıyı ağzı veya ada ekseni oluşmaz. Tekil sıcak leke ve tortu adası yoktur.

### Risk analizi

- **Kara sızıntısı:** herhangi bir kapalı şekil, kıyı çevresi, ada silueti veya merkez boşluğu reddedilir.
- **Ayrı renk karesi:** sıcaklık farkı normal masa mesafesinde kartı seçtirirse azaltılır.
- **Aile kaybı:** yakın mesafede BACK_SEA_ROCK’tan hiç ayrılamıyorsa yalnız çizgi aralığı/tortu alt tonu bir mikro-adım artırılır; ikon eklenmez.
- **Fayans etkisi:** her kartta aynı geniş boşluk landmark gibi tekrarlanamaz.
- **Yön/kesim:** tek yönde uzayan sakin bant ve baskın köşe yoktur.

### Kabul ölçütü

Altı kartın hangi Ada önüne ait olduğu ve yönü öğrenilemez. Yakında aile, daha yavaş/tortulu aynı deniz davranışıyla seçilir; karışık 5×5’te ayrı kara veya renk adası oluşturmadan ortak FOULWAKE denizine karışır.

## 8. BACK_LIGHTHOUSE — 4

### Sanat fikri: “Aynı denizin rüzgârla incelen yüzeyi”

BACK_LIGHTHOUSE’da fener, ateş veya mimari resmedilmez. COMMON_MAP_BACK ana denizi sürer; yalnız yüzeye eşit dağılmış daha ince çapraz-rüzgâr çizgileri ve çok hafif daha soğuk/açık hava değeri kullanılır. Çapraz iz ışın, rota, merkezden yayılım veya yön oku değildir; küçük kümeler halinde kırılır ve exact 180 eşleriyle dağılır.

Aile kimliği bir cihazdan değil, denizin insan yapımı bir işarete yaklaşırken taşıdığı daha açık ve rüzgârla taranmış atmosferden gelir. Bu bir lore kanıtı ya da belirli fenerin hava durumu değildir.

### Korunacak duygu ve sanatçı payı

**Korunacak duygu:** Uzakta bir işaret ihtimali varmış gibi daha açık hava; fakat henüz ışık, kule veya güvenli yön görünmez.

**Açık karar alanı:** Sanatçı ince çapraz-rüzgâr izlerinin kesin el ritmini kurabilir. Radyal kompozisyon, ışın, alev, kule, mekanik kesit, tek parlak nokta veya yönlü beacon kullanamaz.

**İlk eleştiri sorusu:** Yakından Fener ailesi daha ince/rüzgârlı suyla seçilirken, masada ayrı bir parlak kare veya görünmez ışın merkezi oluşuyor mu?

### Çizgi, palet ve kenar

- Ortak üçlü mikro-ölçek korunur; en ince katmanda kırık çapraz-rüzgâr taraması bir mikro-adım artar.
- Kurum indigosu, tuz mavi-grisi, tar grisi ve kemik aynıdır; ortalama değer yalnız çok hafif daha açık/soğuktur.
- Kenar zarfı diğer iki map binarysiyle aynı yoğunluk aralığında kalır.
- Hardal/köz, alev kırmızısı, glow, ışık huzmesi, halka, cam, taş, metal ve mimari iz yoktur.
- Catoptric reflektör, Argand, Fresnel, elektrik, modern beacon, pusula veya rota grafiği yoktur.

### 180 derece ve tekrar yapısı

Çapraz-rüzgâr mikro-kümeleri tek bir baskın diyagonal kurmadan yüzeye dağılır; her kümenin uzak yarım-dönüş eşi vardır. Merkez sıradan su dokusudur. Parlak merkez, radyal açılma, fener odası halkası, ateş ızgarası ve üst/alt hava farkı yoktur.

### Risk analizi

- **Işık/ikon sızıntısı:** parlak nokta, ışın, halka, alev, kule veya rozet reddedilir.
- **Ayrı parlak kare:** ortalama değer farkı 5×5’te kartı seçtirirse azaltılır.
- **Rota/yön sızıntısı:** çapraz çizgiler tek koridor veya yön oku kuramaz.
- **Aile kaybı:** yakın mesafede ayrım yetersizse yalnız ince rüzgâr katmanı bir mikro-adım artırılır; nesne eklenmez.
- **Dönem riski:** arka yüzde teknoloji göstermemek dönem hatasını da bilgi sızıntısını da önler; modern kartografi dili yine yasaktır.
- **Fayans etkisi:** aynı parlak açıklık veya çapraz küme her kartta landmark gibi görünemez.

### Kabul ölçütü

Dört kartın belirli fener kimliği ve yönü öğrenilemez. Yakında aile ince/rüzgârlı aynı deniz davranışıyla seçilir; karışık ve rastgele 180 çevrilmiş 5×5’te ışık, kule, parlak kare veya radyal amblem oluşturmadan ortak denize karışır.

## 9. BACK_SUPPORT — 3

### Sanat fikri: “İki rıhtım, bir boş merkez”

İki karşıt yönde exact eşli taş rıhtım babası ve aralarında merkezi boş bırakan tek kenevir palamar halkası. Merkezde kişi, sandalye, liman adı, anahtar veya mühür yoktur. Bu boşluk Kalkış, Varış ve Kaptan Makamı için ortak olan “işlevin insan/yer değişse de kalması” fikrini taşır.

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

Üç kart aynı kurumsal destek ailesi olarak hissedilir; Kalkış, Varış veya Kaptan Makamı ayrımı ve yönü arka yüzden öğrenilemez.

## 9A. Zorunlu harita-masası QA kanıtları

Bu brief mockup üretmez. Görsel üretim yetkisi verilirse Görsel Tasarım aşağıdaki on kanıtı birlikte teslim eder:

1. BACK_SEA_ROCK, BACK_ISLAND ve BACK_LIGHTHOUSE’ın birlikte kullanıldığı kapalı 5×5 masa mockup’ı.
2. Aynı kartların rastgele 180 derece çevrildiği ikinci 5×5 mockup.
3. Belgelenmiş normal masa bakış mesafesinden bütünlük incelemesi.
4. Kart birleşimlerinde kenar, dalga ölçeği, çizgi yoğunluğu ve değer kopması yakın incelemesi.
5. Merkezî şekil, amblem, madalyon veya tekrar eden göz alıcı leke kontrolü.
6. BACK_SEA_ROCK için Açık Deniz/Kayalık kör sınıflandırma testi.
7. Ada ve Fener binarylerinin yalnız amaçlanan aile bilgisini taşıdığı, belirli kart kimliğini sızdırmadığı kontrol.
8. Okunabilir yazı, sayı, yön, koordinat, rota, pusula ve anlamsız script kontrolü.
9. Mat baskıda koyu kare, parlaklık farkı ve kart-başına tanınabilir leke kontrolü.
10. Birkaç kabul edilmiş ön yüz açılarak hazırlanan “keşif sonrası masa” mockup’ı.

Ek değerlendirmeler:

- 5×5 görsel hem net hem hafif bulanık/squint görünümde incelenir; bulanık görünümde 25 koyu merkez veya üç renk adası çıkmamalıdır.
- Düz ve 180 çevrilmiş örnekler yan yana gösterilir; bütünlük yalnız tek yönlü dizilimde çalışıyorsa sonuç FAIL’dir.
- Açık Deniz/Kayalık tahmini şans düzeyini anlamlı biçimde aşarsa BACK_SEA_ROCK FAIL’dir.
- Aile bilgisi yakın mesafede seçilemezse mikro-fark düzenlenebilir; çözüm hiçbir aşamada ikon, merkez motif veya renk rozetiyle güçlendirilemez.

Kabul cümlesi: **Kart adları ve tekil sınırlar uzaktan seçilmeden önce masa, üzerinde bazı kartlar duran bir alan değil; parça parça keşfedilen tek bir FOULWAKE denizi gibi görünmelidir.**

## 10. Binaryler arası çakışma kontrolü

| Binary | Uzakta algı / masa rolü | Yakında maddi imza | Kaçınacağı komşu |
|---|---|---|---|
| CHARACTER | Bez oval + çift halat S | İş aşınması izleri | LOYALTY’nin kapalı düğümü |
| POWER | İki uçtan kapalı rulo | Yağlı bez + pas | SUPPORT’ın açık merkezi |
| LOYALTY | Kapalı koyu keten + çift bağ | Nötr düğüm | CHARACTER’ın iş izleri |
| SEA_ROCK | Ortak harita denizinin nötr baseline’ı; büyük biçim yok | Orta aralıklı kırık su çizgisi | ISLAND/LIGHTHOUSE mikro-farklarının aşırı büyümesi |
| ISLAND | Aynı denizde bir mikro-adım yavaş/tortulu nefes | Biraz geniş çizgi aralığı + hafif sıcak tuz-grisi | Kara lekesi, gelgit madalyonu ve ayrı renk karesi |
| LIGHTHOUSE | Aynı denizde bir mikro-adım ince/rüzgârlı hava | Kırık çapraz-rüzgâr izi + hafif soğuk/açık değer | Işık, radyal amblem ve ayrı parlak kare |
| SUPPORT | İki rıhtım babası + boş merkez | Taş + palamar | POWER’ın kapalı rulosu |

Yedi arka yüz aynı mat kâğıt, ana mürekkep ve el çizgisi ailesini paylaşır. Karakter, Güç, Sadakat ve Yardımcı yönleri f0389711… kabulüyle korunur. Üç harita binarysinde ayrım büyük motiften değil, ortak deniz içindeki düşük şiddetli su davranışından gelir. Renk körlüğü ve mat baskı koşulunda yakın aile ayrımı korunmalı; normal masa mesafesinde ise üç harita binarysi tek alan olarak birleşmelidir.

## 11. Üretim ve hash disiplini

Onaydan sonra Görsel Tasarım her binary için tek master üretir ve:

- dosya adını binary kimliğiyle eşler;
- her fiziksel kopyayı aynı masterdan türetir;
- flattened dosya hashini manifestte bir kez kaydeder;
- 180 rotate/difference kanıtını saklar;
- baskı lotu, kâğıt ve vernik bilgisini ayrı teknik raporda tutar;
- hiçbir karta kart-başına random distress eklemez;
- test baskısı başarısızsa sanat dosyasını revize eder, kart kopyalarını ayrı ayrı “düzeltmez”.

Üç harita masterı ayrı ayrı değil, aynı COMMON_MAP_BACK_VISUAL_SYSTEM sürümü altında birlikte teslim edilir. Teknik pakette üç hash ile birlikte iki kapalı 5×5 mockup, normal-mesafe/kenar incelemesi, kör sınıflandırma sonucu ve keşif-sonrası masa mockup’ı aynı kanıt setinde bulunur. Aile masterları tek tek geçse bile ortak masa QA’sı başarısızsa harita arka-yüz paketi FAIL’dir.

Bu targeted rework dosya formatı, DPI, bleed veya ICC profilini kilitlemez; bunlar Görsel Tasarımın teknik üretim ve Baş Editör entegrasyon alanıdır. Sanat fikri, masa bütünlüğü ve sızıntı riskleri bağlayıcı brief olarak sunulur.

## 12. Dispozisyon

ART_DIRECTION_STAGE: BRIEF  
INPUT_VISUAL_BRANCH: NONE — BRIEF STAGE  
INPUT_VISUAL_COMMIT: NONE — BRIEF STAGE  
INPUT_CONTACT_SHEETS: NONE — BRIEF STAGE  
CREATIVE_VERDICT: TARGETED_MAP_BACK_REWORK_DELIVERED / PENDING_PROJECT_OWNER_AND_CHIEF_EDITOR_REVIEW  
PROJECT_OWNER_DECISION_REQUIRED: YES  
FINAL_VISUAL_AND_PDF_OWNER: Görsel Tasarım — NOT AUTHORIZED  
INTEGRATION_AND_DISPOSITION: Baş Editör  
LOCK_REQUESTED: NO
