# FOULWAKE ART DIRECTION BIBLE v2.7

Status: OWNER RESET / KAPTAN VISUAL+COPY / FRAMING GATE / VISUAL PRODUCTION PAUSED  
Workstream: Sanat Yönetimi  
Source branch: work/v2.7-art-direction  
Current authority: governance/CURRENT_STAGE.json / STAGE-20260830-KAPTAN-FRAMING-PATCH-CORRECTION  
Baseline: v2.6 STABLE / LOCKED  
Historical accepted brief source: work/v2.7-art-direction@7418d9c2c89c265cb6efd30f6a5a7f2addd528da  
Project Owner override: KAPTAN uploaded-card source; copy lock; framing gate; three back reworks  
Visual production authorized: NO  
Current write scope: only the existing KAPTAN patch correction; this Bible is an integrated source contract, not an authorization.

## 1. Yetki, kaynak ve sınır

Bu belge FOULWAKE’ın görsel dünyasını tarif eder; kart kimliğini, exact metni, mekaniği, lore’u, governance’ı veya release statüsünü değiştirmez. Sanat Yönetimi yalnız working/v2.7/visual/art_direction/** altında brief üretir. Final görsel ve PDF üretimi Görsel Tasarımın; nihai estetik kabul proje sahibinin; entegrasyon ve dispozisyon Baş Editörün alanıdır.

Bağlayıcı okuma sırası:

1. AI_HANDOFF.md ve releases/v2.6/** — kilitli mekanik, kart sayıları ve değişmemiş aileler.
2. working/v2.7/FOULWAKE_CARD_TEXTS_v2.7.json — v2.7 Karakter ve Güç görünür metni.
3. working/v2.7/FOULWAKE_RULEBOOK_STORY_v2.7.md — izinli anlatı katmanı.
4. working/v2.7/FOULWAKE_STORY_FRAMEWORK.md — ton ve lore kısıtları; release canon yaratmaz.
5. FOULWAKE_ART_DIRECTOR_WORK_ORDER_v2.7.md, FOULWAKE_FULL_DECK_ART_REWORK_DIRECTIVE_v2.7.md ve FOULWAKE_VISUAL_SYSTEM.md — sanat, sunum ve baskı çerçevesi.

Kaynak riski SRC-002 açık tutulur: aktif v2.7 metin kaynağı GUC-22’yi Kaptanın Çatlak Kupası, GUC-23’ü Bayat Peksimet olarak tanımlar; bazı v2.6 kayıtları GUC-22’yi Bayat Peksimet gösterir. Bu belge aktif v2.7 exact metnini kullanır, fakat çatışmayı çözmüş veya kilitlemiş sayılmaz.

work/v2.7-visual@e91581bb336dfcbab5da1d48a256577f9251f891 içindeki sanat bütünüyle REJECTED_ART / TECHNICAL_PIPELINE_REFERENCE_ONLY’dir. Yalnız 121 kimliğin kilitli PDF envanteriyle eşlenmesini doğrulayan teknik indeks olarak kullanılmış; kompozisyon, karakter, renk, ışık, nesne, çizgi veya mizah kaynağı yapılmamıştır.

Yüklenen KAPTAN kartı `SET-KP-01` için bağlayıcı ana görsel ve copy kaynağıdır.
KAPTAN figürü ile ana kompozisyon korunur; yalnız küçük crop, ölçek, renk veya
arka-plan temizliği yapılabilir. Boş sandalye ya da başka özneyle değiştirilemez.
Aynı kart bütün deste için eski baskı, kalın mürekkep, yoğun gravür taraması,
sıcak kirli kâğıt ve mat lacivert–oker–pas dili anahtarıdır. Gemi ve martı diğer
kartlarda kopyalanmak zorunda değildir. Exact copy
`working/v2.7/FOULWAKE_OWNER_CARD_TEXT_OVERRIDES_v2.7.json` kaynağındadır.

## 2. Tek cümlelik sanat tezi

FOULWAKE, kahraman korsanların değil; birbirinin tanıklığına muhtaç ama ondan emin olamayan insanların, ıslak bir gemiyi seçimlerle ayakta tuttuğu ve tuzun her karara fiziksel bir bedel eklediği aşınmış deniz anlatısıdır.

### 2.1 Sanat Yönetmeninin bakışı

Sanat Yönetmeni bu projede 121 resmi uzaktan tarif eden bir “prompt yazarı” değildir. Görevi, her görsel için dört şeyi korumaktır:

1. **Duygusal hakikat:** oyuncunun kartı ilk gördüğünde ne hissetmesi gerektiği.
2. **Oyun hakikati:** resmin, mekaniği açıklamadan oyundaki karar baskısını nasıl taşıdığı.
3. **Dünya hakikati:** insan, gemi, deniz ve nesnenin aynı 1721 maddi dünyasına ait olması.
4. **Deste hakikati:** tek resim güzel olsa bile 121 kart içinde tekrar, gürültü veya yanlış vurgu üretmemesi.

Brief, “şurada şu açıyla tam olarak bunu çiz” diye kapalı bir çekim listesi kurmamalıdır. Önce **neyin doğru kalacağını**, sonra **neyin kesinlikle söylenmeyeceğini** tarif eder; çözümün önemli bir bölümünü sanatçıya bırakır. Sanatçı bu sınırlar içinde yalnız uygulayıcı değil, görsel yazar ve gözlemcidir. Sanat Yönetmeni sanatçının daha iyi çözümünü tanıyabilmeli, briefteki ilk nesne veya kadraj fikrini sırf kendisi yazdı diye savunmamalıdır.

Bu nedenle 121 manifestteki kadraj, nesne ve beden çözümleri üç farklı statüde okunur:

- **BINDING:** exact kimlik/mekanik, ilk duygu, tek ana fiil, spoiler ve dönem sınırı.
- **COLLISION_GUARD:** başka kartla karışmayı önleyen yaş, siluet, iş izi ve ritim koordinatları.
- **STARTING_VECTOR:** kamera, mikro-jest, hava, ikincil nesne ve çizgi yoğunluğunun ilk savunulabilir yönü; sanatçı daha iyi bir çözüm getirirse değişebilir.

### 2.2 Tat çekirdeği: “Islak Tanıklık”

“Islak Tanıklık” yalnız ekip içi bir eleştiri terimidir; oyun içi isim, slogan, logo, kart yazısı veya pazarlama ifadesi değildir.

Her ön yüz, olaydan sonra kuru bir odada uydurulmuş korsan resmi gibi değil, olayın ağırlığına yakın durmuş bir gözün eksik tanıklığı gibi hissettirmelidir. Göz **neyin olduğunu** seçer; fakat çoğu zaman **neden olduğunu**, kimin haklı olduğunu veya bir sonraki sonucun ne olacağını bilemez.

Bu tat şu karşılıklardan doğar:

- Ufuk ve gemi kütlesi gözleme dayanır; dekoratif eğrilik veya rastgele “eski zaman” bozulması kullanılmaz.
- Su, duman, bez ve insan bedeni aynı rüzgârı taşır; atmosfer sonradan yapıştırılmış filtre değildir.
- Çizgi kusursuz dijital kabuk değil, karar alan bir elin izi gibi canlıdır; ancak küçük ölçekte çamura dönüşmez.
- Kâğıt, kurum, yağlı parmak, su yolu ve ip sürtünmesi insan kullanımını hissettirir; rastgele grunge değildir.
- Olay görünür, hüküm eksik kalır. Bir el yararlı olabilir; niyeti okunmaz. Bir liman yakın olabilir; zafer değildir. Bir mühür gerçek olabilir; faili kanıtlamaz.
- En güzel ayrıntı çoğu zaman “büyük lore ipucu” değil; yük altında açılan el, ıslak bezin omzu çekişi, bordada birikmiş tuz veya yanlış anda boş kalan bir sandalyedir.

Bu yaklaşım, eski deniz çizimlerinin yerinde gözlem ve tanıklık niteliğinden beslenir; belirli bir sanatçının stilini kopyalamaz. Hedef “gravür efekti” değil, gözlemin çizgiye dönüşmesidir.

### 2.3 Oyunun masa deneyiminden türeyen görsel ilkeler

Kural kitabı görsel dünyanın dekorunu değil, bakışını belirler. FOULWAKE’ta oyuncu sürekli eksik bilgiyle, başkalarının anlatısıyla ve geri alınamayan ortak kararla yaşar.

| Masadaki gerçek | Görsel sonuç |
|---|---|
| Yakın Ufuk hakkında bilgi özel olabilir; anlatan kişi yalan söyleyebilir | Resim olayı okunur kılar, nedeni ve ahlaki hükmü açık bırakır |
| Rota açık tartışma ve eşzamanlı oyla seçilir | Eller, bakış eksenleri, boşluklar ve nesne yönleri sosyal basıncı taşır; yüzler “iyi/kötü” diye kodlanmaz |
| Kaptan iki oy taşır ama Sadakati kanıtlanmaz; makam değişebilir | Güç karizmatik portreden değil, mekânsal ağırlık, erişim ve devredilen nesneden doğar |
| Gemi yalnız iki Gövde dayanımına sahiptir | Ağır hasar slapstick değildir; küçük çatlak bile yapısal sonuç ve sessizlik taşır |
| Çürümüş Erzak adayı zorunlu kılabilir | Ada yalnız ödül/cennet değildir; rahatlama, gecikme ve kuşku aynı sahnede bulunabilir |
| Limana varmak yetmez; Liman Gecesi sağ çıkılmalıdır | Varış kartları final güneşi veya zafer resmi değil, eşik ve bekleyiştir |
| Sadakat ölümde dahi açılmaz | Yüz, ten, giysi, ışık, hayvan veya ortak amblem hiçbir insanı peşinen ele vermez |
| Moderatör atmosfer kurar ama şüphe üretmez | Hava ve malzeme gerilim yaratır; gizli ipucu, spot kanıt veya “kötü gölge” yaratmaz |
| Harita yolu değil, masadaki tartışmayı değiştirir | Coğrafya yalnız manzara değildir; bedensel karar, erişim ve risk geometrisidir |

### 2.4 Bağlayıcı niyet / sanatçı yorum alanı

Her brief aşağıdaki sözleşmeyle okunur:

| Sanat Yönetiminin koruduğu | Sanatçının yorumlayabildiği |
|---|---|
| Exact kart kimliği, kaynak metni ve mekanik gerçek | Exact metni resme yazmadan, aynı gerçeği taşıyan mikro-hikâye |
| İlk iki saniye duygusu ve tek ana hareket | Jestin anatomisi, hareketin anı, yüzün mikro-ifadesi |
| Karakter matrisi ve diğer kartlardan ayrışma | Matrise zarar vermeyen yüz ayrıntıları, saçın doğal düzensizliği, giysinin kişisel kullanımı |
| Dönem, malzeme, teknoloji ve gerçek mekân | Döneme uygun eşdeğer nesne, hava durumu ve yerel aşınma |
| Deste ritmindeki ölçek/değer görevi | Aynı ritim görevini koruyan kamera yüksekliği ve kırpma |
| Yazısızlık, spoiler vermeme, mizah sınırı | Ana olaya rakip olmayan tekil insan gözlemi veya sessiz ayrıntı |
| Arka yüzde aile aynılığı ve bilgi güvenliği | Güvenlik testlerini geçen çizgi karakteri ve maddi yüzey çözümü |

Manifestteki bütün ayrıntılar eşit derecede “kilitli çekim” değildir. Bir sanatçı nesne listesini eksiksiz uygulayıp duyguyu kaçırırsa brief başarısızdır; bazı nesneleri daha iyi bir görsel cümleyle değiştirip duygu, mekanik, dönem ve ayrışmayı korursa çözüm değerlendirmeye değerdir.

### 2.5 İsimden bağımsız görsel omurga

Arden, San Cordelio, Saint Verena, Veyr, Gusto ve Siyah Mühür mevcut metindeki çalışma adlarıdır ve bu sürümde exact kaynak olarak korunur. Fakat FOULWAKE’ın görsel kimliği bu sözcüklerin yazılışına, baş harfine, armasına, renk koduna veya tekil mimari logosuna bağlanmaz.

Görsel çözüm şu işlevlere dayanır:

- **salgın baskısı altındaki kalkış bölgesi;**
- **karantina eşiğindeki hedef liman;**
- **yarar mı zarar mı vereceği kanıtlanmamış hassas yük;**
- **akıbeti çözülmemiş kayıp komuta figürü;**
- **varlığı ihtimal olan fakat kesin görsel markası olmayan düşmanca ağ;**
- **oyuncuların verdiği, geri alınamayan rota kararı.**

Bir özel isim yarın değiştiğinde resim anlamsızlaşıyorsa çözüm fazla literal kurulmuştur. Liman adı okunmaz; arma üretilmez; “Siyah” sözcüğü siyah paleti mecbur etmez; geçici lore adı bütün desteye motif olarak yayılmaz. Exact isimler dosyada kaynak izlenebilirliği için kalır, estetik kilit olmaz.

### 2.6 FOULWAKE’ın lezzeti

FOULWAKE’ın tadı **“dünya ciddi; insanlar her zaman kusursuz değil”** gerilimindedir.

- Deniz kötü değildir; kayıtsızdır. İnsanların verdiği kararları büyütür ama ahlaki hüküm vermez.
- İnsanlar “korsan tipi” değil, işi bedene yazılmış bireylerdir. Omuz, parmak, işitme, uyku, yaş, alışkanlık ve yanlış ölçülmüş özgüven karakter yaratır.
- Kurumlar kuru değildir; ıslanır, kabarır, gecikir, yine de işlemeye devam eder. Kuru mizah buradan çıkabilir.
- Güzellik gösterişli kahramanlıktan değil, malzeme doğruluğu ile insan kırılganlığının aynı karede bulunmasından doğar.
- Deste sürekli bağırmaz. Bazı kartlar neredeyse yalnız su, gök ve tek bir gerilim çizgisidir; bazıları sıkışık beden ve eşya örgüsüdür. Sessizlik de sanat kararıdır.
- “Karanlık” olmak, her şeyi siyaha boyamak değildir. Açık gök altında verilen kötü karar, zifiri ambar kadar huzursuz olabilir.
- Mizah punchline değildir; dünya ciddiyetini korurken insan davranışının bıraktığı küçük tortudur.

### 2.7 Araştırma ve görsel soy — kopya değil yöntem

Bu yön aşağıdaki kaynaklardan **stil kopyalamak için değil**, çalışma yöntemini sınamak için yararlanır:

- Magpie Games’in sanat yönetimi süreci: sanat notunu üretim spesifikasyonuna dönüştürme, eskiz/final onayı ve sanatçı koordinasyonu.  
  https://magpiegames.com/blogs/news/art-director-process-outline
- Matt Paquette’in masaüstü oyunlarında sanatçıyla çalışma yaklaşımı: zorunlu çekirdeği netleştirirken sanatçının daha iyi çözüme gitmesine izin verme.  
  https://www.mattpaquette.com/design-blog/2018/7/15/art-direction-for-tabletop-games-working-with-artists
- Daniel Solis’in masaüstü oyunlarında sanatın öğretim/oyun kolaylığı işlevi ve sanat yönetmeni–sanatçı ilişkisini editör–yazar ilişkisine benzeten uygulama notları.  
  https://www.reddit.com/r/tabletopgamedesign/comments/25dpdv/im_a_graphic_designer_and_art_director_for/
- Uygulayıcı forum tartışmaları: yapısal geri bildirimi renderdan önce verme, kartı gerçek ölçekte değerlendirme ve ayrıntılı brief ile yaratıcı özgürlük arasındaki denge.  
  https://www.reddit.com/r/tabletopgamedesign/comments/1e8jg14/i_dont_like_the_result_of_my_artist_how_do_i_tell/
- Royal Museums Greenwich’in Van de Velde deniz çizimleri: yerinde gözlem, ufuk disiplini, hızlı tanıklık çizgisi ve sonradan ayrıntılı mürekkep çalışmasına dönüşen süreç.  
  https://www.rmg.co.uk/stories/art-culture/sea-drawings-art-van-de-veldes/war-artist
- Royal Museums Greenwich’in karantina ve gemide sağlık arşivleri: karantinanın tek bir “veba ikonu” değil, bekleme suyu, yük usulü ve idari altyapı olarak görünmesi.  
  https://www.rmg.co.uk/stories/maritime-history/library-archive/quarantine-never-ending-story

Bu kaynaklar FOULWAKE’a dışarıdan tema eklemez. Exact oyun, hikâye ve governance kaynakları bağlayıcı kalır.

## 3. v2.7 anlatısal görsel omurga — işlev esaslı, isimden bağımsız

Aşağıdaki özel isimler mevcut exact kaynakla konuşmak ve kartları izlemek için korunur; tekrar eden logo, renk kodu, mimari marka veya görsel evrenin taşıyıcı motifi değildir. İsim değişse de salgın baskısı, karantina eşiği, belirsiz yük, kayıp komuta ve çözülmemiş düşmanca irade işlevleri ayakta kalmalıdır.

Bu omurga 121 kartın tamamına serpiştirilecek bir lore deseni değildir. Yalnız kimliği ve mekânı doğal olarak taşıyan kartlarda görünür; diğer kartlara siyah balmumu, sandık, hasta bedeni veya Gusto izi eklenmez. Amaç gizemi çözmek değil, seferin neden ağır olduğunu maddi ve kurumsal zeminde hissettirmektir.

### 3.1 Arden’deki veba baskısı

Veba dekoratif ceset, hastalık makyajı veya yeşil “zehir sisi” olarak kullanılmaz. Baskı; karantina demir yeri, sağlık kâğıdı, mühür kontrolü, uzayan yük sırası, taze erzak yokluğu, kapalı lazaretto penceresi ve borç/tedarik altyapısıyla görünür. İnsan acısı şakanın nesnesi değildir. Kuru mizah varsa sağlık usulünün dünya parçalanırken de işlemeye devam etmesinden doğar.

### 3.2 San Cordelio — Saint Verena yük ekseni

San Cordelio’dan Saint Verena’nın şehir dışındaki karantina demir yerine deneysel tiryak sandıkları ile demir köşeli küçük formül kutusu taşınır. Sandık ve kutu yalnız gerekli kartlarda görünür; bütün destenin tekrar eden “gizemli yük” maskotu olmaz.

- Sahne içinde okunabilir İLAÇ etiketi veya yeni metin yoktur.
- Sandıklar modern ilaç kasası, laboratuvar kabı veya parlayan görev nesnesi gibi görünmez.
- Saint Verena’ya ulaşmak tedavinin başarılı olduğunu göstermez; gemi karantina eşiğinde bekler.
- SET-KL-01 yükleme/ayrılış, SET-VL-01 karantina eşiği, SAD-T-10 yük sorumluluğu üzerinden ekseni taşır.

### 3.3 Veyr terkibinin tedavi/zehir belirsizliği

Veyr’in terkibi görsel olarak “iyi ilaç” veya “kesin zehir” diye kodlanmaz. Şifa için beyaz-altın ışık, zehir için yeşil/siyah duman, iyileşmiş hasta, ölü denek, kafatası veya simyasal amblem kullanılmaz. Kapalı yük, başarısız/eksik kayıt ve bekleyen sağlık usulü aynı anda hem ihtimali hem riski taşır. Görsel hiçbir sonucu deneysel iddiadan kanıta yükseltmez.

### 3.4 Gusto’nun kayboluşu

Gusto yalnız yoklukla karşılık bulabilir: boş kalan komuta yeri, sahibi belirlenemeyen eksik sayfa lifleri veya devredilen makam. Bedeni, kaçış rotası, saldırganı, satın alınışı, ölümü, gemide saklanması veya gerçek Sadakati resmedilmez.

- SET-KP-01’in boş makamı Gusto’nun kaderini değil, vekilsiz yokluğun kurumsal sonucunu gösterir.
- GUC-13’teki eksik sayfalar defterin Gusto’ya ait olduğunu veya sayfaları kimin aldığını kanıtlamaz.
- Gusto’ya ait ayırt edici yüz/siluet başka kartlarda “gizli ipucu” olarak tekrarlanmaz.

### 3.5 Siyah balmumu ve Siyah Mühür sınırı

Siyah Mühür kesin örgüt logosu, ortak üniforma, Hain işareti veya kusursuz suç zinciri değildir. Koyu balmumu yalnız karta doğal olarak gerekiyorsa görünür; kurum, katran veya sıradan eski balmumundan kesin ayrışmaz. Emblem, harf, hayvan, geometri veya her Hain kartında tekrar eden renk kodu taşımaz.

- GUC-18’de mühür emblemsiz ve kaynağı belirsizdir.
- Sadakat kartlarında ortak siyah balmumu, eşleşen bileklik veya örgüt üniforması yoktur.
- BACK_LOYALTY ve diğer arka yüzlerde siyah balmumu bulunmaz; Tayfa/Hain veya belirli kart sızıntısı yaratmaz.
- Siyah balmumu spot ışıkla “işte kanıt” diye izole edilmez.

### 3.6 CAN-03 / CAN-04 çözmeme kapısı

Her anlatısal uygulama şu iki soruyu geçmelidir:

1. Görsel Siyah Mühür’ü tek merkezli kesin suçluya, ortak logoya veya eksiksiz kanıt zincirine dönüştürüyor mu?
2. Görsel Gusto’nun kaderini, rolünü veya Sadakatini kesinleştiriyor mu?

Sorulardan birine “evet” çıkarsa ayrıntı kaldırılır. Belirsizlik bulanıklık değil, birden çok maddi açıklamanın açık kalmasıdır.

### 3.7 Karta sınırlı uygulama haritası

| Kart | İzin verilen yazısız karşılık | Kesinlikle kanıtlamayacağı şey |
|---|---|---|
| SET-KL-01 | Mühürlü tiryak sandıkları, küçük demir köşeli kutu, Gusto’suz ayrılış düzeni | Okunabilir İLAÇ, kaçırılma, Siyah Mühür saldırısı |
| SET-VL-01 | Dış karantina demir yeri, kapalı yük, uzaktan sağlık kayığı | Tedavi başarısı, zehir sonucu, tamamlanmış zafer |
| SET-KP-01 | Boş ve devredilen makam | Gusto’nun ölümü/kaçışı, yeni Kaptanın Sadakati |
| GUC-13 | Okunamayan, yaprakları eksik eski seyir defteri | Defterin kesin sahibi, sayfaları alan kişi |
| GUC-18 | Emblemsiz kurum-koyu sıradan balmumu | Tek örgüt, Hain kimliği, kesin Siyah Mühür |
| SAD-T-10 | Saint Verena’ya taşınan tek kapalı tiryak sandığı | Terkibin iyi/kötü oluşu |
| SAD-H-01…05 | Yük ve karantina görevinin artırdığı farklı baskılar | Ortak merkez, ortak amblem, aynı motivasyon |

Diğer 110 kart, kendi exact kimliği gerektirmiyorsa bu omurgadan hiçbir nesne almaz.

## 4. FOULWAKE’ı jenerik korsan estetiğinden ayıran dünya hissi

FOULWAKE’ın ana sahnesi “macera” değil, işleyen fakat her an bozulabilecek deniz düzenidir. Dünya üç eşzamanlı basınç taşır:

- Deniz fiziksel olarak üstün: su ağırdır, rüzgâr yön değiştirir, ahşap şişer, tuz bağları yer, sis bilgi üretmez.
- Kurumlar kırılgandır ama gerçektir: Kaptanlık, vardiya, gümrük, oy, zabıt ve liman düzeni insanlardan uzun yaşar.
- Mizah sonuçtan değil sürtünmeden çıkar: yetki ile araç, niyet ile beden, resmî usul ile ıslak gerçeklik birbirine tam oturmaz.

Görsel dünya şu kolay kodlardan uzak durur:

| Jenerik korsan kısayolu | FOULWAKE karşılığı |
|---|---|
| Kafatası, hazine, göz bandı, tropik kartpostal | Islak yük rampası, karantina kazığı, balast, sintine, onarım kaması |
| Tek karizmatik kaptan | Açık ve değişebilir makam; işi taşıyan farklı bedenler |
| Sürekli kavga ve zafer pozu | Karar öncesi durak, ekipman basıncı, eksik bilgi, görev hareketi |
| Parlak altın ve doygun mavi | Oksitli pirinç, donuk hardal, kurum indigosu, tuz grisi |
| Neşeli hayvan maskotları | Yalnız kartın exact kimliği gerektirdiğinde tekil, doğal hayvan davranışı |
| “Eski” görünmek için rastgele lekeli parşömen | Malzemeye bağlı, nedensel aşınma: su yolu, ip sürtünmesi, kurum yönü, baskı kayması |

Tarih duygusu müze temizliği de kostüm tiyatrosu da değildir. İnsanlar 1721’i “oynamaz”; o yılın aletleriyle, bilmedikleri sonraki teknolojiler olmadan çalışır.

## 5. Maddi dünya: tuz, pas, kurum, ıslak ahşap, bez ve eski baskı

Her yüzey kendi yaşama biçimini taşır. Genel “grunge” filtresi yasaktır.

| Malzeme | Görsel davranış | Çizgi davranışı | Kaçınılacak şey |
|---|---|---|---|
| Tuz | Kenarda kristal kabuk, kumaşta beyaz sertleşme, ciltte ince iz | Kesik açık rezerv, kısa kırılmalar | Rastgele beyaz benek spreyi |
| Pas / oksit | Bağlantıdan aşağı akan yerel leke, sürtünmede açılan metal | Sık kısa paralel + birkaç akış çizgisi | Turuncu neon, her metali aynı pas |
| Kurum / katran | Isı ve duman kaynağında yoğunlaşan mat siyah | Çapraz taramanın en koyu katı | Saf dijital siyah blok, plastik parlaklık |
| Islak meşe | Damar boyunca koyulaşma, ek yerinde şişme, kenarda su | Uzun lif çizgisi + yerel koyu temas | Kahverengi düz dolgu, mobilya cilası |
| Kenevir halat | Büküm yönü okunur, tuzla sert, temas yerinde tüylenmiş | Çift sarmal kontur + kısa lif | Sentetik düzgün ip, dekoratif düğüm kalabalığı |
| Keten / yün / yelken bezi | Kat, dikiş, gerilme ve ıslak ağırlık farklıdır | Geniş açık alan + dikişe yakın yön taraması | Foto-gerçek kumaş dokusu, bembeyaz bez |
| Kâğıt / balmumu | Nemle kabarma, parmak ve kurum izi, çatlamış mühür | Lifin seyrek çizgisi, yazısız yüzey | Okunabilir sahne-içi metin, sahte font |
| Taş | Jeolojiye özgü katman, kırık ve su aşınması | Bazaltta dik kırık; kumtaşında yatay tabaka | Her kayayı sivri fantastik dağ yapmak |
| Cilt | Yaş, güneş, iş ve hastalık izleri; karikatür “kir” değil | Formu izleyen kısa tarama | Aynı burun, aynı çene, aynı kırışık şablonu |

Aşınma yereldir. Menteşe çevresi, halat temas çizgisi, su oluğu, avuç izi ve dikiş gibi nedenler görünür olmalıdır. Doku, kompozisyonun yerine geçmez.

## 6. Çizgi, kontur, çapraz tarama ve gravür dili

### 6.1 Ana ilke

Hacim boya gradyanıyla değil, kontur ağırlığı, çizgi yönü, tarama yoğunluğu ve kâğıt rezerviyle kurulur. İzleyici önce büyük değer kütlesini, sonra ana hareketi, sonra maddi ayrıntıyı okur.

### 6.2 Kontur hiyerarşisi

- Birincil siluet: en koyu ve kesintisiz; ancak bütün çevreyi kalın çizgiyle çevirmez. Işık alan kenarda kırılabilir.
- İkincil form: birincilin yaklaşık yarı ağırlığı; kol, yelken katı, kaya tabakası, sandık kapağı.
- Malzeme çizgisi: kontur değildir; lif, dikiş, pas, tüy, su yönü.
- Atmosfer çizgisi: uzaklık arttıkça seyrelir; sis içinde nesne “blur” edilmez, çizgi sayısı fiziksel olarak azalır.
- Mikro ayrıntı: yalnız odağa yakın yerde; her köşeyi eşit ayrıntılandırmak yasak.

### 6.3 Tarama sözlüğü

- Ahşap: yapısal lif yönünde uzun, kesintili; hasarda lif açılır.
- Metal: kısa, kontrollü paralel; koyu değer yalnız ek/oyukta.
- Kumaş: gerilim yönünü izleyen geniş aralıklı; kat altında çapraz ikinci kat.
- Cilt: yüz anatomisini ve beden hacmini izleyen kısa eğriler; kir efekti gibi serpilmez.
- Su: hava durumuna göre yatay, diyagonal veya spiral; aynı “dalga fırçası” bütün kartlara uygulanmaz.
- Sis/gök: çoğu zaman çizgisiz kâğıt rezervidir; atmosferi doldurmak için dijital pus tabakası kullanılmaz.
- Kaya: jeolojiye göre yönlü; yüzeyi yalnız nokta doldurarak taş yapmak yasaktır.

Moiré ve baskı çamuru riski için çok ince, eş aralıklı dijital crosshatch kullanılmaz. Tarama aileleri elde küçük sapma gösterir; çizgiler mekanik filtre gibi kusursuz tekrarlanmaz.

## 7. Mat palet ve vurgu mantığı

Temel palet hedefi şöyledir; bunlar baskı öncesi renk yönetiminin yerine geçen kilitli CMYK değerleri değildir.

| İşlev | Önerilen referans | Kullanım |
|---|---:|---|
| Kâğıt / kemik ışık | #D7C39B / #E1D2AE | Zemin, ışık rezervi, açık bez; “parlak beyaz” değildir |
| Ana mürekkep | #1B201F | En koyu kontur, katran, derin iç mekân |
| Deniz indigosu | #23333A | Su, gece, lacivert giysi; siyaha komşu mat kütle |
| Tuz mavi-grisi | #68777A | Uzak su, sis içi form, taşın soğuk yüzü |
| Pas kahvesi | #7B4B32 | Ahşap yarası, oksit, ciltte yerel sıcaklık |
| Islak meşe | #5A4635 | Güverte, gövde, sandık; tek düz kahve değildir |
| Donuk hardal | #B07A26 | Pirinç, yağ alevi, küçük odak |
| Sinyal kırmızısı | #8C3A2B | Balmumu, tek düğüm/manşet, etik gerilim odağı |
| Küf zeytini | #59604A | Erzak, rutubet, bazı kıyı bitkileri; kahraman yeşili değil |

Kurallar:

1. Kart alanının çoğu kâğıt, koyu mürekkep ve iki ana mat tondan kurulur.
2. Hardal veya kırmızı vurgu toplam görünür alanın yaklaşık yüzde 5–8’ini geçmez.
3. Aynı vurgu rengi her kartta aynı semantik anlama kilitlenmez; fakat daima odağı destekler.
4. Alev veya fener “glow” ile değil, çevresindeki taramanın azalmasıyla parlar.
5. Deniz hiçbir zaman turkuaz/tropik, metal krom, deri cilalı, yüz plastik değildir.
6. Deste genelinde açık/koyu dağılımı çeşitlenir; tek tek kartlar aynı sepya reçeteye dönmez.

## 8. Işık, atmosfer ve hacim

Işık bir boya tabakası değil, çizginin çekildiği veya çekilmediği karardır.

- Açık değer: kâğıt rezervi, seyrek kontur ve malzeme kenarında kısa beyaz kırılma.
- Orta değer: tek yönlü tarama; formu ve malzemeyi aynı anda açıklar.
- Koyu değer: ikinci tarama katı veya katran mürekkebi; yalnız yapısal gölge/derinlikte.
- Sis: uzak form çizgileri kademeli kaybolur; beyaz gradient ve lens bloom yok.
- Gece: her yeri siyaha boğmaz; birkaç açık kâğıt yolu, metal kenarı veya su kırığı mekânı taşır.
- Islaklık: parlak airbrush değil, koyu malzeme tonu ve az sayıda keskin kâğıt rezervi.
- Hacim: yüz ve bedende anatomiyi izleyen çizgi; yanakta yumuşak dijital gölge yok.
- Atmosfer perspektifi: uzak form küçülmekle kalmaz, çizgi aralığı genişler ve sıcak vurgu kaybeder.

Her kartın ışığı tek fiziksel kaynağa veya açık hava durumuna dayanır. Doğaüstü olay exact kimlik tarafından zorunlu tutulmadıkça görünür ışık halesi yoktur.

### 8.1 1721 fener teknolojisi sınırı

FOULWAKE fenerleri teknolojik ilerleme simgesi değil, ateşi rüzgâr ve kurum içinde sürdüren basit kıyı altyapısıdır.

İzin verilen çözümler:

- açık kömür/odun ateşi ve dövme demir ateş ızgarası;
- kalın camla çevrili basit ateş veya mum grubu;
- basit fitilli yağ kandili ya da elde taşınır hizmet feneri;
- elle açılan ağır ahşap panjur;
- taş taşıyıcı, cam bölme ve havalandırma açıklığı.

Kullanılmayacak çözümler:

- catoptric metal reflektör veya optik ayna;
- Argand düzeni;
- Fresnel merceği;
- elektrik, modern beacon renk kodu;
- dijital ışın, bloom, lens flare veya glow;
- ışığı optik olarak “taşıyan” mika levha veya metal yüzey.

HAR-FN-03 yalnız donyağı mumlu hizmet feneri ve panjurla; HAR-FN-04 yanlış burundaki basit kömür işaret ateşiyle çözülür. Işık hacmi, çevre taramasının azalması ve küçük kâğıt rezerviyle kurulur.

## 9. İnsan sistemi: yüz, beden, siluet ve meslek izleri

FOULWAKE’ın insanları aynı modelin kostüm varyasyonları değildir. Her görünür ana insan şu dört bağımsız eksende tasarlanır:

1. Yüz geometrisi: alın yüksekliği, göz aralığı, burun kökü/ucu, elmacık, çene ve kulak birbirinden ayrılır.
2. Beden geometrisi: uzun-kısa, ince-geniş, yuvarlak-köşeli, kambur-dik, ağırlık merkezi ve kol/bacak oranı.
3. Yaş ve sağlık: genç yüz yalnız pürüzsüz, yaşlı yüz yalnız çok kırışık değildir; diş, tırnak, güneş, yorgunluk, yara ve hastalık kartın işine göre.
4. Meslek izi: ipin kestiği avuç, kurumlu tırnak, tuzla sert saç, bir omuzun düşük kalması, eksik parmak ucu, balmumu/mürekkep lekesi.

Sakal ve bıyık varsayılan denizci özelliği değildir. Karakter ayrımının ana aracı olamaz; briefte belirtilmedikçe temiz yüz, kısa sakal, saç kaybı, örgü, bez bağ ve farklı yüz kılları dengeli dağılır. Karakterlerin çoğunda yüz kılı olmaması bilinçli bir korumadır.

Siluet testi: karakter adı ve kostüm ayrıntısı kapatıldığında, ana beden/baş/alet biçimi başka karakterden ayrılabilmelidir. El testi: yakın plan eller de yaş, iş ve anatomi bakımından tekrar etmemelidir.

Yasak tekrarlar:

- Aynı iri burun + küçük göz + geniş çene yüz şablonu.
- Aynı kollar çapraz Kaptan pozu veya üç çeyrek “kahraman portresi”.
- Bütün kadınları ince, bütün yaşlıları kambur, bütün işçileri geniş omuzlu yapmak.
- Ten rengi ile ahlak, beden ölçüsü ile beceriksizlik, yara ile kötülük kodlamak.
- Aynı karakteri Karakter, Güç, Sadakat ve Harita kartlarında fark edilmeden çoğaltmak.
- Karikatür etnik kostüm, “vahşi ada halkı” veya egzotikleştirme.

### 9.1 20-karakter karşılaştırma matrisi

Bu matris kostümden önce ana insan temelini kilitler. Üretim eskizinde yüz, beden ve el sütunlarından ikisi başka karakterle çakışırsa kostüm eklemek çözüm sayılmaz; temel model yeniden çizilir.

| ID | Yaş | Yüz geometrisi | Saç | Yüz kılı | Beden | Boyun / omuz | Duruş | El / meslek izi | Siluet anahtarı |
|---|---|---|---|---|---|---|---|---|---|
| KAR-01 | 40–47 | Oval, dolgun düzlemler; geniş düz burun | Kısa dalgalı koyu | Yok | Çok uzun, ince bel, geniş üst gövde | Uzun dik boyun; sağ omuz düşük | Ayakta ileri açılan | İşaret parmağı/başparmak rüzgâr ve halat nasırı | Uzun açık çatal |
| KAR-02 | 28–34 | Dar kalp; yüksek alın, küçük çene | Çene hizası düz koyu | Temiz | Orta boy, dar göğüs, uzun önkol | Kısa boyun; öne yuvarlanan omuz | Masaya köşeli eğim | Sol elde mürekkep/pergel baskısı | İnce masa üçgeni |
| KAR-03 | 42–49 | Geniş trapez; yüksek elmacık, ağır çene | Çok kısa sık kıvırcık | Yok | Uzun, geniş, atletik | Kalın boyun; düz güçlü omuz | Dümen basıncına çapraz karşı yatış | İki avuçta dümen/halat yanığı | Geniş X |
| KAR-04 | 48–55 | Dikdörtgen; yarık çene, geniş burun | Tepeyi örten çok kısa koyu | Temiz | Orta boy, ağır armut gövde | Çok kısa kalın boyun; yuvarlak omuz | Derin çömelme | Avuçta halka ip yanığı | Alçak daire |
| KAR-05 | 66–73 | Kalp; sivri çene, yüksek dar burun | Ense kısa, sıkı gümüş topuz | Yok | Kısa, ince telli, sinirli kas | Uzun eğimli boyun; çok dar omuz | Kulağı bordaya veren yan bükülme | Düzleşmiş başparmak, katranlı tırnak | Sıkışmış L |
| KAR-06 | 27–34 | Uzun dar; düz yanak, kırık burun kökü | Tıraşlı baş | Temiz | Kısa, sinirli kaslı kompakt V | Görünür uzun boyun; tek omuzda ip çukuru | İp merdivende dik uzanış | Geniş avuç, su/metal aşınması | Açılı küçük V |
| KAR-07 | 24–29 | Elmas; dar çene | İki uzun sıkı örgü | Yok | Aşırı uzun, kamış gibi ince | Uzun boyun; düşük dar omuz | Rüzgârla kıvrılan | Parmak uçlarında iplik kesikleri | S |
| KAR-08 | 52–59 | Geniş beşgen; tek altın diş | Başörtüsü altında | Yok | Kısa, geniş kalça/sırt | Boyun az görünür; yüksek omuz | Diz önde kayık itişi | Kürek kabarcığı ve tuz çatlağı | Kompakt kama |
| KAR-09 | 63–69 | Uzun oval; kemerli burun, ince dudak | Tepesi seyrek, yanlar gri | Temiz | Çok küçük ve dar | İnce boyun; içe çöken omuz | Raflar arasında sıkışık diklik | Eklemli parmak, anahtar cilası | Küçük dik + büyük halka |
| KAR-10 | 46–53 | Kare; düz burun, geniş kaş | Koyu yoğun kıvırcık | Yok | Uzun, güçlü kalça/omuz | Kalın boyun; geniş düz omuz | İki ekibe açık sağlam taban | Sağ serçe ucu eksik | Yatay T |
| KAR-11 | 20–23 | Keskin üçgen; çilli | Kısa kesim | Yok | Küçük, hafif, androjene yakın | Uzun boyun; dar omuz | Yay gibi sıçrama | İp taban ve palamar sürtünmesi | Gerilmiş yay |
| KAR-12 | 17–19 | Dar dikdörtgen | Yoğun kıvırcık başlık | Tüylenme; sakal yok | Uzun bacaklı, çok ince | İnce boyun; eğimli omuz | Platformda katlanmış oturuş | Fiş/ince halat sıkıştıran parmak | Küçük düğüm |
| KAR-13 | 50–57 | Kare; düşük alın, geniş kaş | Bez başlık altında | Temiz | Geniş karın, kısa kollar | Kısa boyun; yüksek omuz | Kazana öne dik basış | Kepçe yanığı ve kurum | Büyük daire |
| KAR-14 | 70–78 | Uzun üçgen; çökmüş yanak, uzun burun | Seyrek beyaz yan saç | İnce favori; bıyık/sakal yok | Çok ince, uzun | Uzun boyun; çökmüş omuz | Alçak ölçüm çömelmesi | Ölçü/mürekkep nasırı | Soru işareti |
| KAR-15 | 42–49 | Geniş elmas; düzleşmiş kırık burun | Gevşek bağ altında kısa kaba kıvırcık | Yok | Orta boy, dolgun, geniş kalça | Orta boyun; gevşek omuz | Dik ve dengeli | Önkolunda kuş çizikleri, tercüman eli | Dolgun oval + ince kuş dikeyi |
| KAR-16 | 55–62 | Büyük yuvarlak; küçük göz, ezik burun ucu | Kel | Temiz | Çok uzun ve olağanüstü iri | Kısa boyun; omuzlar kadrajı doldurur | Fıçıya nazik içe eğim | Büyük ama hassas parmak, çember cilası | Kapı dolduran blok |
| KAR-17 | 31–37 | Uzun dar; keskin kaş | Omuz hizası dalgalı | İnce bıyık | Çok ince | Aşırı uzun boyun; düşük omuz | Teatral yukarı uzanış | Mürekkep lekeli parmak | Ünlem |
| KAR-18 | 18–21 | Yuvarlak açık yüz; belirgin kulak | Yeni kısa kesim | Temiz | Kısa, tıknaz | Boyun neredeyse yok; omuzlar içe | Bordaya tutunan geri dönüş | Yeni oluşmuş halat nasırı | Kompakt kanca |
| KAR-19 | 58–65 | Kare çene; geniş yanak | Enseye kısa gümüş | Yok | Kısa, sağlam dikdörtgen | Kısa dik boyun; yük omzu düşük | Küçük kararlı adım | Sabun/kül kuruluğu, keten taşıma izi | Demetli dikdörtgen |
| KAR-20 | 49–56 | Geniş dikdörtgen | Gerileyen dalgalı gri | Gri bıyık; sakal yok | Kaslı fakat çökmüş | Kalın öne boyun; tek omuz çökmüş | İçe kapalı yarım profil | Boğumda eski vurma nasırı | Küt virgül |

### 9.2 Çarpışma dispozisyonu

- KAR-01 / KAR-05: KAR-01 daha genç, çok uzun, geniş üst gövdeli ve açık çatal; KAR-05 kısa, yaşlı, dar omuzlu ve sıkışmış L’dir. Yaşlı-uzun-kemikli ortak model kaldırılmıştır.
- KAR-04 / KAR-06: KAR-04 saçlı, orta boy, ağır armut gövdeli ve kısa boyunlu; KAR-06 tıraşlı başlı, kısa ama sinirli kaslı V gövdeli ve uzun boyunludur. Kısa-iri-kel ortak model kaldırılmıştır.
- KAR-02 / KAR-15: KAR-02 dar kalp yüzlü, düz saçlı ve masa üçgeni; KAR-15 geniş elmas yüzlü, kaba kıvırcık saçlı ve dik dolgun çift kütledir. Yuvarlak yüz/kısa kıvırcık ortak model kaldırılmıştır.
- Matrisin geri kalanında aynı yüz geometrisi + saç + beden + duruş dörtlüsünü paylaşan iki karakter yoktur.
- Karakter üretiminde kostüm kapatılarak 20 siyah siluet yan yana test edilir; aynı temel model ancak kostümle ayrılıyorsa brief başarısızdır.

## 10. Kompozisyon ve kadraj sözlüğü

Deste, 121 kez aynı orta plan portreyi taşıyamaz. Aşağıdaki sekiz kurulum düzenli ama mekanik olmayan aralıklarla dolaşır:

| Kurulum | İşlev | Örnek görsel mantık |
|---|---|---|
| Aşırı yakın maddi temas | Bir mekanik etkiyi tek temas noktasına indirger | çatlak, düğüm, sızıntı, oy taşı |
| Bel/omuz hizası tek hareket | Beden dilini ve işi birlikte okutur | yeke itme, bandaj bağlama |
| İnsan göz hizası karşılaşma | Etik veya sosyal gerilim | gümrük, savunma, ikmal |
| Alçak güverte / su hattı | Deniz ve gemi kütlesini büyütür | dalga, borda, kayalık |
| Yüksek eğik / tepeden | Nesne ilişkisi, sayım, rota | oy, arama, akıntı |
| Uzun eksen / koridor | Seçim ve kaçış | dar boğaz, kamara, liman ağzı |
| Geniş hava / coğrafya | Atmosfer ve ritim nefesi | sakin deniz, yerel sağanak |
| İnsansız kurumsal natürmort | Makam ve sistem | boş sandalye, mühür, defter |

Tek ana hareket kuralı: her kartta anlatı fiili birdir. İkincil şaka varsa harekete rakip olmaz. Önce/sonra durumları iz, gölge, kıç suyu, aşınma veya nesne konumuyla ima edilir; sahne bir çizgi romana bölünmez.

Negatif alan artık boş “metin kutusu” değildir; sis, gök, koyu duvar, açık su veya sade ahşap gibi sahnenin fiziksel parçasıdır. Metin yerleşimi için yeterli sakin alan bırakırken illüstrasyonun kendi içinde tamamlanmış kalması gerekir.

Aynı aile içinde art arda:

- aynı bakış yüksekliği,
- aynı gemi yönü,
- aynı ufuk oranı,
- aynı merkezlenmiş yüz,
- aynı diyagonal,
- aynı yakın plan el

kullanılmaz. Manifestteki similarity_risk ve do_not_repeat alanları üretim takibinin aktif kontrol listesidir.

### 10.1 Kadraj önerisi kilitli çekim değildir

Manifestteki framing_viewpoint_focus_negative_space alanı, destenin çarpışmasını önleyen ilk kompozisyon vektörüdür. Sanatçı aynı ilk duygu, ana hareket, negatif alan görevi ve ritim farkını daha güçlü bir kamerayla kurabiliyorsa üç küçük eskizden birinde bunu önermelidir. Değişiklik “daha havalı” olduğu için değil, kartın dramatik sorusunu daha yalın kıldığı için savunulur.

Görsel üretim yetkisi verildiğinde her pilot için üç siyah-beyaz küçük eskiz istenir:

1. briefteki başlangıç vektörünü en yalın biçimde sınayan çözüm;
2. aynı niyeti insan yerine malzeme/boşluk ağırlığıyla sınayan çözüm;
3. en bariz çözümü bilinçli olarak reddeden, fakat exact mekanik ve dönem sınırını koruyan sanatçı önerisi.

İlk değerlendirme çizgi güzelliğine değil; “ilk iki saniyede hangi duygu var, tek fiil okunuyor mu, resim gereksiz bir hüküm veriyor mu?” sorularına yapılır. Bu aşamada render ve yüzey cilası geri bildirimi verilmez.

## 11. Ciddi deniz atmosferi ve kuru mizah dengesi

Ana olay daima gerçektir. Görsel şaka varsayılan değil, gerekçelendirilmesi gereken istisnadır. Flavor metni zaten mizahı taşıyorsa illüstrasyonun ikinci kez şaka yapması gerekmez.

### 11.1 Varsayılan politika

- secondary_wordless_joke_max_one alanının varsayılan değeri NONE’dır.
- Ölüm, denize düşme, ağır Gövde hasarı, Kraken tehdidi, Çürümüş Erzak, bütün Sadakat/Hain kartları, fener yanıltması ve kurumsal destek kartlarında ikincil şaka kullanılmaz.
- Ciddi karttaki küçük gerçekçi ayrıntı otomatik olarak “şaka” sayılmaz; ana dramaturjinin parçasıysa nesne/metafor alanına taşınır.
- Şaka sırf contact sheet’i “eğlenceli” göstermek için eklenmez.
- Bir kartta en fazla bir ikincil, yazısız şaka olabilir; ikinci şaka taslakta dahi üretilmez.

### 11.2 Koruma filtresi

Bir şaka ancak şu koşulların hepsini sağlarsa tutulur:

1. Kart adı, exact flavor veya meslek kimliği onsuz belirgin biçimde zayıflar.
2. Gerekçe yalnız o karta özgüdür; başka karta kolayca taşınamaz.
3. Ana hareket, tehlike ve ilk iki saniye duygusu şakadan önce okunur.
4. İnsan aptal, sarhoş, pis veya beceriksiz maskota dönüşmez.
5. Yazı, tabela, slogan, konuşma balonu, anlamsız harf veya tekrar eden hayvan gerekmez.
6. Gizem çözülmez, Hain işaretlenmez, veba/ölüm küçültülmez.

### 11.3 Rework sonrası dağılım

| Aile | Toplam | Şakalı | NONE |
|---|---:|---:|---:|
| Karakter | 20 | 5 | 15 |
| Güç | 30 | 6 | 24 |
| Çürümüş Erzak | 1 | 0 | 1 |
| Sadakat | 15 | 0 | 15 |
| Açık Deniz | 30 | 4 | 26 |
| Kayalık | 12 | 0 | 12 |
| Ada | 6 | 3 | 3 |
| Deniz Feneri | 4 | 0 | 4 |
| Yardımcı | 3 | 0 | 3 |
| Toplam | 121 | 18 | 103 |

Korunan 18 istisnanın karta özgü gerekçesi 121 manifestindeki ilgili alanda yazılıdır. Bunun dışındaki bütün kayıtlar tam olarak NONE kullanır.

Martı yalnız exact kimliğin gerektirdiği HAR-AD-03 ve GUC-25’te farklı dramaturjiyle; papağan KAR-15 ve GUC-17’de aynı model/poz olmadan; fare KAR-14’te tekil ve görevsel biçimde kullanılır. Hayvanın görünmesi şaka izni anlamına gelmez: HAR-AD-03’ün alanı NONE’dır.

## 12. Yazısız görsel hikâye anlatımı

Kart adı, etki ve flavor zaten tipografi alanında yer alır; illüstrasyon içindeki okunabilir metin gereksiz ve yasaktır. Şunlar kullanılabilir:

- aşınmış, okunmayan kâğıt yüzeyi;
- harf olmayan basit, döneme uygun nesne işareti;
- düğüm, su izi, gölge, boşluk, tekrar ve karşıtlık;
- farklı nesne sayısı, ancak mekanik sayıyı öğretici ikon gibi yazmadan;
- yaklaşan/uzaklaşan kıç izi;
- kapalı/açık fiziksel düzen.

Şunlar kullanılamaz:

- tabela, logo, rota adı, liman adı, sayı, yön harfi;
- konuşma balonu, ses efekti, nota, ünlem;
- kartın etki metnini resim içinde yeniden yazan form veya mühür;
- anlamsız “eski yazı” dokusu;
- tipografi alanıyla rekabet eden rastgele belge.

Exact flavor sahne-içi yazıdan söz ediyorsa fikir yazısız eşdeğere çevrilir. Örneğin Zıpkın Sandığı üzerindeki “büyük balık yazısı”, harf içermeyen acele fırçalanmış balık siluetiyle çözülür; metin uydurulmaz.

## 13. Kart aileleri

| Aile | Ön yüzde baskın sanat fiili | Siluet / mekân | Ton ve vurgu | Ayrıştırıcı ilke |
|---|---|---|---|---|
| Karakter — 20 | Mesleği tek davranışla görünür kıl | Dikey insan + gerçek görev noktası | Cilt/iş malzemesi; küçük sıcak vurgu | Yüz, beden, el, meslek izi birbirinden benzersiz |
| Güç — 30 | Nesnenin kullanım anını veya sosyal etkisini göster | Yakın nesne-el, bazen kurumsal masa | Malzeme odaklı koyu-açık kontrast | “Ürün fotoğrafı” değil, karar ve bedel |
| Çürümüş Erzak — 1 | Çürümenin rota baskısını kur | İnsansız karanlık ambar | Küf zeytini/pas; tiksinti kontrollü | Güç arkasını paylaşır ama ön dramaturjisi yabancı ağır durak |
| Sadakat — 15 | Niyeti açıklamadan davranışın etik ağırlığını kur | Eller, beden dili, ortak iş/divan | Daha kısıtlı vurgu, psikolojik gölge | Tayfa/Hain arka yüzde sızmaz; önler şeytan/melek koduna düşmez |
| Açık Deniz — 30 | Hava, akıntı ve gemi ilişkisini tek olayla kur | Geniş coğrafya ile aşırı yakın temas dönüşümlü | İndigo/tuz; değer aralığı en geniş | Aynı dalga, gemi açısı veya fırtına reçetesi tekrar etmez |
| Kayalık — 12 | Jeolojinin rota ve gövde üzerindeki fiziksel etkisi | Sert kütle, dar kanal, sualtı temas | Soğuk gri/kurum/pas | Her kaya ayrı jeoloji ve ölçek; fantastik sivri dağ dizisi yok |
| Ada — 6 | Kıyı kurumunu ve alışveriş/bedeli göster | İnsanlı kıyı, iskele, karakol/atölye | Taş, meşe, zeytin-gri | Tropik kartpostal veya kolonyal “öteki” yok |
| Deniz Feneri — 4 | Işık, bilgi ve yanlış yön ilişkisi | Taş kule, basit ateş/mum/yağ ışığı ve ahşap panjur | Koyu kurum + çok küçük hardal | Catoptric metal reflektör, Argand, Fresnel, elektrik ve glow yok |
| Yardımcı — 3 | Seferin kurumsal uçlarını kur | Liman altyapısı veya boş makam | Dengeli bütün palet | Tutorial ikonu değil, dünyanın gerçek mekânı |

## 14. Bütün destenin görsel ritmi

121 kart tek tek güçlü olmalı, fakat deste topluca nefes almalıdır. Her kartın eşit derecede dolu, eşit derecede taranmış ve eşit derecede ‘gösterişli’ olması bütünlüğü değil monotonluğu üretir. Ritim beş eksende planlanır:

### 14.1 Ölçek

Yakın — orta — geniş — yakın döngüsü; aynı ailede üçten fazla arka arkaya aynı ölçek yok. Açık Deniz geniş planların evidir ama her hava kartı uzak gemi değildir. Güç ailesi yakın plan ağırlıklıdır fakat uzun koridor, açık gök ve manevra planlarıyla kırılır.

### 14.2 Değer

- En açık kartlar: sis, Beyaz Gece, yedek yelken, sakin su.
- Orta değer kartlar: karakter görevleri, ikmal, liman.
- En koyu kartlar: ambar, gece hasarı, kurumlu fener, kapalı makam.

Koyu kartlar art arda duvar oluşturmaz; açık negatif alan veya sıcak materyal kartıyla ayrılır.

### 14.3 Geometri

Daireler (can halkası, pusula, para), dikeyler (direk, fener, insan), yataylar (ufuk, masa, rıhtım), spiraller (akıntı), sıkıştırmalar (kayalık) ve açık U/V biçimleri (liman, geçit) dengelenir. Aynı geometrinin semantik işlevi de kopyalanmaz.

### 14.4 İnsan yoğunluğu

Tek yüz → eller/nesne → grup beden dili → insansız hava/coğrafya sıraları dolaşır. İnsan görünmeyen kartlar “daha az sanat” değil, kurum ve denizin özne olduğu kartlardır.

### 14.5 Duygusal kadans

Merak → maddi güven → kuşku → hasar → kuru rahatlama → yeniden kuşku. Mizah iki ağır kartı otomatik olarak ayıran dolgu değildir; exact kimlik ve sahne içinden çıkmadıkça eklenmez.

Üretim contact sheet’i Görsel Tasarım aşamasında şu çapraz kontrollerle okunmalıdır: yüz tekrarları, el tekrarları, gemi yönleri, ufuk yükseklikleri, hayvan sayısı, vurgu renk yüzdesi, açık/koyu kümelenmesi, aynı nesne ve şaka tekrarları. Bu belge contact sheet üretmez; kontrol mantığını tanımlar.

## 15. Arka yüz ilkeleri

Yedi arka yüz ön yüzlerle aynı sanat dünyasına aittir; ayrı bir logo sistemi veya soyut dijital desen değildir. f0389711… içindeki BACK_CHARACTER, BACK_POWER, BACK_LOYALTY ve BACK_SUPPORT yönleri korunur. d578feca… içindeki dosya ve kapsam bütünlüğü de korunur. Bu hedefli rework yalnız BACK_SEA_ROCK, BACK_ISLAND ve BACK_LIGHTHOUSE’ın aile görünürlüğünü ve değişken masa davranışını değiştirir.

### 15.1 Korunan topoloji ve bağlayıcı bilgi sözleşmesi

| Binary | Exact adet/master | Arka yüzün söylemesine izin verilen tek aile bilgisi | Kesinlikle söyleyemeyeceği bilgi |
|---|---:|---|---|
| BACK_SEA_ROCK | 42; 30 Açık Deniz + 12 Kayalık exact aynı master | Kartın Açık Deniz/Kayalık ortak ailesinde olduğu | Açık Deniz mi Kayalık mı olduğu; belirli ön kimlik, sonuç, güven/tehdit veya yön |
| BACK_ISLAND | 6; altı Ada exact aynı master | Kartın Ada ailesinde olduğu; genel ve anonim kara görülür | Altı Ada önünden hangisi olduğu; özel kıyı, yerleşim, ürün, kişi, olay veya sonuç |
| BACK_LIGHTHOUSE | 4; dört Deniz Feneri exact aynı master | Kartın Deniz Feneri ailesinde olduğu; genel ve anonim fener görülür | Dört Fener önünden hangisi olduğu; özel yapı, hasar, ışık davranışı, paket, kıyı, olay veya sonuç |

Proje sahibi kararına göre aile görünürlüğü bilgi sızıntısı değildir. Sızıntı, arka yüzün aile bilgisinden ileri gidip belirli ön kartı, alt türü, sonucu, güvenli/tehlikeli hâli veya yönü tahmin ettirmesidir. Kart adı; effect veya flavor içeriği; olumlu/olumsuz sonuç; güven/tehdit durumu; ön yüzdeki özel mekân, karakter, nesne veya sahne; kart yönü kesinlikle gösterilemez.

- Üç binary ayrı kalır, fakat aynı COMMON_MAP_BACK_VISUAL_SYSTEM içinden çıkar.
- Aynı ailedeki bütün fiziksel kopyalar bit-bit exact aynı master dosyayı kullanır.
- BACK_SEA_ROCK arkasında kaya, sığlık, köpüren kırıcı dalga, jeolojik işaret veya başka bir Açık Deniz/Kayalık ayracı yoktur.
- BACK_ISLAND’daki ada altı ön yüzdeki hiçbir özel adanın biçimi, kıyısı veya içeriği değildir.
- BACK_LIGHTHOUSE’daki fener dört ön yüzdeki hiçbir özel kulenin mimarisi, durumu veya olayını taşımaz.
- Okunabilir yazı, logo, tür etiketi, sayı, yön işareti, koordinat, rota çizgisi ve pusula gülü yoktur.
- Parlaklık, vernik, kesim, koyu köşe, baskı kiri veya eskitme kartı, kopyayı ya da yönü tanıtamaz.
- Exact 180 derece güvenliği sanat kompozisyonunun parçasıdır; sonradan eklenen dijital simetri efekti değildir.

### 15.2 Referans sınırı

Ekli masa görseli MAP_TABLE_REFERENCE: TABLE_READ_ONLY /
COMPOSITION_PRINCIPLE_ONLY olarak sınıflandırılır. Yalnız kapalı kartların
birlikte tek bir keşfedilmemiş deniz alanı gibi okunması ilkesi alınır.
Referanstaki 5×5 sayı, sabit grid, satır/sütun düzeni, dalga çizgileri, renk,
çerçeve, kart yüzleri ve yüzey yerleşimi kopyalanmaz veya üretim şartı yapılmaz.
KAPTAN ise `SET-KP-01` görsel/copy kaynağı ve deste sanat dili anahtarıdır;
harita-masa referansının yetkisini genişletmez.

### 15.3 COMMON_MAP_BACK_VISUAL_SYSTEM

Harita arka yüzlerinin bağlayıcı kompozisyon birimi sabit bir grid değil, oyun sırasında kurallara uygun biçimde oluşan değişken harita alanıdır. Sistem kompakt, genişleyen, uzayan ve komşuluğu değişen düzenlerde aynı ilkelerle çalışır.

1. **Ortak deniz omurgası:** Üç ailede aynı çizgi kalınlığı merdiveni, kısa/kırık su çizgileri, seyrek çapraz tarama, mat kâğıt ve değer zarfı kullanılır. Deniz, ada ve fenerin çevresinde farklı bir “kart zemini”ne dönüşmez.
2. **Mat malzeme:** Kurum indigosu, tuz mavi-grisi, tar grisi ve kemik kâğıt rezervi ana palettir. Kara ve taş aynı mat baskı dünyasına küçük sıcak/soğuk değer ayrımlarıyla girer; doygun aile renk kodu yoktur.
3. **Çizgiyle hacim:** Su, kara ve taş hacmi boya gradyanı, glow veya dijital noise ile değil; çizgi aralığı, çapraz tarama, kâğıt rezervi ve kontur basıncıyla kurulur.
4. **Kenar bağımsızlığı:** Yüzey trim ve bleed’e kadar sürer. Kenar zarfında üç aile aynı dalga ölçeği, ortalama çizgi yoğunluğu ve değer aralığını paylaşır. Uzun rota benzeri çizgi trimde kesilmez; literal komşu eşleşmesi aranmaz.
5. **İstatistiksel devamlılık:** Kartlar farklı sayıda ve farklı komşulukta birleştiğinde devamlılık, tek çizginin karşı karta bağlanmasıyla değil aynı ölçek, hava, değer ve kenar ritmiyle kurulur. Bu nedenle sistem belirli satır, sütun, kart sayısı veya dizilime bağımlı değildir.
6. **Odaksız ana zemin:** BACK_SEA_ROCK’ta merkez, köşe veya eksen ayrıcalıklı değildir. Ada ve fener ailelerinde görünür coğrafya vardır; fakat dekoratif halka, rozet, renk adası veya merkezî grafik alanla zeminden koparılmaz.
7. **Exact master tekrarının yönetimi:** Büyük tekil su lekesi, imza dalga, merkez koyuluğu ve kolay ezberlenen çizgi takımyıldızı yoktur. Çok sayıda küçük yarım-dönüş eşli mikro-küme normal masa mesafesinde tekrar değil deniz ritmi oluşturur.
8. **Açılan ön yüzlerle bağ:** Kapalı arka yüzler sessiz keşfedilmemiş alan; açılan ön yüzler aynı çizgi/malzeme dünyasında keşfedilmiş olay ve coğrafya parçalarıdır. Arka yüzler ön yüz kontrastıyla yarışmaz.
9. **Mekanik tarafsızlık:** Sanat yeni bir kurulum, sabit grid, yön, rota veya komşuluk kuralı önermez. Yalnız mevcut kurallarda oluşan alanı görsel olarak birleştirir.

### 15.4 Aile-görünür doğal coğrafya

| Binary | Sanatsal rol | Aileyi görünür kılan çözüm | Ön-kart sızıntısını önleyen yasak |
|---|---|---|---|
| BACK_SEA_ROCK | Ortak denizin nötr ve en geniş zemini | Genel, keşfedilmemiş açık su | Kaya, resif, sığlık, köpüren kırıcı dalga, jeolojik renk veya belirli olay havası |
| BACK_ISLAND | Ortak denizde doğal bir kara eşiği | Dik kuşbakışında tek, alçak ve anonim ada; deniz kartın bütün kenarlarına ulaşır | Yerleşim, gümrük, kamp, tersane, erzak, bayrak, insan, ürün, özel palmiye düzeni veya ön yüzlerden birine benzeyen kıyı |
| BACK_LIGHTHOUSE | Ortak denizde insan yapımı fakat anonim seyir unsuru | Çok dik kuşbakışında alçak nötr kaya üzerinde küçük, dönemsel ve açıkça fener olan taş kule | Yanıltıcı ışık, ışın, özel ateş, saklı paket, belirli hasar, özel kıyı, olay sonucu veya dört ön yüzden birine özgü mimari |

**Ada çözümü:** Kara kütlesi kart ortasında bir madalyon gibi yüzmez. İki karşıt burun ve aralarında alçak bir omurga taşıyan, elle çizilmiş uzun bir kıyı kütlesi denizin içine doğal biçimde oturur. Deniz halkası, halo, etiket alanı ve kusursuz geometrik çevre yoktur. İç ayrıntı yalnız anonim taş, düşük çalı ve aşınmış topraktır; belirli iklim veya ekonomi anlatılmaz. Ada, normal masa mesafesinde aileyi seçtirecek kadar açık; altı ön adadan birini çağrıştırmayacak kadar geneldir.

**Fener çözümü:** Ufuksuz, çok dik kuşbakışı seçilir. Küçük, sade yığma taş kule ve basit fener üst yapısı alçak, anonim bir kaya sırtına gömülür; çevresindeki deniz üç aileyle aynı kenar ritmini sürdürür. Kule etrafında rozet halkası, ışık halesi, ışın, pusula geometrisi veya boşaltılmış grafik disk yoktur. Kule bir ikon gibi suyun üstüne yapıştırılmaz; kaya, su ve bakım aşınmasıyla aynı fiziksel sahnenin parçasıdır. Normal masa mesafesinde aile okunur, belirli fener veya olay okunmaz.

### 15.5 Exact 180 derece için sanatsal kurgu

- **BACK_SEA_ROCK:** Dağılmış su çizgisi mikro-kümeleri uzak yarım-dönüş eşleriyle exact dengelenir. Dönüş merkezi sıradan sudur; dört kollu akıntı ve koyu çekirdek yoktur.
- **BACK_ISLAND:** Tek ada gövdesi dönüş merkezinden doğal bir uzun eksenle geçer. İki burun, iki küçük koy, taş/çalı kümeleri ve kıyı kırıkları yarım-dönüş eşlidir; sağ-sol ayna simetrisi veya kusursuz oval değildir. Yerel kıyı düzensizliği korunur, fakat bütün flattened master 180 derece döndüğünde exact eşleşir.
- **BACK_LIGHTHOUSE:** Tek kule exact dönüş noktasına yerleşir; bu nokta grafik amblem değil fiziksel yön-güvenliği çözümüdür. Kulenin sade çokgen planı, fener üst yapısı, kaya sırtının iki ucu, su yarıkları ve bakım aşınmaları yarım-dönüş eşlidir. Kuleyi çevreleyen halka, radyal çizgi veya simetrik boşluk diski yoktur; kaya sırtı merkezden iki yana uzanarak kompakt rozet siluetini kırar.
- Üçünde de ufuk, tek yönlü gölge, rüzgâr oku, tek tarafta köpük, üst/alt değer farkı ve serbest uç yoktur.
- Eskitme, kâğıt lifi ve baskı kayması sonradan rastgele filtrelenmez; exact dönüş eşli masterın içindedir.
- 180 güvenliği yalnız düz/ters görsel bakışla değil flattened rotate/difference testiyle doğrulanır.

### 15.6 Değişken masa ve keşif sonrası ilişki

Sabit 5×5, grid, satır, sütun veya kart sayısı koşulu yoktur. Ortak sistem, kuralların izin verdiği farklı kart sayıları ve farklı harita biçimlerinde çalışmalıdır.

- Kompakt bir kümede de uzayan/dağılan bir haritada da ortak deniz kenar zarfı sert kopmaz.
- Ada ve fener farklı ailelerle hangi kenardan komşu olursa olsun ayrı bir poster, logo veya renk karesi gibi görünmez.
- Rastgele 180 derece dönüşler denizin ritmini, adanın doğal coğrafyasını ve fenerin yön güvenliğini bozmaz.
- Ada ve fenerin aile görünürlüğü normal masa mesafesinde korunur; bu görünürlük ön kimlik tahminine dönüşmez.
- Birkaç ön yüz açıldığında kapalı alan, açılan sahneleri çevreleyen ortak keşfedilmemiş deniz olarak kalır.
- Literal kıyı/dalga eşleşmesi gerekmediği için geçerli bir düzenin başka bir düzene dönüşmesi sanatı “yanlış dizilmiş” göstermez.

### 15.7 REPRESENTATIVE_VARIABLE_MAP_LAYOUT_QA

Görsel üretim yetkisi verilirse Görsel Tasarım aşağıdaki kanıtların tümünü üretmeden harita arka yüzleri kabul adayı olamaz:

1. Üç aileyi birlikte gösteren, kural kitabına uygun tamamen kapalı temsilî harita düzenleri.
2. Aynı kartların rastgele 180 derece çevrildiği temsilî düzenler.
3. Bazı kartların açıldığı keşif-sonrası masa düzenleri.
4. Kuralların izin verdiği ölçüde daha kompakt ve daha geniş/uzayan harita düzenleri.
5. Ada, Fener ve Deniz/Kayalık ailelerinin farklı komşuluklarda bulunduğu örnekler.
6. BACK_SEA_ROCK için Açık Deniz/Kayalık kör ayrım testi.
7. Altı Ada ön kimliği için kör tahmin testi.
8. Dört Deniz Feneri ön kimliği için kör tahmin testi.
9. Ada ve Fener ailelerinin normal masa mesafesinde anlaşılabildiği kontrol.
10. Ada ve fener unsurlarının ikon, rozet veya madalyon gibi görünmediği sanat incelemesi.
11. Okunabilir yazı, sayı, rota, pusula, koordinat, yön işareti ve gereksiz şekil kontrolü.
12. Kart kenarı, kesim, parlaklık, exact master ve yön sızıntısı kontrolü.
13. Farklı kurala uygun düzenlerde ortak deniz hissinin korunduğu kontrol.
14. Arka yüzlerin açılan ön yüzlerle aynı FOULWAKE sanat dünyasına ait göründüğü kontrol.

Kabul cümlesi: **Oyuncu kapalı kartın Deniz/Kayalık, Ada veya Fener ailesinden olduğunu anlayabilir; ancak kart çevrilmeden hangi ön kart olduğunu veya sonucunu tahmin edemez. Harita, belirli bir ölçü veya dizilimde değil, oyun sırasında oluşabilecek kurala uygun farklı masa düzenlerinde tek bir keşfedilmemiş FOULWAKE denizi gibi görünür.**

Ayrı yedi brief ve ayrıntılı risk/QA sözleşmesi FOULWAKE_7_BACK_BRIEFS_v2.7.md içindedir.

## 16. Baskı ve küçük boy okunurluğu

Sanat nihai baskı dosyası değildir, fakat brief ölçek gerçeğini gözetir:

- İlk iki saniye duygusu küçük kart boyunda büyük kütleyle çalışmalıdır.
- Ana hareket, karta adını okumadan önce tek fiil olarak seçilmelidir.
- Mikro tarama gerçek ölçekte kapanmamalı; prova baskısında çizgi birleşmesi ayrıca test edilir.
- Yüzler küçük baskıda tek lekeden ibaret kalmamalı; göz-burun çizgisi değil siluet ve ışık düzlemi taşır.
- Kare Harita kartlarında ufuk/çerçeve ritmi dikey Karakter/Güç kartlarıyla karıştırılmaz.
- Kesim alanına yüz, el, ana nesne, tekil vurgu veya bilgi sızıntısı taşıyan asimetri yaklaşmaz.
- Her arka yüz düz/ters karıştırılarak kör masa testi görmelidir.
- Dijital ekranda güzel duran düşük kontrast, mat baskıda kaybolabilir; değer merdiveni önceliklidir.

## 17. Üretim kapıları

Görsel üretim henüz yetkili değildir. Yetki verilirse yönlendirme dört sırada yapılır; geç aşamanın ayrıntısı erken aşamayı boğmaz:

| Aşama | Sanat Yönetmeninin ilk sorusu | Bu aşamada geri bırakılan şey |
|---|---|---|
| 0 — küçük eskiz | Duygu, tek fiil ve ahlaki belirsizlik okunuyor mu? | Doku, ince tarama, renk cilası |
| 1 — yapı | Siluet, bakış yüksekliği, negatif alan ve kart ölçeği çalışıyor mu? | Mikro yüz, baskı eskisi |
| 2 — dünya | Mekân, malzeme, teknoloji ve meslek izi döneme/desteye ait mi? | Son renk ayarı |
| 3 — çizgi/renk | Çizgi hacmi kuruyor, mat palet odağı taşıyor, aile ritmi korunuyor mu? | Yeni kompozisyon icadı |

Geri bildirim “beğenmedim” diye verilmez. Önce gözlenen sorun, sonra kartın hangi protected intent’ini zayıflattığı, ardından çözüm alanı söylenir. Sanatçının gerekçeli karşı önerisi değerlendirilir; briefteki starting vector nihai estetik karardan üstün değildir.

Bir illüstrasyon brief kabulüne aday olmadan önce şu soruların hepsine evet denmelidir:

1. Exact kart kimliği ve mekanik değiştirilmeden mi anlatılıyor?
2. İlk iki saniyedeki duygu tek ve açık mı?
3. Tek ana hareket var mı?
4. Gerçek gemi/deniz/kıyı mekânı inandırıcı mı?
5. Özne başka kartın yüzü, pozu, hayvanı veya sahnesiyle karışıyor mu?
6. Hacim çizgi/tarama ile mi kuruluyor; plastik gradient var mı?
7. Palet mat ve vurgu kontrollü mü?
8. Yazısız anlatı çalışıyor mu; sahne-içi okunabilir metin var mı?
9. Mizah tehlikeyi veya kişiyi küçültüyor mu?
10. Dönem dışı alet, lens, kilit, giysi, ambalaj veya liman altyapısı var mı?
11. Aile kimliği anlaşılırken arka yüz bilgi sızdırıyor mu?
12. Küçük baskıda ana kütle ve hareket okunuyor mu?
13. Çözüm, briefin nesne listesini değil korunmuş niyeti mi taşıyor?
14. Sanatçının yorumu FOULWAKE’a özgü bir gözlem katıyor mu; yoksa yalnız uyumlu fakat jenerik mi?
15. Özel ad veya geçici lore motifi değişirse görsel hâlâ çalışıyor mu?

Herhangi bir “hayır” taslağı üretimden sanat yönü düzeltmesine döndürür. Nihai kabul değildir; proje sahibi ve Baş Editör dispozisyonu gerekir.

## 18. Değişmez red listesi

- Reddedilmiş e91581 sanatından kompozisyon, yüz, renk, nesne veya çizgi almak.
- Aynı insan modelini kostüm değiştirerek çoğaltmak.
- Sakal/bıyığı denizci varsayılanı yapmak.
- Martı, fare, papağan veya beceriksiz tayfayı tekrar eden maskot yapmak.
- Kafatası, tropik hazine, parlayan altın ve kahraman Kaptan kısa yolları.
- Tabela, slogan, konuşma balonu, anlamsız yazı veya okunabilir sahne-içi belge.
- Airbrush glow, boya gradyanı, plastik yüz, krom metal, stok grunge filtresi.
- Kart mekaniklerini ikonlaştırıp illüstrasyonu infografiğe çevirmek.
- KAPTAN figürünü başka kartlara kopyalamak veya SET-KP-01'de KAPTANı boş
  sandalye/başka özneyle değiştirmek.
- Final görsel, render, PDF, contact sheet veya baskı paketi üretimini Sanat Yönetimi içinde yapmak.

## 19. Güncel owner override ve dispozisyon

Proje sahibi exact 23c062f6… pilotunu reddetmiştir. KAPTAN görsel/copy sözleşmesi
bu Bible'daki önceki portresiz çözümü supersede eder. BACK_SEA_ROCK mat ve
ışıldamayan deniz olarak rework edilir; BACK_ISLAND eski varlıktan türetilmeden
FULL REDRAW yapılır; BACK_LIGHTHOUSE daha büyük okunur ve uzun kayalık sırt
zorunlu değildir. Diğer dört arka HOLD'dur.

Bütün ön/arka illüstrasyonlar exact oran, 3 mm bleed, 4–5 mm safe area, özne
ölçeği, odak, gerekli crop, metin alanı çakışması, thumbnail/masa okunurluğu ve
kadraj çeşitliliği için bağımsız Sanat Yönetimi kapısından geçer. Görsel
Tasarım self-PASS veremez; yalnız FRAMING_PASS veya REFRAME_REQUIRED. Sapma
BLOCKED_FRAMING_DRIFT'tir.

Güncel yetki yalnız CURRENT_STAGE içindeki tek dosyalık patch düzeltmesidir.
Yeni görsel, full 121, PDF, Simülasyon, release veya lock yetkili değildir.
