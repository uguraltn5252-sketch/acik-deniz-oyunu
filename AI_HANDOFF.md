# AI Handoff Protocol

Bu dosya farklı ChatGPT oturumları/model sürümleri arasında oyunun kanonik durumunu yeniden kurmak için zorunlu protokoldür.

## Baş editörlük yönetişimi

Her çalışma oturumu aşağıdaki dosyaları bu sırayla okumalıdır:

1. `AI_HANDOFF.md`
2. `PROJECT_STATE.md`
3. `governance/EDITORIAL_CHARTER.md`
4. `governance/DECISION_REGISTER.md`
5. `governance/ACTIVE_WORKSTREAMS.json`
6. `governance/WORKSTREAM_ASSIGNMENTS.md`
7. `governance/WORKSTREAM_PROTOCOL.md`
8. `governance/COORDINATION_LOG.md` içindeki en son kayıt

- Kanonik durum, kaynak önceliği, release entegrasyonu ve kilitleme yalnız Baş Editör tarafından yürütülür.
- Proje sahibinin açık `kilitle`, `stable yap` veya `release et` talimatı kilit sürecinin zorunlu tetikleyicisidir; tek başına yeterli değildir.
- Simülasyon Testi bağımsız ve zorunlu release kapısıdır. Mekanik, matematik, strateji, sosyal deneyim, görsel kullanılabilirlik, PDF, baskı, manifest ve dosya bütünlüğünü kapsar.
- Açık `FAIL`, `BLOCKER` veya tam candidate commite bağlı olmayan test sonucu varken sürüm kilitlenmez.
- Hikâye, Görsel Tasarım ve Simülasyon Testi başka hattın alanını sessizce değiştirmez; zorunlu handoff biçimini kullanır.
- GitHub'a yazılmış olmak bir çıktıyı kendiliğinden kanon, STABLE veya LOCKED yapmaz.

## Resmî çalışma alanı ve geçici ajan yasağı

- Resmî uzman alanları kullanıcının oluşturduğu `Foulwake Hikâye Editör`,
  `FOULWAKE görsel tasarım` ve `Simülasyon Testi` görünür sohbetleridir.
- Bir iş yalnız ilgili görünür sohbet içinde yapılıp
  `VISIBLE_CHAT_ACK: YES` handoffuyla exact commite bağlandığında o uzman hatta
  mal edilir.
- Geçici alt ajan oluşturmak yasaktır. Çok zorunlu istisna yalnız proje
  sahibinin önceden açık izniyle mümkündür; sonuç `TEMPORARY_SUBAGENT` olarak
  etiketlenir ve uzman sohbet teslimi, onayı veya PASS'i sayılmaz.
- Baş Editör başka görünür sohbetin geçmişine doğrudan mesaj ekleyemez. GitHub
  görev kaydı `PENDING_VISIBLE_CHAT_ACK` iş emridir; kendi başına iletişim veya
  kabul kanıtı değildir.
- Uzman dalları `work/v2.7-story`, `work/v2.7-visual` ve
  `work/v2.7-simulation`; entegrasyon hedefi `v2.7-design`dır. Kanonik durum,
  `main`, release ve kilit yalnız Baş Editör kapsamındadır.

### Güncel görünür sohbet ACK durumu

20 Ağustos 2026 tarihinde proje sahibi üç resmî görünür sohbete ayrı ayrı
salt-okunur iletişim testi iletti. `Foulwake Hikâye Editör`, `FOULWAKE görsel
tasarım` ve `Simülasyon Testi`, kaynak
`v2.7-design@52f6c3b3c196a5af9c48d4694cd3091eb3da8129` için
`VISIBLE_CHAT_ACK: YES` verdi. Baş Editör bu üç cevabı yalnız
`ACKNOWLEDGED_COMMUNICATION_TEST_ONLY` olarak kabul etti.

Bu 3/3 ACK; uzman yeniden doğrulaması, çalışma dalı oluşturulması, dosya
değişikliği, commit, test, PASS, blocker kapanışı veya release teslimi değildir.
Üç uzman dalı ilk yetkili gerçek teslim sırasında oluşturulacaktır. Bağlayıcı
kanıt `governance/VISIBLE_CHAT_ACKS_20260820.json` içindedir ve `COM-001`
gerçek uzman revalidasyonları ile branch-bound teslimler tamamlanana kadar açık
kalır.

## Aktif v2.7 kararları

- **Sea=Rock:** Açık Deniz ve Kayalık v2.7 DRAFT içinde aynı metinsiz binary
  arka yüzü kullanır. Bu, proje sahibinin bağlayıcı taslak kararıdır; yeniden
  sorulmaz veya Görsel Tasarım tarafından ayrı Kayalık arka yüzüne çevrilmez.
- Bu karar v2.6'nın ayrı Kayalık arka yüzünü geriye dönük değiştirmez ve bilgi
  mimarisi farkı nedeniyle exact candidate üzerinde tam Simülasyon ile kör
  fiziksel sızıntı testi geçmeden release olamaz.
- v2.7 Karakter/Güç görünen metni `FOULWAKE_CARD_TEXTS_v2.7.json`; tanımlı
  rulebook anlatı blokları `FOULWAKE_RULEBOOK_STORY_v2.7.md`; ton/lore çiti
  `FOULWAKE_STORY_FRAMEWORK.md` kaynağından alınır.
- Reset öncesi 121/121 üretim tarihsel kanıttır; güncel branch ve exact
  candidate ile bağlanmadan v2.7 release kanıtı değildir.

## Sürüm durumu

- **Son kullanıcı onaylı kilitli stabil sürüm:** `v2.6 STABLE / LOCKED` — `releases/v2.6/`.
- `v2.5` önceki kilitli mekanik baseline ve tarihsel geri dönüş referansıdır.
- Otomatik "en yeni LOCKED/STABLE" çalışma protokolü **v2.6'yı** seçmelidir.
- v2.6 yerinde değiştirilmez; yeni çalışma `v2.7+ DRAFT` olarak açılır.

## Her yeni çalışma oturumunda

1. `AI_HANDOFF.md` ve `PROJECT_STATE.md` dosyalarını oku.
2. `releases/v2.6/README_RELEASE_v2.6.md`, `V26_RELEASE_MANIFEST.json`, `BINARY_ARTIFACTS.md`, `CARD_BASELINE.md`, `V26_RELEASE_VALIDATE_OUTPUT.txt` ve `V26_BLIND_RULEBOOK_AUDIT.md` dosyalarını kontrol et.
3. v2.6 artefaktlarının hashlerini manifestteki değerlerle doğrula.
4. Mekanik motor ayrıntısı gerektiğinde `releases/v2.5/` baseline kayıtlarını kullan.
5. v2.6 üzerinde yerinde değişiklik yapma. Her yeni fikir, kart, kural, hikâye veya fiziksel bileşen değişikliği v2.7+ DRAFT hattında tutulur.
6. v2.7 işi için `working/v2.7/SOURCE_HIERARCHY_v2.7.json`,
   `V27_MECHANIC_DECISIONS.json` ve
   `working/v2.7/qa/RELEASE_BLOCKER_RESOLUTION_PLAN_v2.7.md` dosyalarını kontrol et.

## v2.6 kilitli omurga

- Gemi `SET-KL-01` Kalkış Limanında başlar; `SET-VL-01` Varış/Hedef Limanı üst sıra hedef sütununa hizalanır.
- Kaptan makamı `SET-KP-01` açık yardımcı kartıyla takip edilir.
- İlk gün yalnız Kaptan seçimi; ilk tarafsız gecede Kaptan Sadakatini bilmeden tam 1 yasal Yakın Ufka gizlice bakar.
- Sadakatler ertesi sabah dağıtılır; ilk gerçek rota normal eşzamanlı oylamadır ve Kaptan rota oyu 2 sayar.
- İlk Hain uyanışı Sadakatlerden sonraki ilk yolculuk gecesidir; Hainler birbirini tanır, 1 Yakın Ufka bakar, saldırı yapamaz.
- Başlangıç paketi N-1 gerçek Güç + Çürümüş Erzak; Çürümüş Erzak sahibi sonuçtan sonra 1 gerçek Güç çeker.
- Gövde 2.
- İskorbüt etkinse Liman Gecesinden önce Ada ziyareti zorunludur; Ada girişinde olaydan önce temizlenir.
- Kamusal Harita açmaları açık kalır; ziyaret edilmedikçe olay çözülmez; açık Geçilmez anında engeldir.
- Relocation guard ve Ada çevresi Girdap/Ters Akıntı invariantı korunur.
- Kaderi Yeniden Yaz × Geçilmez hükmü v2.5 mekanik baseline ile aynıdır.
- Kaptan ölür, Kamaraya girer, mahsur kalır, Kayıkçı seferine çıkar veya başarılı İsyanla düşerse hemen yenisi seçilir.
- Hain tablosu: 6:1, 7:2, 8–10:3, 11–13:4, 14–15:5.
- Ana kart seti: 20 Karakter / 30 Güç / 1 Çürümüş Erzak / 15 Sadakat / 52 Harita = 118 ana kart.
- Yardımcı kartlar: Kalkış Limanı + Varış Limanı + Kaptan = 3 kart; toplam 121 basılabilir fiziksel kart.
- Mahkûm için ayrı kart/token yok; Moderatör not alır.
- **Kayalık arka yüzleri KAYALIK kategorisi olarak kalır. Açık Deniz ile aynı arka yüz yapma deneyi v2.6'ya alınmamıştır.**

## Kilitli artefaktlar

- Kural PDF: `/Oyun-GitHub/v2.6/OYUN_Kural_Kitabi_v2.6.pdf`
  - SHA-256: `192f790d89e987a312d6a36879e7b063ee13426c9508b4e474f16f2cad723c2a`
- Kart PDF: `/Oyun-GitHub/v2.6/OYUN_Kartlar_A4_Prototip_v2.6.pdf`
  - SHA-256: `769eaadf989b3d7e4b35ca00d62b0505bcafd7dc61174a11314b607887de9298`
- Full ZIP: `/Oyun-GitHub/OYUN_SIMULASYON_PAKETI_v2.6.zip`
  - SHA-256: `ffc9c17c725e6093c62a3ebddc5f19c36fb0647f6a51a3e7014852fe0623d534`

## Kısa devam komutu

> GitHub'daki Açık Deniz reposunda `v2.7-design` dalını aç. `AI_HANDOFF.md`, `PROJECT_STATE.md`, `governance/EDITORIAL_CHARTER.md` ve `governance/DECISION_REGISTER.md` dosyalarını oku. Son kullanıcı-onaylı kilitli sürüm olarak v2.6 STABLE / LOCKED'u kullan. `governance/ACTIVE_WORKSTREAMS.json` içindeki açık engelleri, görünür sohbet kabul durumunu ve görev sahiplerini kontrol et. Yalnız kendi uzman dalında çalış; v2.6'yı yerinde değiştirme ve görünür sohbet handoffu olmadan işi teslim edilmiş sayma.
