# FOULWAKE v2.7 — Görünür Hikâye Hattı Yeniden Doğrulaması

**Durum:** STORY WORKSTREAM PASS / DRAFT / NOT LOCKED  
**Görünür sohbet:** `Foulwake Hikâye Editör`  
**Kanıt türü:** `VISIBLE_CHAT_WORKSTREAM`  
**Çalışma dalı:** `work/v2.7-story`  
**Entegrasyon tabanı:** `v2.7-design@bc148e33343b4066259a996a9c299aab17fd8e3d`  
**Baseline:** `v2.6 STABLE / LOCKED`  
**Tarih:** 20 Ağustos 2026

## Kapsam ve sonuç

Bu kayıt, görünür Hikâye Editörü sohbetinde yapılan bağımsız anlatı yeniden
doğrulamasıdır. Yalnız hikâye, görünen ad/flavor, dönem dili ve kural kitabının
tanımlı anlatı katmanı incelenmiştir.

**Sonuç:** Hikâye kaynakları Görsel Tasarıma metin/lore kaynağı olarak
devredilebilir. Bu hüküm mekanik QA, artefakt PASS'i, release PASS'i, kanon
entegrasyonu veya kilit kararı değildir.

## İncelenen kaynaklar

| Dosya | Bu teslimdeki blob | Hüküm |
|---|---|---|
| `FOULWAKE_STORY_FRAMEWORK.md` | `962222d83d669763c4ac8e2765f024b9fade180c` | PASS — CAN-01–07 kanon çiti korunuyor; CAN-08/09 yalnız TASLAK |
| `FOULWAKE_RULEBOOK_STORY_v2.7.md` | `f1e0eb75434540a85e8b21484acd99ca0abc66cf` | PASS — yalnız 3.1, 3.3, 3.4 anlatı notu, 3.6 ve 17 anlatı katmanı |
| `FOULWAKE_CARD_TEXTS_v2.7.json` | `38a03b71cd3232fd844db8d80d8e53662510b6a3` | PASS FOR STORY SCOPE — 20 Karakter ve 30 Güç; bu teslimde değiştirilmedi |
| `FOULWAKE_NARRATIVE_VALIDATION_v2.7.md` | `9c27b177fb86be584a4817f38470dc425ac9c0de` | RECORDED PASS / REPRODUCTION PENDING; bu teslimde değiştirilmedi |

## Anlatı denetimi

- 1721 maddi ve kurumsal zemini korunuyor; dünya, kurumlar ve olay örgüsü
  FOULWAKE'a özgü kalıyor.
- Arden, San Cordelio, Saint Verena ve Mattias Veyr adları korunuyor.
- Siyah Mühür tek ve kesin merkezi örgüt olarak açıklanmıyor.
- Gusto'nun kaderi, siyah balmumunun kanıt değeri ve eksik sayfaların faili
  kesinleştirilmiyor.
- Veyr'in terkibinin işe yaradığı ilan edilmiyor; kayıtlar, yöntem ve başarısız
  denemeler değerli yük olarak kalıyor.
- Mizah modern benzetmelerden değil; sefer kefaleti, sağlık kâğıdı, mühür,
  borç, vardiya, güverte davranışı ve karakter kusurlarından doğuyor.
- İskorbüt bir anda oluşan veya Ada'da mucizevi biçimde iyileşen hastalık gibi
  anlatılmıyor.
- Kaptan seçimi ve rota oylaması hikâyeye gerekçe kazanıyor; oyun sonucu
  anlatıyla geri alınmıyor.

## Uygulanan küçük düzeltme

`3.6 İlk yolculuk sabahı — Sadakat` paragrafındaki “sonuncusuna” sayımı,
değişken oyuncu/Hain dağılımında tam beş kişilik sabit bir grup ima ediyordu.
Tekliflerin sayısı açık bırakıldı. Hain tablosu, Sadakat dağıtımı, ilk Hain
gecesi veya herhangi bir mekanik alan değişmedi.

Değişiklik kaydı `CHG-20260820-05` olarak Story Framework'e eklendi.

## Korunan alanlar

- `FOULWAKE_CARD_TEXTS_v2.7.json` bu committe değişmez; kart kimliği, adet,
  `effect`, zamanlama, grup, başlangıç havuzu ve desteye dönüş alanlarına
  dokunulmaz.
- Kural kitabı akışı, `ŞİMDİ YAP`, `KURAL`, tablo ve hızlı referans alanları
  değiştirilmez.
- `releases/v2.6/**`, görsel üretim dosyaları, `working/v2.7/qa/**`,
  `governance/**`, `PROJECT_STATE.md`, `AI_HANDOFF.md`, `main` ve
  kilit alanları değiştirilmez.
- `QA-001` açık kalır. Mekanik eşdeğerliğin yeniden üretilebilir karşılaştırması
  ve exact-candidate attestation yalnız görünür Simülasyon Testi hattına aittir.

## Handoff

Görsel Tasarım; Karakter/Güç görünen metni için kart JSON'unu, tanımlı kural
kitabı blokları için Rulebook Story dosyasını, ton ve lore çiti için Story
Framework'ü kullanmalıdır. Metni kısaltma veya yeniden yazma gereği doğarsa
dosyayı sessizce değiştirmeden Hikâye Editörüne geri iletmelidir.

**Sonraki alıcılar:** `FOULWAKE görsel tasarım`, `Simülasyon Testi`, ardından
entegrasyon için Baş Editör.  
**LOCK_REQUESTED:** NO
