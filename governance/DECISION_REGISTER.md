# FOULWAKE Karar Kaydı

**Durum:** ACTIVE  
**Kapsam:** v2.7 DRAFT ve sonraki çalışma hatları  
**Kilitli baseline:** v2.6 STABLE / LOCKED

Bu dosya, sohbetler arasında tekrar tartışılmaması gereken açık proje sahibi
kararlarını kanonik durumdan ve release kilidinden ayırarak kaydeder. Bir kararın
`APPROVED FOR DRAFT` olması, sürümün `STABLE / LOCKED` olduğu anlamına gelmez.

| Karar | Durum | Bağlayıcı hüküm | Sonuç / zorunlu kapı |
|---|---|---|---|
| `DEC-20260820-01` | APPROVED FOR v2.7 DRAFT | Açık Deniz ve Kayalık aynı, metinsiz ve yön sızdırmayan binary arka yüzü kullanır. | v2.6'nın ayrı Kayalık arka yüzünü geriye dönük değiştirmez. Bilgi mimarisi farkı nedeniyle exact candidate üzerinde tam Simülasyon ve kör fiziksel sızıntı testi zorunludur. |
| `DEC-20260820-02` | APPROVED FOR v2.7 DRAFT | Karakter/Güç görünen metni `FOULWAKE_CARD_TEXTS_v2.7.json`; tanımlı rulebook anlatı blokları `FOULWAKE_RULEBOOK_STORY_v2.7.md`; ton/lore çiti `FOULWAKE_STORY_FRAMEWORK.md` kaynağından alınır. | Kimlik, adet, etki, zamanlama, deste davranışı ve kural akışı v2.6 mekanik baseline'ından korunur. |
| `DEC-20260820-03` | APPROVED VISUAL DIRECTION | Mürekkep/gravür etkili yetişkin karikatürü ve sınırlı dönem paleti kullanılır; mizah yalnız fareye bağlanmaz. | Sanat yönü onayı release kilidi değildir; tam 121 kart, preflight ve fiziksel prova gerekir. |
| `DEC-20260820-04` | ACTIVE QA MANDATE | Simülasyon Testi mekanik, matematik, strateji, sosyal deneyim, sıkılma, adalet, görsel kullanılabilirlik, PDF, baskı, manifest ve dosya bütünlüğünü denetler. | Tek bir validator veya kazanma oranı genel PASS sayılmaz. Exact-candidate attestation zorunludur. |
| `DEC-20260820-05` | LOCK POLICY | Proje sahibi açık `kilitle`, `stable yap` veya `release et` talimatıyla süreci başlatır; kilidi yalnız Baş Editör uygular. | Açık FAIL/BLOCKER, eksik candidate veya geçersiz attestation varken kilit uygulanmaz. |

## Uygulama kuralı

- Proje sahibinin daha yeni açık kararı bu kayıtla çelişirse Baş Editör önce bu
  dosyayı ve etkilenen çalışma kaynaklarını günceller.
- Taslak karar kilitli v2.6'yı yerinde değiştirmez.
- Hikâye, Görsel veya Simülasyon hattı bu kararları tek taraflı yeniden açamaz;
  uygulama riski veya test sonucu Baş Editöre handoff edilir.
- Reset öncesi üretim ve preflight kayıtları tarihsel kanıttır; güncel branch ve
  exact candidate ile yeniden bağlanmadan release kanıtı sayılmaz.
