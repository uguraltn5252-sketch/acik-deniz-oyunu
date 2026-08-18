# OYUN — Değişiklik Kaydı v2.4

## Kök nedenler

v2.3 kırma testi dört ana sistem sorunu buldu: Harita-dışı başlangıç nedeniyle geri dönülemez ilk-kol kilidi; kart yer değiştirmelerinin nadiren global çözümsüzlük yaratması; kamusal Harita gösterimlerinin tekrar kapanması nedeniyle açık/bilinen Geçilmez durumunun belirsizliği; simülasyon paketinin dış bağımlılığa ihtiyaç duyması. Ayrıca Kaptan seçiminde teorik sonsuz beraberlik bulundu.

## Uygulanan düzeltmeler

1. Kalkış Limanı gerçek geri dönülebilir başlangıç konumu oldu.
2. Acil geri dönüş Kalkış Limanına kadar uzatıldı.
3. Kaptan ilk tarafsız gecede Sadakat öncesi tek Yakın Ufuk gizli bakışı aldı.
4. İlk rota normal rota oylamasına döndü; Kaptan 2 oyla siyasi ağırlığını korudu.
5. Kamusal Harita açmaları kalıcı yüzü-açık bilgi oldu; olay çözümü fiziksel ziyaretten ayrıldı.
6. Kamusal Geçilmez anında rota/Ufuk hedefinden çıkarıldı.
7. Harita relocation için Kalkış Limanı→Hedef Liman solvability guard eklendi.
8. Kaptan seçiminde ikinci beraberlik Kader Zarıyla sonlandırıldı.
9. Rota/sosyal-proxy motoru self-contained yeniden yazıldı; proje-içi `tam_sistem_sim.py` / `prototype_balance_sim.py` bağımlılığı tamamen kaldırıldı.
10. 118 ana kart kimliğinin dışında 1 fiziksel Kalkış Limanı kurulum kartı prototip PDF’sine eklendi.
11. Manifest/hash üretimi artefaktlardan sonra yapılacak şekilde release notuna bağlandı.

## Bilinçli olarak değiştirilmeyenler

- Başlangıç Gövdesi: 2.
- Hain dağılımı.
- 20 Karakter, 30 gerçek Güç, 15 Sadakat, 52 Harita ve 118 ana oyun kartı kimliği.
- 12 Kayalık içinde 2 gizli Geçilmez kimliği (`HAR-KY-01`, `HAR-KY-03`).
- Küçük Haritalarda 1, büyük Haritalarda 2 Geçilmez kullanımı.
- Kaptan rolünün kalıcı olması ve İsyan/ölüm/Kamara/mahsur/Kayıkçı seferiyle yenilenmesi.

## Release sonucu

Regresyon, exhaustive rota, self-contained 9.000 oyun, kural/kart PDF çapraz kontrolü ve baskı preflight kapıları PASS edilmiştir. **v2.4 STABLE / LOCKED** olarak dondurulmuştur; sonraki tasarım değişiklikleri v2.5+ hattında yapılacaktır.
