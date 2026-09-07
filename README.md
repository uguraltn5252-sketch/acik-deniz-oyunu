# FOULWAKE

1721'in deniz dünyasında eksik bilgi, geçici güven ve ortak kararların bedeli üzerine kurulu masa oyunu. Hikâye, sanat ve mekanikler aynı masa deneyimini destekler; kara mizah tehlikeyi ortadan kaldırmaz.

Bu repository kalıcı kaynak ve karar kaydıdır. Aktif geliştirme dalı `v2.7-design`; v2.6 kilitli, v2.7 taslaktır.

Güncel oynama dosyaları: [Kuru Pay — tam kural kitabı](working/v2.7/FOULWAKE_KURAL_KITABI_v2.7.md), [121 kart metni](working/v2.7/FOULWAKE_KART_METINLERI_v2.7.md) ve [7 Eylül revizyonu](working/v2.7/README_CURRENT_v2.7.md). Hikâye/kart/kural metni uygulanmıştır; görsel ve baskı paketi ayrı kalır.

Yeni sohbetler: [ekip başlangıcı](governance/v4/TEAM_START.md).
Canlı durum: [v4 state](governance/v4/runtime/STATE.json).
Roller: [çalışma hatları](governance/WORKSTREAM_ASSIGNMENTS.md).

Doğrulama: `python -B governance/validate_governance.py`.
Kısa rol bağlamı: `python -B governance/v4/bootstrap.py --role <ROLE_ID>`.

v3 kapanış kayıtları tarihsel checkpoint olarak korunur. Güncel görev yetkisi v4 state ve exact görev kaydından gelir.
