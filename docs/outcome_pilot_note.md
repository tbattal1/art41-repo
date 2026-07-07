# ART-41 — Ş1 Outcome Pilot Notu (Rotterdam, İLK GERÇEK VERİ KOŞUSU)
**Tarih:** 07.07.2026 | **Koşan:** Hocam (yerel venv, API modu — Mac kurulumu dahil uçtan uca kendi koşusu)
**Girdi:** IMF PortWatch Daily Ports Data, port1114, 2019-01-01→2022-01-09 (52 taban + 90 pencere haftası)

## 1. Gerçek veri sonuçları (script v1, LEVEL tanımı)
| Metrik | portcalls (toplam) | portcalls_container |
|---|---|---|
| 2019 haftalık taban | 678,4 | 150,7 |
| Dip haftası | 2020-12-28 | 2020-12-21 |
| Düşüş derinliği | %17,0 | %30,3 |
| İlk temas (%95) | +7 hafta | +16 hafta |
| Sürdürülmüş (4h) | YOK (null) | YOK (null) |
| Yarı ömür | +1 hafta | +2 hafta |

## 2. Değerli bulgu (tanımdan bağımsız, sağlam)
**Konteyner segmenti toplam trafiğin ~2 katı sert vuruldu** (%30 vs %17). COVID'in Rotterdam'da yük türlerine asimetrik etkisi — Discussion hammaddesi; ikili metrik tasarımının ilk gerçek getirisi.

## 3. Tespit edilen sorun: MEVSİMSELLİK ARTEFAKTI
Dip haftaları = Noel/yılbasi (28.12 ve 21.12). Yarı ömrün "1 hafta" çıkması ele veriyor: bu COVID toparlanması değil, Ocak'ın Noel çukurundan doğal sıçraması. LEVEL tanımı (taban-ortalama) şoku değil takvimi yakalıyor. COVID'in bilinen akut fazı (Nisan–Mayıs 2020) dip olarak seçilmiyor çünkü mutlak seviyede yıl sonu çukuru daha derin.

## 4. Çözüm: YoY aynı-hafta oranı (script v2'ye eklendi)
ratio_t = değer(yıl, ISO-hafta) / değer(2019, aynı ISO-hafta) — Noel iki yılda da var → oranda iptal; kalan sinyal = şok. 4 haftalık yuvarlanan ortalama ile gürültü yumuşatma. W53→W52 eşlemesi loglanıyor. **v2 her koşuda İKİ tanımı birden raporlar** (level + yoy yan yana) — tanım kararı gerçek karşılaştırmayla verilecek.

## 5. Sentetik doğrulama (yalnız yazılım testi — bulgu DEĞİL, veriler yapay)
Enjekte edilen gerçek: şok dibi Nisan–Haziran 2020 (%25) + Noel çukuru her yıl (%35).
| Tanım | Bulduğu dip | Derinlik | Değerlendirme |
|---|---|---|---|
| LEVEL | 27.12.2021 | %35,1 | Noel'e kandı (gerçek Rotterdam patolojisinin birebir kopyası) |
| YOY | 22.06.2020 | %26,3 | Enjekte şoku doğru buldu; sürdürülmüş toparlanma şok bitişiyle uyumlu |
→ YoY tanımı artefaktı öldürüyor; algoritma doğrulanmış.

## 6. KARAR (KİLİT — 07.07.2026)
**Y = YoY aynı-hafta oranı.** Rotterdam gerçek verisinde dört tanım yan yana test edildi:
| Tanım | Konteyner dibi | Değerlendirme |
|---|---|---|
| LEVEL-raw | 21 Ara 2020 (%30) | Noel artefaktı |
| LEVEL-mask | 10 Şub 2020 (%27) | erken-2020 kış/ÇYY çukuru — yanlış |
| LEVEL-seasonal | 10 Şub 2020 (%30) | aynı Şubat sorunu — yanlış |
| **YoY** | **8 Haz 2020 (%14,5)** | **✅ gerçek COVID dibi** |
Yalnız YoY doğru tarihi buldu → ana tanım YoY. LEVEL robustness ekine düştü. Ş2 referansı = 2022 (script v5). Codebook Bölüm B kilitlendi.
**Açık kalan tek alt-kalem:** fsQCA ana Y'si konteyner mi toplam mı — Ağustos'ta ikinci vaka teyidiyle.

## 7. Süreç notu (repro zinciri)
Kurulum yolu belgelendi: macOS Homebrew Python 3.14 → PEP 668 engeli → venv çözümü (python3 -m venv venv; source venv/bin/activate; pip install pandas requests). GitHub README'ye aynen girecek — ilk kullanıcı testini Hocam yaptı ve geçti.
