# FOULWAKE Karar Kaydı

**Durum:** ACTIVE  
**Kapsam:** v2.7 DRAFT ve sonraki çalışma hatları  
**Kilitli baseline:** v2.6 STABLE / LOCKED

Bu kayıt proje sahibinin tekrar sorulmaması gereken açık kararlarını tutar.
`APPROVED FOR DRAFT`, release veya `STABLE / LOCKED` anlamına gelmez. Daha yeni
karar daha eski kararı yalnız açıkça `SUPERSEDED` olarak işaretlendiğinde
geçersiz kılar.

| Karar | Durum | Bağlayıcı hüküm | Zorunlu kapı |
|---|---|---|---|
| `DEC-20260820-01` | APPROVED FOR v2.7 DRAFT | Açık Deniz ve Kayalık aynı metinsiz binary arka yüzü kullanır. | v2.6'yı değiştirmez; exact candidate üzerinde tam Simülasyon ve kör fiziksel sızıntı testi gerekir. |
| `DEC-20260820-02` | ACTIVE SOURCE CONTRACT | Karakter/Güç görünen metni `FOULWAKE_CARD_TEXTS_v2.7.json`; rulebook anlatı blokları `FOULWAKE_RULEBOOK_STORY_v2.7.md`; ton/lore çiti `FOULWAKE_STORY_FRAMEWORK.md` kaynağından alınır. | Kimlik, adet, effect, zamanlama, deste davranışı ve kural akışı v2.6 baseline'ından korunur; çelişki durdurulur. |
| `DEC-20260820-03` | SUPERSEDED 2026-08-25 | Önceki genel mürekkep/gravür sanat yönü onayı. | Eski örnek ve tam üretim sanatı artık kabul kanıtı değildir; `DEC-20260825-01..05` uygulanır. |
| `DEC-20260820-04` | ACTIVE QA MANDATE | Simülasyon mekanik, matematik, strateji, sosyal deneyim, görsel kullanılabilirlik, PDF, baskı, manifest ve dosya bütünlüğünü denetler. | Tek validator/hash veya kazanma oranı genel PASS değildir; exact-candidate attestation gerekir. |
| `DEC-20260820-05` | LOCK POLICY | Kilit sürecini proje sahibi açık talimatla başlatır; kilidi yalnız Baş Editör uygular. | Açık FAIL/BLOCKER veya eksik candidate/attestation varken kilit yoktur. |
| `DEC-20260820-06` | WORKSTREAM IDENTITY | Resmî uzman işi yalnız kullanıcının oluşturduğu görünür sohbet ve exact branch-bound handoff ile o hatta mal edilir. Geçici alt ajan yasaktır. | Önceden izinli istisna bile uzman teslimi/PASS sayılmaz. |
| `DEC-20260820-07` | WORKSTREAM BRANCH | Uzman dalları `work/v2.7-story`, `work/v2.7-visual`, `work/v2.7-simulation`; entegrasyon hedefi `v2.7-design`dır. | Governance, releases, main ve kilit yalnız Baş Editördedir. |
| `DEC-20260820-08` | COMMUNICATION EVIDENCE | GitHub iş emri görünür sohbet ACK'i değildir. | Doğru sohbet `VISIBLE_CHAT_ACK: YES` handoff vermeden teslim kaydedilemez. |
| `DEC-20260825-01` | BINDING ART REJECTION | `work/v2.7-visual@e91581...` teslimindeki bütün ön ve arka yüz sanatı reddedildi. | Eski render/PDF/plakalar yalnız teknik tarihsel referanstır; yeni candidate olamaz. |
| `DEC-20260825-02` | BINDING FULL-DECK REWORK | 121 kartın her biri ayrı art brief ve semantik olarak ayrı, sıfırdan özgün sahne alır. | Aile plakası türevi ve `unique SHA = unique artwork` kabulü yasaktır; kör contact-sheet QA gerekir. |
| `DEC-20260825-03` | BINDING STYLE/TEXT RULE | Kullanıcının KAPTAN görseli STYLE_ONLY referanstır. İllüstrasyon alanına tabela, slogan, konuşma balonu, açıklama veya saçma/anlamsız okunabilir yazı eklenmez. | Okunabilir metin yalnız exact başlık/effect/flavor/kimlik alanlarında olabilir. |
| `DEC-20260825-04` | BINDING BACK TOPOLOGY | 7 arka yüz: Karakter 20; Güç+Çürümüş 31; Sadakat 15; Deniz+Kayalık 42; Ada 6; Deniz Feneri 4; yardımcı 3. | Metinsiz, aile içinde exact aynı, 180° güvenli, kesim/parlaklık sızıntısız ve önlerle aynı sanat dilinde olmalıdır. |
| `DEC-20260825-05` | BINDING PRODUCTION GATE | 12 ön-yüz pilotu ve 7 arka-yüz taslağı kullanıcı ile Baş Editörce kabul edilmeden tam 121 üretim/PDF başlamaz. | Pilot ret edilirse brief/sanat düzeltilir; teknik hash başarısı bu kapıyı atlayamaz. |
| `DEC-20260825-06` | BINDING ART DIRECTION ROLE | Kalıcı görünür `FOULWAKE Sanat Yönetmeni` hattı `work/v2.7-art-direction` dalında sanat yönü, görsel dramaturji, 121+7 brief incelemesi ve somut yaratıcı rework tavsiyesi üretir. | Final sanat üretmez; metin/mekanik/lore/governance/release/kilit değiştirmez; geçici ajan kullanmaz. |
| `DEC-20260825-07` | BINDING CREATIVE GATE | Görsel Tasarımın kendi teknik/estetik kontrolü tek başına sanat kabulü değildir; pilot ve tam deste Sanat Yönetmeninin bağımsız ruh, doku, kompozisyon, ayrışma ve deste ritmi incelemesinden geçer. | Sanat Yönetmeni tavsiyesi release PASS'i değildir; nihai estetik karar proje sahibinin, kayıt/entegrasyon Baş Editöründür. |
| `DEC-20260825-08` | ART DIRECTION BRIEF ACCEPTED | `work/v2.7-art-direction@7418d9c2c89c265cb6efd30f6a5a7f2addd528da` üzerindeki Bible, 121 brief manifesti, 12 pilot production briefi ve 7 arka-yüz briefi proje sahibi ile Baş Editörce kabul edildi. | Kabul yalnız brief kapısını geçer; final sanat, release veya kilit PASS'i değildir. |
| `DEC-20260825-09` | BINDING FAMILY-VISIBLE MAP BACKS | `BACK_SEA_ROCK` genel denizdir ve Açık Deniz/Kayalık ayrımını gizler; `BACK_ISLAND` anonim genel ada, `BACK_LIGHTHOUSE` 1721'e uygun anonim genel fener gösterir. Aile görünür; exact ön kimlik ve sonuç gizlidir. Sabit 5×5/grid/kart sayısı şartı yoktur. | Değişken kurala uygun düzen, exact master, 180° güvenliği, normal masa mesafesinde aile görünürlüğü ve kör exact-kimlik testleri gerekir. |
| `DEC-20260825-10` | PILOT-ONLY PRODUCTION AUTHORIZATION | Proje sahibi kabul edilen sanat yönü altında kontrollü pilot aşamasını onayladı. | Yalnız 12 ön yüz, 7 arka yüz, contact sheet, değişken harita mockup'ı ve gerekli pilot reworkü yapılabilir; kullanıcı + Baş Editör pilot kabulünden önce kalan 109 ön yüz, tam 121 üretim/PDF, Simülasyon veya release yoktur. |
| `DEC-20260825-11` | BINDING PILOT REVIEW DISPOSITION | Sanat Yönetmeninin `work/v2.7-visual@b4afbcf...` exact incelemesi kabul edildi: 3 ön KEEP, 9 ön REWORK; 7 arka yüzün tamamı REWORK. | Sonraki candidate kabul edilmiş 12 zor-vaka kartıyla sınırlıdır; `SAD-H-03` ve `HAR-KY-06` exact korunur, on kart üretilir/yeniden çizilir, yedi arka yüz sıfırdan yapılır. `GUC-24` set dışı provisional KEEP; diğer set dışı reworkler pilot PASS sonrasına ertelenir. |

## Açık kaynak dispozisyonu

`SRC-002`: v2.6 kayıtlarındaki `GUC-22 = Bayat Peksimet` ile v2.7 kaynağındaki
`GUC-22 = Kaptanın Çatlak Kupası`, `GUC-23 = Bayat Peksimet` çelişkisi karar
değildir. Exact kilitli kaynak karşılaştırması veya proje sahibinin açık hükmü
gelmeden Baş Editör, Hikâye veya Görsel hattı kimlik/effect alanını değiştiremez.

## Uygulama kuralı

- Daha yeni açık kullanıcı kararı önce bu dosyaya ve etkilenen aktif DRAFT
  kaynaklarına kaydedilir.
- Taslak karar v2.6'yı yerinde değiştirmez.
- Eski teslimler silinmez; yanlışlıkla yeniden aday olmamaları için açık
  sınıflandırılır.
- Sohbet özeti, geçici ajan raporu veya GitHub'a yazılmış dosya tek başına
  release kanıtı değildir.
