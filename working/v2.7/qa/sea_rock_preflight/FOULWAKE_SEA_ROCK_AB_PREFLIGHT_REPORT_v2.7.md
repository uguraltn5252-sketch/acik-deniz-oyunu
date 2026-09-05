# FOULWAKE — Deniz/Kayalık A/B ön testi

**RESULT: INCONCLUSIVE / HUMAN_PLAYTEST_REQUIRED**

Ortak arka yüzün hangi bilgiyi kaldırdığı doğrulandı. Hangi tasarımın bütün
oyun için daha iyi olduğu belirlenemedi. Paket erişilebilir ve hashleri doğru;
motorun iki davranışı tam oyun karşılaştırmasını engelliyor. MEC-001 OPEN.

## Yetki ve yeniden üretim

- TASK_ID: `MEC-SEA-ROCK-PREFLIGHT-001`; rol: SIMULATION_QA; dal: `work/v2.7-simulation`.
- SOURCE_HEAD: `dba2dff0b9ec7c1f3361630da41d5f31c232e029`.
- Görev kaynak commit'i: `9779f6bb05504a01ca9817bcb8d20fc407efe657`.
- Çalışma başlangıcı: `75763ab1736733f41eff40618a36a82c8a172909`; v2.6 tree: `efb41c46f06174c42dcdab2859b7c0ba517f86f0`.
- Paket: `/Oyun-GitHub/OYUN_SIMULASYON_PAKETI_v2.6.zip`.
- v2.6 ZIP SHA-256: `ffc9c17c725e6093c62a3ebddc5f19c36fb0647f6a51a3e7014852fe0623d534`.
- İç v2.5 ZIP SHA-256: `975dd77d435a835fcf3faa864c5624b0542fadb419fa7d34217ed32fe87aa046`.
- İç manifestin 44 üyesi byte düzeyinde doğrulandı.
- Repo/paket v2.5 delta dosyaları farklı JSON biçimindedir; nesne içerikleri
  birebir eşittir. İki ayrı byte hash'i RESULTS içinde korunur.
- Çalıştırıcı SHA-256: `541e371cd98c750ce2b612acaa415f35c685f1ebf280d1873e0ee08c188c4827`.
- RESULTS SHA-256: `d60cb046618536b59b4e53cea5495119a6b43e103c99d23fdbf1c5dd881dcd5a`.
- Ortam: CPython 3.12.13; Linux; yalnız standart kütüphane.
- Seed: 20260905; her oyuncu/süre hücresinde 32 kurulum.

```bash
python -B working/v2.7/qa/sea_rock_preflight/FOULWAKE_SEA_ROCK_AB_PREFLIGHT_v2.7.py --package /absolute/path/OYUN_SIMULASYON_PAKETI_v2.6.zip --authority dba2dff0b9ec7c1f3361630da41d5f31c232e029 --seed 20260905 --samples-per-cell 32
```

`--check` eklendiğinde dosyaları değiştirmeden kayıtlı hesap ve rapor bütünlüğü
doğrulanır; farklı ortam bilgisi ayrı bildirilir. Paket yeniden indirilirse
manifest hash'i zorunludur. Yeni kaynak/candidate için bu sonuç devralınmaz.
Teslim commit'i bu üç dosyayı taşıyan Git commit'idir; handoff exact commit ve
blobları verir. Bu rapor kabul/kapanış kaydı değildir.

| Girdi | Beklenen Git blob |
|---|---|
| `releases/v2.6/CARD_BASELINE.md` | `40e9a2cda56c484d88b976941a4a80d46507bc5b` |
| `releases/v2.6/V26_RELEASE_MANIFEST.json` | `11377990fbbe2cc156b954e801cb0bad535c1155` |
| `releases/v2.6/SOURCE_PACKAGE.md` | `0470dfba2a82c0c4bb297d23eb356bb5b843c99a` |
| `releases/v2.5/OYUN_SIMULASYON_SPEC_v2.5.delta.json` | `d89fb57e298a943f6db6b548a1fd524747ee4c01` |
| `working/v2.7/V27_MECHANIC_DECISIONS.json` | `8551f63339fc3b5645330ea2e6d1941d19aa2840` |

## Kontrollü A/B bulgusu

A, kilitli v2.6 Deniz ve Kayalık kategori arka yüzlerini ayırır. B, yalnız
`DEC-20260820-01` gereğince bunları BACK_SEA_ROCK altında birleştirir. Ada ve
Fener ayrı kalır. Envanter 30 Deniz, 12 Kayalık, 6 Ada, 4 Fener; Geçilmezler
HAR-KY-01/HAR-KY-03'tür. Kapalı Geçilmezler A'da da diğer Kayalıklardan
ayırt edilemez. Görülmüş ön yüz bilgisi her iki modelde korunur.

52 kimlikten eşit olasılıkla tek kart seçilen ideal etiket modelinde B,
0.697136 bit kategori bilgisini
kaldırır. Arka yüzden ayırt edilemeyen kimlik çiftleri
522 → 882
olur; ek 360 çift tam olarak 30×12 Deniz/Kayalık
çiftidir. Bu, basılı arka yüzün fiziksel sızıntı testi değildir.

6–15 oyuncu × üç süre üzerinden 960 geçerli açılış üretildi;
aynı board/seed üzerinde iki görünürlük modeli uygulandı. Bütün kurulumlar
spec'ten ayrı yazılmış kota, komşuluk ve Ada→Liman yol denetimlerini geçti.
409 açılışta ilk Ufukta hem Deniz hem
Kayalık vardı. Sıradan oyuncu için toplam
601 aday çifti arasındaki
kategori ayrımı silindi; Kaptanın başlangıç bakışı korunduğunda bu sayı
175. Bunlar kurulum örnekleminin
betimidir; insan oyunu frekansı veya kazanma oranı değildir. JSON, her örneğin
seed'ini, kimlikli haritasını, limanlarını, bakışını ve iki gözlemini içerir.

## Tek amaçlı, konumsuz risk örneği

Aşağıdaki ayrı sonlu deneyde kurulumun yalnız Deniz/Kayalık havuzundan iki
farklı kart eşit olasılıkla çekilir. Amaç sadece Geçilmez seçmemektir. A,
görüyorsa Deniz'i seçer; eşit görünen seçeneklerde iki model de ilk konumu
seçer. Bütün sıralı çiftler tüketilmiştir; örnekleme hatası yoktur.

| Kota kaynağı | Deniz / Kayalık / Geçilmez | A: Geçilmez seçimi | B: Geçilmez seçimi |
|---|---:|---:|---:|
| 5x5 | 15 / 6 / 1 | 1.190% | 4.762% |
| 5x6 | 18 / 7 / 1 | 1.000% | 4.000% |
| 5x7 | 21 / 8 / 2 | 1.724% | 6.897% |
| 6x5 | 18 / 7 / 1 | 1.000% | 4.000% |
| 6x6 | 21 / 8 / 2 | 1.724% | 6.897% |
| 6x7 | 25 / 10 / 2 | 1.513% | 5.714% |

Bu tablo **yasal ilk Ufuk riski değildir**: konum, son satır yasağı, Ada
komşuluğu, kurulum elemesi, özel bilgi, oylar ve geri dönüş dışarıdadır.
Kapalı kartlar için tek tek bağımsız zar gibi yorumlanamaz. A'nın bu dar
amaçtaki avantajı ortak arka yüzün oyuna uygun olmadığını kanıtlamaz; B'nin
artan bilgi ihtiyacı da daha eğlenceli olduğunu kanıtlamaz.

## Motor bulguları — tam oyun kanıt kapısı FAIL

1. **PREFLIGHT-ENGINE-01 / gizli bilgi erişimi.**
   `AuditGame._make_claims`, bilgisiz Hainin blöf hedefini `true_worst`
   üzerinden seçer. Seed 0, dengeli persona; iki adayın arkasında da Deniz
   vardır, kişisel/takım/kamusal bilgi boştur. HAR-AD-01/HAR-AD-11 yer
   değiştirince iddia hedefi (0,1) → (0,0) değişir; iki kayıtta da
   `informed=false`. Gözlem ve RNG aynı kaldığı halde karar gizli ön yüze
   bağlıdır. JSON iki dünya ve iddiaları saklar. Bu iki adaylı birim örneği
   tam kurulum değildir; karar yordamının bilgi sınırını sınar.
2. **PREFLIGHT-ENGINE-02 / ilk rota bilgi penceresi.**
   Gerçek kanonik kurulum: 10 oyuncu, kısa oyun, seed 3. Kaptan 7;
   Tayfa oyuncusu 4, ilk hareket öncesinde Kırık Dürbün tüketip (0,1)'i
   öğrenir. Gün 1, gemi hâlâ (-1,2)'dedir. Paket kural kitabı §11.3,
   ilk rota öncesi isteğe bağlı bilgi güçlerini yasaklar. `run` gerçek bilgi
   yordamını çalıştırır; test yalnız ilk `move_once` çağrısında durdurur.
   Açılış bilgi avantajı bu nedenle baseline sözleşmesini karşılamaz.

Kaynak motor değiştirilmedi. Bu bulgular düzeltilmeden yalnız kategori
ortalamalarını birleştiren bir A/B yaması geçerli denge kanıtı olmaz.
`look_for_player`, `look_for_hains`, `perceived_value` ve ek hareket kararları
da gerçek kategoriye erişir; B için bütün karar girdilerinin görünür bilgi
sınırından geçirilmesi bağımsız yeni motor görevinin kapsamı olmalıdır.

## Sınırlar ve teslim

- Tamamlanmış oyun: **0**. Yapılanlar: matematiksel bilgi modeli, sonlu
  iki-seçenek deneyi, eşleştirilmiş açılış gözlemleri ve motor tekrar testleri.
- İnsan eğlencesi, güven, şüphe, tempo ve denge hakkında PASS verilmedi.
  Kabul eşiği veya insan verisi uydurulmadı.
- Sonraki açık işler: iki motor bulgusu, gözleme bağlı A/B motoru, tam
  simülasyon, kör insan testi ve fiziksel bilgi sızıntısı/baskı proof'u.
- MEC-001 OPEN. Üretim/PDF/release/lock izinleri false; v2.6 değişmedi.
- Yalnız görevdeki üç QA çıktısı teslim edilir. CHIEF_EDITOR exact commit
  ve blobları bağımsız inceleyip kabul/kapanış kaydını yönetir.
