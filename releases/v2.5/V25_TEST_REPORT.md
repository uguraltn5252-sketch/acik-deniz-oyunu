# OYUN v2.5 — Teknik Test Raporu

**Durum: PASS — STABLE / LOCKED release gate.**

## Sonuç
v2.4'ün geri dönüşlü rota güvenliği korunurken, v2.4 testinde yeni bulunan İskorbüt-Ada relocation açığı ve Ada çevresi relocation açığı v2.5'te sıfır kabul edilen ihlale indirildi. Final tam-sistem modelinde Tayfa/Hain sonucu merkeze yakın; Hull veya Hain sayısında ek değişiklik yapılmadı.

## Mekanik güvenlik
- 13/13 çekirdek regresyon PASS; 8/8 tam motor regresyon PASS.
- 51.204 teorik geometri / 51.102 legal / kalıcı ilk-kol hard-lock 0.
- 1.667.231 baseline relocation / 20 global unsafe rollback / kabul edilen hard-lock 0.
- 5×5 İskorbüt exact: 1.836.984 transition / 5.288 Ada-yolu kaybı önerisi / 5.288 rollback / 0 kabul.
- 6M kritik relocation örnekleminde bütün Harita boylarında kabul edilen İskorbüt-kazanılabilirlik ihlali 0.
- 50k Ada çevresi relocation örneğinde 2.461 ihlal önerisi guard tarafından reddedildi; kabul 0.
- 448.812 stateful fuzz eyleminde invariant/hard-lock hatası 0.

## Tam-sistem denge
- Final mekanik: **100.200 oyun**.
- Tayfa: **%50,28**, yaklaşık %95 GA **%49,97–%50,59**.
- Ortalama yolculuk günü: **5.56**.
- En zayıf model hücresi: **7 oyuncu / long — %42,04**.
- En güçlü model hücresi: **9 oyuncu / short — %54,79**.
- Persona duyarlılığı Tayfa: temkinli %44,39, dengeli %47,50, kaotik %53,50.
- Politika zarfı Tayfa: random %36,80, social %50,73, crew_omniscient %73,27, hain_omniscient %12,53.
- A/B: canonical %50,39, Scurvy off %51,11, Hull 3 %73,83. Hull 3 açık biçimde aşırı Tayfa lehine; Hull 2 korunur.

## Sosyal çıkarım proxy
Pairwise `trust[A][B]` 27.000 oyun: temkinli ayrım 0.013, dengeli 0.059, kaotik 0.102. Bu değerler gerçek insan güveni değildir; davranış modeline bağlı yapısal proxy'dir.

## Moderatör yükü
300.000 rastgele tam kurulum adayında tek-deneme kabul oranı **%11,74–%37,50**. Bu oynanabilirlik oranı değil; kontrollü/rejection tabanlı Moderatör kurulumunun gerekli olduğunu gösteren iş-yükü proxy'sidir.

## Fiziksel prototip
- Kural PDF: 24 sayfa A4; preflight/görsel tarama PASS.
- Kart PDF: 32 sayfa A4; 118/118 ana kimlik + SET-KL-01.
- v2.4'e göre yalnız sayfa 1 ve15 değişti; 30 sayfa piksel olarak aynı.
- 12 Kayalık arka yüz normalize iç kırpımda max piksel farkı 0.

## Kalan insan-only alanlar
Gerçek eğlence, mizahın çalışması, sosyal baskı, konuşma eşitsizliği, bekleme hissi, 7 kişilik uzun oyunun masada gerçekten zayıf olup olmadığı ve moderatörün fiziksel yükü kör playtest ile ölçülmelidir.
