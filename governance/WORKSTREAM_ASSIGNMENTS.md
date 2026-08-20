# FOULWAKE v2.7 Çalışma Hattı Görevleri

**Durum:** ACTIVE / RELEASE BLOCKED

**Kaynak commit:** `9758b848f0395525b395e3f2ccf9e9f7408fed99`

**Baseline:** v2.6 STABLE / LOCKED

Önceki çapraz denetim geçici alt ajanlarla yapılmıştır ve resmî uzman teslimi
değildir. Aşağıdaki görevler ilgili görünür sohbet kendi geçmişinde okuyup
zorunlu handoffu verene kadar `PENDING_VISIBLE_CHAT_ACK` durumundadır.

## Görünür sohbet ve dal haritası

| Hat | Resmî görünür sohbet | Çalışma dalı | Güncel kabul |
|---|---|---|---|
| Hikâye | `Foulwake Hikâye Editör` | `work/v2.7-story` | `PENDING_VISIBLE_CHAT_ACK` |
| Görsel | `FOULWAKE görsel tasarım` | `work/v2.7-visual` | `PENDING_VISIBLE_CHAT_ACK` |
| Simülasyon | `Simülasyon Testi` | `work/v2.7-simulation` | `PENDING_VISIBLE_CHAT_ACK` |

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
| `COM-001` | Baş Editör | Bütün görünür uzman sohbetleri | Yanlış atıfların kaldırılması ve görünür sohbet handoffları | Üç görünür sohbetten branch-bound `VISIBLE_CHAT_ACK: YES` teslimi |

## Bağlayıcı teslim sırası

1. Her görünür uzman sohbet kendi görevini bu kayıttan okur ve kendi çalışma dalında yürütür.
2. Hikâye, görünür sohbet handoffuyla kesin metin alanlarını ve korunacak mekanik alanları Görsel Tasarıma verir.
3. Görsel Tasarım kaynakları değiştirmeden candidate üretir ve manifestleri görünür Simülasyon Testi sohbetine devreder.
4. Simülasyon exact candidate üzerinde bütün kapıları çalıştırır; ürünü değiştirmez.
5. Baş Editör görünür sohbet handofflarını ve exact commitleri karşılaştırır, kapsam ihlalini reddeder ve kabul edilenleri `v2.7-design`a entegre eder.
6. Yeni ürün candidate commit'i önceki bütün v2.7 attestation sonuçlarını geçersiz kılar.

## Hattın değişiklik sınırı

- Hikâye; kart kimliği/adedi, etki, zamanlama, deste davranışı veya kural akışını değiştiremez.
- Görsel; metni kısaltamaz, yeniden yazamaz, mekanik veya lore hükmü üretemez.
- Simülasyon; bulguyu doğrudan yeni kurala çeviremez, candidate ürünü değiştiremez ve kilitleyemez.
- Hiçbir hat `PROJECT_STATE.md`, `AI_HANDOFF.md`, `governance/**` veya `releases/**`
  alanında Baş Editörden bağımsız kanonik değişiklik yapamaz.

Her teslim `WORKSTREAM_PROTOCOL.md` içindeki zorunlu handoff biçimiyle Baş Editöre gönderilir.

Geçici alt ajan raporu, GitHub iş emri veya başka bir sohbetin özeti bu teslimin
yerine geçmez ve uzman hat adına `ACKNOWLEDGED`, `DELIVERED` veya `PASS`
durumu oluşturmaz.
