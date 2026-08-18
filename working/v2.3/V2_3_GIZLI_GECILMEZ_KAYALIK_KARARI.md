# v2.3 — Gizli Geçilmez Kayalık çekirdek kararı

Tarih: 2026-08-18
Durum: v2.3 geliştirme kararı; v2.2 stabil sürüme dokunmaz.

## Kesin karar

Geçilmez Kayalık artık ayrı işaret/token değildir. 52 Harita kartının içindeki 12 Kayalık kartından **iki fiziksel kart Geçilmez Kayalık** olur. Toplam Harita kartı sayısı **52 olarak kalır**; 53/54 olmaz.

Bu iki kart kapalıyken normal Kayalık kartlarından **hiçbir biçimde ayırt edilemez**:

- aynı KAYALIK kategori yüzü,
- aynı arka yüz ve baskı dili,
- kapalı/kategori yüzünde ek sembol, renk, yazı, çerçeve veya token yok,
- bütün normal Harita kartı kuralları, bilgi kuralları ve Ufuk kuralları geçerlidir.

Oyuncular yalnız Kayalık kategorisini görür; olay yüzünün Geçilmez Kayalık olduğunu ancak normal oyun kurallarıyla olay yüzü öğrenildiğinde bilir. Bir oyuncu gizli bilgiyle bunu öğrenmişse doğruyu söylemek, susmak veya yalan söylemek bakımından diğer Harita bilgileriyle aynı sosyal çıkarım kurallarına tabidir.

## Kart havuzu

Mevcut 12 Kayalık kartından iki **hasarsız** kart Geçilmez Kayalığa dönüştürülür. Böylece mevcut 5 doğrudan Kayalık Gövde hasarı korunur. İlk aday dönüşüm:

- Ufak Kayalık ×1 -> Geçilmez Kayalık ×1
- Batık Kalyon ×2 içinden bir kopya -> Geçilmez Kayalık ×1

Sonuç yine 12 Kayalık ve toplam 52 Harita kartıdır. Kart kimliği kataloğu yeni kimlik eklenmeden mevcut iki kimliğin olay içeriği değiştirilerek güncellenecektir.

## Harita boyuna göre kullanım

- 5×5, 5×6, 6×5: kurulumda iki Geçilmez Kayalık kartından **tam 1** tanesi kullanılan Harita kartları arasına girer.
- 5×7, 6×6, 6×7: **iki Geçilmez Kayalık kartının ikisi de** kullanılan Harita kartları arasına girer.

Bunlar normal Kayalık kotasının içindedir; Kayalık kotasına eklenmez.

## Kurulum kısıtları

Geçilmez Kayalık olay yüzünü Moderatör kurulum sırasında bilir ve gizli tutar. Kartlar diğer Harita kartları gibi yerleştirilir ancak:

1. Geçilmez Kayalık Limanın hemen kıçındaki son Harita/Ufuk hattına konulamaz.
2. Kurulum baştan matematiksel olarak çözümsüz olamaz.
3. İlk rota tamamen kapatılamaz.
4. İskorbüt/ada erişimi gibi mevcut zorunlu erişilebilirlik koşulları korunur.
5. Bu kısıtlar oyunculara kartın kimliğini açıklamaz.

## Keşif ve hareket semantiği

Geçilmez Kayalık baştan görünür engel değildir. Bu nedenle v2.2'deki `impassable_rock_is_never_route_or_horizon_target` hükmü v2.3 için geçersizdir.

- Kimliği henüz bilinmeyen kapalı bir Kayalık normal bir yasal rota/Ufuk hedefi olabilir.
- Rota o kareye seçildiğinde olay yüzü normal şekilde açılır.
- Olay **Geçilmez Kayalık** ise Gemi karta girmez; geldiği karede kalır.
- Başarısız giriş o günün normal hareketini tüketir; ardından normal gece akışı uygulanır.
- Geçilmez Kayalık açıldıktan sonra konumu kamusal olarak bilinen geçilemez bir kare olur ve artık yasal rota/Ufuk hedefi değildir.
- Geçilmez Kayalık olayı Gövde hasarı vermez; asıl bedeli rota kaybı/zaman/gece baskısıdır.

## Acil geri dönüş

Normalde geri hareket hâlâ yasaktır. Ancak **açılmış/bilinen Geçilmez Kayalıklar** nedeniyle bütün ileri yollar gerçekten kapanmışsa v2.2'de kararlaştırılan acil geri dönüş ilkesi korunur:

- yalnız Kayalık kaynaklı tam çıkmazda,
- geldiği bir önceki ziyaret edilmiş kareye,
- bir normal hareket/gün harcayarak,
- geri dönülen çözülmüş olay tekrar çalışmadan,
- çıkmaz sürerse sonraki normal günde yeniden uygulanabilir.

Gizli ve henüz keşfedilmemiş bir Geçilmez Kayalık sırf Moderatör onun kimliğini bildiği için oyuncuların yasal rotasını önceden engellemez.

## Kaptan ve diğer v2.2 hükümleri

Değişmez:

- Kaptan rolü kalıcıdır.
- İlk rotayı Kaptan tek başına ve olay yüzlerini bilmeden seçer.
- Başarılı İsyan, ölüm veya mevcut görev-yapamaz durumlarında yeni Kaptan seçilir.
- Kaptan gece ayrıca uyanmaz ve makamı otomatik Ufuk bilgisi vermez.
- Gemi her harita boyunda 2 Gövdedir.

## Eski v2.2 testinin statüsü

v2.2 Geçilmez Kayalık testi engelleri baştan görünür/rota dışı kabul ettiği için **v2.3 denge kanıtı olarak kullanılamaz**. Yalnız eski sistem için tarihsel kanıttır.

v2.3 için yeniden test zorunludur. Test motoru özellikle şunları ölçmelidir:

1. Geçilmez Kayalığın rota seçildikten sonra açılması ve başarısız giriş günü.
2. Eklenen gece sayısı.
3. Açılmış Kayalık sonrası acil geri dönüş oranı.
4. Kalıcı rota kilidi ve kurulum kilidi.
5. Tayfa/Hain kazanma oranı değişimi.
6. Gizli Ufuk bilgisi üzerinden Hain/Tayfa bilgi avantajı.
7. 1 Kayalık ve 2 Kayalık kullanılan haritaların ayrı sonuçları.

Bu testler tamamlanmadan v2.3 stabil ilan edilmez.