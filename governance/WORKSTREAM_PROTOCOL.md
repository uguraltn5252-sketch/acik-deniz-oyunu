# FOULWAKE — Kısa çalışma protokolü

## Kaynak ve başlangıç

Güncel `v2.7-design` HEAD'i → `governance/v4/runtime/STATE.json` → rol brief'i → exact atanmış görev → yalnız gereken kaynaklar. İlk açılışta `governance/v4/TEAM_START.md` okunur. v3 checkpointleri tarihsel kanıttır. Varsayılan default-deny: dal veya sohbet adı tek başına yazma yetkisi vermez.

## Çalışma

Baş Editör görev ve entegrasyonu yönetir; uzman kendi path ve rolünde çalışır. Kayıtlı delegasyon rutin, geri alınabilir görev kararlarında tekrar owner onayı gerektirmez. Kapsam değişince görev kaydı güncellenir; specialist kendi yetkisini genişletemez.

Görev source/baseline, input blobları, çıktı pathleri, kabul ölçütü ve bağımsız reviewer taşır. CI uzman dalındaki politikaya güvenmez; `v2.7-design` üzerindeki exact yetkiyi cumulative farkla karşılaştırır. Ana state ilerleyince uzman dalı otomatik birleştirilmez: içerik girdisi değişmişse görev durur; yalnız governance ilerlemişse güncel yetki yeniden okunur.

## Kalite ve teslim

Sözleşme: `governance/v4/contracts/CONTRACTS.json`. Copy kanonik kaynaktan yerleştirilir; uyuşmazlık `BLOCKED_COPY_DRIFT`. Sanat Yönetimi kadrajı bağımsız değerlendirir: `FRAMING_PASS` veya `REFRAME_REQUIRED`; uyumsuzluk `BLOCKED_FRAMING_DRIFT`. Teknik PASS estetik, insan deneyimi, fiziksel proof veya release kabulü değildir.

Teslim şu yedi alanı taşır; uzun kanıt repo dosyasına bağlanır:

```text
TASK_ID:
SOURCE_HEAD:
DELIVERY_COMMIT:
CHANGED_PATHS:
RESULT_AND_EVIDENCE:
OPEN_BLOCKERS:
NEXT_RESPONSIBLE_ROLE:
```

Araç/model/sürüm, komut ve seed sonucu etkiliyorsa evidence içinde yazılır. Kullanılmayan bütün eklentileri listelemek gerekmez. Geçici ajan bu beş görünür rolün yerine geçirilmez. Sohbetleri kullanıcı taşır; başka sohbete mesaj iletildiği doğrulanmadan teslim alındı denmez.
