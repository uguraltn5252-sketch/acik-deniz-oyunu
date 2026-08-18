# v2.1 Sonrası Karşılaştırma

Tarih: 2026-08-18

Amaç: Kilitli/stabil v2.1 kaynaklarını, v2.1 sonrasında alınan yeni kararlarla karşılaştırmak. Bu belge `develop` için geçiş planıdır; `releases/v2.1/` yerinde değiştirilmez.

## Durum etiketleri

- **TAŞINACAK**: açık kullanıcı kararı var; yeni geliştirme hattına uygulanacak.
- **KORU / OMURGA**: kaldırılmayacak veya değiştirilmeyecek çekirdek kural.
- **TEST GEREKİYOR**: karar yönü belli; uygulama ayrıntısı regresyon testine bağlanmalı.

---

## 1. Gemi başlangıç konumu — TAŞINACAK

### v2.1

Gemi Haritanın alt kenarının dışında ancak sabit merkez/sağ-orta sütunda başlar.

### Yeni karar

Gemi Haritanın alt kenarının dışındaki **herhangi bir hizada** başlayabilir. Sabit merkez başlangıcı kaldırılır.

Başlangıç sütunu seçildikten sonra ilk Yakın Ufuk, ilk Sis yasağı ve Limana erişilebilirlik o başlangıca göre dinamik hesaplanır.

---

## 2. Kaptan — KORU / OMURGA

Kaptan rolü **asla kaldırılmayacak**.

Kesin hükümler:

- Kaptan oyunun kalıcı çekirdek rolüdür.
- Oyun başında Kaptan açık oylamayla seçilir.
- **Geminin ilk rotasını Kaptan tek başına seçer.** İlk rota olay bilgisi olmadan kör seçimdir.
- Sonraki rota oylamalarında Kaptanın rota oyu 2'dir.
- Rota beraberliğini Kaptan yalnız berabere seçenekler arasından bozar.
- İsyan sistemi Kaptana bağlı kalır.
- Kaptan ölür/Kamaraya girer/mahsur kalır/Kayıkçı seferine giderse yeni Kaptan seçilir.
- Kaptan gece ayrıca uyanmaz.
- Kaptan makamı otomatik Yakın/Uzak Ufuk bilgisi vermez.

Bu maddeler yeni sürümlerde "Kaptanı kaldır" şeklinde yorumlanamaz.

---

## 3. Geçilmez Kayalık — TAŞINACAK

Geçilmez Kayalık fiziksel olarak girilemeyen özel Harita engelidir. Her oyunda bulunur; sayısı Harita büyüklüğüne göre 1 veya 2 olur.

### Adet kuralı

Mevcut Harita boyları için temiz eşik:

| Harita | Geçilmez Kayalık |
|---|---:|
| 5×5 | 1 |
| 5×6 | 1 |
| 6×5 | 1 |
| 5×7 | 2 |
| 6×6 | 2 |
| 6×7 | 2 |

Genel ifade: **30 veya daha az Harita karesi = 1; 35 veya daha fazla Harita karesi = 2.**

### Yerleşim kuralı

**Geçilmez Kayalık, Limanın hemen kıçındaki son Harita/Ufuk hattına konulamaz.** Limana son yaklaşımı oluşturan hat Geçilmez Kayalık içermez.

Ayrıca kurulum sonunda:

- ilk rotada en az bir yasal ileri seçenek bulunmalıdır;
- Geçilmez Kayalıklar Haritayı başlangıçtan itibaren matematiksel olarak tamamen çözümsüz hâle getirmemelidir.

Bu iki kontrol, acil geri hareket kuralının "imkânsız kurulumu tamir eden" bir araç değil, oyunda oluşan gerçek bir çıkmazdan geri dönme mekanizması olarak kalmasını sağlar.

### Acil geri hareket — tek istisna

Normal kural değişmez: **Gemi geri gidemez ve bekleyemez.**

Tek istisna:

> Rota seçimi anında hiçbir yasal ileri rota kalmamışsa ve bu çıkmazın nedeni Geçilmez Kayalık ise Gemi geri hareket edebilir.

Uygulama tanımı:

1. Önce normal ileri rota yasallığı hesaplanır.
2. En az bir yasal ileri rota varsa geri hareket **yasaktır**.
3. Hiç ileri rota yoksa, Geçilmez Kayalık(lar) yok sayıldığında ileri rota yeniden doğuyorsa çıkmazın nedeni Geçilmez Kayalık sayılır.
4. Yalnız bu durumda Gemi **bir önceki bulunduğu kareye bir adım geri döner**.
5. Geri dönülen kart daha önce çözülmüşse olayı yeniden çalışmaz.
6. Bu geri hareket o günün normal hareketini tüketir; bedelsiz bir "undo" değildir.
7. Sonraki turda normal ileri rota seçimi yeniden yapılır.
8. Gerekirse, aynı şartlar tekrar oluşursa daha eski bir kareye bir sonraki turda bir kez daha geri dönülebilir.

Bu istisna başka rota kısıtları, oyuncu kararı, Güç kartı veya geçici etkiler yüzünden oluşan çıkmazlara otomatik olarak uygulanmaz. Tetik için Geçilmez Kayalığın nedensel olması gerekir.

### Neden bu biçim?

Geçilmez Kayalık artık yalnız kurulum süsü değil, gerçek bir rota baskısıdır. Oyuncular yanlış koridora girerse sefer bir veya daha fazla gün uzayabilir; fakat oyun sırf engel yüzünden sonsuza kadar kilitlenmez. Geri dönüşün bir tam hareket tüketmesi, engelin bedelini korur.

---

## 4. Başlangıç Gövdesi — KORU / OMURGA

**Gemi bütün Harita boylarında 2 Gövdeyle başlar.**

- 2 = sağlam
- 1 = su alıyor
- 0 = battı

Harita boyuna göre 3 Gövdeye çıkma fikri reddedildi. Önceki denemelerde 3 Gövde Hainin gemiyi batırma yolunu gereğinden fazla zayıflatıyordu. Kullanıcı kararıyla Gövde tekrar kesin biçimde **2** olarak kilitlendi.

Tersane Koyu gibi başlangıç Gövdesine kadar onarım yapan etkilerin tavanı da 2 olarak kalır.

---

## 5. Hain sayısı — KORU

| Oyuncu | Hain | Tayfa |
|---:|---:|---:|
| 6 | 1 | 5 |
| 7 | 2 | 5 |
| 8 | 3 | 5 |
| 9 | 3 | 6 |
| 10 | 3 | 7 |
| 11 | 4 | 7 |
| 12 | 4 | 8 |
| 13 | 4 | 9 |
| 14 | 5 | 9 |
| 15 | 5 | 10 |

---

## 6. İlk Hain uyanışı ve Sis — KORU

İlk Hain uyanışında Hainler birbirini tanır ve takım olarak bir Yakın Ufka bakar; saldırı yapamazlar. Sis ilk uyanıştaki saldırı yasağını kaldırmaz.

---

## 7. Ufuk geometrisi — KISMEN DEĞİŞECEK

Genel Yakın/Uzak Ufuk tanımı korunur. Yalnız ilk Ufuk artık sabit sütunlara bağlı değildir; geminin seçilen alt-kenar başlangıcına göre dinamik türetilir.

Geçilmez Kayalık bir Ufuk karesindeyse o kare yasal rota/Ufuk hedefi değildir. Acil geri hareket yalnız ileri yasal rota sayısı sıfıra düştüğünde ayrıca değerlendirilir.

---

# Son durum

Doğrudan yeni sürüme taşınacak kararlar:

1. Gemi alt kenarın dışında herhangi bir hizada başlayabilir.
2. İlk rotayı Kaptan tek başına seçer.
3. Kaptan rolü kalıcı omurgadır ve asla kaldırılmaz.
4. Gemi bütün Haritalarda 2 Gövdeyle başlar.
5. Her oyunda Harita büyüklüğüne göre 1 veya 2 Geçilmez Kayalık bulunur.
6. Geçilmez Kayalık Limanın hemen kıçındaki son Ufuk/Harita hattına konulamaz.
7. Normalde geri hareket kesin yasaktır; yalnız Geçilmez Kayalık bütün ileri rotaları kapattığında Gemi önceki karesine bir adım geri dönebilir.
8. Geri hareket bir tam hareket/gün maliyetidir ve çözülmüş olayı tekrar tetiklemez.

## Regresyon/test hedefleri

- Her Harita boyunda doğru 1/2 Geçilmez Kayalık adedi.
- Son Liman yaklaşım hattında Geçilmez Kayalık üretilememesi.
- İlk rota kilidinin kurulumda engellenmesi.
- En az bir ileri rota varken geri hareketin kesinlikle yasak olması.
- Sıfır ileri rota + Geçilmez Kayalık nedenselliğinde geri hareketin açılması.
- Geri dönülen açık kart olayının ikinci kez çözülmemesi.
- İki Geçilmez Kayalık bulunan büyük Haritalarda tekrar geri dönüşün sonlu ve izlenebilir kalması.
