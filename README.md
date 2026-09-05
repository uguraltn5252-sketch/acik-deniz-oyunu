# FOULWAKE

1721'in deniz dünyasında eksik bilgi, geçici güven ve ortak kararların bedeli üzerine kurulu masa oyunu. Hikâye, sanat ve mekanikler aynı masa deneyimini destekler; kara mizah tehlikeyi ortadan kaldırmaz.

Bu repository kalıcı kaynak ve karar kaydıdır. Aktif geliştirme dalı `v2.7-design`; v2.6 kilitli, v2.7 taslaktır.

Yeni sohbetler: [ekip başlangıcı](governance/v4/TEAM_START.md).
Canlı durum: [v4 state](governance/v4/runtime/STATE.json).
Roller: [çalışma hatları](governance/WORKSTREAM_ASSIGNMENTS.md).

Doğrulama: `python -B governance/validate_governance.py`.
Kısa rol bağlamı: `python -B governance/v4/bootstrap.py --role <ROLE_ID>`.

v3 kapanış kayıtları tarihsel checkpoint olarak korunur. Güncel görev yetkisi v4 state ve exact görev kaydından gelir.
