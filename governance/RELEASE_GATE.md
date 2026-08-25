# FOULWAKE Release ve Kilitleme Kapısı

## Sonuç sınıfları

| Sonuç | Anlamı | Kilit |
|---|---|---|
| `PASS` | Bütün zorunlu kontroller geçti | Değerlendirilebilir |
| `PASS_WITH_MINOR_ISSUES` | Kanon/mekanik/kullanılabilirliği bozmayan kayıtlı küçük sorunlar | Baş Editör değerlendirebilir |
| `FAIL` | Bir veya daha fazla kapı geçmedi | Yasak |
| `BLOCKER` | Yanlış kaynak, mekanik drift, reddedilmiş/eksik temel artefakt, bilgi sızıntısı veya ciddi çakışma | Derhal durur |

## Zorunlu kapılar

### 1. Kaynak ve sürüm bütünlüğü

- Son `STABLE / LOCKED` baseline ve exact candidate commit doğru mu?
- `releases/v2.6/**` değişmedi mi?
- Kimlik/adet/effect/zamanlama/deste davranışı/kural akışı kaynaklarla aynı mı?
- `SRC-002` GUC-22/GUC-23 çelişkisi exact kaynakla çözüldü mü?
- İç ve dış manifest, ZIP self-provenance, blob, SHA-256, boyut ve yol kayıtları
  aynı candidate'ı mı gösteriyor?

### 2. Mekanik, matematik ve strateji

- 6–15 oyuncu, bütün harita şekli ve süreler test edildi mi?
- Illegal durum, kilitlenme, sonsuz döngü, zorunlu kayıp veya baskın/sahte
  strateji var mı?
- Sea=Rock bilgi modeli A/B ve yetkili/yetkisiz bilgi sözleşmesini koruyor mu?

### 3. Sosyal deneyim

- Şüphe/güven anlamlı bilgiye dayanıyor mu?
- Bekleme, susma, elenme, sıkılma, adalet, kingmaking ve moderatör yükü
  ölçüldü mü?
- Kör yeni oyuncu testleri ve öğretilebilirlik kanıtı var mı?

### 4. Görsel sanat ve semantik özgünlük

- Proje sahibinin reddettiği eski ön/arka yüz, aile plakası veya türevi yeniden
  kullanılmış mı? Kullanıldıysa `BLOCKER`.
- 121 kartın ayrı art briefi ve semantik olarak ayrı özgün sahnesi var mı?
- KAPTAN referansı yalnız STYLE_ONLY mı; yüz/poz/kompozisyon kopyası yok mu?
- Başlık ve metin kapalı contact sheetlerde aynı yüz, saç/sakal, beden, poz,
  kadraj, sahne, siluet, hayvan veya şaka tekrarı var mı?
- `unique render SHA` yalnız dosya farkı olarak mı yorumlanmış?
- İllüstrasyonda tabela, slogan, konuşma balonu, açıklama veya anlamsız
  okunabilir resim-içi yazı var mı? Varsa `BLOCKER`.
- Mizah en fazla bir ikincil şaka mı; aynı maskot/şaka kalıbı tekrar ediyor mu?
- Çizgi, tarama, mat palet ve eski baskı dili bütün destede tutarlı mı?

### 5. Kart arka yüzleri ve bilgi sızıntısı

- Exact mapping `20+31+15+42+6+4+3 = 121` ve 7 binary mi?
- Aile içi binaryler byte/piksel olarak aynı mı?
- Sea+Rock ve Sadakat gizli bilgiyi sızdırmıyor mu?
- Bütün arka yüzler metinsiz ve exact 180° yön güvenli mi?
- Kesim, kenar koyuluğu, parlaklık, opaklık ve duplex sapması aile/yön
  sınıflandırmasına izin veriyor mu?
- Arka yüzler önlerle aynı sanat dilinde fakat ön yüz kopyası olmadan mı üretildi?

### 6. Metin, düzen ve erişilebilirlik

- Exact başlık/effect/flavor/kimlik kaynağı kelimesi kelimesine korunmuş mu?
- Eksik glif, overflow, kesilen metin, aşırı küçültme veya düşük kontrast var mı?
- İllüstrasyon mekanik metni bastırıyor mu?
- Gerçek kart ölçüsünde ve gerçek ışıkta okunabilirlik eşiği geçildi mi?

### 7. PDF, baskı ve artefakt

- 121/121 source→render→PDF ön/arka sayfa/slot zinciri var mı?
- Ölçü, 300 dpi, 3 mm taşma, font, glif, sayfa, XObject ve duplex doğru mu?
- Fiziksel baskı/kesim/duplex/opaklık/ışık kanıtı var mı?
- Kaynak ZIP iç ve dış manifestleri exact aynı final commit/hashleri mi taşıyor?

## Kilitleme sırası

1. Hikâye ve Görsel handoffları kabul edilir.
2. Baş Editör kaynak, kapsam, sanat ve kanon denetimi yapar.
3. Exact ürün candidate commit'i dondurulur.
4. Simülasyon Testi bütün kapıları aynı candidate üzerinde uygular.
5. FAIL/BLOCKER düzeltilir; yeni candidate oluşursa önceki sonuçlar iptal edilir.
6. Fiziksel ve kör insan kanıtları tamamlanır.
7. Proje sahibi açık kilitleme talimatı verir.
8. Baş Editör attestation, manifest, checksum ve açık blocker listesini doğrular.
9. Yalnız bundan sonra release ve kanonik durum güncellenir.

## Bağlayıcı attestation

Release kapısında yalnız exact candidate'a bağlı
`working/v2.7/qa/SIM_QA_ATTESTATION_v2.7.json` ve hashli kanıt paketi
bağlayıcıdır. En az kimlik/mekanik, matematik, strateji, sosyal deneyim,
semantik sanat, arka-yüz/bilgi sızıntısı, metin/düzen, paket/provenance,
fiziksel kanıt ve açık sorun hükümlerini içerir.

Eski candidate'ın PASS kaydı yeni candidate'a taşınmaz. GitHub'a yazılmış olmak,
farklı SHA üretmek veya yalnız dijital preflight geçmek release PASS'i değildir.
