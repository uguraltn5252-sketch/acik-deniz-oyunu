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

**v2.7 = CLEAN BASELINE CLONE / DRAFT / NOT LOCKED**

Yeni v2.7 henüz yeni bir hikâye, mekanik, görsel tasarım veya test kararı içermez. Bundan sonraki değişiklikler yalnızca aktif DRAFT içinde, ilgili çalışma hattının yetki sınırlarına göre yapılmalıdır.

## Lock rule

Yalnız kullanıcının açıkça `kilitle`, `stable yap` veya `release et` demesi v2.7'yi STABLE / LOCKED durumuna dönüştürebilir.

Onay, beğeni veya `devam et` ifadesi kilitleme yetkisi değildir.
