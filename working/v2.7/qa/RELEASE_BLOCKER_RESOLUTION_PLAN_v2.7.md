# FOULWAKE v2.7 Release Blocker Çözüm Planı

**Durum:** ACTIVE QA PLAN / CURRENT VERDICT BLOCKER  
**Kaynak:** `v2.7-design@af064df83ac4132c7d8d75aec67a3f1b51150fdb`  
**Baseline:** v2.6 STABLE / LOCKED; mekanik motor v2.5

Sea=Rock ortak arka yüz kararı v2.7 DRAFT için bağlayıcıdır ve yeniden açılmaz.
Bu karar v2.6'nın ayrı arka yüz modelinden bilinçli bir bilgi-mimarisi farkıdır;
tam yeniden test bitmeden `MEC-001` kapanmaz.

## Candidate ve kontrol modeli

Tam ürün commit'i `C` olarak dondurulur.

- **A kontrolü:** `C` ile aynı kart, metin ve görseller; yalnız v2.6 ayrı Deniz/Kayalık bilgi modeli.
- **B adayı:** `C` ile aynı kaynaklar; v2.7 ortak Sea=Rock arka yüz modeli.

Böylece yalnız bilgi mimarisi ölçülür; hikâye ve sanat farkları deneyi kirletmez.

## Mekanik ve gizli bilgi kapısı

- Geometri sonucu: `51.204 teorik / 51.102 yasal / 102 reddedilen` değişmemeli.
- Bütün 6–15 oyuncu sayıları, altı harita şekli ve kısa/standart/uzun süreler test edilir.
- Yetkisiz oyuncuya kapalı kartın Deniz/Kayalık kategorisi sızıntısı: `0`.
- Yetkili Ufuk bakışı, kamusal açma ve Geçilmez davranışında yanlış bilgi: `0`.
- En az `1.000.000` stateful fuzz eylemi; motor/invariant hatası ve kalıcı rota kilidi: `0`.
- Birden fazla rota varken hiç kimsede rota-relevant bilgi olmayan salt tahmin kararları: en fazla `%40`.

## Sayısal ve stratejik paired A/B

Ana deney: 10 oyuncu sayısı × 6 harita × 3 süre × en az 2.500 eşlenmiş oyun =
`450.000` A/B oyun çifti; üç ayrı seed bloğu.

Kabul eşikleri:

- Dengeli/sosyal politika genel Tayfa kazanması: `%45–55`.
- Her oyuncu × harita × süre hücresi: `%40–60`.
- Her hücrede %95 güven aralığı yarı genişliği: en fazla 2 yüzde puanı.
- B–A genel kazanma farkı: en fazla 5 yüzde puanı; tek hücrede en fazla 10 puan.
- Medyan oyun süresi/gün sayısı artışı: en fazla `%15`.
- `social – random` Tayfa başarısı: en az 8 puan.
- `crew_omniscient – social`: en az 10 puan.
- `social – traitor_omniscient`: en az 20 puan.
- Sabit sol/orta/sağ politikalarından hiçbiri sosyal politikayı 3 puandan fazla geçemez.
- Özel/kamusal bilgi, eşlenmiş karşı-olgusal rota kararlarının en az `%15`ini değiştirmeli.

Sınır aşımı `FAIL`; illegal durum, bilgi sızıntısı veya motor hatası `BLOCKER` olur.

## Kör insan A/B testi

- En az 24 oturum / 12 eşlenmiş A-B çifti.
- Oyuncu bantları `6–7`, `8–10`, `11–13`, `14–15`; her bantta üç çift.
- Sıra karşı dengelenir; oyuncular hipotezi bilmez.
- En az dört moderatör; ikisi yalnız candidate kural kitabından ilk kez yönetir.
- Katılımcıların en az yarısı yeni oyuncudur.

Kabul:

- Yarıda kalan veya dış müdahale gerektiren oyun: `0`.
- Anlamlı rota kararı medyanı en az `4/5`; hiçbir bant `3,5` altı değil.
- Adalet medyanı en az `3,5/5`; sıkılma medyanı en fazla `2,5/5`.
- “Rotalar çoğunlukla saf tahmindi” diyenler en fazla `%20`.
- Somut bilgi veya sosyal gerekçe gösterebilen oyuncular en az `%75`.
- A'ya göre anlamlı karar/adalet düşüşü ve sıkılma artışı en fazla `0,5`.
- Tek oyuncunun konuşma payı en fazla `%35`.
- İstemsiz pasif beklemenin 90. yüzdeliği toplam sürenin en fazla `%20`si.

## Sea=Rock fiziksel sızıntı testi

- Ortak arka yüz binary'si bütün Deniz/Kayalık kartlarında bit/piksel olarak aynıdır.
- Baskı, kesim, kenar, opaklık ve dönüş yönü için en az 800 kör sınıflandırma ve 10 kişi.
- Deniz/Kayalık ve kart yönü tahmin doğruluğunun %95 üst güven sınırı `%55`i geçmez.

## Üretim ve görsel kabulü

- Tam envanter: `121/121`.
- Kart kesim ölçüsü toleransı: `±0,75 mm`; taşma payı: `3 mm`.
- Etkin çözünürlük: en az `300 dpi`; duplex sapması: en fazla `1,5 mm`.
- Eksik font, glif, overflow veya kesilen mekanik metin: `0`.
- Gerçek ışıkta mekanik metin doğru okuma oranı: en az `%95`.

## Dosya bazlı kapanış

| Engel | Zorunlu dosya / kanıt | Kapanış türü |
|---|---|---|
| `CAN-001` | Story Framework CAN-08/09 `KANON → TASLAK`; diğer Story blobları değişmez | Dokümantasyon + statik test |
| `MEC-001` | `V27_MECHANIC_DECISIONS.json`, ortak arka yüz setup/bilgi sözleşmesi ve A/B sonuçları | Dokümantasyon + tam test |
| `SRC-001` | `SOURCE_HIERARCHY_v2.7.json`, source blob SHA'ları, ID/section → render → PDF eşleme ve normalize metin diff'i | Dokümantasyon + üretim + test |
| `ART-001` | Kart/rulebook artefakt manifestleri, güncel `BINARY_ARTIFACTS.md`, tam 121 candidate | Üretim + preflight |
| `QA-001` | Sabit baseline JSON, karşılaştırma scripti, ham çıktı, motor ve hashler | Yeniden üretilebilir test |
| `QA-002` | Fiziksel proof, kör arka yüz testi ve kör playtest raporu | Fiziksel üretim + insan testi |
| Final | `EVIDENCE_MANIFEST_v2.7.json` ve `SIM_QA_ATTESTATION_v2.7.json` | Exact-candidate attestation |

Narrative whitelist yalnız onaylı ad/flavor alanları ile rulebook `3.1`, `3.3`,
`3.4`, `3.6` ve `17` anlatı bloklarıdır. Kart kimliği/adedi, effect, timing,
group, start veya returns alanında whitelist dışı fark `BLOCKER`dır.

## Attestation sırası

1. Ürün kaynakları ve artefaktlar `C` commitinde dondurulur.
2. QA yalnız `C`yi checkout ederek çalışır.
3. Ham kanıtlar ve attestation sonraki `Q` kanıt commitine yazılır;
   attestation içindeki `candidate_commit=C` olur.
4. `C` sonrasında ürün kaynağı, render veya binary değişirse `C2` oluşur ve
   önceki bütün attestation geçersizleşir.
5. `Q` yalnız `working/v2.7/qa/**` ve yönetişim kanıtlarını değiştirebilir.
6. Release, `C` ürün ağacı ve `Q` kanıtıyla değerlendirilir.
