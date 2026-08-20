# Project State

**Son güncelleme:** 20 Ağustos 2026  
**Son kullanıcı-onaylı stabil prototip:** **v2.6 STABLE / LOCKED**  
**Kanonik locked release:** `releases/v2.6/`  
**ACTIVE_DRAFT:** **v2.7 DRAFT / NOT LOCKED**  
**ACTIVE_BRANCH:** `v2.7-design`  
**ACTIVE_WORKSPACE:** `working/v2.7/`

## Locked baseline

v2.6 kullanıcı tarafından açıkça kilitlenmiştir, yalnızca okunur ve yerinde değiştirilmez.

Kanonik kaynak:

`releases/v2.6/`

## v2.7 temiz yeniden kuruluşu

Kullanıcının açık talimatıyla önceki `working/v2.7/` çalışma ağacı tamamen kaldırılmıştır.

Yeni `working/v2.7/`, `releases/v2.6/` Git ağacının eksiksiz ve birebir kopyası olarak yeniden oluşturulmuştur.

- v2.6 içindeki GitHub tarafından izlenen bütün dosyalar alınmıştır.
- Dosya içerikleri yeniden yazılmamış veya sürüm adı topluca değiştirilmemiştir.
- Kopyalanan dosyalar v2.6 kaynaklarıyla aynı Git blob kimliklerini taşır.
- Önceki v2.7 tasarım, hikâye, test, onay ve üretim kayıtları yeni çalışma ağacına aktarılmamıştır.
- Kilitli `releases/v2.6/` ağacı değiştirilmemiştir.
- Önceki v2.7, Git geçmişinden geri alınabilir durumdadır.

## Binary artefaktlar

GitHub deposunda v2.6 binary dosyalarının kendileri yerine kanonik yol ve SHA-256 kayıtları tutulmaktadır. Yeni v2.7, `BINARY_ARTIFACTS.md` ve ilgili manifest/checksum kayıtlarını v2.6'dan eksiksiz devralır.

Kilitli binary kaynaklar taşınmamış, yeniden yazılmamış veya silinmemiştir.

## Current result

**v2.7 = ACTIVE STORY DRAFT / NOT LOCKED**

Temiz v2.6 kopyasına v2.7 anlatı çalışma kaynakları eklenmiştir:

- `working/v2.7/FOULWAKE_STORY_FRAMEWORK.md`
- `working/v2.7/FOULWAKE_RULEBOOK_STORY_v2.7.md`
- `working/v2.7/FOULWAKE_CARD_TEXTS_v2.7.json`
- `working/v2.7/FOULWAKE_NARRATIVE_VALIDATION_v2.7.md`

Kural kitabının mevcut akışı korunarak yalnız 3.1, 3.3, 3.4 anlatı notu, 3.6 ve Bölüm 17 için v2.7 hikâye metni hazırlanmıştır. 20 Karakter ve 30 Güç kartının tam metin kaynağı v2.7'ye alınmış; yalnız seçili görünen ad ve flavor alanları güncellenmiştir.

Otomatik karşılaştırmada kart sayıları, kimlikler, etkiler, zamanlamalar, başlangıç havuzu ve desteye dönüş alanları baseline ile aynı bulunmuştur. Harita, Sadakat, Çürümüş Erzak ve yardımcı kartlar değiştirilmemiştir.

Kilitli v2.6 hikâyesi ve binary artefaktları değiştirilmemiştir. v2.7 PDF'leri henüz üretilmemiş, sürüm kanonlaştırılmamış ve kilitlenmemiştir.

## Lock rule

Yalnız kullanıcının açıkça `kilitle`, `stable yap` veya `release et` demesi v2.7'yi STABLE / LOCKED durumuna dönüştürebilir.

Onay, beğeni veya `devam et` ifadesi kilitleme yetkisi değildir.
