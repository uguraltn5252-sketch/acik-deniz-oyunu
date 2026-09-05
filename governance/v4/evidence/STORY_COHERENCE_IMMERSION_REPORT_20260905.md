# STORY-COHERENCE-IMMERSION-001 — Gelen ayrıntılı rapor

Gönderen: STORY_EDITOR. Proje sahibi tarafından CHIEF_EDITOR sohbetine 5 Eylül 2026'da aktarıldı. Aşağıdaki raporun tablo ve handoff biçimi Markdown'a düzenlendi; değerlendirme ve öneriler gönderen role aittir. GitHub kaydını CHIEF_EDITOR oluşturdu; bu işlem Story dalında uzman teslim commit'i değildir. Rapor yeni kanon, mekanik veya uygulama yetkisi vermez. Baş Editörün bağımsız kararı ve kapsam tablosundaki kategori düzeltmesi `STORY_COHERENCE_IMMERSION_ACCEPTANCE_20260905.json` içindedir; aşağıdaki özgün tablo sessizce düzeltilmemiştir.

---

FOULWAKE — STORY-COHERENCE-IMMERSION-001 ayrıntılı inceleme raporu

Gönderen: STORY_EDITOR  
Değerlendirecek rol: CHIEF_EDITOR  
Tarih: 5 Eylül 2026

İnceleme tamamlandı. Üç hikâye belgesinin tamamı ve mevcut kaynaklardan çözümlenen 51 kart kaydı incelendi. Öncelikli sonuçlar: iki karakter kartında gece adlandırması uyuşmazlığı, KAPTAN metninde yetki kapsamı belirsizliği ve Siyah Mühür anlatısında eski metinden kalan bir kesinlik sorunu bulunuyor. Oyuncunun sorumluluğunu açılışta daha erken görünür kılmak ve bazı karakterlerin seslerini ayrıştırmak da öneriliyor.

Bu teslim, kaynaklara dayalı editoryal değerlendirmedir. Kaynak dosyaları değiştirilmedi; öneriler henüz kabul edilmiş metin veya kanon değildir.

**Yetki ve sürüm doğrulaması:** İnceleme `v2.7-design@fb64fbcba2d6f359cc274f9e3cb9aa4df36fae5b` üzerinden tamamlandı. Rapor aktarılırken güncel HEAD `1a9e212b7b0df9bfbbdf950657613acccc0c2eda` olarak doğrulandı. Görevin 12 sabitlenmiş girdisinin tamamı bu sürümde değişmeden duruyor. Görev kaydındaki kaynak commit’i `23b8ba547d58008e69c400140e16ccfc0186aee9`.

Güncel kayıt, tamamlanma bildiriminin alındığını ve ayrıntılı raporun bağımsız değerlendirmesinin beklendiğini belirtiyor. Yazma yetkisi kapalı; teslim kanalı görünür STORY_EDITOR sohbeti. [Güncel görev kaydı](https://github.com/uguraltn5252-sketch/acik-deniz-oyunu/blob/1a9e212b7b0df9bfbbdf950657613acccc0c2eda/governance/v4/tasks/STORY-COHERENCE-IMMERSION-001.json)

Görevde istenen model `gpt-6-astra / xhigh`; doğrulanmış gerçek çalışma modeli `UNKNOWN`. Geçici ajan kullanılmadı.

**Genel değerlendirmem:** Hikâyenin taşıyıcı gücü, aynı yükün farklı kişiler için farklı anlamlar taşıması. Halk kurtuluş ihtimali görüyor; kraliçe ticaret ailelerine bağımlılığını azaltmak istiyor; Veyr doğrulanmamış bir iddiayı savunuyor; salgından kazananlar mevcut düzeni korumaya çalışıyor. Bu çatışma, gemideki güvensizliği destekliyor.

En önemli gelişim alanı, oyuncunun bu büyük tablonun içindeki yerini daha erken anlaması. Açılış, kurumları ve terkibi ayrıntılandırırken oyuncunun kişisel sorumluluğu daha sonra belirginleşiyor. İlk seçimden önce “Bu gemide benim sorumluluğum ne, başarısız olursak ne kaybederim, neden diğerlerine ihtiyacım var?” sorularının karşılığı daha görünür olmalı.

**Korunmasını önerdiğim güçlü parçalar:**

- Gusto’nun vekil bırakmaması ve sefer kefaleti, oyuncuların aralarından kaptan seçmesini dünyaya bağlayan güçlü bir neden oluşturuyor.
- Terkibin başarısının kesinleşmemesi, görevin ahlaki gerilimini koruyor. Sandığın üzerindeki “İLAÇ” ile Veyr’in ihtiyatı arasındaki fark etkili.
- Gusto’nun çizmeleri, eksik sayfalar ve balmumu birden fazla yoruma açık kalıyor. Bunlar kesin suçlu veya çözüm üretmemeli.
- Borç, erzak, ip, kürek, sağlık evrakı ve gemideki alışkanlıklardan doğan kuru mizah dünyaya uyuyor.
- Tahtaya Vuran ile Tahtakakan arasındaki ilişki gibi kartlar arası küçük bağlar, ortak gemi hayatını hissettiriyor.
- Saint Verena’da limanı görmenin yeterli olmaması, son geceyi hem anlatısal hem oyun açısından anlamlı kılıyor.
- İskorbütün önceki haftaların birikimi olarak açıklanması, açılışta birkaç saatte ortaya çıkan bir hastalık izlenimini azaltıyor.

1721, Arden, San Cordelio, Saint Verena, Veyr, Gusto ve Siyah Mühür çevresindeki mevcut çerçeve korunmalı. Framework içindeki şablonlar gerçekleşmiş olay veya yeni kanon olarak kullanılmamalı.

**Öncelikli bulgu 1: KAR-01 ve KAR-02’de gece adlandırması uyuşmuyor.**

Türü: Doğrulanmış metin uyuşmazlığı; uygulama sonucunun ve düzeltmenin QA tarafından değerlendirilmesi gerekiyor.

Kaynak: `working/v2.7/FOULWAKE_CARD_TEXTS_v2.7.json`  
Git blob: `38a03b71cd3232fd844db8d80d8e53662510b6a3`

| Kart | JSON alanı | Mevcut ifade |
|---|---|---|
| KAR-01 — Uzakgören | `/characters/0/effect` | “Tanışma gecesi hariç her gece bir Yakın Ufuk kartının olay yüzüne gizlice bakar. Sis onu engellemez.” |
| KAR-02 — Kıyıçizen | `/characters/1/effect` | “Tanışma gecesi hariç, Sis olmayan her gece bir Uzak Ufuk kartının olay yüzüne gizlice bakar.” |

Kilitli v2.6 kural kitabının 22. sayfasındaki §14, iki karakter için de istisnayı **“İlk tarafsız gece hariç”** olarak tanımlıyor.

Bunun yalnız sözcük farkı olmadığını gösteren kurulum akışı:

| Oyun anı | Kilitli kural |
|---|---|
| §3.5, s.7 — İlk tarafsız gece | “Bu gece yalnız Kaptanı uyandır. Karakter gece yetenekleri, Güçler ve Hain eylemi çalışmaz.” |
| §3.8, s.8 — İlk yolculuk gecesi, Hainlerin tanışması | Önce uygun gece karakterleri işletilir; Hainler en son uyandırılır. |

Karttaki “Tanışma gecesi” Hainlerin tanıştığı gece olarak anlaşılırsa, kural kitabında çalışması gereken karakterler o gece çalıştırılmayabilir. İlk tarafsız gecenin ayrı bir aşama olduğu da kart üzerinden anlaşılamayabilir. Bu, oyuncuların hangi bilgiye ne zaman erişeceğini etkileyebilir.

Önerilen işlem: Başeditör ve SIMULATION_QA, bu iki kartın ifadelerini §3.5, §3.8 ve §14 ile birlikte değerlendirmeli. Kaynak çatışması kaydedilmeli; düzeltilecek ifade ayrı görevle belirlenmeli. Bu rapor herhangi bir zamanlama değişikliğini kabul edilmiş saymıyor.

**Öncelikli bulgu 2: SET-KP-01 KAPTAN metninin kapsamı farklı yorumlara açık.**

Türü: Bağlayıcı proje sahibi metni ile ayrıntılı kurallar arasında açıklık sorunu; karar gerekiyor.

Kaynak: `working/v2.7/FOULWAKE_OWNER_CARD_TEXT_OVERRIDES_v2.7.json`  
Git blob: `1a0e03e19cbe3eacd1769aa186b0a444f4cc3e30`  
Alan: `/records/0/effect`

> “Oylamada eşitlik olursa, senin tarafın geçerli olur.”

Kilitli kural kitabındaki ilgili ayrımlar:

| Durum | Kaynak ve hüküm |
|---|---|
| Rota oylaması | §5.1, s.12: Kaptanın oyu 2; beraberliği yalnız berabere seçenekler arasından bozar. |
| Kaptan seçimi | §3.3, s.6: Önce berabere adaylar yeniden oylanır; tekrar eşitlikte d12 uygulanır. |
| Suçlama | §8.1, s.15: Başarı için uygun oyuncuların salt çoğunluğu gerekir. |
| Suçlama hedefinin ön seçimi | §8.1, s.15: Eşitliği Kaptan bozar; metin bunun resmî oylama olmadığını açıkça belirtir. |
| Suçlama/İsyan oy değeri | Arka kapak hızlı referansı, s.29: Kaptanın oyu 1’dir. |

“Oylamada” sözcüğü bütün oylamalara uzanan bir yetki gibi okunabilir. “Senin tarafın” ifadesi de Kaptanın daha önce oy verdiği seçeneğin otomatik kazanması izlenimi yaratabilir; rota kuralı ise berabere seçenekler arasından seçim yaptırıyor.

Burada “Kaptan yalnız rota beraberliğini bozar” şeklinde genel bir düzeltme de eksik olur: Suçlama hedefinin ön seçiminde ayrıca beraberlik yetkisi bulunuyor.

Önerilen karar yolları:

1. **Önerilen:** Mevcut ayrıntılı mekanik korunacaksa, kart metninin kapsamı yeni bir proje sahibi kararıyla açıklaştırılsın.
2. Exact kart metni korunacaksa, nasıl uygulanacağı ilgili kural açıklamasında netleştirilsin. Kart tek başına okunduğunda belirsizlik kalabileceği hesaba katılsın.

Ek yazım adayı: Aynı kaynağın `/records/0/flavor` alanı **“Lidere et. Gemi senin emrinde.”** biçiminde. “Lidere et.” ayrıca değerlendirilmesi gereken bir ifade; bağlayıcı exact metin olduğu için sessizce düzeltilmemeli.

**Öncelikli bulgu 3: Siyah Mühür anlatısında kesinlik düzeyi aynı kalmıyor.**

Türü: Anlatı tutarlılığı ve entegrasyon açığı.

v2.7 hikâye metninin §17 “Aynı işaret, ayrı eller” bölümünde bütün girişimlerin tek örgütten çıktığı kesinleştirilmiyor. Ortak talimat için de şu ifade kullanılıyor:

> “Hepsine aynı cümle söylenmiş olabilir. Ya da cümleyi içlerinden biri uydurmuş olabilir:”

Buna karşılık kilitli kural kitabının §5.3, s.12 bölümündeki anlatı notu şöyle başlıyor:

> “Siyah Mühür, geminin açık bir siyasi cinayete dönüşmesini istemez.”

İkinci ifade, Siyah Mühür’ün ortak iradesini anlatıcının bildiği bir gerçek gibi sunuyor. Yeni §17 ise örgütlenmenin niteliği ve ortak emir konusundaki belirsizliği koruyor.

Mevcut v2.7 hikâye dosyasının değiştirme blokları §3.1, §3.3, §3.4 anlatı notu, §3.6 ve §17’yi kapsıyor. §5.3’teki eski anlatı notu bu değişikliklerin dışında kalıyor.

Oyuncuya etkisi: Gizemin bir bölümünde özellikle korunan belirsizlik, başka bir bölümde anlatıcının kesin hükmüyle zayıflayabilir.

Önerilen işlem: Gelecek anlatı görevine §5.3’teki ilgili anlatı notu da alınmalı. Aynı paragraftaki, hikâyenin yeni mekanik yasak getirmediğini açıklayan hüküm korunmalı. Siyah Mühür’ün yapısı veya Gusto’nun akıbeti bu düzenlemeyle çözülmemeli.

**Açılış ve tempo için önerilerim mevcut oyun anlarına bağlı:**

| Mevcut an | Gözlem | Öneri ve beklenen yarar |
|---|---|---|
| §3.1 — Dünya ve görev | Terkip, formül kutusu ve kurumlar, oyuncunun kişisel sorumluluğundan önce ayrıntılanıyor. | Sefer heyetinin mevcut sorumluluğunu daha erken görünür kıl. Oyuncu ilk seçimden önce kendi yerini kavrasın. |
| §3.3 — Gusto ve Kaptan seçimi | Gizem ayrıntıları ilgi çekiyor; uzun tartışma ayrı bir dedektiflik oyunu beklentisine dönüşebilir. | Ayrıntıları mevcut Kaptan seçimine bağlayan geçişi güçlü tut. Gusto sorulduğunda mevcut “Bilmiyorsunuz.” sınırı korunsun. |
| §3.3 — Kalkış baskısı | v2.6’daki yeniden karantina riski, v2.7’de sağlık kâtiplerinin tekrar sayım şakasına dönüşmüş. | Kuru mizahla birlikte somut gecikme riskini de korumayı değerlendir. “Gemi bekleyemez” cümlesinin nedeni hissedilsin. |
| §3.2 — Karakter dağıtımı | Karakter sesi güçlendirilebilir; karakter kimliği gizli kalmalı. | Kart sahibinin kendi okuyacağı kısa davranış ve istek ipuçları düşünülsün. Herkesin karakterini açıkladığı zorunlu tanışma turu eklenmesin. |
| §3.6 — Sadakat | Borç, korku ve farklı inançlar güçlü motivasyonlar sağlıyor. | Metin kartı görme ve saklama anına doğrudan bağlansın; gizli kişilere dair ek ipucu üretmesin. |
| Harita olayı çözümü | Atmosfer anlatımı oyuncu konuşmasının yerini alabilir. | Kısa atmosferin ardından yazılı sonuç uygulansın; tartışma oyunculara bırakılsın. |
| Saint Verena — Liman Gecesi | Varış ile görevin tamamlanması arasındaki fark güçlü. | Son gece baskısı ve şafakta teslim fikri korunsun; terkip kesin başarılı ilan edilmesin. |

§3.1, §3.3 ve §3.6’daki üç `OKU` bloğu sırasıyla 149, 143 ve 94 sözcük; toplam 386 sözcük. Bu sayı tüm kurulum anlatımının uzunluğu değildir. §17 isteğe bağlı arka plan olarak kalmalı.

Tempo önerileri editoryal değerlendirmedir. Bu uzunlukların oyuncuları sıktığı veya önerilen kısaltmanın deneyimi iyileştirdiği insanlarla doğrulanmış değildir.

**Karakter sesleri ve küçük metin bulguları:**

Aşağıdaki kart alanlarının ortak kaynağı `FOULWAKE_CARD_TEXTS_v2.7.json`, git blobu `38a03b71cd3232fd844db8d80d8e53662510b6a3`.

| Kart ve alan | Bulgu | Önerilen yaklaşım |
|---|---|---|
| KAR-01 `/characters/0/flavor`, KAR-02 `/characters/1/flavor`, KAR-12 `/characters/11/flavor` | Görme/bilme fikrinden başlayıp ikinci cümlede ters köşe yapan benzer anlatıcı sesleri var. Bu bir mekanik hata değil. | Özellikle KAR-12’nin sesi, rota desteği sağlayan etkisiyle ilişkili olarak ikna ve yönlendirme davranışına yaklaşabilir. |
| KAR-13–KAR-20, `/characters/12`–`/characters/19` içindeki `effect` ve `flavor` alanları | “Özel mekanik gücü yoktur.” yazan karakterlerde kimlik yalnız şakadan ibaret algılanabilir. Bu, güçsüz veya dengesiz olduklarını kanıtlamaz. | Kısa bir istek, korku veya baskı altındaki davranış, mevcut tartışma ve oy verme imkânlarıyla bağ kurabilir. Yeni yetenek eklenmemeli. |
| KAR-18 `/characters/17/flavor` | “Dört saattir denizde. Üç saattir dönüş yolunu soruyor.” ifadesi, §3.4’teki haftalar süren Arden–San Cordelio yolculuğuyla birlikte zaman belirsizliği yaratıyor. | Dört saatin dönüş seferinin başlangıcından itibaren olduğu kastedilebilir. Bu nedenle kesin kronoloji hatası olarak kaydedilmemeli; sonraki metin düzenlemesinde açıklık değerlendirilmeli. |
| GUC-25 `/powers/26/effect` | “Bir oyuncının önüne koy…” biçiminde yazım hatası adayı var. | Copy QA’ya iletilmeli; ayrı yetkili düzeltme kapsamında ele alınmalı. |

Karakterleri ayrıştırmak için her karta uzun geçmiş eklemek gerekmiyor. Kimin nasıl itiraz ettiği, neyi sakladığı, neye alındığı veya tehlike karşısında hangi alışkanlığa sığındığı birkaç sözcükle farklılaşabilir.

**Üç kısa ifade örneği yalnız öneriyi somutlaştırıyor; yayımlanacak yeni metin değildir:**

| Yer | Mevcut ifade veya durum | Kısa öneri örneği |
|---|---|---|
| §3.1 | Sefer heyetinin yük defteriyle ilişkili sorumluluğu esas olarak §3.3’te açıklanıyor. | “Yük defterinde adınız var. Saint Verena’ya bu sandıkları siz ulaştıracaksınız.” |
| §3.3 | Beklemenin sonucu sağlık kâtiplerinin tekrar sayımı üzerinden anlatılıyor. | “Sabahki gelgit uygun. Beklersek yeniden karantinaya alınabiliriz.” |
| KAR-12 `flavor` | “Yukarıdan bakınca herkes küçük görünür. Şüpheler değil.” | “Orayı gördüm demedim. Oradan gidelim dedim.” |

İlk örnek mevcut sefer sorumluluğunu öne getiriyor. İkincisi kilitli kaynakta zaten bulunan karantina baskısını hatırlatıyor. Üçüncüsü KAR-12’yi gözlem yapan diğer karakterlerden ses bakımından ayırmayı deniyor. Hiçbiri bu teslimle kaynak metne eklenmedi.

**Hikâye, gizli bilgi ve sanat ilişkisine dair değerlendirme:**

Moderatörün atmosfer kurarken yeni ipucu, suçlu iması veya gizli eylem sonucu üretmemesi gerekiyor. Şüphe oyuncuların sözleri ve mevcut kuralların görünür sonuçlarından doğmalı. Anlatım, oyuncunun kararının sonucunu geri almamalı.

Art Bible’ın özellikle §§2–5, 11–12 ve 19 bölümleri ile kabul edilmiş KAPTAN patch’i dikkate alındı. KAPTAN’ın eski boş koltuk yaklaşımı güncel kabul edilmiş yönelim olarak kullanılmadı. Bağlayıcı ana figür korunmalı; bu figür kendiliğinden Gusto diye tanımlanmamalı.

Her karta siyah balmumu, Gusto veya aynı gizem simgesini yerleştirmek ortak dünya duygusunu tekdüzeleştirebilir ve istemeden kanıt izlenimi yaratabilir. Gemideki iş, eşya ve kişiler arası küçük ilişkiler de süreklilik sağlamalı. Görsel uygulama ve estetik kabul kararları Sanat Yönetimi ile proje sahibinin alanında kalıyor.

**İncelenen kapsam ve sınırlar açıkça şöyledir:**

Üç hikâye belgesinin tamamı okundu:

| Belge | Git blob |
|---|---|
| `working/v2.7/FOULWAKE_STORY_FRAMEWORK.md` | `962222d83d669763c4ac8e2765f024b9fade180c` |
| `working/v2.7/FOULWAKE_RULEBOOK_STORY_v2.7.md` | `f1e0eb75434540a85e8b21484acd99ca0abc66cf` |
| `working/v2.7/FOULWAKE_STORY_REVALIDATION_v2.7.md` | `2b4b4d423c65d5b72f756d322d9b0bd3c8537afa` |

Kart incelemesi örneklemle sınırlı kalmadı:

| Grup | İncelenen kimlikler | Kayıt |
|---|---|---|
| Karakter | KAR-01–KAR-20 | 20 |
| Güç | GUC-01A/B, GUC-02A/B, GUC-03–GUC-28 | 30 |
| KAPTAN | SET-KP-01, proje sahibi override metni | 1 |
| **Toplam** | **Mevcut çözümlenen kart metinleri** | **51** |

121 kimlikli manifest yalnız kapsam kontrolünde kullanıldı. Aşağıdaki 70 kimlik için bu görevde yetkili kart metni incelemesi tamamlanmış sayılmıyor:

| Grup | Kimlikler | Kayıt | Durum |
|---|---|---|---|
| Erzak | ERZ-01 | 1 | UNREVIEWED_SOURCE_GAP |
| Sadakat | SAD-T-01–10, SAD-H-01–05 | 15 | UNREVIEWED_SOURCE_GAP |
| Ada | HAR-AD-01–30 | 30 | UNREVIEWED_SOURCE_GAP |
| Kayalık | HAR-KY-01–12 | 12 | UNREVIEWED_SOURCE_GAP |
| Açık deniz | HAR-AA-01–06 | 6 | UNREVIEWED_SOURCE_GAP |
| Fener | HAR-FN-01–04 | 4 | UNREVIEWED_SOURCE_GAP |
| Liman | SET-KL-01, SET-VL-01 | 2 | UNREVIEWED_SOURCE_GAP |
| **Toplam** | | **70** | |

Bu durum, söz konusu metinlerin hiçbir yerde bulunmadığı iddiası değildir. Kaynakları mevcut QA envanteriyle doğrulanıp incelemeye alınmalıdır. Sanat brief’leri eksik kart metinlerinin yerine kullanılmadı.

`COPY-SOURCE-INVENTORY-001` bağımlılığı sürüyor. Bu rapor 121 kartın tamamına PASS vermiyor. Önceki `STORY_REVALIDATION` belgesindeki tarihsel PASS da yeni, bağımsız insan deneyimi kanıtı olarak kullanılmadı.

SRC-002’nin bağlayıcı eşlemesi korundu: GUC-22 **Kaptanın Çatlak Kupası**, GUC-23 **Bayat Peksimet**, GUC-24 **Islak Çorap**.

Kural karşılaştırmalarında kullanılan dosya, kilitli v2.6 paketindeki `OYUN_Kural_Kitabi_v2.6.pdf` dosyasıdır. PDF SHA-256:

`192f790d89e987a312d6a36879e7b063ee13426c9508b4e474f16f2cad723c2a`

Sayfa numaraları bu 29 sayfalık PDF’ye aittir. Paket kimliği ve konumu [v2.6 kaynak paket kaydında](https://github.com/uguraltn5252-sketch/acik-deniz-oyunu/blob/1a9e212b7b0df9bfbbdf950657613acccc0c2eda/releases/v2.6/SOURCE_PACKAGE.md), diğer sabitlenmiş girdiler [görev dosyasının inputs alanında](https://github.com/uguraltn5252-sketch/acik-deniz-oyunu/blob/1a9e212b7b0df9bfbbdf950657613acccc0c2eda/governance/v4/tasks/STORY-COHERENCE-IMMERSION-001.json) bulunuyor.

**Başeditörden beklenen işlem:** Üç öncelikli bulguyu kaynaklarıyla bağımsız değerlendirmek; kabul edilen bulguları, stil önerilerini ve karar bekleyen maddeleri kaydetmek. Ardından gerekli uygulama görevleri rol ve dosya kapsamıyla açılabilir.

Gece terminolojisi ile KAPTAN’ın kural kapsamı SIMULATION_QA değerlendirmesi gerektiriyor. Bağlayıcı KAPTAN metnindeki değişiklik proje sahibi kararı gerektiriyor. Açılış, §5.3 anlatı notu ve karakter sesi önerileri kabul edilirse STORY_EDITOR için sınırları belirli görev açılabilir.

Oyuncuyu içine çekme ve tempo önerilerinin etkisi henüz kanıtlanmış değil. Daha sonraki yetkili insan denemesinde, oyuncunun ilk seçimden önce görevini kendi sözleriyle açıklayıp açıklayamadığı ve anlatımın tartışmayı kesip kesmediği gözlenebilir.

```text
TASK_ID: STORY-COHERENCE-IMMERSION-001
SOURCE_HEAD: fb64fbcba2d6f359cc274f9e3cb9aa4df36fae5b
DELIVERY_COMMIT: NONE / READ_ONLY_CHAT_REVIEW
CHANGED_PATHS: []
RESULT_AND_EVIDENCE: Üç hikâye belgesi ve 51 kartın incelemesi tamamlandı. Bu teslim; üç öncelikli kaynak bulgusunu, açılış ve tempo önerilerini, karakter sesi değerlendirmesini, kısa ifade örneklerini ve kapsam sınırlarını içerir. Rapor aktarımında güncel HEAD 1a9e212b7b0df9bfbbdf950657613acccc0c2eda doğrulandı; 12 görev girdisi değişmemiştir.
OPEN_BLOCKERS: Başeditörün ayrıntılı raporu kabul değerlendirmesi; QA kaynak envanteri; KAR-01/KAR-02 gece terminolojisi; KAPTAN kapsam kararı; 70 kart için kaynak doğrulaması ve metin incelemesi. Oyuncu deneyimi önerileri insanlarla doğrulanmamıştır.
NEXT_RESPONSIBLE_ROLE: CHIEF_EDITOR
```
