# Yayın teslimi — değişiklik ve kalite kontrol kaydı

FOULWAKE-PUBLICATION-REDESIGN-001 · 9 Eylül 2026 · SAME_OPERATOR_SELF_CHECK

İki çıktı: **121 kartın tamamı tek 46 sayfalık A4 çift taraflı PDF**, **30 sayfalık A4 kural kitabı**. [Baskı dosyaları](../../publication_20260909/README.md).

## Değişiklikler

- Kraliçe Tesella, Port Avanta, Santa Veda ve Malum güncel kanondur. Tesella'nın siyasi yetkisi, kalkış limanının ticaret hayatı, varışın karantina baskısı ve Malum'un borç/izin ağları hikâyeye işlendi. Gusto'nun akıbeti ile deneysel terkibin başarısı kesinleştirilmedi.
- Kart kaynağındaki 13 görünür alan yalnız yetkili yer adı dönüşümüdür. Tüm 121 kimlik, oyun etkisi, özel zamanlama, Kaptan override'ı, kişisel Sadakat gerekçeleri ve dört örtük gönderme korunur. Önceki görevlerde giderilmiş gece terminolojisi ve Kaptan kapsamı bu baskıda yeniden bozulmadı.
- Tek Alegreya ailesi, daha sakin okuma panelleri ve belirgin etki/tat ayrımı kullanıldı. Papağanın İfadesi ve Duvar Gibi Kayalık başlıkları 0,3 mm aşağı alındı. Çürümüş Erzak başlığı, kaynaktaki zorunlu açma zamanını eksiksiz gösterir.
- Kitap yeniden dizildi: yalnız FOULWAKE yazılı özgün kapak, özgün iki küçük illüstrasyon, içindekiler ve PDF gezinmesi, OKU/YAP kutuları, yinelenen tablo başlıkları, gerçek kurala bağlı Harita/Ufuk şemaları, sık karışan durumlar ve tek sayfalık hızlı başvuru. Kaynak kuralların tamamı korunur.
- 121 özgün ön çizim ve yedi ortak arka master değiştirilmedi. Tek kuleli fener ve kumlu palmiye Adası korunur. Harita olayları yeniden uydurulmadı.

## Kontrol sonuçları

[Teknik doğrulama](verification.json) PASS: 363 kart başlık/etki/tat alanı, ek zaman/rol/yer metinleri ve 714 kitap kaynak birimi son PDF ile eşleşir. Üç ad taraması; dört ana kaynak, 11 türetilmiş güncel kayıt ve 76 son PDF sayfası ile metadata üzerinde eski isim bulmadı. Tarihsel kararlar, eski çıktılar ve dondurulmuş v2.6 paketi güncel üretim girdisi değildir; kanıt geçmişi değiştirilmedi.

121 çiftin tümünde arka konum, öne göre yatay yansımadır. Kartların kendileri aynalanmadı. Kesimler 70×120, 63,5×88,9 ve 70×70 mm; taşma 3 mm. Ana metnin gerçek harf sınırları en az yaklaşık 4,5 mm güvenli alanda kalır. Küçük üretim kimliği ayrı kontrol edilir. A4 sayfa ölçüleri, çift sayfa sayısı, uzun-kenar tercihi, gömülü fontlar ve bozuk karakterler denetlendi. Görsellerin en düşük etkin çözünürlüğü kartlarda 300,08 ppi, kitapta 304,22 ppi'dir.

[Görsel inceleme](visual_review.json): 121 tam kart yüzü 23 panoda, 30 kitap sayfası 15 ikili görünümde, 46 baskı sayfası 12 panoda incelendi. Son üç kart düzeltmesi ve yeni arka görselleri kullanan kitap sayfası 4 ayrıca yeniden görüldü. Başlık/metin çakışması, eksik görsel, yanlış ortak arka, ikinci fener ve yanlış kesim yerleşimi gözlenmedi. Kartların fotoğrafik referans kırpımı olmadığı ve mevcut özgün gravür dilini koruduğu kontrol edildi.

İlk teknik geçiş beş güncel metadata ad kalıntısı, eksik Erzak başlığı ve iki başlığın kesim yakınlığını buldu; bunlar düzeltildi ve aynı kontroller yeniden PASS verdi. Güvenli alan testi fontun satır yüksekliğinden değil gerçek harf çizgisinden ölçer; görünür metin sınırı korunur.

Bu, üreticinin dijital kontrolüdür; bağımsız estetik kabul, fiziksel yazıcı provası, renk profili provası veya insanlarla oynanmış deney sonucu değildir. İnsan eliyle üretildiği veya eğlencenin ölçülerek arttığı iddia edilmez. Ev tipi A4 baskı hedeflenmiştir; yazıcı kayması ve kâğıt opaklığı ilk yaprakta fiziksel olarak denetlenmelidir. Release/lock kararı verilmedi.

## Yeniden üretim

Depo kökünde `python3 -B working/v2.7/qa/publication_20260909/cards.py`, ardından `book.py` ve `verify.py` çalıştırılır. ReportLab, PyMuPDF, Pillow ve fontTools gerekir. Özgün çizimler önceki tam deste klasöründen, üç yeni kitap çizimi ve gömülü fontlar bu yayın klasöründen okunur. Teknik kontrol kanıtındaki SHA-256 değerleri teslim PDF'lerini tanımlar; yeniden oluşturma, dosya metadata'sına bağlı olarak yeni byte kimliği üretebilir. [Araştırma](research.md), [görsel kaynak kaydı](generation_provenance.json), [kart kaynak değişiklikleri](copy_changes.json).

## Tek dosyalık GitHub aktarımı

PDF'ler kalite kaybıyla küçültülmedi. Bağlantının 16 MiB istek sınırı nedeniyle dosya byte'ları küçük Git blob parçalarıyla taşındı. Geçici, yalnız iki sabit SHA-256'ya ve exact aktif göreve izin veren işlem, bunları GitHub üzerinde aynı PDF'ler olarak birleştirir. Kullanıcı iki normal PDF indirir; parça birleştirme yapmaz. Koordinasyon kaydı `governance/v4/evidence/PUBLICATION_BINARY_TRANSFER_20260909.json`. Nihai byte eşitliği kapanış kanıtına bağlanır. Bu aktarım herhangi bir kural, PDF içeriği veya release kararı üretmez.
