# FOULWAKE GitHub Baş Editör Denetimi — 25 Ağustos 2026

**Kapsam:** aktif dallar, yönetişim kayıtları, v2.7 kaynak sözleşmesi, Görsel
teslim, QA/release kapıları ve GitHub koruma dosyaları  
**Hüküm:** **BLOCKER / DÜZELTME UYGULANDI / RELEASE VE KİLİT YOK**  
**Kilitli baseline:** `v2.6 STABLE / LOCKED` — değiştirilmedi

## 1. Doğrulanan dal durumu

| Dal | Denetlenen head | Hüküm |
|---|---|---|
| `main` | `b2e0c9c92811ae34a96fec0bc4ef71a69e95d057` | Varsayılan dal; aktif v2.7 entegrasyon dalıyla ayrışmış |
| `v2.7-design` | `fb73852d76c45977a0ed3bcf0af8cae68f813fb0` | Bu denetimin başlangıç parent'ı |
| `work/v2.7-story` | `e04eef7f1fef6ea407feaaf26558551297c44b37` | Hikâye teslimi Baş Editörce kabul edilmiş |
| `work/v2.7-visual` | `e91581bb336dfcbab5da1d48a256577f9251f891` | Teknik teslim var; sanat reddedildi |
| `work/v2.7-simulation` | yok | Yetkili Simülasyon çalışması başlamadı |

`main...v2.7-design` karşılaştırması denetim başında `diverged`, tasarım dalı
50 commit ileride ve 2 commit gerideydi. İki dal da korumasızdı; repository
ruleset veya required status check uygulanmıyordu.

## 2. Kritik bulgular

### A. Yönetim gerçeği eskiydi — düzeltildi

`AI_HANDOFF.md`, `PROJECT_STATE.md`, `ACTIVE_WORKSTREAMS.json`, görev kaydı ve
doğrulayıcı Görsel teslimini hâlâ “bekleniyor” gösteriyordu. Oysa görünür
Görsel sohbet `e91581...` exact head ile teslim vermişti. Kayıt artık teslimi
gerçek olarak tanıyor; Baş Editör dispozisyonu
`REJECTED_ART_REWORK_REQUIRED`dır.

### B. Teknik farklılık, sanatsal özgünlük sanılmıştı — düzeltildi

Görsel preflight 121 farklı ön-yüz hashini başarı olarak sayarken kaynak paketi
yalnız altı aile illüstrasyon plakası içeriyordu. Bu, dosyaların farklı olduğunu
kanıtlar; 121 ayrı sahne veya insan olduğunu kanıtlamaz. Yeni kapı, kör contact
sheet ve insan tarafından semantik tekrar incelemesi olmadan `ART-001`i
kapatmaz.

### C. Bütün ön ve arka yüzler reddedildi — düzeltildi

Önceki belgelerde “onaylı sanat yönü örneği” veya “full visual digital
candidate” denen görseller artık yalnız `REJECTED_ART / TECHNICAL_PIPELINE_REFERENCE_ONLY`
sınıfındadır. Hiçbiri yeni adaya kopyalanamaz, dönüştürülemez veya temel plaka
olarak kullanılamaz.

### D. Arka yüz sözleşmesi eksikti — düzeltildi

Eski sistem yalnız Sea=Rock ile Ada/Deniz Feneri hakkında kısmi hüküm veriyordu.
Yeni bağlayıcı topoloji 7 binary arka yüz ve 121 eşlemeyi açıkça kaydeder:
Karakter 20; Güç+Çürümüş 31; Sadakat 15; Deniz+Kayalık 42; Ada 6; Deniz Feneri
4; yardımcı 3. Hepsi metinsiz, aile içinde exact aynı ve 180° yön güvenlidir.

### E. İllüstrasyon içi anlamsız yazı kapısı yoktu — düzeltildi

Yeni direktif tabela, pankart, isimlik, konuşma balonu, slogan ve okunabilir
dekor yazısını bütün kart ailelerinde yasaklar. Okunabilir metin yalnız şablonun
bağlayıcı başlık/effect/flavor/kimlik alanlarında bulunabilir.

### F. Provenance kayıtlarında iki tutarsızlık — açık blocker

- Preflight `font_table_has_embedded_dejavu=false` derken materialize edilen
  baskı PDF incelemesi gömülü DejaVu kaydı buldu.
- Kaynak ZIP içindeki self-provenance/final-commit alanları dış nihai kayıtla
  aynı sürümde değildir.

Eski aday reddedildiği için bu paket onarılıp yeniden aday yapılmayacak. Yeni
sanat üretiminde gömülü ve dış manifestler aynı exact candidate için sıfırdan
oluşturulacak.

### G. Sea/Rock yön güvenliği kanıtı yok — açık blocker

Eski teslim diğer altı arka yüzü simetrik ilan etmiş; `BACK_SEA_ROCK` için aynı
hükmü vermemiştir. Önceki piksel incelemesi de exact 180° simetriyi
doğrulamamıştır. Yeni binary sıfırdan üretilecek ve dijital + kör fiziksel test
geçecektir.

### H. Güç kartı kimlik kaynağı çelişkili — yeni `SRC-002`

Kilitli v2.6 `CARD_BASELINE.md` ve `CHANGELOG.md`, Bayat Peksimet'i `GUC-22`
olarak kaydeder. Aktif v2.7 Card Texts ise `GUC-22 = Kaptanın Çatlak Kupası`,
`GUC-23 = Bayat Peksimet` der; aynı zamanda anlatı doğrulama kaydı Güç
kimlik/effect alanlarının baseline ile aynı olduğunu iddia eder. GitHub'da bu
iddianın yeniden üretilebilir sabit baseline/script kanıtı yoktur.

Baş Editör mekanik kimliği tahmin ederek değiştirmedi. `SRC-002`, kilitli v2.6
kart PDF/source paketinden exact kimlik/effect tablosu çıkarılıp v2.7 kaynağıyla
karşılaştırılana veya proje sahibi açık karar verene kadar BLOCKERdır.

### I. GitHub kilidi dosya düzeyinde, platform düzeyinde zorunlu değil — açık blocker

`CODEOWNERS` ve CI dosyaları var fakat branch protection/ruleset yoktur. Bu
nedenle “yalnız Baş Editör kilitler” kuralı GitHub ayarlarında teknik olarak
zorunlu değildir. Workflow kapsam kontrolleri güçlendirildi; gerçek merge/push
zorlaması için repository branch protection/ruleset ayrıca etkinleştirilmelidir.
Bu denetim kullanıcıyı yanlışlıkla kilitlememek için repository ayarlarını
değiştirmedi.

## 3. Uygulanan dosya düzeltmeleri

- Kanonik durum ve handoff kayıtları güncellendi.
- Kabul edilmiş Hikâye tesliminin exact üç değişen blobu `v2.7-design`a entegre edildi.
- Görsel teslim için exact commitli kanıt ve Baş Editör ret dispozisyonu eklendi.
- Tam deste rework direktifi ve 7 arka-yüz topolojisi eklendi.
- Eski binary/PDF kayıtları reddedilmiş teknik referans olarak ayrıldı.
- Görsel sistem; KAPTAN style-only yönü, 121 özgün sahne, resim-içi yazı yasağı,
  mizah sınırı ve pilot kapısıyla yeniden yazıldı.
- QA/release kapılarına semantik sanat, contact sheet, arka-yüz sızıntısı ve
  provenance tutarlılığı eklendi.
- Doğrulama betiğinin eski Görsel “pending” hükmü kaldırıldı; yeni durumu ve
  dosyalar arası sözleşmeleri doğrulayacak biçimde güncellendi.
- PR şablonu ve workflow, uzman dalı kapsam ihlali ile kilitli v2.6 değişikliğini
  daha görünür biçimde reddedecek şekilde güçlendirildi.

## 4. Değiştirilmeyen alanlar

- `releases/**`, özellikle `releases/v2.6/**`
- `main`
- Hikâye ve mekanik içerik alanları
- `work/v2.7-story` ve `work/v2.7-visual` uzman dalları
- STABLE / LOCKED etiketleri ve release artefaktları

## 5. Sonraki zorunlu sıra

1. Proje sahibi bu Baş Editör düzeltme commitini Görsel Tasarım sohbetine verir.
2. Görsel Tasarım 121 brief + 12 ön-yüz pilotu + 7 arka-yüz taslağı üretir.
3. Kullanıcı ve Baş Editör pilotu açıkça kabul etmeden tam desteye geçilmez.
4. `SRC-002` exact kaynak karşılaştırmasıyla çözülür.
5. Yeni tam aday teknik, semantik ve fiziksel kapılardan geçer.
6. Yalnız bundan sonra Simülasyon Testi exact candidate üzerinde başlar.
