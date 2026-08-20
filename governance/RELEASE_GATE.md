# FOULWAKE Release ve Kilitleme Kapısı

## Sonuç sınıfları

| Sonuç | Anlamı | Kilit durumu |
|---|---|---|
| PASS | Zorunlu kontroller geçti | Değerlendirilebilir |
| PASS WITH MINOR ISSUES | Kanonu, mekaniği veya kullanılabilirliği bozmayan kayıtlı küçük sorunlar | Baş Editör kararıyla değerlendirilebilir |
| FAIL | Bir veya daha fazla zorunlu kapı geçmedi | Kilitlenemez |
| BLOCKER | Yanlış baseline, kilitli dosya değişikliği, mekanik drift, eksik temel artefakt veya ciddi çakışma | Derhal durur |

## Zorunlu test katmanları

### 1. Kaynak ve sürüm bütünlüğü

- Doğru STABLE / LOCKED baseline kullanıldı mı?
- Kilitli release klasöründe değişiklik var mı?
- Aktif branch ve commit açık mı?
- Manifest, checksum ve dosya yolları uyumlu mu?

### 2. Mekanik ve kart bütünlüğü

- Kart sayıları ve benzersiz kimlikler doğru mu?
- Etki, zamanlama, deste davranışı ve başlangıç havuzu korunuyor mu?
- Kural kitabı, kart kaynağı, JSON ve simülasyon kodu aynı hükmü veriyor mu?
- Rota, Ufuk, Liman, İskorbüt, Kaptan, Hain, kurtarma ve Gövde akışlarında çelişki var mı?

### 3. Matematik ve strateji

- 6–15 oyuncu aralığı ve ilgili Hain dağılımları test edildi mi?
- Kilitlenme, sonsuz döngü, zorunlu kayıp veya anlamsız karar oluşuyor mu?
- Stratejilerden biri baskın veya sahte seçenek hâline geliyor mu?
- Kazanma oranı kadar karar kalitesi ve varyans da incelendi mi?

### 4. Sosyal ve oyuncu deneyimi

- Şüphe ve güven anlamlı bilgi üzerinden oluşuyor mu?
- Oyuncu bekleme/susma/erken elenme süresi kabul edilebilir mi?
- Haksızlık, sıkılma, kingmaking veya bilgi tekeli riski var mı?
- Moderatör yükü ve öğretilebilirlik ölçüldü mü?

### 5. Görsel kullanılabilirlik

- Başlık ve mekanik metin gerçek kart ölçüsünde okunuyor mu?
- Kart aileleri, makam/destek, gizli/açık bilgi ve arka yüzler doğru ayrılıyor mu?
- İllüstrasyon mekanik alanı bastırıyor mu?
- Mizah aynı evrene ait, kontrollü ve tekrarsız mı?
- Renk, kontrast, ikon ve masa üstü tanınabilirliği yeterli mi?

### 6. PDF, baskı ve artefakt

- Kaynak ile PDF metni birebir uyumlu mu?
- Sayfa sayısı, kart sayısı, kesim, taşma, font ve glif kontrolü geçti mi?
- Çift taraf hizası ve arka yüz eşleşmesi doğru mu?
- Print-ready iddiası varsa fiziksel baskı/kesim/duplex/gerçek ışık provası yapıldı mı?

## Kilitleme sırası

1. Çalışma hatları handofflarını tamamlar.
2. Baş Editör kapsam ve kanon denetimi yapar.
3. Simülasyon Testi bağımsız tam sistem raporunu üretir.
4. FAIL/BLOCKER düzeltilir ve yeniden test edilir.
5. Release candidate commit’i dondurulur.
6. Proje sahibi açık kilitleme talimatı verir.
7. Baş Editör kilit tutanağı, manifest ve checksumları doğrular.
8. Kanonik durum dosyaları güncellenir ve yeni release yayımlanır.

Kilit sonrası aynı sürüm yerinde değiştirilmez.

## Bağlayıcı Simülasyon QA kanıtı

Release kapısında yalnız exact candidate commite bağlı
`SIM_QA_ATTESTATION_vX.Y.json` ve onun hashli kanıt paketi bağlayıcıdır. En az şu
alanlar bulunur:

- candidate ve baseline commit SHA'ları
- validator ve test motoru hashleri
- çalıştırılan komutlar, seed'ler ve örneklem sayıları
- ham test çıktılarının hashleri
- kaynak → render → PDF izlenebilirliği
- kart, PDF ve ZIP manifestleri
- fiziksel prova ve kör insan testi kayıtları
- açık sorunlar ve en yüksek şiddete göre genel hüküm

Eski sürümlerin PASS kayıtları yalnız baseline kanıtıdır. Tek bir validator,
Monte Carlo sonucu veya sonuç belgesindeki `PASS` satırı genel v2.7 PASS'i değildir.
Candidate commit değişirse önceki attestation otomatik olarak geçersizleşir.

## Taslak kanon kuralı

`DRAFT / NOT LOCKED` bir dosyanın içindeki `KANON` etiketi tek başına release
kanonu oluşturmaz. Yeni veya izlenemeyen kanon maddeleri ya taslak kısıt olarak
sınıflandırılır ya da proje sahibinin açık kararıyla Baş Editör kaydına alınır.
