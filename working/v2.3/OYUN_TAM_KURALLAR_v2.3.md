# OYUN - Tam Kural Sözleşmesi v2.3

**Tarih:** 18 Ağustos 2026  
**Durum:** Geliştirme / teknik PASS / insan masa testi bekleniyor.  
**Temel:** v2.2 stabil prototip. Bu dosya v2.2 tam kurallarının üzerine uygulanan kanonik v2.3 delta sözleşmesidir. Burada değiştirilmeyen bütün hükümler v2.2'den aynen miras alınır.

## 1. Değişmeyen çekirdek

- 6-15 oyuncu + 1 Moderatör.
- Kaptan kalıcı roldür ve kaldırılmaz.
- Geminin ilk rotasını Kaptan tek başına ve olay bilgisi olmadan seçer.
- Kaptanın rota oyu 2, diğer resmî oyları 1'dir; rota beraberliğini Kaptan berabere yasal rotalar arasından çözer.
- Mevcut İsyan ve Kaptanın görev dışı kaldığı durumlarda yeni Kaptan seçimi hükümleri korunur.
- Kaptan gece ayrıca uyanmaz; makamı otomatik Yakın/Uzak Ufuk bilgisi vermez.
- Gemi bütün Harita boylarında 2 Gövdeyle başlar.
- Gemi Haritanın alt kenarının dışında herhangi bir sütun hizasında başlayabilir.
- Harita kategorileri 30 Açık Deniz + 12 Kayalık + 6 Ada + 4 Deniz Feneri = **52 Harita kartı** olarak kalır.
- Toplam fiziksel kart kimliği **118** olarak kalır.

## 2. v2.3 değişikliği: Geçilmez Kayalık artık Harita kartıdır

v2.2'de kullanılan ayrı görünür Geçilmez Kayalık işaret/token sistemi v2.3'te kaldırılır.

İki mevcut Kayalık kartı Geçilmez Kayalığa dönüştürülür:

| Kimlik | v2.2 | v2.3 |
|---|---|---|
| `HAR-KY-01` | Ufak Kayalık - hasar yok | **Duvar Gibi Kayalık - Geçilmez Kayalık** |
| `HAR-KY-03` | ikinci Batık Kalyon kopyası | **Yolun Bittiği Yer - Geçilmez Kayalık** |

`HAR-KY-02` tek Batık Kalyon olarak kalır. Böylece 5 doğrudan Gövde hasarı veren Kayalık kartının tamamı ve bütün benzersiz Kayalık mekanikleri korunur.

Kayalık kategorisi yine **12 kart**, Harita havuzu yine **52 karttır**. Geçilmez Kayalıklar 53. veya 54. kart değildir.

## 3. Ayırt edilemez kategori yüzü

- İki Geçilmez Kayalığın kapalı/kategori yüzünde yalnız normal **KAYALIK** kategorisi görünür.
- Diğer Kayalık kartlarından farklı sembol, renk, çerçeve, ikon, yazı veya token kullanılamaz.
- Kategori yüzü diğer Kayalıklarla aynı baskı tasarımına tabidir.
- Oyuncular kart açılmadan yalnız Kayalık olduğunu bilir; Geçilmez olduğunu kart yüzünden anlayamaz.

## 4. Diğer Harita kartlarıyla aynı kurallar

Kapalı Geçilmez Kayalık bütün normal Harita kartı hükümlerine tabidir:

- normal Yakın/Uzak Ufuk hedefi olabilir;
- rota oylamasında seçilebilir;
- normal Harita bakma/bilgi yetenekleriyle gizlice görülebilir;
- Pusula ve diğer geçerli bilgi etkileriyle incelenebilir;
- geçerli kart yer değiştirme/değiştirme etkilerinden etkilenebilir;
- olay yüzünü gören oyuncu bilgiyi doğru söyleyebilir, yalan söyleyebilir veya saklayabilir;
- gizli bilgi, diğer Harita bilgileriyle aynı sosyal çıkarım kurallarına tabidir.

Gizli Geçilmez Kayalık rota hesabında önceden bilinen fiziksel engel sayılmaz. Oyuncular açısından normal kapalı Kayalık kartıdır.

## 5. Kurulum kotası

Harita boyuna göre normal Kayalık kotasının **içinde** şu kadar Geçilmez Kayalık bulunur:

| Harita | Geçilmez Kayalık |
|---|---:|
| 5x5 | 1 |
| 5x6 | 1 |
| 6x5 | 1 |
| 5x7 | 2 |
| 6x6 | 2 |
| 6x7 | 2 |

Küçük Haritada kullanılmayan ikinci Geçilmez Kayalık, diğer kullanılmayan Harita kartlarıyla birlikte havuz dışında kalır.

## 6. Kurulum güvenliği ve gizlilik

- Geçilmez Kayalık son Liman/Ufuk hattına yerleştirilemez.
- Moderatör gerçek olay yüzlerini bildiği için, seçilen başlangıçtan en az bir erişilebilir Ada üzerinden seçilmiş Limana normal ileri hareketlerle ulaşan en az bir **gerçek yol** kaldığını kurulumda doğrular.
- Bu doğrulama Geçilmez Kayalık konumlarını oyunculara açıklamaz.
- İlk gün Sis yasağı, normal kapalı Harita kuralına göre uygulanır; Geçilmez Kayalık kapalıyken özel görünür hedef sayılmaz.

## 7. Geçilmez kart rota ile açılırsa

Bir normal rota seçimi Geçilmez Kayalık kartına yönelirse:

1. Kart normal Harita kartı gibi açılır.
2. **Gemi o kareye girmez.**
3. Gemi hareketten önce bulunduğu konumda kalır.
4. Normal rota gününün hareketi/günü harcanmış sayılır.
5. Geçilmez Kayalık kartı açık kalır ve konumu kamusal bilgi olur.
6. Bu kare bundan sonra normal rota veya Yakın/Uzak Ufuk hedefi değildir.
7. Günün kalan normal akışı ve gece, başka bir kural engellemiyorsa devam eder.

İlk rotada bu olursa Gemi Harita dışındaki başlangıç konumunda kalır; gün harcanır ve ertesi normal gün kalan yasal rotalardan seçim yapılır.

## 8. Olay içi/ek hareket Geçilmez kartı açarsa

Girdap veya başka bir zorunlu/isteğe bağlı olay içi ek hareket kapalı Geçilmez Kayalığa yönelirse:

- kart açılır;
- Gemi bulunduğu karede kalır;
- o ek hareket sona erer/boşa düşer;
- kart açık kamusal engel olur;
- aynı olay çözümü içinde acil geri dönüş başlamaz.

## 9. Acil geri dönüş

Normal geri hareket hâlâ yasaktır. Acil geri dönüş yalnız şu durumda açılır:

1. normal rota gününde bütün normal yasallık/kısıt çözümleri sonunda hiç ileri rota kalmaz;
2. bu çıkmazı oluşturan engeller **açılmış/bilinen Geçilmez Kayalık kartlarıdır**;
3. bu açık Geçilmezler geçici olarak yok sayıldığında en az bir ileri rota yeniden doğar.

Bu durumda Gemi daha önce bulunduğu bir önceki kareye geri çekilir. Geri dönüş bir tam hareket/gün tüketir; dönülen çözülmüş olay tekrar çalışmaz. Çıkmaz sürerse sonraki normal günde koşullar yeniden kontrol edilir.

**Kapalı/gizli Geçilmez Kayalık**, acil geri dönüş nedensellik hesabında bilinen engel sayılmaz.

## 10. Kart metinleri

### HAR-KY-01 - Duvar Gibi Kayalık

**Aile:** Geçilmez Kayalık  
**Etki:** Gemi bu kareye giremez. Kart rota veya olay içi hareketle açılırsa Gemi önceki konumunda kalır; kart açık kalır. Normal rota günü ise hareket harcanır.  
**Lezzet:** Haritada çizgi değildi. Duvarmış.

### HAR-KY-03 - Yolun Bittiği Yer

**Aile:** Geçilmez Kayalık  
**Etki:** Gemi bu kareye giremez. Kart rota veya olay içi hareketle açılırsa Gemi önceki konumunda kalır; kart açık kalır. Normal rota günü ise hareket harcanır.  
**Lezzet:** Kestirme diye bakıldı. Dönüş yolu diye hatırlandı.

## 11. Teknik durum

- Kanonik v2.3 kart karması SHA-256: `3f8c5a0f311d569f12730e032d66a189f5e14e562483a0a89853458f8a2160ab`.
- Kart çifti karşılaştırması: 7.200 oyun.
- Seçilen çift davranış testi: 6.000 oyun.
- 6-15 oyuncu/süre duyarlılığı: 9.000 oyun.
- Kalıcı rota kilidi: 0; kurulum hatası: 0.
- Kesin geometri: 51.204 teorik / 51.102 yasal / 102 kurulumda reddedilecek.
- Kart PDF: 32 sayfa; Kural Kitabı: 32 sayfa; görsel preflight PASS.

Bu sonuçlar insan blöfü, güveni ve eğlenceyi kanıtlamaz. v2.3 stabil release kilidi için insan masa testi ayrıca değerlendirilmelidir.
