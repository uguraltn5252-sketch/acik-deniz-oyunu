# FOULWAKE — baştan sona kontrol ve uygulanan düzeltmeler

8 Eylül 2026 · CHIEF_EDITOR · FOULWAKE-WHOLE-GAME-POLISH-001

Bu çalışma yalnız öneri raporu değildir. Kart JSON'u, hikâye, kural kitabı, sanat yönlendirmesi ve yeni baskı PDF'leri değiştirildi. Başlangıç GitHub HEAD'i `50cb0c73854364812c5573e75f403619fe18e58a`; güncel owner yetkisi `OWNER_WHOLE_GAME_POLISH_AUTHORITY_20260908.json` ile kaydedildi. Çalışma ve entegrasyon dalı v2.7-design'dır.

## İncelenen kapsam

Üç hikâye belgesi ve tam kural kitabı baştan sona okundu. 121 kartın ad, sınıflandırma, zaman, etki ve tat metinleri kaynak üzerinden incelendi; PDF'deki yazılar ayrıca kaynakla karşılaştırıldı. 121 ön resmin tamamı ve yedi arka aile, görsel inceleme ile baskı sayfalarında görüldü. Sayfa kaydı `pdf_inspection_index.json`; kart bazındaki kayıt `review_matrix.json` içindedir.

| Grup | Kapsam |
|---|---|
| Karakter | KAR-01–20: 20 |
| Güç | GUC-01A/B, GUC-02A/B, GUC-03–28: 30 |
| Erzak | ERZ-01: 1 |
| Sadakat | SAD-T-01–10, SAD-H-01–05: 15 |
| Açık deniz | HAR-AD-01–30: 30 |
| Kayalık | HAR-KY-01–12: 12 |
| Ada | HAR-AA-01–06: 6 |
| Fener | HAR-FN-01–04: 4 |
| Yardımcı | İki liman ve KAPTAN: 3 |

Önceki rapordaki 70 kaydın kaynak açığı artık yoktur: 7 Eylül'de bulunan yetkili kaynaklar bu kontrolde yeniden kullanıldı. Art brief'i eksik kural metni yerine geçmedi. Kilitli v2.6 paketi değişmedi.

## Gerçek düzeltmeler

| Yer | Sorun ve uygulanan çözüm |
|---|---|
| Fener ortak arkası | Aynı kartta ikinci, ters kule görünüyordu. Beğenilen üst sahne aynı kaynak ve ölçekte korundu; alt kopyanın yerine deniz devamı geldi. Dört fener aynı tek kuleli masterı kullanıyor. |
| HAR-KY-02 | “Dipgören kullanılırsa 1 ek Güç kazanır” alıcının Dipgören olduğu izlenimi veriyordu. “1 ek Güç kazanılır” oldu; normal alıcı seçimi korunuyor. |
| HAR-AA-02, HAR-FN-01 | Uzun kamusal açma metni kısaldı. Kapalı, yasal Ufuk seçilir; açık kalır, olay ilk girişte çözülür. Mekanik kapsam daraltılmadı. |
| GUC-27 ve §6.4 | Metin ve “Olay açılınca” etiketi hareket penceresini bulanıklaştırıyordu. Etiket “Hareket sırasında” oldu. Önceden Pusulayla açılan kartın ilk girişinde de kullanılabilir; Pusula/Fenerin yalnız uzaktan göstermesi tetiklemez. Ada temizliği ve Geçilmez ayrımı korunur. |
| §4.2, §8.4, §11.2 | “Gemide ve Kamarada olmayan” yerine gemide bulunma ve Kamara dışında olma açıkça yazıldı. Kaptan Kamaraya girerse önce yeni Kaptan seçilir; konuşma iznini yeni Kaptan verir. |
| HAR-AD-14 | “Bir Kişilik Eksildik” → “Yoklamada Bir Eksik”. Olayı ve kuru mizahı doğal Türkçeyle taşıyor. |
| HAR-AA-06 | “Gümrükçünün Tek Yaşadığı Ada” → “Tek Kişilik Gümrük”. Kısa, söylenebilir ve resimdeki tek memurla uyumlu. |
| HAR-AA-01 | Resim erzak alışverişi gösterirken tat metni sahipsiz yağma izlenimi veriyordu. Şimdi yükün taşınması ve borcun kime yazılacağı üzerinden ilerliyor. |
| Yedi tat metni | SAD-T-07/10; HAR-AD-24/26; HAR-AA-01/05; HAR-KY-02 somut davranış veya nesneye bağlandı. Otomatik ikinci cümle ters köşeleri azaltıldı. |
| Açılış | San Cordelio'nun ecza rıhtımı ve Arden'in dönülen krallık olduğu ilk paragrafta açıklanıyor. Saint Verena varıştaki karantina limanı. |
| Kitap ve kart dizgisi | Zafer cümlesinin sayfa arasında parçalanması giderildi. Kapak alt başlıkları ayrı satırlara alındı. Boş meslek çizgileri kart üst bilgisinden çıkarıldı. Hızlı referanstaki iç dosya yolları temizlendi. |
| Güncel kayıtlar | “12 pilot / 109 tamamlanmadı” gibi eski kapsam notları ve eski PDF bağlantıları güncel belgelerde düzeltildi. Tarihsel raporlar tarihsel olarak işaretlendi. |

Bu turda 12 kartın kaynak alanlarında değişiklik vardır. Önce/sonra ifadeleri ve gerekçeler `changes.json` dosyasındadır. Kurulum adetleri, Hain sayıları, Gövde, Etki değerleri, zafer koşulları ve SRC-002 eşlemesi korunmuştur.

## Göndermeler gerçekten uygulanmış mı?

Dördü de birer kartın tat metninde bulunuyor. Resim, franchise figürü veya ayrı bir bulmaca olarak genişletilmedi. Bunların nasıl anlaşılacağını oyuncuya açıklamak gerekmiyor.

| Eser | Kart | Kullanılan küçük bağ |
|---|---|---|
| One Piece | GUC-15 — Kaptanın Eski Şapkası | Geri verilecek şapka ve önce tutulması gereken söz. Resim FOULWAKE'ın dönem şapkasıdır. |
| Karayip Korsanları | GUC-03 — Pusula | Kuzey yerindeyken sahibinin başka bir şey araması. Mekanik pusulaya büyülü istek bulma gücü eklenmez. |
| Prens | GUC-18 — Mühürlü Emir | Prensin adına boşluk ayrılmış, buyruğu üç sayfa. Yeni bir prens karakteri kurulmaz. |
| Moby-Dick | GUC-05 — Yama Tahtası | İyileşen bir müşteri için hazırlanmış tabut tahtasının gemide işe yaraması. Balina veya Ahab hikâyesi eklenmez. |

Kaynaklar yeniden kontrol edildi: [Netflix'in şapka/söz açıklaması](https://www.netflix.com/tudum/articles/one-piece-ending-explainer), [Karayip Korsanları resmî hesabının pusula açıklaması](https://www.facebook.com/PiratesoftheCaribbean/photos/this-compass-does-not-point-northit-points-to-the-thing-you-want-most-in-this-wo/10152659240458830/), [HBO Max Prens tanıtımı](https://www.hbomax.com/tr/tr/show/9b669a12-2428-421c-94e7-d295675cc742), [Moby-Dick tam metni](https://www.gutenberg.org/files/2701/2701-h/2701-h.htm). Netflix ve romanın ilgili metinleri okundu; resmî sosyal hesap ve HBO tanıtımı arama sonucunun görülebilen açıklamaları üzerinden doğrulandı. Buradaki dönüştürme ve kartlara uygunluk değerlendirmesi editoryal yargıdır.

## Adlar, karakterler ve tempo

Kuru Pay korunuyor: adı, gemide tehlikeyi paylaşmadan kıyıda kazanılan gelire bağlanıyor. Kısa ve oyunun çıkar çatışmasıyla ilişkili. Bunun dünyada tek bir örgütün kesin adı olduğu söylenmiyor. Siyah balmumu kanıt haline getirilmiyor. Gusto'nun akıbeti ve Veyr'in terkibinin başarısı çözülmüyor.

Arden, San Cordelio ve Saint Verena'yı sırf yeni ad üretmek için değiştirmedim. İşlevlerini ayırmak daha faydalı: memleket/krallık, ecza rıhtımı, karantina varışı. Eleonora, Mattias Veyr ve Gusto Varela'nın çıkarları farklıdır. Bu adların akılda kalıcılığına ilişkin insan ölçümü yapılmış değildir.

Beş Hain aynı “para aldın” cümlesinin çeşitlemesi değildir: bakım borcu, çıkış belgesi karşılığında rehin aile, ölü birinin kimliğiyle kaçışın açığa çıkması, eksik hastane kaydına inanma ve sahte denizde kayıp kaydı. On Tayfanın da ev, hastalık, borç ve söz gerekçeleri bulunur; hasta ailesi olmak Hain kanıtı olmaz. Gerekçeler gizlidir, yeni yan görev veya farklı zafer şartı üretmez.

Kara komedi hastayı küçültmekten değil; ödenen ücret, sağlam kalan kilit, eksik duvar, gümrük, kayıp çorap ve tehlikede bile süren alışkanlıklardan doğar. Sekiz özel yeteneksiz Karakter, konuşma ve oy hakkıyla oyundadır. Karga Yuvası ikna eden, Kıyıçizen düzen arayan, Uzakgören mesafeye güvenen ayrı seslerini korur.

Karşılaştırılabilir üç OKU bloğu 88 + 99 + 52 = 239 sözcüktür; ilk raporda 386 idi. Bu, bütün kurulumun uzunluğu değildir. §17 isteğe bağlı kalır. Olay anlatımından sonra söz oyuncuya bırakılır; zorunlu konuşma turu, ek sayaç veya ipucu üretilmez. Tempo ve eğlence etkisi insan masasında henüz ölçülmedi.

## Görsel ve baskı kanıtı

121 ön kaynak dosyası ve KAPTAN'ın sabit kırpımı korunmuştur. Karakterlerin yüzü, beden ölçeği, işi ve kadrajı; Güçlerde nesnenin kullanımı; Sadakatlerde gizli kimlik sızdırmama; Haritalarda aynı aile içindeki sahne ayrımı incelendi. Sözcüklerle resim arasındaki belirgin uyuşmazlık HAR-AA-01'de metin üzerinden giderildi. Resimleri sırf yeniden üretmek için değiştirmedim.

Tek fener masterı native PDF katmanıdır: üst 0–650 kaynak satırı eski çizim, alt bölüm yeni deniz. Karşılaştırma birleşim sınırından önceki 0–649 satırda yapıldı. 300 DPI'da 898×465 piksel, kanal farkı 0. `lighthouse_preservation_check.json` bu sınırlı ama birebir korumayı kanıtlar. Alt bölümün değiştiği açıktır; resmin tamamı aynı denmez. Modelin düzenlenmiş üst kısmı nihai baskıda kullanılmaz.

Etki 8,6 ve tat metni 8 punto kaldı. HAR-AA-02 resim alanı 13,853'ten 21,684 mm'ye; GUC-27 14,790'dan 18,706 mm'ye çıktı. En düşük ön resim çözünürlüğü 386,94 DPI. 48 kart, 24 görsel inceleme ve 30 kitap sayfası render edildi. Metin, taşma, kadraj, arka eşleme ve sayfa sürekliliği kontrol edildi; düzeltmeden sonra etkilenen yerleşimler yeniden görüldü.

## Teknik sonuç ve gerçek sınırlar

- 27 kural regresyonu geçti. Test kaynakları mevcut motorun gözlem ve hedefleme sınırlarını denetler.
- 3.600 eşlenmiş, sabit tohumlu model yolculuğu yeniden çalıştı. A ve B'de 1.800'er oyun; boş gemi çıkmazı ve kimlik kartı ıskartası sıfır. Bu motor bütün kart etkileşimlerini veya insan konuşmasını modellemez; kazanma yüzdeleri denge onayı değildir.
- 121 kartın kaynak/PDF metni, 121 resim kimliği ve yedi aile arkası geçti. İndirme bölümlerinin 99 sayfası ana PDF'lerle raster olarak eşleşti. Kitabın kaynak parçaları PDF'de doğrulandı.
- Güncel dosya özetleri `render_manifest.json`, teknik sonuç `print_checks.json`, model ham verisi `simulation_games.csv`, model sınırları `simulation_results.json` içindedir.

Kontrol ve üretim aynı operatörce yapıldı. Doğrulanmış ana model kimliği UNKNOWN; resim düzenleme aracı image_gen.imagegen, sürümü açıklanmıyor. Geçici ajan veya bağımsız değerlendirici kullanılmadı. İnsan oyunu, fiziksel baskı/opaklık, bağımsız estetik kabul ve release/lock verilmedi.
