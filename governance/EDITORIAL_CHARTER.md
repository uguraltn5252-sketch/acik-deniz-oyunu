# FOULWAKE Baş Editörlük Tüzüğü

**Durum:** ACTIVE  
**Yürürlük:** v2.7 ve sonraki bütün taslaklar  
**Proje sahibi:** Uğur Altun  
**Kilitli baseline:** v2.6 STABLE / LOCKED

Bu tüzük, FOULWAKE projesindeki Hikâye, Görsel Tasarım, Simülasyon Testi ve üretim çalışmalarının aynı kanonik kaynakla ilerlemesini sağlar. Kilitli sürümler yerinde değiştirilmez; her değişiklik yeni bir DRAFT sürümünde yapılır.

## 1. Nihai karar ve kilit yetkisi

- Proje sahibi mekanik, yaratıcı yön, hikâye ve sanat hakkındaki nihai kararı verir.
- Bir sürümü kilitleme sürecini yalnız proje sahibinin açık `kilitle`, `stable yap` veya `release et` talimatı başlatabilir.
- Sürümü `STABLE / LOCKED` durumuna geçirme, release manifestini onaylama ve kanonik kaynakları güncelleme yetkisi yalnız **Baş Editör** rolündedir.
- `beğendim`, `onaylıyorum`, `devam et` veya görsel yön onayı release kilidi değildir.
- Baş Editör, açık BLOCKER veya MAJOR sorun varken kilit işlemini tamamlamaz. Önce düzeltme ve yeniden doğrulama ister.

## 2. Rol ve yetki matrisi

| Rol | Yetkili olduğu alan | Yetkili olmadığı alan |
|---|---|---|
| Proje sahibi | Nihai mekanik ve yaratıcı karar; kilit sürecini başlatma | Kilitli sürümü geriye dönük değiştirmiş sayma |
| Baş Editör | Kanon, kaynak önceliği, entegrasyon, çakışma çözümü, release gate, kilitleme | Kendiliğinden yeni mekanik veya yaratıcı kanon üretme |
| Hikâye Editörü | Lore, anlatı, görünen ad, flavor ve dil akışı | Kart kimliği/adedi, etki, zamanlama, deste davranışı ve kural akışı |
| Görsel Tasarım | İllüstrasyon, düzen, tipografi, ikon, baskı ve görsel kullanılabilirlik | Mekanik, kanonik metin veya lore hükmünü tek taraflı değiştirme |
| Simülasyon Testi | Mekanik, matematik, strateji, sosyal deneyim, görsel okunabilirlik, PDF/dosya/manifest denetimi | Bulguyu doğrudan yeni kurala dönüştürme veya sürüm kilitleme |
| Üretim/PDF | Onaylı kaynaklardan baskı ve export üretimi | Taşmayı çözmek için metin, kart veya mekanik budama |

## 3. Korunan alanlar

Aşağıdaki alanların kanonik durumu yalnız Baş Editör tarafından güncellenir:

- `PROJECT_STATE.md`
- `AI_HANDOFF.md`
- `CHANGELOG.md`
- `README.md` içindeki kanonik sürüm kaydı
- `governance/**`
- `releases/**`
- release manifestleri, checksum kayıtları ve kilit tutanakları
- `STABLE / LOCKED` etiketi ve sürüm numarası

Diğer çalışma hatları bu alanlarda değişiklik ihtiyacı görürse dosyayı doğrudan değiştirmez; handoff raporunda Baş Editöre bildirir.

## 4. Kaynak önceliği

Çakışmada aşağıdaki sıra uygulanır:

1. Proje sahibinin en son açık kararı.
2. Değişmeyen mekanikler için son STABLE / LOCKED release.
3. Baş Editör tarafından `governance/DECISION_REGISTER.md` içinde kayda alınmış aktif DRAFT kararları.
4. İlgili çalışma hattının onaylı kaynak dosyaları.
5. Taslak üretimler ve sohbet özetleri.
6. Eski, kaynağı belirsiz veya GitHub’a aktarılmamış notlar.

Yeni bir kullanıcı kararı kilitli sürümü yerinde değiştirmez; sonraki DRAFT sürümünde uygulanır.

## 5. Bağımsız Simülasyon Testi

Simülasyon Testi, Baş Editörün yerine geçmez; Baş Editörün kilit kararı için zorunlu bağımsız kanıt üretir.

- `PASS` veya kayıt altına alınmış `PASS WITH MINOR ISSUES` olmadan release değerlendirmesi tamamlanmaz.
- `FAIL` veya `BLOCKER` kilidi durdurur.
- Bir bulgu yalnız düzeltilmiş kaynak ve yeniden test ile kapanır.
- Simülasyon Testi yalnız kazanma oranlarını değil mekanik, mantık, strateji, sosyal deneyim, sıkılma, adalet, görsel kullanılabilirlik ve dosya bütünlüğünü denetler.

## 6. Kilitli sürüm ilkesi

- Kilitli klasörler salt okunur baseline kabul edilir.
- Kilit sonrası düzeltme gerekiyorsa yeni bir sürüm veya yama sürümü açılır.
- Kart eksiltme/ekleme, kimlik değiştirme, etki veya zamanlama değişikliği yalnız proje sahibinin açık mekanik kararıyla yeni DRAFT içinde yapılabilir.
- Hiçbir çalışma hattı kendi çıktısını kanonik veya kilitli ilan edemez.

## 7. İletişim ve handoff

Çalışma hatları birbirinin dosyasını sessizce değiştirmez. Her teslim; kaynak commit, kapsam, değişen dosyalar, korunmuş alanlar, testler, açık riskler ve sonraki alıcı bilgisiyle kaydedilir. Ayrıntılı yöntem `governance/WORKSTREAM_PROTOCOL.md` içindedir.
