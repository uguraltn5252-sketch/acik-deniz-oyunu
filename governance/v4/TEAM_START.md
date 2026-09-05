# FOULWAKE — Yeni sohbet başlangıcı

## Ortak amaç

İyi çalışan, özgün, iç tutarlılığı olan bir masa oyunu: kararları anlamlı,
şüphesi oyuncular arasında doğan, arka planı ve sanatı aynı dünyaya ait.
Kalite yalnız dosya sayısı, render hash'i veya test puanı değildir.

Mevcut kaynaklarda 1721, Arden, San Cordelio, Saint Verena, Gusto ve Siyah
Mühür korunur. Gusto'nun akıbeti ile Siyah Mühür'ün niteliği kesinleştirilmez.
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
resim olduğu anlamına gelmez; mevcut copy resolver kapsamı 51 kayıttır.

## İş sırası

Önce kaynak/copy bütünlüğü ve Sea/Rock bilgi modeli kanıtı; ardından mevcut
hikâye ve sanatın hedefli tutarlılık incelemesi; sonra exact görevle küçük
görsel kapı ve bağımsız değerlendirme. Kabulden sonra kontrollü yayılım,
tam deste/oyun testi ve fiziksel proof gelir. Bu sıra planlama çerçevesidir;
aktif görev yalnız state'te bulunur. Yeni içerik üretimi bu dosyayla başlamaz.

Handoff yedi alanı `governance/WORKSTREAM_PROTOCOL.md` içindedir. Sohbet
bağlamını azalt; araştırma, yaratıcı eleştiri ve kanıt kalitesini azaltma.
