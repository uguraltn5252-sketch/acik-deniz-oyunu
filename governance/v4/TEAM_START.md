# FOULWAKE — Yeni sohbet başlangıcı

## Ortak amaç

İyi çalışan, özgün, iç tutarlılığı olan bir masa oyunu: kararları anlamlı,
şüphesi oyuncular arasında doğan, arka planı ve sanatı aynı dünyaya ait.
Kalite yalnız dosya sayısı, render hash'i veya test puanı değildir.

Güncel kaynaklar 1721 ve Arden dünyasındadır. Kesin adlar **Kraliçe Tesella**,
**Port Avanta**, **Santa Veda** ve **Malum**. Gusto'nun akıbeti ile terkibin
başarısı kesinleştirilmez. Malum gizli örgüttür; merkezi ve üyeleri açıklanmaz.
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

## Güncel sanat incelemesi

`read_only_assignments.ART_DIRECTION` → `ART-PUBLICATION-REVIEW-001`.
[Tek inceleme girişi](planning/ART_DIRECTION_REVIEW_BRIEF_20260909.md).
Ana görsel referans özgün KAPTAN kartıdır; hazırlanmış kitap/kartlar
ikincil ilham ve inceleme konusudur. Referanstaki eski copy kullanılmaz.
Eski KAPTAN patch'inin figür/kırpım ve Ada yeniden çizim talimatları güncel
emir değildir. Son gemili kapaklar yalnız denemedir; onay veya yeni kanon
oluşturmaz. Uzman dalı dondurulmuş kalır; güncel girdiler v2.7-design'dan
okunur. İnceleme görünür rol sohbetindedir; yeni üretim henüz açılmamıştır.

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

## 9 Eylül 2026 — güncel teslim

`FOULWAKE-PUBLICATION-REDESIGN-001` teslim edildi; bu görevin üretim izinleri kapandı. Güncel indirme girişi `working/v2.7/publication_20260909/README.md`: 121 kart tek 46 sayfalık A4 çift taraflı PDF ve 30 sayfalık kural kitabı. Kanon, kart metinleri, hikâye, kitap ve sanat kayıtları birlikte güncellendi. 121 özgün kart çizimi, yedi ortak arka, tek fener ve palmiye Adası korunur. Kanıt `governance/v4/evidence/PUBLICATION_DELIVERY_20260909.json`; aynı operatörün dijital kontrolüdür. Bağımsız estetik kabul, fiziksel prova ve insan oyunu kanıtı ayrı kalır.

Önceki görev devirleri ve teslim notları [Git geçmişinde](https://github.com/uguraltn5252-sketch/acik-deniz-oyunu/blob/d4072fbff19aeae3508801b733164fdae8517e7a/governance/v4/TEAM_START.md) korunur; bunlar güncel üretim yetkisi değildir. Yeni iş için canlı state ve exact görev okunur.
