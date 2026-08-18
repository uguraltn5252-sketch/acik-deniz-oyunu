# OYUN v2.4 — Teknik Test Raporu

**Durum:** PASS — geliştirme adayı; binary/PDF release gate tamamlanmadı.

## Hedeflenen regresyonlar

- v2.3 geri dönülemez ilk-kol hard-lock.
- Islak Deniz Haritası / Hayalet Işıkları gibi Harita yer değiştirmelerinde global solvability kaybı.
- Pusula ve kamusal Harita gösterimlerinde açık/kapalı durum çelişkisi.
- Kaptanın kör tek başına ilk rota seçimi yerine yeni açılış akışı.
- Kaptan seçimi sonsuz beraberlik olasılığı.
- v2.3 davranış paketinin kayıp proje-içi Python bağımlılığı.

## Regresyon testleri

`test_v24_regressions.py`: **8/8 PASS**.

Kritik örnekler: Kalkış Limanına geri dönüş; Kaptan bakışının private/kapalı kalması; kamusal Geçilmezin anında blocker olması; ordinary public reveal'in açık ama unresolved kalması; unsafe relocation rollback'i; self-contained sim import sözleşmesi.

## Exhaustive geometri

- Teorik: **51,204**
- Legal: **51,102**
- Rejected: **102**
- Görünür ilk rota dalları: **135,430**
- Sonradan çıkmaz olabilen ama Kalkış Limanıyla geri kazanılan ilk dallar: **8,791**
- Kalıcı ilk-dal kilidi: **0**

## Harita relocation exhaustive testi

- Denenen Near-Horizon pair transition: **1,667,231**
- Kalkış Limanı→Hedef Liman bütün gerçek yollarını yok edeceği için rollback edilen: **20**
- Guard sonrası kabul edilen kalıcı kilit: **0**

Unsafe örnekler bu exhaustive modelde 6×6 segmentinde 20 kez oluştu; guard tamamını reddetti.

## 9.000 oyun self-contained rota/sosyal-proxy matrisi

- Oyun: **9,000**
- Setup error: **0**
- Hedef Limana ulaşma: **100.00%**
- Hard route lock: **0.00%**
- Ortalama yolculuk günü: **6.21**
- Geçilmez çarpması/oyun: **0.091**
- İlk rota Geçilmez çarpması/oyun: **0.013**
- Acil geri dönüş/oyun: **0.060**
- Kalkış Limanına kadar geri dönüş/oyun: **0.0037**
- Kaptan ilk-gece bakışı: **1.0/oyun**

Bu motor **tam Tayfa/Hain kazanma dengesi değildir**. Yalnız yeni rota güvenliği, bilgi görünürlüğü ve basit oyun davranışı için regresyon proxy'sidir.

## Release engineering

`gizli_gecilmez_kayalik_v24_sim.py` proje içi hiçbir Python modülünü import etmez. Python standart kütüphanesi + `OYUN_SIMULASYON_SPEC_v2.4.json` ile tek başına çalışır. v2.3'teki eksik `tam_sistem_sim.py` sınıfı bu nedenle v2.4 canonical route testinde yoktur.

## Sonuç

**Kural/state-machine/rota güvenliği düzeltmeleri PASS.** v2.4 `TEST-PASSED` geliştirme adayıdır. PDF/kart binary'leri güncellenmeden ve preflight edilmeden `STABLE / LOCKED` yapılmamalıdır.
