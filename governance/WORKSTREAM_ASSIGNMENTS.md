# FOULWAKE Çalışma Hattı Görevleri

**Yetki kaynağı:** `governance/CURRENT_STAGE.json`  
**Aktif visual candidate:** **YOK**  
**Kapanış:** **V3_CLEAN_CLOSURE_COMPLETE / V4_MIGRATION_READY / NOT_STARTED**  
**Varsayılan:** Bütün specialist yazmaları kapalıdır.

| Hat | Exact dal/head | Durum | Aktif görev |
|---|---|---|---|
| Hikâye | `work/v2.7-story@e04eef7f1fef6ea407feaaf26558551297c44b37` | PAUSED | YOK |
| Sanat Yönetimi | `work/v2.7-art-direction@917f8b71f47eeecdfb12b7ec930796bf111e2858` | PATCH PROJECT_OWNER_ACCEPTED / PAUSED | YOK |
| Görsel | `work/v2.7-visual@23c062f6de06c32eab224b3440c8474725d4fe9e` | OWNER-REJECTED / HOLD | YOK |
| Simülasyon | Dal yok | NOT STARTED | YOK |
| Baş Editör | `v2.7-design` | V3 CLEAN CLOSURE | Yalnız exact yeni emirle sonraki aşama |

Sanat Yönetimi kabulü Görsel, thumbnail, candidate, tam 121, PDF, Simülasyon,
release veya lock yetkisi vermez. Yeni görev için `CURRENT_STAGE.json` ve
`WORKSTREAM_SCOPE_BASELINES.json` birlikte yeni exact yetki taşımak zorundadır.

v4 migrasyonu hazır fakat başlamamıştır; yalnız ayrı branch ve yeni exact Baş
Editör emriyle yürütülebilir.
