> **Tarihsel ilk teslim kaydı:** Aşağıdaki 20 test, 125 alan ve A/B sayıları `d96967c0b87490982ebc6bec9363c3d1c2b1646e` teslimini anlatır. Güncel dosyalar ikinci kontrolde yenilendi: 27 test, 127 alan değişikliği, yeni 3.600 yolculuk ve görsel/PDF üretimi için [güncel raporu](../recheck_visual/recheck_report.md) kullanın. Eski görsel kapsam dışı ifadesi güncel görevin yetkisi değildir.

# FOULWAKE - uygulanmış editoryal revizyon ve teknik kanıt

**7 Eylül 2026 · FOULWAKE-EDITORIAL-OVERHAUL-001 · SAME_OPERATOR_SELF_CHECK**

Hikâye, 121 kartın metin kaynağı ve tam kural kitabı düzenlendi. Bu, önceki incelemeye verilmiş yeni bir öneri listesi değildir; değişiklikler çalışma dosyalarındadır. Başeditörün geçici Story/Simulation yetkisi kullanıldı. Görsel ve sanat üretimi yapılmadı.

## Uygulanan sonuç

- Siyah Mühür yerine Kuru Pay: kıyıda kalan çıkar sahiplerinin kazancı üzerinden doğan lakap. Tek örgüt, ortak emir veya Gusto'nun faili kesinleşmez.
- Heyetin kişisel sorumluluğu ilk paragrafta; karantina ve ücret baskısı Kaptan seçimine bağlanır. İlk tarafsız gece kurulum aşaması olarak açıklanır.
- Beş Hain ve on Tayfa için özel, mekanik olmayan gerekçeler; daha ayrışan karakter sesleri ve dönem içinden kara komedi.
- One Piece, Karayip Korsanları, Prens ve Moby-Dick için birer kısa nesne/durum çağrışımı. Kaynaklar araştırma notunda; replik veya olay örgüsü aktarılmadı.
- KAR-01/02 gece istisnası, KAPTAN'ın rota ve diğer oylar arasındaki farkı, §5.3 anlatıcı kesinliği ve GUC-25 yazımı giderildi. Şüpheli Martı'nın artık uygun olmayan hedefte tüketilmesi ED-13 ile ayrıca karara bağlandı.
- Tam kural kitabı anlatıyı, kurulumu, olayları ve bütün karakter/Güç referanslarını birleştirir. Okunabilir 121 kart dökümü aynı kaynaklardan üretilir.

## Kaynak kapsamı

20 Karakter, 30 Güç ve 1 KAPTAN önceki 51 kayıttır. 15 Sadakat, 1 Erzak, 52 Harita ve 2 Liman ile kalan 70 metin kaydı tamamlandı. `source_inventory.json` eski kayıtları, paket/PDF hashlerini ve 70 kaydın PDF sayfasını içerir. Kart PDF'sinin 27. sayfasındaki önler rasterdir; 29/31. sayfalarda sonradan eklenen olay yazıları normal çıkarım sırasının dışındadır. Bu 11 kart görsel olarak okunarak karşılaştırıldı. Güncel yardımcı kart kaynağı s.33'tür; s.31'deki eski Kalkış çizimi ek bir kimlik sayılmadı.

121 kimlik, manifestin kimlik kümesiyle aynıdır. Etki değerleri, zaman penceresi alanları, skorlar, hasar işaretleri, olay aileleri, adetler ve SRC-002 kimlik eşlemesi değişmez. `copy_changes.json` **125 alan değişikliğini** eski/yeni biçiminde gösterir; metnin dosyaya yeni alınması ile oyuna yeni kart eklenmesi karıştırılmaz.

Üç karşılaştırılabilir OKU bloğu 149/143/94 sözcükten 85/99/52 sözcüğe indi: **386 → 236**. Bu, bütün kurulum anlatısının uzunluğu veya insanların sıkılmadığının kanıtı değildir. Yeni açıklık köprüleri diğer oyun anlarına yerleştirildi; §17 isteğe bağlıdır.

## Simülasyonda düzeltilen somut kusurlar

Doğrulanmış kilitli paketin 44 manifest üyesi hash kontrolünden geçirilir; kaynak motor geçici alanda yüklenir. Kilitli dosyalar değiştirilmez. Yeni `observation_engine.py` katmanı şunları düzeltir:

1. Bilgisiz Hainin blöf hedefi, kapalı olayın gerçek değerinden seçilmez. Ortak Deniz/Kayalık arkasında bakış tercihi, rota tahmini ve ek hareket tercihi yalnız ortak kategori bilgisine dayanır. Bilinen ön yüz bilgisi korunur.
2. İlk rota öncesinde bilgi kartı ve Islak Harita kullanılmaz; ilk yolculuk gecesinde uygun Karakterler çalışır, Sis olsa da saldırı yoktur. Kamaradaki Hain takım bakışını almaz.
3. Bazı Güç hedeflerinde gizli Sadakat yerine oyuncunun kamusal şüphesi veya gecede gerçekten tanıdığı takım kullanılır. Şüphe güncellemesinde Hain olduğu için gizli ayrıcalık uygulanmaz.
4. Rehin Adası artık Güç ödeme pazarlığı değildir; yazılı zorunlu rastgele mahsur bırakma uygulanır. Gümrük Adasında Sadakat Güç sayılmaz. Güç kaybı yalnız Gücü olanları hedefler; iki kazanç iki ayrı alıcıya gider.
5. Uğurlu Altın aynı hedefi yeniden seçebilir. Martı uygunluğu tetikleme anında kontrol edilir. Kayıkçı kurtarması tam vardiya sürer. Limanda yeni siyasi işlem yapılmaz. Açılan Geçilmez ziyaret sayılmaz; olay içi hedefsiz ek hareket acil geri dönüş başlatmaz.

**20 hedefli regresyon geçti.** Kapalı iki ön yüzün yerini değiştirip oyuncuların mevcut bilgilerini sabit tutan test, blöflerin, rota oylarının ve bakış tercihlerinin değişmediğini doğrular. Testler kural kaynaklarına bağlı kritik davranışları kontrol eder; sırf çıktı dosyası var diye PASS üretmez.

## Model yolculukları

6-15 oyuncu × 3 uzunluk × 3 davranış profili × 20 tohum × 2 arka bilgi modeli = **3.600 tamamlanmış yolculuk**, 1.800 eş başlangıç. A eski ayrı kategori, B güncel ortak Deniz/Kayalık arka bilgisidir.

| Model | Tayfa zaferi | Batma | İskorbüt | Bütün Tayfa ölümü | Ortalama gün |
|---|---:|---:|---:|---:|---:|
| A | 1069 / 1800 | 601 | 110 | 20 | 5.60 |
| B | 1045 / 1800 | 623 | 108 | 24 | 5.64 |

Sonuçsuz güvenlik durdurması, rota kilidiyle hükmen kayıp, boş gemi kilidi ve Sadakat atımı görülmedi. Bütün sonuçlar yazılı dört sonuç sınıfından birine ulaştı. Ayrıntılar ham CSV ve oyuncu sayısına göre JSON'dadır.

**Bu oranlar denge kabulü değildir.** Tarihsel motorun konuşma, Kaptan seçimi ve yeniden oylama davranışı yaklaşık kalır. Yeniden oylamada bütün kart ağırlıklarının korunması, bazı karakterlerin (Üç Anahtar/Güvertebaşı) seçim politikaları, Bayat Peksimet'in gerçek konuşmaya etkisi, Güvercin Mektubu, gündüz Kamara/Anahtar Deliği penceresi ve Seyir Zabtı'nın yalnız gerçekleşmiş zarar koşulu tam modellenmez. Bazı anlık tepki seçimleri iyimser gönüllü yardım varsayımı kullanır. A/B başlangıçları eş olsa da karar sonrası rastgele akışlar ayrılır; 24 zaferlik fark arka tasarımın nedensel etkisi diye yorumlanmaz. Bu nedenle Sea/Rock için tam kurallı insan ve fiziksel kontrol kapısı açık kalır; bu teslimden mekanik sayısal denge değişikliği çıkarılmadı.

## Yeniden üretim

Depo kökünden, doğrulanmış v2.6 ZIP yoluyla çalıştırın:

```bash
python working/v2.7/qa/editorial_revision/render_texts.py
python working/v2.7/qa/editorial_revision/verify_content.py
FOULWAKE_SOURCE_ZIP=/path/OYUN_SIMULASYON_PAKETI_v2.6.zip PYTHONDONTWRITEBYTECODE=1 python working/v2.7/qa/editorial_revision/test_rules.py
PYTHONDONTWRITEBYTECODE=1 python working/v2.7/qa/editorial_revision/run_simulation.py --package /path/OYUN_SIMULASYON_PAKETI_v2.6.zip --seeds 20
```

`content_checks.json` teslim edilen oyun metinleri, motor katmanı, testler ve sonuç dosyalarının hashlerini bağlar. `rulebook_template.md` yalnız üretim şablonudur; oynama dosyası kökteki tam kural kitabıdır.

İnsan masasındaki katılım, tempo ve eğlence etkisi henüz gözlenmedi. Uygulanabilir gözlem sayfası `human_playtest.md` içindedir. Kendini değerlendiren operatör bağımsız QA kabulü veya proje sahibi beğenisi yazmamıştır. Görsel uzman/Sanat Yönetimi alanı, fiziksel baskı ve release/lock bu teslimin dışında kalır.
