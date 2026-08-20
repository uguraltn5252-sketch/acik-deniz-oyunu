# FOULWAKE v2.7 Çalışma Hattı Görevleri

**Durum:** ACTIVE / RELEASE BLOCKED

**Yönetişim tabanı:** `v2.7-design@bc148e33343b4066259a996a9c299aab17fd8e3d`

**Kabul edilen Hikâye kaynağı:** `work/v2.7-story@e04eef7f1fef6ea407feaaf26558551297c44b37`

**Baseline:** v2.6 STABLE / LOCKED

Önceki çapraz denetim geçici alt ajanlarla yapılmıştır ve resmî uzman teslimi
değildir. Üç görünür sohbetin 3/3 iletişim ACK kaydı yalnız
`COMMUNICATION_TEST_ONLY` kapsamındadır. Bunun ardından `Foulwake Hikâye
Editör` görünür sohbeti bağımsız revalidasyonunu kendi dalında teslim etmiş;
Baş Editör exact commit ve kapsamı doğrulayarak Görsel Tasarım girdisi olarak
kabul etmiştir. Görsel ve Simülasyon gerçek teslimleri henüz beklenmektedir.

## Görünür sohbet ve dal haritası

| Hat | Resmî görünür sohbet | Çalışma dalı | Güncel kabul |
|---|---|---|---|
| Hikâye | `Foulwake Hikâye Editör` | `work/v2.7-story` | `ACCEPTED_STORY_WORKSTREAM_PASS / READY_FOR_VISUAL_INPUT` |
| Görsel | `FOULWAKE görsel tasarım` | `work/v2.7-visual` | `AUTHORIZED_BRANCH_CREATED / PENDING_VISIBLE_CHAT_DELIVERY` |
| Simülasyon | `Simülasyon Testi` | `work/v2.7-simulation` | `ACKNOWLEDGED_COMMUNICATION_TEST_ONLY / PENDING_REAL_DELIVERY` |

Hikâye tesliminin bağlayıcı kaydı
`governance/STORY_HANDOFF_20260820.json` içindedir. Bu kabul release PASS'i,
mekanik eşdeğerlik veya kilit değildir; Hikâye değişiklikleri henüz
`v2.7-design`a entegre edilmemiş, exact çalışma commitinde tutulmuştur.

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
| `COM-001` | Baş Editör | Bütün görünür uzman sohbetleri | Yanlış atıfların kaldırılması; 3/3 iletişim ACK tamamlandı | Her uzman sohbetinde bağımsız revalidasyon, oluşturulmuş çalışma dalı ve branch-bound gerçek teslim |

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

`ACKNOWLEDGED_COMMUNICATION_TEST_ONLY`, uzman teslimi değildir.
`work/v2.7-story` ve `work/v2.7-visual` oluşturulmuştur;
`work/v2.7-simulation` ilk yetkili Simülasyon çalışmasında oluşturulacaktır.
`COM-001`, Görsel ve Simülasyon branch-bound gerçek teslimleri tamamlanana kadar
açık kalır.
