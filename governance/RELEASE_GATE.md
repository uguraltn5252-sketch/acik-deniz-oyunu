# FOULWAKE Release ve Kilitleme Kapısı

## Önkoşul

`governance/CURRENT_STAGE.json` içinde active candidate `null` ise release
değerlendirmesi başlamaz. Tarihsel PASS, Görsel handoffu, benzersiz hash veya
GitHub commiti candidate değildir.

| Sonuç | Anlam | Release/lock |
|---|---|---|
| `PASS` | Bütün zorunlu gate'ler aynı exact candidate üzerinde geçti | Proje sahibi kilit talimatı verirse değerlendirilebilir |
| `PASS_WITH_MINOR_ISSUES` | Kanon/mekanik/kullanılabilirliği bozmayan kayıtlı küçük sorun | Baş Editör ve proje sahibi değerlendirmesi gerekir |
| `FAIL` | En az bir gate geçmedi | Yasak |
| `BLOCKER` | Kaynak, mekanik, sanat, bilgi sızıntısı, fiziksel kanıt veya governance sorunu | Derhal durur |

## 1. Kaynak ve governance

- Exact candidate ve Baş Editör kabul commiti var mı?
- `releases/v2.6` tree SHA
  `efb41c46f06174c42dcdab2859b7c0ba517f86f0` olarak korunuyor mu?
- `SRC-002` proje sahibi kararıyla kapandı mı?
- Specialist değişiklikleri yetkili baseline, exact path ve kapsam içinde mi?
- Güncel stage ile handoffun `AUTHORIZATION_STAGE` alanı eşleşiyor mu?
- Açık blocker veya superseded iş emri aktif kaynak gibi kullanılmış mı?

## 2. Kimlik, mekanik ve exact copy

- 121 kimlik/adet/aile ve `20+31+15+42+6+4+3` back mapping exact mı?
- Title, section label, effect, flavor, zamanlama, group ve davranış doğru
  kanonik kaynaktan mı?
- `SET-KP-01` görünen başlık `KAPTAN` ve exact owner copy mi?
- Görsel model kart yazısı üretmemiş mi?
- Her front için OCR veya render-source → kanonik UTF-8 exact karşılaştırması
  var mı?
- Tek uyuşmazlık `BLOCKED_COPY_DRIFT` olarak ele alındı mı?

## 3. Sanat ve semantik özgünlük

- KAPTAN kartı yüklenen ana figür/kompozisyonu koruyor mu; boş sandalye veya
  başka figürle değiştirilmiş mi?
- Deste, KAPTANın mürekkep/gravür/kirli kâğıt/mat palet dilini taşıyor mu?
- Gemi/martı/sahne yanlışlıkla deste genelinde zorunlu motif yapılmış mı?
- Reddedilmiş asset, aile plakası veya türevi yeniden kullanılmış mı?
- 121 ayrı brief ve semantik olarak ayrı sahne insan gözüyle doğrulanmış mı?
- Resim-içi anlamsız yazı, dönem dışı nesne, tekrarlı yüz/poz/hayvan/şaka var mı?
- `unique render SHA` yalnız dosya farkı olarak mı yorumlanmış?

## 4. Kadraj

Her front ve back için bağımsız Sanat Yönetimi kanıtı gerekir:

- exact kart oranı ve illüstrasyon penceresi;
- 3 mm taşma, 4–5 mm güvenli alan;
- ana özne ölçeği, odak, denge, negatif alan;
- yüz/el/gerekli nesnede anlamsız kesim;
- title/effect/flavor/card-id çakışması;
- thumbnail ve normal masa-mesafesi okunurluğu;
- plan/model/kadraj çeşitliliği.

Yalnız `FRAMING_PASS` veya `REFRAME_REQUIRED` kabul edilir. Görsel Tasarımın
self-PASS'i geçersizdir. Her eksik/başarısız kayıt `BLOCKED_FRAMING_DRIFT`tir.

## 5. Arka yüzler ve bilgi sızıntısı

- Yedi binary ve 121 eşleme exact mı?
- Aile içinde binaryler byte/piksel aynı ve exact 180° güvenli mi?
- Kesim, kenar, değer, parlaklık, opaklık ve duplex yön/aile bilgisi sızdırıyor mu?
- `BACK_SEA_ROCK` mat mı; krom/specular, beyaz parlama veya AI cilası var mı?
- `BACK_ISLAND` önceki reddedilmiş adadan türetilmeden tam yeniden çizilmiş mi?
- `BACK_LIGHTHOUSE` normal mesafede büyük ve okunur mu; uzun kayalık sırt
  zorunlu kompozisyon dayanağı yapılmış mı?
- Aile bilgisi görünürken exact ön kimlik ve sonuç kör mü?

## 6. Mekanik, strateji ve sosyal deneyim

- 6–15 oyuncu, bütün yasal harita şekilleri ve süreler test edildi mi?
- Illegal durum, kilitlenme, sonsuz döngü, zorunlu kayıp veya baskın strateji var mı?
- Sea=Rock bilgi modeli yetkili/yetkisiz bilgiyi ve A/B karşılaştırmasını koruyor mu?
- Şüphe, bekleme, susma, elenme, adalet, kingmaking, moderatör yükü,
  öğretilebilirlik ve kör yeni oyuncu testi ölçüldü mü?

## 7. PDF, baskı ve provenance

- 121/121 source→render→PDF slot zinciri exact mı?
- Ölçü, 300 dpi, 3 mm taşma, font/glif, sayfa, duplex ve imposition doğru mu?
- Source, render, sheet, layout, PDF ve dış paket hashleri aynı candidate'a mı bağlı?
- Gerçek baskı, kesim, duplex, opaklık, ışık ve masa-mesafesi kanıtı var mı?
- Tools/plugins beyanı ve yeniden üretilebilir komut/seed kaydı tamam mı?

## 8. Zorunlu sıra

1. Sanat yönü + proje sahibi yön kabulü.
2. Yetkili küçük görsel kapılar.
3. Copy ve kadraj PASS.
4. Baş Editör exact candidate ilanı.
5. Data Analytics tabanlı bağımsız Simülasyon ve QA attestation.
6. Fiziksel/kör insan kanıtı.
7. Bütün blockerların kapanışı.
8. Proje sahibinin açık kilitleme talimatı.
9. Baş Editör release/lock uygulaması.

Eski candidate attestationı yeni commite taşınmaz. Release kanıtı exact
`working/v2.7/qa/SIM_QA_ATTESTATION_v2.7.json` ve ona bağlı hashli pakettir.
