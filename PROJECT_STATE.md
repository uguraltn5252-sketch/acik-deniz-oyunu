# Project State

**Son güncelleme:** 19 Ağustos 2026  
**Son stabil prototip:** **v2.5 STABLE / LOCKED**  
**Önceki rollback:** **v2.4 STABLE / LOCKED**  
**Kanonik kaynak:** `releases/v2.5/`  
**Sonraki tasarım hattı:** **v2.6+**

v2.5, v2.4 kapsamlı testinde bulunan İskorbüt-Ada relocation açığını, oyun-boyu Ada çevresi invariantını, Kaderi×Geçilmez belirsizliğini ve release/spec bütünlüğü eksiklerini düzeltir. v2.4 yerinde değiştirilmez.

## Kilitli v2.5 kararları

- Kaptan kalıcı rol; ilk gün yalnız seçim. İlk tarafsız gecede Sadakat bilinmeden tam 1 Yakın Ufka gizli bakış; sonraki gecelerde makam otomatik bilgi vermez.
- Sadakat ertesi sabah; ilk gerçek rota normal eşzamanlı oylama, Kaptan oyu 2.
- N-1 gerçek Güç + Çürümüş Erzak kurulum paketi; Erzak sahibi sonuçtan sonra 1 gerçek Güç çeker. Her oyuncu ilk yolculuk gününe 1 gerçek Güçle başlar.
- Kalkış Limanı `SET-KL-01` 118 kimliğin dışında fiziksel kurulum bileşenidir; geri dönüş hedefidir.
- Kamusal açılan Harita kapanmaz; ziyaret edilmedikçe olayı çözülmez; kamusal Geçilmez blocker olur.
- İskorbüt aktifse relocation sonrası Ada→Hedef Liman kazanılabilirliği zorunlu; İskorbüt temizse Hedef Liman yolu zorunlu.
- Girdap/Ters Akıntı Ada 8-komşuluk yasağı oyun-boyu invarianttır ve relocation bunu bozamaz.
- Kaderi Geçilmezde kullanılabilir; Geçilmez ziyaret sayılmaz ve açık engel kalır. Ada girişi İskorbütü olaydan önce temizler.
- Gövde 2; Hain tablosu 6:1, 7:2, 8-10:3, 11-13:4, 14-15:5.
- 20 Karakter / 30 Güç / 1 Çürümüş Erzak / 15 Sadakat / 52 Harita / 12 Kayalık / 118 ana kimlik.

## Test kapıları

- 13/13 çekirdek regresyon PASS; 8/8 tam motor regresyon PASS.
- 51.102 legal blocker geometrisinde kalıcı ilk-kol kilidi 0.
- 1.667.231 baseline relocation; 0 kabul edilen kalıcı kilit.
- 1.836.984 exact 5x5 İskorbüt transition; 5.288 kötü önerinin tamamı rollback.
- 6M kritik relocation örnekleminde kabul edilen İskorbüt ihlali 0.
- 50k Ada çevresi swap'ında kabul edilen ihlal 0.
- 448.812 stateful fuzz eylemi; hata 0.
- 100.200 final tam-sistem oyununda Tayfa %50,28; %95 GA yaklaşık %49,97-%50,59; hata 0.
- Fiziksel PDF audit PASS; Kayalık arka-yüz sızıntısı 0.

## Kalan insan-only sorular

Eğlence, masa gerilimi, mizah, bekleme hissi, gerçek güven/şüphe, konuşma eşitsizliği ve özellikle 7 kişilik Uzun oyunun hissi kör insan playtestiyle ölçülmelidir. Bu alanlar stable-lock için zorunlu değildir ama sonraki tasarım kararları için gereklidir.

## Artefakt

Library ZIP: `/Oyun-GitHub/OYUN_SIMULASYON_PAKETI_v2.5.zip`  
SHA-256: `975dd77d435a835fcf3faa864c5624b0542fadb419fa7d34217ed32fe87aa046`
