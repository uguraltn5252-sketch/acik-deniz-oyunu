# OYUN v2.5 — STABLE / LOCKED

**Taban:** v2.4 STABLE / LOCKED  
**Durum:** STABLE / LOCKED  
**Tarih:** 19 Ağustos 2026

v2.5, v2.4 kapsamlı testinde bulunan İskorbüt-Ada relocation açığını, oyun-boyu Ada çevresi invariantını, Kaderi Yeniden Yaz × Geçilmez hükmünü ve release/spec bütünlüğü eksiklerini en küçük müdahalelerle düzeltir.

## Ana kilitler
- Hull/Gövde **2** kalır.
- 20 Karakter / 30 Güç / 1 Çürümüş Erzak / 15 Sadakat / 52 Harita / 12 Kayalık / 118 ana kimlik korunur.
- `HAR-KY-01` ve `HAR-KY-03` gizli Geçilmez kalır; arka yüz sızıntısı 0.
- `SET-KL-01` 118 kimliğin dışında ayrı Kalkış Limanı kurulum bileşenidir.
- İlk gün yalnız Kaptan seçimi; ilk tarafsız gecede Kaptan Sadakatini bilmeden tam 1 yasal Yakın Ufka gizlice bakar; Sadakat ertesi sabah; ilk gerçek rota normal eşzamanlı oylamadır ve Kaptan oyu 2 sayar.
- Çürümüş Erzak sahibi İskorbüt sonucu belirlendikten sonra 1 gerçek Güç çeker; ilk yolculuk gününe herkes 1 gerçek Güçle başlar.
- Kamusal açılan Harita kapanmaz; ziyaret edilmedikçe olay çözülmez; kamusal Geçilmez anında blocker olur.
- Relocation, İskorbüt aktifse **Ada üzerinden Hedef Limana kazanılabilir yolu**, İskorbüt temizse Hedef Liman yolunu ve oyun-boyu Ada çevresi yasağını korur; aksi işlem gizlice rollback edilir.
- Kaderi Yeniden Yaz Geçilmezde kullanılabilir; Geçilmez girilmiş/ziyaret edilmiş sayılmaz, açık engel kalır ve aynı hareket penceresinde başka yasal Yakın Ufka yönlenilir. Ada girişi İskorbütü önce temizler.

## Nihai doğrulama
- Çekirdek regresyon: **13/13 PASS**.
- Tam motor regresyonu: **8/8 PASS**.
- Geometri: **51.204 teorik / 51.102 legal / 102 rejected / 0 kalıcı ilk-kol kilidi**.
- Baseline relocation: **1.667.231 transition / 20 unsafe rollback / 0 kabul edilen kalıcı kilit**.
- İskorbüt 5×5 exact: **1.836.984 transition / 5.288 gerekli rollback / 0 kabul edilen ihlal**.
- Kritik altı Harita boyunda **6.000.000** relocation örneklemi: kabul edilen İskorbüt-kazanılabilirlik ihlali **0**.
- Ada çevresi 50k: **2.461** ihlal önerisi / **2.461 rollback / 0 kabul**.
- Stateful fuzz: **448.812 eylem / 0 invariant ihlali**.
- Final tam-sistem Monte Carlo: **100.200 oyun / Tayfa %50,28 / %95 GA %49,97–%50,59 / 0 motor hatası**.
- Hull 3 A/B Tayfa %73,83; bu yüzden Hull 2 korunur.
- Fiziksel PDF audit: **PASS**; 118/118 kimlik; Kayalık arka-yüz piksel farkı 0.

## Model sınırı
Tam-sistem motoru kanonik mekanik sözleşmesini çalıştırır fakat insan blöfü, mizah, sosyal yorgunluk ve gerçek güveni kanıtlamaz. Persona/pairwise güven testleri yalnız davranış duyarlılığıdır; kör insan playtesti önerilmeye devam eder fakat stable lock için zorunlu değildir.

`releases/v2.5/` kilitlidir; sonraki tasarım değişiklikleri **v2.6+** hattında yapılır.
