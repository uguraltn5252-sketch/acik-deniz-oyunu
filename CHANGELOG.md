# Changelog

## v2.6 - Entegre kural/anlatı ve fiziksel bileşen sürümü

**Tarih:** 19 Ağustos 2026  
**Durum:** **STABLE / LOCKED - `releases/v2.6/`**  
**Mekanik baseline:** **v2.5 STABLE / LOCKED**

Kullanıcı v2.6'yı açıkça kilitlemiştir.

Kilitlenen değişiklikler:

- Kural kitabı oyuncu öğretimi, Moderatör/storyteller akışı, referans ve arka plan hikâyesini tek belgede birleştirir.
- Ayrı Moderatör masa kartı kaldırılmıştır; Moderatör oyunu kural kitabının tek akış bölümünden yönetir.
- Moderatör hafif storyteller rolündedir; atmosferi kurar fakat gizli bilgi/şüphe yönlendirmez.
- Kaptan Gusto'nun kayboluşu, Siyah Mühür ve Saint Verena anlatısı entegre edilmiştir.
- Final kural kitabı 29 sayfa A4'tür.
- Final kart PDF 34 sayfa A4'tür.
- 118 ana oyun kartı korunur: 20 Karakter / 30 Güç / 1 Çürümüş Erzak / 15 Sadakat / 52 Harita.
- Ana setin dışında üç yardımcı fiziksel kart kilitlenmiştir: Kalkış Limanı (`SET-KL-01`), Varış/Hedef Limanı (`SET-VL-01`) ve Kaptan makamı (`SET-KP-01`).
- Toplam basılabilir fiziksel kart sayısı 121'dir.
- Mahkûm için ayrı kart/token kaldırılmıştır; Moderatör not alır.
- `ERZ-01` Çürümüş Erzak ve `GUC-22` Bayat Peksimet değiştirilmemiştir.
- Kart PDF'deki eski görünmeyen Kayalık metin kalıntıları temizlenmiştir.
- **Kayalık arka yüzlerini Açık Deniz ile aynı yapma deneyi v2.6'ya alınmamıştır; Kayalık kategori arka yüzleri korunmuştur.**
- v2.6 final validator PASS; kör Moderatör yürüyüşü 28/28 PASS; PDF preflight PASS.
- Kilitli paket: `/Oyun-GitHub/OYUN_SIMULASYON_PAKETI_v2.6.zip`.

## v2.5 - Önceki stabil mekanik baseline

**Tarih:** 19 Ağustos 2026  
**Durum:** **STABLE / LOCKED - `releases/v2.5/`**

- İskorbüt aktif relocation sonrası Ada üzerinden Hedef Liman kazanılabilirliği zorunlu hâle getirildi.
- Girdap/Ters Akıntı - Ada 8-komşuluk yasağı oyun-boyu invariant olarak korundu.
- Kaderi Yeniden Yaz × Geçilmez hükmü kesinleştirildi.
- Çürümüş Erzak sahibinin İskorbüt sonucu sonrası gerçek Güç çekimi ve ilk yolculuk gününde herkesin 1 Güçle başlaması sabitlendi.
- Gövde 2 ve 118 ana kimlik korundu.
- Tam-sistem 100.200 oyun: Tayfa yaklaşık %50,28; motor hatası 0.

## v2.4 - Önceki mekanik stabil

- Fiziksel Kalkış Limanı, Kaptanın tarafsız ilk-gece bakışı, kalıcı kamusal Harita bilgisi ve rota/relocation güvenlik hükümleri kilitlendi.
- v2.5 tarafından mekanik olarak devralındı.

## v2.3 - Stabil prototip

**Tarih:** 18 Ağustos 2026  
**Durum:** **Kilitli release - `releases/v2.3/`**

- Ayrı görünür Geçilmez Kayalık işaret/token sistemi kaldırıldı.
- Geçilmez Kayalıklar 52 Harita kartının içindeki 12 Kayalık kartına entegre edildi; toplam kart kimliği 118 kaldı.
- `HAR-KY-01` ve `HAR-KY-03` Geçilmez Kayalık oldu; kapalı kategori yüzleri normal Kayalıktan ayırt edilemez.
- Küçük Haritalarda 1, büyük Haritalarda 2 Geçilmez normal Kayalık kotasının içinde zorunludur.
- Kapalı Geçilmez normal Harita/Ufuk hedefidir ve bütün gizli bilgi/bakma/blöf kurallarına tabidir.
- Seçilip açıldığında Gemi kareye girmez; mevcut konumda kalır. Normal rota gününde hareket harcanır ve kart açık kalıcı engele dönüşür.
- Acil geri dönüş yalnız açılmış/bilinen Geçilmezlerin oluşturduğu tam ileri çıkmazda uygulanır.
- Kaptan kalıcı rol, Kaptan yenileme kuralları ve bütün Haritalarda 2 Gövde korunur.
- 51.204 geometri taraması ve v2.3 stabil doğrulayıcı PASS.

## v2.2 - Önceki stabil prototip

`releases/v2.2/` değiştirilemez geri dönüş referansıdır.

## v2.1 - Tarihsel stabil temel

`releases/v2.1/` değiştirilemez tarihsel geri dönüş referansıdır.
