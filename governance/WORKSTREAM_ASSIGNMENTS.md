# FOULWAKE v2.7 Çalışma Hattı Görevleri

**Durum:** ACTIVE / RELEASE BLOCKED  
**Kaynak commit:** `af064df83ac4132c7d8d75aec67a3f1b51150fdb`  
**Baseline:** v2.6 STABLE / LOCKED

## Sorumluluk haritası

| Engel | Birincil sorumlu | Destek | Teslim | Kapanış ölçütü |
|---|---|---|---|---|
| `CAN-001` | Hikâye | Baş Editör | `CAN-08/09` sınıflandırma düzeltmesi | İki satır `TASLAK`; diğer Story kaynakları ve mekanik alanlar değişmez |
| `MEC-001` | Simülasyon Testi | Görsel + Baş Editör | Ortak Sea=Rock bilgi modeli için spec ve tam A/B QA | Karar kaydı + kaynak uyumu + mekanik/stratejik/sosyal/kör fiziksel PASS |
| `SRC-001` | Görsel Tasarım | Hikâye + Simülasyon | Tek kaynak hiyerarşisi ve source → render → PDF izlenebilirliği | Exact source/blob kayıtları ve sıfır yetkisiz metin farkı |
| `ART-001` | Görsel Tasarım | Simülasyon | Tam 121 kart candidate ve artefakt manifestleri | 121/121 kimlik, front/back eşleme, hash, PDF preflight ve fiziksel prova |
| `QA-001` | Simülasyon Testi | Hikâye | Yeniden üretilebilir narrative/mechanics karşılaştırması | Sürümlü baseline, script, komut, ham çıktı ve hashler |
| `QA-002` | Simülasyon Testi | Görsel | Fiziksel ve kör insan test paketi | Print/cut/duplex/ışık, arka yüz sızıntısı ve kör masa testi kayıtları |
| `GOV-001` | Baş Editör | Bütün hatlar | Dal uzlaştırması, release PR ve zorunlu check | Tutarlı state, intentional merge planı ve korunan release akışı |

## Bağlayıcı teslim sırası

1. Hikâye, Görsel Tasarıma kesin metin alanlarını ve korunacak mekanik alanları verir.
2. Görsel Tasarım kaynakları değiştirmeden candidate üretir ve manifestleri Simülasyona verir.
3. Simülasyon exact candidate üzerinde bütün kapıları çalıştırır; ürünü değiştirmez.
4. Baş Editör handoffları karşılaştırır, kapsam ihlalini reddeder ve kanonik durumu günceller.
5. Yeni ürün candidate commit'i önceki bütün v2.7 attestation sonuçlarını geçersiz kılar.

## Hattın değişiklik sınırı

- Hikâye; kart kimliği/adedi, etki, zamanlama, deste davranışı veya kural akışını değiştiremez.
- Görsel; metni kısaltamaz, yeniden yazamaz, mekanik veya lore hükmü üretemez.
- Simülasyon; bulguyu doğrudan yeni kurala çeviremez, candidate ürünü değiştiremez ve kilitleyemez.
- Hiçbir hat `PROJECT_STATE.md`, `AI_HANDOFF.md`, `governance/**` veya `releases/**`
  alanında Baş Editörden bağımsız kanonik değişiklik yapamaz.

Her teslim `WORKSTREAM_PROTOCOL.md` içindeki zorunlu handoff biçimiyle Baş Editöre gönderilir.
