# ART-41 — Pilot Kodlama Sayfası: MERSİN (Vaka #2)
**Kodlama tarihi:** 07.07.2026 | **Pencere:** 2019 sonu itibarıyla (şok öncesi)
**Statü:** PİLOT — Hocam sezgi testi bekleniyor (bu vakanın asıl hakemi sensin)
**Bayrak lejantı:** ✅ güçlü kaynak | ⚠️ teyit gerekli | ⛔ MISSING-pending | 🔍 HOCAM-CHECK

---

## ÖN KARAR — Analiz Birimi Sorunu (Mersin'in codebook'a ilk darbesi)
Mersin'de Rotterdam tipi bir "liman otoritesi" YOK. Kamu tarafı: TCDD (imtiyaz vereni/mal sahibi, bakanlığa bağlı KİT) + Liman Başkanlığı (bakanlık taşra teşkilatı). Özel taraf: MIP (36 yıllık işletme hakkı devri).
**⚠️ CODEBOOK REVİZYON NOTU #5:** Tam imtiyazlı, otoritesiz limanlarda C1'in öznesi KAMU yönetim tarafıdır (imtiyaz vereni + düzenleyici); operatörün ticari serbestisi C1'e değil C2'ye yazılır. Aksi halde C1 ile C2 aynı şeyi ölçer (çoklu-doğrusallık benzeri sorun, fsQCA'da koşul ayrışıklığını bozar). 🔍 HOCAM-CHECK: Bu birim kararı sence doğru mu?

---

## C1 — Regulatory Autonomy → **0.05 provizyonel** 🔍

| Alt kanıt | Bulgu | Kaynak |
|---|---|---|
| Kamu yönetim organı | TCDD: bakanlık bağlı KİT; imtiyaz Özelleştirme İdaresi + TCDD ile imzalandı ("36 Yıl Süreyle Mersin Limanı İşletme Hakkı Devri Sözleşmesi", 11.05.2007) | Akfen Holding kurumsal, GIHub |
| Yerel özerk otorite | Yok — korporatize liman otoritesi kurumu Türk sisteminde mevcut değil | kurumsal yapı, mevzuat taraması ⚠️ |
| Davada kamu tarafı | 2021 genişleme davasında TCDD "limanın sahibi" sıfatıyla müdahil — mal sahipliği merkezi yapıda | Denizcilik Dergisi/BirGün (2021) |

**Gerekçe:** Kamu yönetim tarafı deconcentrated devlet yapısı → 0.05. (MIP'in ticari serbestisi C2'de.)

## C2 — Ownership Hybridity → **0.70** ✅

| Alt kanıt | Bulgu | Kaynak |
|---|---|---|
| İmtiyaz | 36 yıl işletme hakkı devri, 11.05.2007 → 2043; bedel $755M | Akfen, FreightWaves, GIHub |
| Operatör yapısı | Tüm liman TEK operatörde (MIP); 2019 itibarıyla PSA %51 / IFM %39 / Akfen %10 (IFM 2017'de Akfen'in %40 satışıyla girdi) | GIHub bond dokümanı, Akfen |

**Gerekçe:** Kural: ">%80 özel ama tek dominant operatör" = 0.70. Kitabına uygun vaka.
**Discussion hammaddesi:** PSA (Singapur devlet fonu bağlantılı) + IFM (Avustralya emeklilik fonu) → finansallaşma/konsolidasyon temasının ders kitabı örneği; CFP'nin "financialization" anahtar kelimesine doğrudan bağlanır. 2019 $600M Eurobond'u da (GIHub) finansallaşma kanıtı.

## C3 — Multi-Level Coordination Density → **0.30 provizyonel** (2⚠️) 🔍

| Gösterge | Bulgu | Bayrak |
|---|---|---|
| 1. Kent–liman organı | Resmî daimi organ kaydı yok; 2021 davası belediye–bakanlık–TCDD/MIP hattında yapısal koordinasyon eksikliğinin belirtisi (pencere dışı ama yapısal gösterge) | 0 ✅ |
| 2. Ulusal koordinasyon organına katılım | Dikey hiyerarşi (bakanlık→TCDD) koordinasyon DEĞİLDİR; daimi ulusal liman koordinasyon organı katılım kaydı bulunamadı | 0 ⚠️ (mevzuat/kurum taraması) |
| 3. Uluslararası ağ (aktif) | AIVP üyeliği var AMA "yeni üye" röportajı 2024 tarihli → 2019'da üyelik şüpheli; TÜRKLİM üyeliği ulusal sektör derneği | ⚠️ 🔍 (2019'da IAPH/ESPO-benzeri aktif üyelik var mıydı?) |
| 4. Yazılı kriz protokolü | AFAD genel çerçevesi ulusal; limana özgü, hinterland aktörleriyle yazılı protokol kaydı bulunamadı | ⚠️ 🔍 |

**Provizyonel:** 1/4 iyimser senaryo → 0.30; göstergeler 3–4 senin bilgi alanında.

## C4 — Compound Lock-In → **provizyonel ~0.22** (1 alt boyut 🔍)

**(a) Düzenleyici katılık → 0.33 ↔ 0.67 açık** 🔍
2005–2019 penceresinde 1 büyük reform: 2007 özelleştirme/işletme hakkı devri. AMA: çerçeve Limancılık Kanunu'nun defalarca taslaklanıp yasalaşamaması = belgelenmiş başarısız reform girişimi kalıbı. Kural bu kombinasyonu ("1 reform + sonrasında tıkanmış çerçeve reformu") öngörmemişti.
**⚠️ CODEBOOK REVİZYON NOTU #6:** v2 kuralı önerisi: gerçekleşen reform pencere İÇİNDE ise taban 0.33; pencere içinde belgelenmiş başarısız ÇERÇEVE reform girişimi varsa +0.34 → 0.67. Mersin bu kuralla 0.67 olur. 🔍 Türk liman mevzuat tarihi senin saha — karar senin.

**(b) Finansal kilit → 0.33** ✅
2043 − 2019 = 24 yıl kalan vade → [10, 25) bandı = 0.33. (İkinci kez bant sınırına düştük; v2'ye bant tanımları yarı-açık aralık olarak yazıldı: [10,25), [25,40).)

**(c) Sosyal meşruiyet açığı → 0 provizyonel** ⚠️🔍
2015–2019 penceresinde web taramasında büyük belgelenmiş ihtilaf bulunamadı. Bulunan büyük olaylar pencere DIŞI: Büyükşehir'in imar planı davası + yürütmeyi durdurma (2021, Atatürk Parkı/Millet Bahçesi gerekçeli), 20-21 no'lu rıhtım ÇED süreci (2022–23). 🔍 Yerel arşiv + senin saha bilgin: 2015–2019'da EMH1 genişlemesine ÇED itirazı, liman işçisi eylemi, dava var mıydı?
**⚠️ CODEBOOK REVİZYON NOTU #7 (tasarım düzeyinde önemli):** 2021 davası Ş2 (2023Q4–) öncesine düşüyor. Tek zaman noktalı koşul kodlaması (2019) Ş2 için C4c'yi eksik ölçüyor. v2 kararı: ana analizde tüm koşullar 2019'da sabit (temiz tasarım); robustness olarak yalnızca zamanla değişen C4c, Ş2 koşusu için 2019–2023 penceresiyle yeniden kodlanır. Böylece hem tasarım temiz kalır hem bilgi kaybolmaz.

**Bileşik provizyonel:** (0.33~0.67 + 0.33 + 0)/3 ≈ 0.22~0.33

## C5 — Social Value Integration → **0.05 provizyonel** (⚠️)

| Gösterge | Bulgu | Skor |
|---|---|---|
| 1. Bağlayıcı mandat | MIP ticari şirket; 2007 devir sözleşmesinde bağlayıcı çevre/topluluk mandatı kamuya açık kayıtlarda görünmüyor (sözleşme tam metni kamuya kapalı) | 0 ⚠️ |
| 2. Paydaş temsil organı | Yok | 0 ✅ |
| 3. İmtiyazda sosyal/yeşil koşul | 2007-dönemi sözleşmesi ağırlıkla mali/yatırım yükümlülüğü; yeşil koşul kaydı yok | 0 ⚠️ |

**⚠️ CODEBOOK REVİZYON NOTU #8:** MIP'in kapsamlı KSS programları var (okullar, kadın konukevi, Gates trafik projesi — AIVP röportajı 2024). Kural netleştirmesi: GÖNÜLLÜ KSS ≠ kurumsallaşmış sosyal değer entegrasyonu. Test: yükümlülük yapısal/bağlayıcı mı (tüzük, sözleşme, organ), yoksa şirket inisiyatifi mi? C5 birincisini ölçer. KSS Discussion'da "governance boşluğunu gönüllülük dolduruyor" bulgusu olarak değerlendirilir — bu başlı başına ilginç bir Türkiye bulgusu.

---

## ÖZET SATIR (provizyonel)
| C1 | C2 | C3 | C4 | C5 |
|----|----|----|----|-----|
| 0.05 🔍 | 0.70 ✅ | 0.30 🔍 | 0.22~0.33 🔍 | 0.05 ⚠️ |

**Rotterdam ile kontrast:** Neredeyse ayna görüntüsü (0.95/0.95/0.95/~0.33/0.40 ↔ 0.05/0.70/0.30/~0.25/0.05). Truth table çeşitliliği açısından mükemmel — iki pilot, konfigürasyon uzayının iki ayrı köşesini test etti.

## HOCAM-CHECK LİSTESİ (5 karar)
1. C1 birim kararı: otoritesiz limanlarda kamu tarafı = özne (Not #5) — katılıyor musun?
2. C4a skoru: Limancılık Kanunu'nun yasalaşamaması "başarısız çerçeve reformu" sayılıp 0.67'ye mi çıkmalı? (Not #6)
3. C4c penceresi: 2015–2019'da bildiğin belgelenmiş Mersin ihtilafı var mı?
4. C3 gösterge 3–4: MIP'in 2019'daki uluslararası ağ üyelikleri ve kriz protokolleri hakkında saha bilgin?
5. Genel sezgi testi: Bu satır senin tanıdığın Mersin'i anlatıyor mu? Anlatmıyorsa hangi hücre yanlış?
