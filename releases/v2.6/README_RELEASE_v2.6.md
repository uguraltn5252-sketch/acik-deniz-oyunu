# OYUN v2.6 — STABLE / LOCKED

**Taban mekanik:** v2.5 STABLE / LOCKED  
**Durum:** STABLE / LOCKED  
**Kilit tarihi:** 19 Ağustos 2026  
**Sürüm tipi:** Entegre kural kitabı + Moderatör/storyteller akışı + anlatı + fiziksel yardımcı kart standardı.

> Kullanıcı v2.6'nın mevcut haliyle, içerikte hiçbir değişiklik yapılmadan kilitlenmesini açıkça onayladı. Bu nedenle **son kullanıcı-onaylı kilitli/stabil sürüm v2.6 STABLE / LOCKED**'tur.

## Kilitli v2.6 içeriği

Bütün oyuncu kuralları, Moderatörün açılış/sefer akışı, hafif storyteller yönergeleri ve Siyah Mühür arka plan hikâyesi **tek 29 sayfalık kural kitabında** bulunur. Ayrı Moderatör kartı veya ayrı hikâye dosyası bu sürümün parçası değildir.

## Kart seti

Ana oyun kartları:
- 20 Karakter
- 30 Güç
- 1 Çürümüş Erzak — İskorbüt Tehlikesi
- 15 Sadakat
- 52 Harita
- toplam 118 ana fiziksel kart kimliği

Ana setin dışında üç açık yardımcı kart baskı yapraklarında fiziksel olarak bulunur:
- `SET-KL-01` Kalkış Limanı
- `SET-VL-01` Varış / Hedef Limanı
- `SET-KP-01` Kaptan makamı

Toplam basılabilir fiziksel kart sayısı **121**'dir. Mahkûm için ayrı kart/token yoktur; Moderatör not alır. `ERZ-01` Çürümüş Erzak ve `GUC-22` Bayat Peksimet değiştirilmemiştir.

Kayalık kartlarının mevcut kategori arka yüzleri **aynen korunmuştur**; Açık Deniz arka yüzü varyantı bu kilitli sürüme uygulanmamıştır.

Kart PDF'sindeki eski görünmeyen Kayalık metin kalıntıları temizlenmiş durumdadır. Güncel `HAR-KY-01 Duvar Gibi Kayalık` ve `HAR-KY-03 Yolun Bittiği Yer` korunur.

## Kilitli artefaktlar

İçerikleri ve hashleri kilit anındaki değerleriyle dondurulmuştur:

- `/Oyun-GitHub/v2.6/OYUN_Kural_Kitabi_v2.6_DRAFT.pdf`
- `/Oyun-GitHub/v2.6/OYUN_Kartlar_A4_Prototip_v2.6_DRAFT.pdf`
- `/Oyun-GitHub/OYUN_v2.6_DRAFT_GUNCEL.zip`

Dosya adlarında ve PDF içindeki kapakta geçen `DRAFT` ibaresi **bilinçli olarak değiştirilmemiştir**; kullanıcı sürümü içerik değiştirmeden kilitlemiştir. Kanonik statüyü bu release kaydı ve `V26_RELEASE_MANIFEST.json` belirler.

Hashler `BINARY_ARTIFACTS.md` ve `V26_RELEASE_MANIFEST.json` içinde kayıtlıdır.

## Doğrulama

- v2.5 mekanik baseline validator: PASS
- v2.6 kart/kural validator: PASS
- kör Moderatör yürüyüşü: 28/28 PASS
- kart PDF preflight: PASS

## Değiştirilemezlik

`releases/v2.6/` altındaki kilitli oyun artefaktları bundan sonra yerinde değiştirilmez. Yeni bir mekanik, kart, kural kitabı, hikâye veya fiziksel bileşen değişikliği **v2.7+ taslak hattında** yapılır.