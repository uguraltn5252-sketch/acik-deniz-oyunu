# FOULWAKE

1721'in deniz dünyasında eksik bilgi, geçici güven ve ortak kararların bedeli üzerine kurulu masa oyunu. Hikâye, sanat ve mekanikler aynı masa deneyimini destekler; kara mizah tehlikeyi ortadan kaldırmaz.

Bu repository kalıcı kaynak ve karar kaydıdır. Aktif geliştirme dalı `v2.7-design`; v2.6 kilitli, v2.7 taslaktır.

9 Eylül güncel yayın teslimi: [121 kart — tek PDF, 46 A4 sayfa](working/v2.7/publication_20260909/pdf/FOULWAKE_KARTLAR_A4_CIFT_TARAFLI_v2.7.pdf), [30 sayfalık A4 kural kitabı](working/v2.7/publication_20260909/pdf/FOULWAKE_KURAL_KITABI_A4_v2.7.pdf). Kesin adlar Kraliçe Tesella, Port Avanta, Santa Veda ve Malum. Özgün kapak, okunur tipografi, moderatör panelleri ve Harita/Ufuk şemaları uygulandı. Kart kimlikleri, mekanikler, özgün çizimler, tek fener ve palmiye Adası korundu. [Baskı ayarları](working/v2.7/publication_20260909/README.md): A4, %100, uzun kenardan çift taraflı. [Teslim kanıtı](governance/v4/evidence/PUBLICATION_DELIVERY_20260909.json). Dijital metin, ad, görsel ve geometri kontrolü tamamlandı; bağımsız kabul, fiziksel prova ve insan denemesi iddia edilmez. Bu exact üretim görevi kapandı.

Yeni sohbetler: [ekip başlangıcı](governance/v4/TEAM_START.md).
Canlı durum: [v4 state](governance/v4/runtime/STATE.json).
Roller: [çalışma hatları](governance/WORKSTREAM_ASSIGNMENTS.md).

Doğrulama: `python -B governance/validate_governance.py`.
Kısa rol bağlamı: `python -B governance/v4/bootstrap.py --role <ROLE_ID>`.

v3 kapanış kayıtları tarihsel checkpoint olarak korunur. Güncel görev yetkisi v4 state ve exact görev kaydından gelir.
