# FOULWAKE — Yeni oturum

Güncel kaynak dalı **v2.7-design**. Önce GitHub HEAD'ini doğrula; eski uzman dalındaki state'i güncel görev kaynağı olarak kullanma.

1. `governance/v4/TEAM_START.md`
2. `governance/v4/runtime/STATE.json`
3. `governance/v4/roles/<ROLE_ID>.md` ve bu role atanmış exact görev

Kısa görünüm: `python -B governance/v4/bootstrap.py --role <ROLE_ID>`.
Güncel yetki v4 state/task/contracts/registry zincirindedir. `governance/CURRENT_STAGE.json` ve `WORKSTREAM_SCOPE_BASELINES.json` korunmuş v3 kapanış kayıtlarıdır.

v2.6 kilitli kalır. Görsel kabul, simülasyon sonucu ve release/lock ayrı kanıtlara dayanır. Rolü seçmek üretim görevi açmaz. Eski sohbet, fixture veya PASS kaydı güncel yetkinin yerine geçmez.

7 Eylül ikinci kontrol teslimi: [güncel oynama/PDF dosyaları](working/v2.7/README_CURRENT_v2.7.md) ve [tam teslim kanıtı](governance/v4/evidence/RECHECK_VISUAL_DELIVERY_20260907.json). 121 metin, 27 hedefli test ve 12 ön/yedi arka görsel pilotu mevcut. Tam özgün çizim yayılımı için somut pilotun proje sahibi değerlendirmesi beklenir; yeni sohbette güncel v4 kaydı okunur.
