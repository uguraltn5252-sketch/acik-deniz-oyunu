# FOULWAKE — Modüler Hikâye Omurgası

**Durum:** DRAFT / NOT LOCKED  
**Çalışma hattı:** `v2.7-design` / `working/v2.7/`  
**Amaç:** Mevcut hikâyeyi baştan yazmadan küçük, izlenebilir ve geri alınabilir değişiklikler yapmak.

Bu dosya yeni bir hikâye değildir. FOULWAKE hikâyesinin parçalarını adlandıran, birbirine bağlayan ve yalnız istenen parçanın değiştirilmesini sağlayan çalışma şablonudur. Kilitli `releases/v2.6/` içeriği yerinde değiştirilmez.

## 1. Çalışma kuralı

Her anlatı parçası tek bir kimlik taşır:

| Önek | Parça | Örnek |
|---|---|---|
| `CAN` | Değişmemesi gereken kanon | `CAN-01` |
| `CHR` | Karakter | `CHR-03` |
| `LOC` | Mekân | `LOC-02` |
| `MYS` | Gizem / şüphe hattı | `MYS-01` |
| `EVT` | Olay | `EVT-04` |
| `SCN` | Oynanabilir sahne | `SCN-05` |
| `DIA` | Ses, diyalog veya anlatıcı tavrı | `DIA-02` |
| `BRG` | Mekanik–hikâye bağlantısı | `BRG-03` |
| `END` | Final veya artçı sonuç | `END-01` |

Bir değişiklik istendiğinde bütün metin değil, yalnız hedef kimlik düzenlenir. Bağlı parçalar önce listelenir; kullanıcı istemedikçe onlar değiştirilmez.

## 2. Durum etiketleri

Her kayıt şu etiketlerden yalnız birini taşır:

- **KANON:** Mevcut sürümün doğrulanmış gerçeği.
- **TASLAK:** Üzerinde çalışılabilir öneri.
- **AÇIK SORU:** Bilerek cevaplanmamış alan.
- **DEĞİŞİKLİK ADAYI:** Kanona alınmamış küçük düzeltme.
- **REDDEDİLDİ:** Tekrar önerilmemesi gereken fikir.

`TASLAK`, `AÇIK SORU` veya `DEĞİŞİKLİK ADAYI` etiketi hiçbir zaman kendiliğinden `KANON` olmaz. “Beğendim”, “devam et” veya bir sonraki konuya geçmek kilitleme ya da kanonlaştırma sayılmaz.

## 3. Korunan kanon çiti

Bu bölüm, mevcut kaynaklar denetlenerek doldurulur. Şimdilik doğrulanmış çalışma sınırları:

| Kimlik | Durum | Korunan gerçek |
|---|---|---|
| `CAN-01` | KANON | Dünya ve dil 1721 dönemine bağlıdır; modern teknoloji ve modern nesne dili kullanılmaz. |
| `CAN-02` | KANON | Arden, San Cordelio, Saint Verena ve Veyr mevcut dünyanın özel adlarıdır; keyfî biçimde değiştirilmez. |
| `CAN-03` | KANON | Siyah Mühür açıklanırken kesin suçlu, eksiksiz kanıt zinciri veya bütün gizemi kapatan tek cevap verilmez. |
| `CAN-04` | KANON | Gusto hakkındaki belirsizlik korunur; kaderi veya gerçek rolü kullanıcı kararı olmadan kesinleştirilmez. |
| `CAN-05` | KANON | Ton yaratıcı, kara mizahlı ve şüphecidir; mizah tehlikeyi iptal etmez. |
| `CAN-06` | KANON | Metin “yapay zekâ yazmış” gibi pürüzsüz, genel ve açıklayıcı olmamalıdır; insan ayrıntısı, niyet ve kusur taşır. |
| `CAN-07` | KANON | Hikâye kontrol edildiğinde sıfırdan yeniden yazılmaz; önce mevcut dosyalar okunur, sonra yalnız gerekli küçük değişiklik önerilir. |

Yeni bir bilgi bu çitle çelişirse otomatik uyarlama yapılmaz; çelişki kullanıcıya gösterilir.

## 4. Hikâye omurgası

Kilitli hikâyeden alınacak özetler, her kutuya en fazla 2–4 cümleyle yazılır. Uzun düzyazı bu bölümde tutulmaz.

| Kimlik | İşlev | Mevcut içerik | Bağlı parçalar |
|---|---|---|---|
| `EVT-01` | Açılış dengesi | `[Kilitli hikâyeden aktarılacak]` | — |
| `EVT-02` | Yolculuğu kaçınılmaz kılan olay | `[Kilitli hikâyeden aktarılacak]` | `EVT-01` |
| `EVT-03` | İlk ciddi şüphe | `[Kilitli hikâyeden aktarılacak]` | `MYS-01` |
| `EVT-04` | Ortadaki yön değişimi | `[Kilitli hikâyeden aktarılacak]` | `CHR-*`, `MYS-*` |
| `EVT-05` | Bedeli görünür kılan kriz | `[Kilitli hikâyeden aktarılacak]` | `BRG-*` |
| `EVT-06` | Son karar | `[Kilitli hikâyeden aktarılacak]` | `END-*` |
| `EVT-07` | Cevap yerine iz bırakan artçı | `[Kilitli hikâyeden aktarılacak]` | `MYS-*` |

## 5. Karakter kayıt şablonu

Her karakter için aşağıdaki blok kopyalanır:

### `CHR-__` — Karakter adı

- **Durum:** TASLAK
- **Masada görünen yüzü:**
- **Asıl istediği:**
- **Kaybetmekten korktuğu:**
- **Sakladığı şey:**
- **Kendisinin bile yanlış bildiği şey:**
- **Baskı altındaki davranışı:**
- **Komik kusuru:**
- **Şüphe uyandıran ama suç kanıtlamayan ayrıntı:**
- **Konuşma ritmi / kelime alışkanlığı:**
- **İlişkili kimlikler:**
- **Değişirse etkilenecek parçalar:**

Karakter yalnız “iyi”, “kötü”, “kurnaz” gibi sıfatlarla tanımlanmaz. En az bir somut alışkanlığı, bir çelişkisi ve bir bedeli olmalıdır.

## 6. Mekân kayıt şablonu

### `LOC-__` — Mekân adı

- **Durum:** TASLAK
- **İlk bakışta:**
- **Yakından fark edilen:**
- **İnsanların burada yalan söyleme sebebi:**
- **Döneme ait somut ayrıntı:**
- **Tehlike:**
- **Kara mizah kaynağı:**
- **Burada açılabilecek bilgi:**
- **Burada asla kesinleşmemesi gereken bilgi:**
- **İlişkili kimlikler:**

## 7. Gizem ve şüphe kayıt şablonu

### `MYS-__` — Gizemin kısa adı

- **Durum:** AÇIK SORU
- **Oyuncuların ilk duyduğu iddia:**
- **Doğrulanabilen parça:**
- **Çelişen tanıklık:**
- **Yanlış ama makul açıklama:**
- **Doğru olabilecek ikinci açıklama:**
- **Bu sırrı taşımanın bedeli:**
- **Kesinlikle açıklanmayacak sınır:**
- **İlişkili kimlikler:**

İyi şüphe yalnız bilgi saklamaz. Aynı kanıtı en az iki farklı biçimde açıklayabilir ve her açıklamanın bir bedeli olur.

## 8. Oynanabilir sahne şablonu

### `SCN-__` — Sahne adı

- **Durum:** TASLAK
- **Sahnenin başladığı somut görüntü:**
- **Oyuncuların amacı:**
- **Karşı baskı:**
- **Gizli gündem:**
- **Mekanik tetikleyici:**
- **Ortaya çıkabilecek bilgi:**
- **Yanlış anlaşılabilecek bilgi:**
- **Mizah vuruşu:**
- **Seçimin bedeli:**
- **Sahne nasıl kapanır:**
- **Bağlı kimlikler:**

Sahne, yalnız lore anlatmak için kurulmaz. En az bir karar, risk veya oyuncular arası sürtüşme üretmelidir.

## 9. Mekanik–hikâye köprüleri

| Kimlik | Mekanik | Dünyadaki anlamı | Oyuncuya hissettirmesi gereken | Açıklama sınırı |
|---|---|---|---|---|
| `BRG-01` | Kaptan seçimi ve yetkisi | `[Doldurulacak]` | Güvenin geçici oluşu | Kural metnini diyalog içinde tekrar etme |
| `BRG-02` | Gizli Sadakat | `[Doldurulacak]` | Yakının bile bütünüyle bilinememesi | Haini erken kesinleştirme |
| `BRG-03` | Ufuk / gizli Harita bilgisi | `[Doldurulacak]` | Bilginin güç ve yük olması | Haritayı doğaüstü kehanete dönüştürme |
| `BRG-04` | Rota oylaması | `[Doldurulacak]` | Ortak kararın ortak suç üretmesi | Oyuncu seçimini geçersizleştirme |
| `BRG-05` | İskorbüt ve erzak baskısı | `[Doldurulacak]` | Bedenin siyaseti bozması | Acıyı yalnız şakaya çevirme |
| `BRG-06` | İsyan / makam değişimi | `[Doldurulacak]` | Düzen ile meşruiyet arasındaki çatlak | Sonucu hikâyeyle geri alma |

## 10. Ses ve insan eli denetimi

Her yeni metin şu kontrolden geçer:

- Anlatılan şey yerine görülebilen veya duyulabilen en az bir ayrıntı var mı?
- Her karakter aynı düzgün cümlelerle mi konuşuyor? Öyleyse sesler ayrıştırılır.
- Mizah bir davranıştan, korkudan veya çıkar çatışmasından mı doğuyor?
- Şüphe yalnız “gizemli bakış” gibi boş işaretlere mi dayanıyor? Öyleyse somut çelişki eklenir.
- Metin oyuncunun anlayacağı şeyi gereksiz yere tekrar açıklıyor mu?
- Üçlü sıfat dizileri, genel destansı sözler, yapay aforizmalar ve sürekli espri kaldırılır.
- Bir cümle fazla düzgünse, karakterin niyeti veya ortamın somut pürüzü geri getirilir.

## 11. Küçük değişiklik fişi

Her düzenleme önce aşağıdaki fişle tanımlanır:

| Alan | İçerik |
|---|---|
| Değişiklik kimliği | `CHG-YYYYMMDD-__` |
| Hedef kimlik | `CHR-__`, `EVT-__` vb. |
| Mevcut ifade | Değişecek cümlenin kısa özeti |
| Önerilen yeni ifade | Yalnız yeni parça |
| Gerekçe | Ton, tutarlılık, mekanik uyum veya açıklık |
| Doğrudan etki | Etkilenen kimlikler |
| Korunan parçalar | Özellikle değiştirilmeyecek kimlikler |
| Kanon çiti kontrolü | PASS / ÇELİŞKİ |
| Kullanıcı kararı | BEKLİYOR / KABUL / RED |

Bir değişiklik kabul edilirse yalnız hedef parça ve zorunlu doğrudan bağlar güncellenir. “Daha güzel olsun” gerekçesi tek başına bütün bölümü yeniden yazma izni değildir.

## 12. Değişiklik günlüğü

| Değişiklik | Tarih | Hedef | Sonuç | Not |
|---|---|---|---|---|
| `CHG-20260820-01` | 20 Ağustos 2026 | Şablon altyapısı | TASLAK | Modüler düzen kuruldu; mevcut hikâye yeniden yazılmadı. |

## 13. Bu dosyayla çalışma komutu

Kullanıcı “hikâyeyi kontrol et” dediğinde:

1. Önce `AI_HANDOFF.md`, `PROJECT_STATE.md` ve bu dosya okunur.
2. Kilitli v2.6 hikâyesi kaynak olarak kontrol edilir.
3. Sorunlar ilgili kimliklerle gösterilir.
4. Yalnız gerekli küçük değişiklik fişleri hazırlanır.
5. Kullanıcı kabul etmeden kanon, kilit veya release durumu değiştirilmez.

