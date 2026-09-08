# FOULWAKE — Yeni sohbet başlangıcı

## Ortak amaç

İyi çalışan, özgün, iç tutarlılığı olan bir masa oyunu: kararları anlamlı,
şüphesi oyuncular arasında doğan, arka planı ve sanatı aynı dünyaya ait.
Kalite yalnız dosya sayısı, render hash'i veya test puanı değildir.

Güncel çalışma kaynaklarında 1721, Arden, San Cordelio, Saint Verena, Gusto
ve Kuru Pay vardır. Proje sahibinin ad değişikliği uygulanmıştır. Gusto'nun
akıbeti, terkibin başarısı ve Kuru Pay çevresindeki ortaklığın niteliği kesinleştirilmez.
Dünya ciddidir; insanların korkuları, çıkarları ve kusurları kuru mizahı
üretir. Görsel omurga ISLAK TANIKLIK, gravür/tarama, mat mürekkep ve tuzlu
kâğıttır. Bunlar mevcut kaynakların özeti; yeni mekanik veya kanon kararı değildir.

## Bir kez başla, görev kadar bağlam oku

Repository: `uguraltn5252-sketch/acik-deniz-oyunu`.
Her açılışta GitHub'daki **güncel `v2.7-design` HEAD'ini** doğrula. Eski sohbet
başlığından, sabit bir prompt SHA'sından veya uzman dalındaki eski state'ten başlama.

1. `governance/v4/runtime/STATE.json` ve kendi `roles/<ROLE_ID>.md` brief'ini oku.
2. `roles/REGISTRY.json` ile atanmış task'ın rol, dal, path ve inputlarını doğrula.
   State'teki `read_only_assignments` da görünür rol incelemesi atayabilir:
   yalnız kaynak okuma ve kendi sohbetinde bulgu/öneri teslimi; dosya yazma yetkisi vermez.
3. Sözleşmenin göreve ilişkin kapılarını ve yalnız gereken kaynak bölümlerini aç.

Yerel kısa görünüm: `python -B governance/v4/bootstrap.py --role <ROLE_ID>`.
İlk cevap en fazla altı satır: `ROLE`, `SOURCE_HEAD`, `ASSIGNED_TASK`,
`WRITE_AUTHORIZED`, `BLOCKER`, `NEXT_ACTION`. Uzun geçmiş özetini tekrar yazma.
Atanmış görev yoksa ilk okuma ve teşhis salt okunurdur; üretime başlanmaz.
`READ_ONLY_ASSIGNED` varsa uzman incelemeyi kendi sohbetinde yürütür; tek aktif
uzman yazma görevi korunur. İnceleme önerilerinin uygulanması ayrıca görevlendirilir.

## Yetki ve kaynak sırası

Git object/ref → güncel v4 state/task/contracts/registry → bağlayıcı owner
kararı → exact kaynak ve kabul kanıtı → çalışma artefaktı → sohbet özeti.
`CURRENT_STAGE.json`, eski scope baseline'ları ve eski iş emirleri tarihsel
kayıttır. Art Bible içindeki eski görev statüleri, eski SRC-002 açıklaması
ve eski KAPTAN mekanik yorumları güncel v4/owner copy'sini geçersiz kılamaz.

Proje sahibi 5 Eylül 2026'da koordinasyon ve yeniden düzenleme yetkisini
genişletti. Önceki yedi dosya/iki commit sınırı tamamlanan iş emrine aittir.
Baş Editör kayıtlı delegasyonla rutin işi yürütür; her rol yine exact görevle
yazar. Kalıcı mekanik/kanon değişikliği, pahalı tam üretim ve release/lock
kendi kalite ve karar kapılarını gerektirir; bu başlangıç bunları açmaz.

## Birlikte kalite

- **Anlam:** Metin, resim ve mekanik aynı karar baskısını mı destekliyor?
- **Tutarlılık:** Kaynak, dönem, kişi, nesne ve kural birbirini tutuyor mu?
- **Özgüllük:** Sahne ve karakterin ayrı bir nedeni var mı; tekrar veya klişe mi?
- **Okunurluk:** Masada anlaşılır mı; arka yüz gizli bilgiyi sızdırıyor mu?
- **Deneyim:** Karar, adalet, tempo, şüphe ve öğretilebilirlik kanıtla değerlendirildi mi?
- **Kanıt:** Üreten rol dışında inceleme, exact teslim bağı ve belirsizlik kaydı var mı?

Bir kaynak çatışması varsa ilgili kart/sahne kimliğini ve iki exact kaynağı
göster; tahminle kapatma. Eksik tam simülasyon motoru veya fiziksel test
UNKNOWN/BLOCKER'dır. Destede 121 kimlik olması, 121 doğru copy ve kabul edilmiş
resim olduğu anlamına gelmez; güncel copy resolver kapsamı 121 kayıttır; bu yalnız metin kapsamıdır.

## İş sırası

Önce kaynak/copy bütünlüğü ve Sea/Rock bilgi modeli kanıtı; ardından mevcut
hikâye ve sanatın hedefli tutarlılık incelemesi; sonra exact görevle küçük
görsel kapı ve bağımsız değerlendirme. Kabulden sonra kontrollü yayılım,
tam deste/oyun testi ve fiziksel proof gelir. Bu sıra planlama çerçevesidir;
aktif görev yalnız state'te bulunur. Yeni içerik üretimi bu dosyayla başlamaz.

Handoff yedi alanı `governance/WORKSTREAM_PROTOCOL.md` içindedir. Sohbet
bağlamını azalt; araştırma, yaratıcı eleştiri ve kanıt kalitesini azaltma.

## 7 Eylül 2026 geçici görev devri

Proje sahibi, bu Baş Editör sohbetine hikâye editörlüğü, kart/kural metni ve simülasyon işini geçici olarak devretti. `OWNER_CONSOLIDATED_EDITORIAL_AUTHORITY_20260907.json` kapsamı ve yeni exact görev, yukarıdaki olağan rol ayrımına bu teslim için açık istisnadır. Siyah Mühür adının değiştirilmesi de istendi. Görsel uzman ve sanat yönetmeni bu devrin dışındadır. Aynı kişinin yaptığı kontroller bağımsız inceleme veya insan deneyimi kanıtı sayılmaz. Yeni görevin bitmesi başka görevler için yazma yetkisi vermez.

## 7 Eylül teslim durumu

`FOULWAKE-EDITORIAL-OVERHAUL-001` çalışma revizyonu teslim edildi. Güncel giriş `working/v2.7/README_CURRENT_v2.7.md`; kanıt `governance/v4/evidence/EDITORIAL_OVERHAUL_DELIVERY_20260907.json`. Kaynak envanteri 121 metne tamamlandı, hikâye/kart/kural değişiklikleri uygulandı. 20 teknik regresyon ve 3.600 yaklaşık model yolculuğu, bağımsız insan veya tam kural motoru kabulü değildir. Bu teslim için geçici üretim yetkisi kapandı; Story ya da COPY-SOURCE-INVENTORY-002 görevini kendiliğinden başlatma. Görsel/Sanat kapsamı devralınmadı.

## 7 Eylül 2026 yeni görsel görev devri

Proje sahibinin son mesajı önce bütün sistemi yeniden kontrol etmeyi, ardından Sanat Yönetimi ve Görsel Tasarım işlerini de bu Baş Editör sohbetinde yürütmeyi istedi. Önceki dışlama bu yeni görev için geçerli değildir. Yetki `OWNER_RECHECK_VISUAL_AUTHORITY_20260907.json` ve `FOULWAKE-RECHECK-VISUAL-001` kapsamındadır. Somut 12 ön/7 arka pilot, 121 kartın metin prototipi ve kural kitabı hazırlanır; tek operatörün incelemesi bağımsız kabul sayılmaz. Kabul edilmiş KAPTAN ana figürü ile kilitli v2.6 korunur; release/lock açılmaz.

## Tam deste çizimi ve fener düzeltmesi

Proje sahibi somut pilot tesliminden sonra “Devam” dedi; ardından fenerin yandan görünümünü araştırıp oyuna uyarlama kararını Baş Editöre verdi. `OWNER_FULL_DECK_ART_AUTHORITY_20260907.json` ve yeni `FOULWAKE-FULL-DECK-ART-001` görevi kalan 109 ön çizimi ile bir Fener arka masterının yenilenmesini kapsar. 12 ön ve diğer altı arka kaynak korunur. Bu devam kararı bağımsız kabul, fiziksel proof veya release/lock değildir. Güncel hikâye adı Kuru Pay; önceki tarihsel bölümdeki Siyah Mühür ifadesi güncel kanon değildir.

## Tam deste teslimi — güncel durum

`FOULWAKE-FULL-DECK-ART-001` tamamlandı: 121 resimli ön, yedi ortak arka,
yandan Fener, 48 sayfalık tam kart baskısı ve 24 sayfalık görsel inceleme.
Kanıt `governance/v4/evidence/FULL_DECK_ART_DELIVERY_20260907.json`;
güncel giriş `working/v2.7/README_CURRENT_v2.7.md`. Üretim izni kapandı,
Baş Editörün olağan koordinasyon dosya sınırı geri getirildi. Önceki
“109 ön eksik” kayıtları tarihsel teslimi anlatır. İnsan oyunu, fiziksel
baskı ve bağımsız estetik kabul açık; release/lock verilmedi.

## 8 Eylül: bütün oyun incelemesi ve tek fener

Proje sahibinin güncel talimatı `governance/v4/evidence/OWNER_WHOLE_GAME_POLISH_AUTHORITY_20260908.json` kaydındadır. `FOULWAKE-WHOLE-GAME-POLISH-001` açıldığında Başeditör hikâye, kural, kart, simülasyon ve görsel düzeltmeleri o görev kapsamında yürütür. Beğenilen fener sahnesi korunur; alttaki ters kule kaldırılır. Fener ailesinin eski 180 derece simetri şartı bu açık kararla aşılmıştır. Diğer gizli arka yüz ve kaynak korumaları sürer.

## 8 Eylül 2026 — tam kontrol teslimi

FOULWAKE-WHOLE-GAME-POLISH-001 uygulandı; güncel teslim governance/v4/evidence/WHOLE_GAME_POLISH_DELIVERY_20260908.json kaydındadır. 121 kart, yedi arka yüz ve kural kitabı kontrol edildi. Fener tek ve diktir; beğenilen üst sahne korunmuştur. Geçici üretim yetkileri kapalıdır; güncel durum runtime/STATE.json üzerinden okunur. Bu teslim bağımsız, fiziksel veya insan oyun testi kabulü değildir.
