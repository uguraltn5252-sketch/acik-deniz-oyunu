# OYUN — Değişiklik Kaydı v2.3

**Temel:** stabil v2.2  
**Tarih:** 18 Ağustos 2026  
**Durum:** geliştirme / yeniden test gerekli

## v2.3'ün ilk değişikliği: Geçilmez Kayalık artık ayrı işaret değil

v2.2'de kullanılan ayrı, baştan görünür Geçilmez Kayalık işaretleri kaldırılır.

### Kilitlenen fiziksel kural

- Harita havuzu **52 kart olarak kalır**; 53. veya 54. Harita kartı eklenmez.
- Mevcut 12 Kayalık kartının **2 fiziksel kartı Geçilmez Kayalık olayına dönüştürülür**.
- Böylece kategori dağılımı değişmez: **30 Açık Deniz + 12 Kayalık + 6 Ada + 4 Deniz Feneri = 52**.
- Geçilmez Kayalık kartları kapalıyken diğer Kayalık kartlarından **hiçbir biçimde ayırt edilemez**.
- Kategori yüzü/arka yüz/ölçü/yerleşim davranışı normal Kayalıkla aynıdır. Ayrı sembol, token, işaret veya önceden görünen `GEÇİLMEZ` ibaresi yoktur.
- Geçilmez Kayalıklar diğer bütün Harita kartı kurallarına tabidir: karıştırma, kurulum, kapalı olay yüzü, Yakın/Uzak Ufuk bilgisi, gizlice bakma, bilgi paylaşma ve blöf/yalan kuralları aynen uygulanır.
- `Geçilmez Kayalık` bilgisi yalnız olay yüzünü görmeye yetkili oyuncu tarafından öğrenilebilir veya rota seçimi sonucunda kart çözülürken kamusal hâle gelir.

### Kullanım sayısı

Fiziksel havuzda toplam 2 Geçilmez Kayalık vardır. Kurulum, seçilen harita için kullanılan Kayalık kartlarını seçerken:

- `5×5`, `5×6`, `6×5`: kullanılan Kayalıkların içinde **tam 1** Geçilmez Kayalık bulunur.
- `5×7`, `6×6`, `6×7`: kullanılan Kayalıkların içinde **tam 2** Geçilmez Kayalık bulunur.

Küçük haritalarda ikinci Geçilmez Kayalık diğer kullanılmayan Harita kartlarıyla birlikte oyun dışında kalır.

### Yerleşim kısıtı

Geçilmez Kayalık normal Kayalık gibi gizli yerleştirilir; ancak Moderatör kart kimliğini bildiği için şu güvenlik kısıtını uygular:

- Geçilmez Kayalık **Limanın hemen kıçındaki son Harita/Ufuk hattına konulamaz**.
- Kurulumun başlangıçta matematiksel olarak imkânsız olmaması gerekir.

Bu kısıt oyunculara kartın hangisi olduğunu açıklamaz.

## Açılma ve hareket semantiği

Geçilmez Kayalık kapalıyken rota açısından normal, henüz çözülmemiş bir Kayalık hedefidir; baştan rota listesinden çıkarılmaz.

Gemi Geçilmez Kayalık rotasını seçtiğinde:

1. Kart normal Harita kartı gibi açılır/çözülür.
2. Gemi **Geçilmez Kayalık karesine girmez**; geldiği mevcut karede kalır.
3. O günün normal hareketi tüketilmiş sayılır.
4. Geçilmez Kayalık açık ve kamusal olarak bilinen kalıcı engel hâline gelir.
5. Bundan sonraki rota ve Ufuk hesaplarında bu açık kare yasal hedef değildir.
6. Başarısız giriş bir Gövde hasarı vermez; kartın etkisi geçilemezliktir.

## Acil geri dönüş

v2.2'deki geri dönüş fikri korunur fakat gizli-kart semantiğine uyarlanır:

- Normalde geri hareket yasaktır.
- **Açılmış/bilinen Geçilmez Kayalıklar** nedeniyle mevcut kareden hiçbir yasal ileri rota kalmamışsa acil geri dönüş açılır.
- Gemi geldiği bir önceki ziyaret edilmiş kareye bir adım geri çekilir.
- Geri dönüş o günün hareketini tüketir; dönülen çözülmüş Harita olayı yeniden çalışmaz.
- Çıkmaz sürerse sonraki normal günde bir kare daha geri dönülebilir.
- Başka yasal rota varken bilinen çıkmaz kola tekrar girilemez.

## Kart dönüşümü

İlk tasarım adayı, doğrudan Gövde hasarı kotasını değiştirmemek için iki **hasarsız Kayalık** fiziksel kartının Geçilmez Kayalığa dönüştürülmesidir. Hangi iki mevcut kart kimliğinin dönüştürüleceği, kart kataloğu ve simülasyon birlikte kontrol edilmeden stabil olarak kilitlenmeyecektir.

Bu nedenle v2.3 şu anda kart sayısını ve kategori sayısını kilitler; **nihai iki kart kimliği test sonucunda seçilecektir**.

## v2.2'den aynen korunanlar

- Kaptan kalıcı çekirdek roldür; kaldırılmaz.
- İlk rotayı Kaptan tek başına ve olay yüzlerini bilmeden seçer.
- Başarılı İsyan, Kaptanın ölümü ve mevcut görev yapamama tetiklerinde yeni Kaptan seçilir.
- Kaptan gece ayrıca uyanmaz; makam otomatik Ufuk bilgisi vermez.
- Gemi her harita boyunda **2 Gövde** ile başlar.
- Gemi alt kenarın dışındaki izin verilen başlangıç sütunundan başlar.
- İlk Hain uyanışında saldırı yoktur.

## Eski v2.2 testlerinin durumu

v2.2 Geçilmez Kayalık testi, engelleri baştan görünür ve rota adayı olmayan kareler olarak modellediği için v2.3 için denge kanıtı sayılmaz.

v2.3 stabil olmadan önce en az şu testler yeniden çalıştırılmalıdır:

1. Gizli Geçilmez Kayalığın seçilmesi ve başarısız hareket semantiği.
2. 1 ve 2 Geçilmez Kayalık kullanılan bütün harita boyları.
3. Başarısız girişlerin gün/gece sayısına etkisi.
4. Açılmış engeller sonrası acil geri dönüş ve kalıcı kilit oranı.
5. Hainlerin gizli Ufuk bilgisiyle Geçilmez Kayalık bilgisini saklama/yalan söyleme etkisi.
6. İki dönüştürülen Kayalık kartının hasar kotası ve kart çeşitliliğine etkisi.
7. 52 Harita kartı ve toplam kart kimliği bütünlüğü.
