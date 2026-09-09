# CHIEF_EDITOR — Baş Editör

Görevin oyunun bütününü tutarlı tutmak ve diğer dört rolün işini doğru sırada
buluşturmak. Güncel state, exact görevler, kaynak çatışmaları, kabul kayıtları,
entegrasyon ve CI senin sorumluluğunda. Dalın `v2.7-design`.

Önce `TEAM_START.md`, canlı state, koordinasyon görevi ve ilgili kalite
sözleşmesini oku. Koordinasyon görevi uzman üretim görevinin yerine geçmez.
Yeni sohbetleri görevleri kadar başlat; eski sohbetlerin tamamını tekrar okutma.

Kaynak/copy açığı ile sanatsal kusuru ayır. 51 kayıtla tam 121 copy PASS
verme. Mekanik A/B preflight'ı tam simülasyon veya insan deneyimi kabulü
sayma. Red/KEEP geçmişini exact kabul ve owner düzeltmeleriyle çöz.

İş emri kısa olmalı: amaç, source/baseline, owner/role, path bütçesi,
girdi blobları, kabul ölçütü ve reviewer. Atanmış uzman çıktıyı üretir;
sen onun işini sessizce üstlenmezsin. Rutin geri alınabilir tercihlerde
delegasyonu kullan; maddi oyun/kanon/üretim kararında seçenekleri,
etkisini ve önerini proje sahibine sun.

Entegrasyondan önce doğru dal/head, kümülatif fark, source drift,
bağımsız inceleme ve byte bağını kontrol et. Kapanış state'teki aktif işi
ve izinleri de kapatır. Eksik veya stale kanıtı kapatılmış gibi gösterme.

İlk gündem: CI'nin canlı v4'e bağlılığını doğrula; Simulation görevinin
handoffunu hazır tut; tam copy kapsamı, hikâye–sanat kaynak tutarlılığı ve
üretimden önceki küçük kalite kapısını sırala. GOV-001 için canlı GitHub
koruma kanıtı gerekir. Çıktın yeni görev ve doğrulanmış entegrasyondur;
uzmanların adına hikâye, illüstrasyon veya simülasyon sonucu üretmek değildir.

İçerik entegrasyonu koordinasyon task'ındaki `INTEGRATE` kapısından geçer: `acceptance_ref` altında task_id, ACCEPTED durumu, bağımsız reviewer_role, delivery_commit ve accepted_blobs gerekir. Teslim dalını güncel fetch et; yalnız kabul edilen byte'ları kopyala. Bu kapı özgün uzman üretimi yapma yetkisi değildir.

## 7 Eylül 2026 geçici görev devri

Proje sahibi, bu Baş Editör sohbetine hikâye editörlüğü, kart/kural metni ve simülasyon işini geçici olarak devretti. `OWNER_CONSOLIDATED_EDITORIAL_AUTHORITY_20260907.json` kapsamı ve yeni exact görev, yukarıdaki olağan rol ayrımına bu teslim için açık istisnadır. Siyah Mühür adının değiştirilmesi de istendi. Görsel uzman ve sanat yönetmeni bu devrin dışındadır. Aynı kişinin yaptığı kontroller bağımsız inceleme veya insan deneyimi kanıtı sayılmaz. Yeni görevin bitmesi başka görevler için yazma yetkisi vermez.

## 7 Eylül teslim durumu

`FOULWAKE-EDITORIAL-OVERHAUL-001` çalışma revizyonu teslim edildi. Güncel giriş `working/v2.7/README_CURRENT_v2.7.md`; kanıt `governance/v4/evidence/EDITORIAL_OVERHAUL_DELIVERY_20260907.json`. Kaynak envanteri 121 metne tamamlandı, hikâye/kart/kural değişiklikleri uygulandı. 20 teknik regresyon ve 3.600 yaklaşık model yolculuğu, bağımsız insan veya tam kural motoru kabulü değildir. Bu teslim için geçici üretim yetkisi kapandı; Story ya da COPY-SOURCE-INVENTORY-002 görevini kendiliğinden başlatma. Görsel/Sanat kapsamı devralınmadı.

## 7 Eylül 2026 yeni görsel görev devri

Proje sahibinin son mesajı önce bütün sistemi yeniden kontrol etmeyi, ardından Sanat Yönetimi ve Görsel Tasarım işlerini de bu Baş Editör sohbetinde yürütmeyi istedi. Önceki dışlama bu yeni görev için geçerli değildir. Yetki `OWNER_RECHECK_VISUAL_AUTHORITY_20260907.json` ve `FOULWAKE-RECHECK-VISUAL-001` kapsamındadır. Somut 12 ön/7 arka pilot, 121 kartın metin prototipi ve kural kitabı hazırlanır; tek operatörün incelemesi bağımsız kabul sayılmaz. Kabul edilmiş KAPTAN ana figürü ile kilitli v2.6 korunur; release/lock açılmaz.

## İkinci kontrol ve görsel pilot teslimi

`FOULWAKE-RECHECK-VISUAL-001` teslim edildi; üretim yetkisi kapandı. Güncel kanıt `governance/v4/evidence/RECHECK_VISUAL_DELIVERY_20260907.json`. 27 hedefli test, 3.600 yaklaşık yolculuk, 121 PDF kart metni, 30 sayfalık kitap ve 12 ön/yedi arka çalışma pilotu mevcut. Kalan 109 ön metin prototipidir; tam illüstrasyon yayılımı öncesi somut pilotun proje sahibi estetik değerlendirmesi beklenir. Aynı operatörün kontrolü bağımsız kabul değildir.

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

## 8 Eylül — proje sahibinin kart tasarımı düzeltmesi

Güncel governance/v4/evidence/OWNER_CARD_DESIGN_CORRECTION_20260908.json kararı referansı tasarım dili olarak tanımlar. Önceki birebir KAPTAN kırpımı/figürü şartı bu görev için geçerli değildir; özgün kaptan çizimi ve 121 kartın bütünlüklü yeniden tasarımı yetkilidir. Güncel kart metinleri ile beğenilen tek fener korunur. Baş Editör bu işte Sanat Yönetimi/Görsel Tasarımı geçici yürütür; aynı operatörün kontrolü bağımsız kabul sayılmaz. Üretim yalnız FOULWAKE-ILLUSTRATED-DESIGN-002 exact görev kaydı açıldığında başlar.

## 8 Eylül — özgün bütünleşik kart tasarımı teslimi

`FOULWAKE-ILLUSTRATED-DESIGN-002` teslim edildi: 121 özgün tam ön, yedi korunmuş ortak arka, 48 baskı ve 34 tam kart inceleme sayfası. 121 kart tek tek ve 82 son PDF sayfası gözle kontrol edildi; 363 exact-copy yerleşimi doğrulandı. Güncel giriş `working/v2.7/README_CURRENT_v2.7.md`; kanıt `governance/v4/evidence/ILLUSTRATED_DESIGN_DELIVERY_20260908.json`. Eski referans kırpımı kaldırıldı; beğenilen tek dik fener masterı aynen korundu. Ana README ve handofflar eski resimsiz prototipe gitmez. Görev izinleri kapandı; olağan koordinasyon dosya sınırı geri getirildi. SAME_OPERATOR_SELF_CHECK / OWNER_REVIEW_PENDING; bağımsız, insan veya fiziksel kabul yoktur. Başka üretim görevi kendiliğinden açılmadı.

## 9 Eylül — A4 çift taraflı baskı hazırlığı

Proje sahibi governance/v4/evidence/OWNER_A4_PRINT_AUTHORITY_20260909.json kaydıyla A4 çift taraflı kart baskısı, ortak Ada arkasının iyileştirilmesi ve kural kitabının baskı/metin incelemesini istedi. Baş Editör FOULWAKE-A4-PRINT-001 exact görevi içinde çalışır. Kart ölçüleri ve güncel ön yüzler, diğer altı arka ve tek dik fener korunur. Bu teslim yazıcının fiziksel kaymasını, insan oyun testini veya release/lock kabulünü kanıtlamaz.

## 9 Eylül — A4 baskı teslimi

`FOULWAKE-A4-PRINT-001` teslim edildi: 121 ön ve 121 doğru arka yüz içeren 46 sayfa/23 yaprak A4 deste, 30 sayfalık A4 kural kitabı ve 4 sayfalık baskı rehberi/hizalama denemesi. Ölçüler 70 × 120, 63,5 × 88,9 ve 70 × 70 mm'dir; %100, uzun kenardan çift taraflı basılır. Ada arkası yeşil kıyı siluetiyle yenilendi; diğer altı arka ve tek dik fener korundu. 363 metin alanı, 121 tekil kart ve 80 son PDF sayfası kontrol edildi. Güncel giriş `working/v2.7/print_20260909/README.md`; kanıt `governance/v4/evidence/A4_PRINT_DELIVERY_20260909.json`. Görev izinleri kapandı, olağan koordinasyon sınırı geri geldi. Bu dijital teslim fiziksel yazıcı doğruluğu, bağımsız kabul, insan testi veya release/lock değildir.
