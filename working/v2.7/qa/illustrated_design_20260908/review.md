# FOULWAKE — bütünleşik kart tasarımı, uygulama ve kontrol

8 Eylül 2026 · FOULWAKE-ILLUSTRATED-DESIGN-002 · CHIEF_EDITOR

121 ön kart, proje sahibinin referansındaki tasarım diliyle özgün olarak yeniden üretildi. Her levha çerçevesi, başlık şeridi, karakter/sahnesi ve yazı zeminiyle tam kart için tasarlandı. Güncel metinler levhaların üzerine native PDF yazısı olarak aynen dizildi. 121 tamamlanmış kart ayrı ayrı, baskının 48 ve incelemenin 34 sayfası ayrıca gözle kontrol edildi. Teslim SAME_OPERATOR_SELF_CHECK; proje sahibi estetik değerlendirmesi bekleniyor.

## Sorunun kaynağı

İncelenen önceki HEAD `641ed130fc2ae76c4217979d510e19a4676b0f0c`.

| Doğrulanan sorun | Kaynak | Yapılan düzeltme |
|---|---|---|
| KAPTAN doğrudan referanstan `(22,180,874,1093)` alanıyla kırpılıyordu. | `qa/whole_game_polish_20260908/build_print.py` | KAPTAN dahil 121 özgün tam levha; bütün önlerde tek, kırpmayan yerleşim yolu. |
| Önceki üretim brief'leri çerçeve ve yerleşimi resimden dışlıyordu; çizim, metinden kalan küçük alana giriyordu. | `qa/full_deck_art/prepare_prompts.py` ve önceki baskı üretimi | Önceden hesaplanan yazı ihtiyacı, karta özel tam tasarım; uzun kurallar için çizim aracında büyütülen paneller. |
| Görsel inceleme yalnız çizimleri gösteriyor, son karttaki metin/resim dengesini gizliyordu. | Önceki `build_review` | İnceleme ve baskı aynı native tam kart masterını kullanır. |
| Önceki metin prototipi resimsiz devam edebiliyordu. | `qa/recheck_visual/build_print.py::front` | Eksik resimde duran üretim; 121 kimliğin açık eşlemesi ve tek güncel giriş. |
| Ana README eski 12 önlü pilotu ve 109 resimsiz kart içeren metin prototipini güncel diye açıyordu. | `README.md@e6398070c4a7b479092946261d0e121952dbbfe7` | Koordinasyon kapanışında kök README ve iki handoff eski dosyalar yerine yeni tam kart dizinine yönlendirilir. |

Son eski 48 sayfalık destede teknik olarak 121 resim vardı ve eksik resimde üretim duruyordu. Kullanıcının gördüğü eski dosya kesin tanımlanmadığı için, “son destenin 121 kaynak resmi eksikti” sonucu çıkarılmadı. Eski prototipe götüren ana README bağlantısı doğrudan doğrulandı; kullanıcının tam olarak o bağlantıyı açtığı iddia edilmez. Doğrulanan tasarım, kırpım, bağlantı ve kontrol kapsamı sorunları giderildi. Ayrıntılı kaynak kaydı: [root_cause.json](root_cause.json).

## Uygulanan sanat kararı

Sıcak tuzlu kâğıt, çift mürekkep çerçeve, kıvrılan şerit, yönlü gravür ve mat lacivert/oker/pas tüm önleri birleştirir. Karakterin yaptığı iş ve tepkisi ana odaktır. Şaka; otoritenin masrafına, gemi alışkanlıklarına ve insanların kendi çelişkilerine bağlıdır. Aynı kaptan, martı veya örgüt simgesi desteye tekrarlanmadı.

KAPTAN'ın yeni sahnesi dümen, ödeme listesi ve yorgun tayfadan kuruldu. Tekrarlanan Harita etkileri farklı iş ve tepkilerle resmedildi. Hainlerin gerekçeleri karikatür kötülüğe dönüşmedi; Tayfa/Hain ortak gizli arkası korundu. Tahtakakan ile Tahtaya Vuran arasındaki kişi sürekliliği düzeltildi. Modern şapka, pano mandalı ve sağlık haçı sapmaları temizlendi; kurtarma halkasının doğal mantar yapısı belirginleştirildi.

Kuralların üzerine giren süsler GUC-28, SAD-H-01/03 ve HAR-AD-09'da kaldırıldı. Uzun metinlerde paneller genişletildi; yazı ile sahne arasındaki sınırlar her karta ayrı ölçüldü. Başlıklar kıvrılan şeridin düz orta kısmına alındı. HAR-AA-03 ve HAR-AD-05'in uzun başlıkları %92 yatay yazı ölçeğiyle şeride sığdırıldı. Son kayıtlar önceki adayları geçersiz kılar; tam değişiklik istemleri [revision_requests.json](revision_requests.json) içindedir.

| Korunan gönderme | Kart | Mevcut anlam |
|---|---|---|
| One Piece | GUC-15 | Şapka ve verilen söz |
| Karayip Korsanları | GUC-03 | Kuzeyi değil sahibinin isteğini izleyen pusula |
| Prens | GUC-18 | Adı boş bırakılmış prens, gereğinden uzun buyruk |
| Moby-Dick | GUC-05 | Yaşayana yarayan tabut tahtası |

Bu göndermeler yeni karakter, alıntı, logo veya kostüm kopyası eklemeden korundu. 1721, Arden, San Cordelio, Saint Verena ve Kuru Pay değişmedi. Güncel hikâye/kart/kural metinleri bu görsel görevde yeniden yazılmadı.

## Sonuç ve kanıt

| Kontrol | Sonuç | Kayıt |
|---|---|---|
| 121 özgün, farklı, kayıpsız kaynak PNG | PASS; en düşük özgün çözünürlük 347,13 DPI | `generation/`, `delivery_checks.json` |
| Her kartın native yazıyla tamamlanmış hâli | 121 ayrı görsel inceleme; kart bazında not ve kaynak/proof SHA-256 | `individual_visual_review.json` |
| Panel, başlık ve güvenli alan | 121 geometri PASS | `art_annotations.json`, `proof_index.json` |
| Ön master, baskı ve incelemede exact metin | 363 yerleşim PASS | `delivery_checks.json` |
| Son master ile incelenen kartın görüntüsü | 121/121 birebir render özeti eşleşmesi | `delivery_checks.json` |
| A4 ön/arka eşleşmesi ve gizli arkalar | 121 çift, yedi ortak aile, doğru sütun aynalama | `render_manifest.json`, `delivery_checks.json` |
| Fener arkasının korunması | Tek dik kule; master byte olarak aynı | `retained_backs.json` |
| Son PDF sayfalarının gözle incelenmesi | 82/82 sayfa, 21 görüntü grubu | `pdf_inspection_index.json` |
| Bölümlenmiş PDF'ler | 19 baskı + 15 inceleme bölümü; 132 sayfanın ana dosyayla render eşleşmesi | `render_manifest.json`, `delivery_checks.json` |

Son kontrolde dört yerel proof dosyasının sıfır byte olduğu görüldü. Son masterdan geri oluşturulan görüntüler, önceden kaydedilmiş ve gözle incelenmiş SHA-256'larla birebir eşleşti. Bir PDF kontaktı da yeniden render edilip gözle incelendi. Kaydetme işlemi geçici dosya/doğrulama/atomik değiştirme ile güçlendirildi. Bu geçici dosya sorununun sistem düzeyindeki nedeni doğrulanmadı; teslim PDF'leri tam açılma, sayfa, byte özeti ve render kontrolünden geçti.

Arka doğrulayıcının ilk denemesi, PDF'nin kırpılmış native formlarının görünmeyen kaynak resimlerini de sayıyordu. Kontrol, gerçekten yerleşen kırpma formunu, aile içinde ortak gömülü kaynağı ve arka masterıyla aynı native sayfa içeriğini doğrulayacak şekilde düzeltildi. Son arka sayfalar ayrıca gözle incelendi. Yalnız nesne adedi estetik kanıt sayılmadı.

## Teslim ve yeniden üretim

[Güncel indirme dizini](../../visual/illustrated_design_20260908/README.md). Baskı 48, tam kart incelemesi 34 sayfadır. Orijinaller `visual/illustrated_design_20260908/assets/` altındadır; yedi korunmuş arka PDF aynı teslimin `pdf/` dizinindedir. Asıl PNG'ler kırpılmadı, yeniden boyutlandırılmadı veya renklendirilmedi. PDF için JPEG 93 kodlama kullanıldı; yazılar raster değildir.

Bu çalışma ortamındaki ReportLab, PyMuPDF, Pillow, NumPy, pypdf ve Liberation Serif ile `python -B working/v2.7/qa/illustrated_design_20260908/build_deck.py` tam PDF'leri yeniden kurar. Var olan arka masterlarının özetleri doğrulandığında eski geçici baskı dosyasına ihtiyaç duyulmaz. Tekil proof üretimi `inspect_cards.py`, son teknik kontrol `verify_delivery.py` ile yapılır. Yeniden üretim yeni görsel kabul oluşturmaz; kayıtlı proof ve kaynak özetleri karşılaştırılmalıdır.

Gerçek ana model kimliği ve görüntü üretim modelinin sürümü çalışma ortamınca açıklanmadı; UNKNOWN kaydedilir. Kullanılan resim aracı `image_gen.imagegen`dir. Geçici alt ajan kullanılmadı. Bütün sanat ve kontrol bu Baş Editör operatörüne aittir. Bağımsız estetik kabul, insanlarla oynanabilirlik, fiziksel baskı/renk/kesim/opaklık veya tam kural motoru eşdeğerliği iddia edilmez. Kilitli v2.6 ve uzman dal başları korunur; release/lock verilmedi.
