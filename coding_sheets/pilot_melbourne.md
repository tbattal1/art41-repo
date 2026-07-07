# ART-41 — Pilot Kodlama Sayfası: MELBOURNE (Vaka #4)
**Kodlama tarihi:** 07.07.2026 | **Pencere:** 2019 sonu itibarıyla (şok öncesi)
**Statü:** PİLOT | **Rol:** Finansallaşma ucu stres testi
**Bayrak lejantı:** ✅ güçlü kaynak | ⚠️ teyit gerekli | 🔍 HOCAM-CHECK

---

## ⚠️ DÜZELTME KAYDI (kalite zinciri gereği açık raporlanır)
Tasarım dokümanı v1'deki vaka tablosunda Melbourne "99 yıllık kira" yazılmıştı — **HATA**. Doğrusu: **50 yıllık kira** (99 yıl Darwin ve NSW liman işlemlerinin süresi). Tablo "doğrulanmamış ön profil" etiketliydi ve doğrulama sistemi hatayı yakaladı — mekanizma tasarlandığı gibi çalıştı. Design doc v2'de düzeltilecek.

---

## C1 — Regulatory Autonomy → **0.70** ✅ (yeni birim kuralıyla)

**Önce birim kararı:** Melbourne'da landlord işlevinin KENDİSİ özelleştirilmiş — PoM (özel kiracı) üçüncü taraf operatörlere rıhtım/arazi kiralayan yönetim organı. Devlette kalanlar: denizcilik/emniyet işlevleri (Victorian Ports Corporation Melbourne) + fiyat regülasyonu (ESC).
**⚠️ CODEBOOK REVİZYON NOTU #12:** C1'in öznesi = landlord/yönetim işlevini fiilen yürüten aktör, KAMU YA DA ÖZEL. Ayrım testi: aktör üçüncü taraf operatörlere kiralama/lisanslama yapıyor mu? Mersin'de MIP tek-operatör imtiyazcısı (üçüncü tarafa kiralamıyor) → özne TCDD (0.05). Melbourne'da PoM landlord → özne PoM. Tutarlı ve savunulabilir. 🔍 Onay?

| Karar alanı | Bulgu (2019) | Kaynak | Özerk? |
|---|---|---|---|
| Tarife | Yasal Pricing Order: tarifeler yılda 1 kez, en fazla TÜFE kadar artabilir (Tariff Adjustment Limit); ESC yıllık uyum beyanı + 5 yıllık denetim; ayrıca ihracat fiyat kararı (konteyner wharfage %2,5/yıl indirim 2019-20'ye kadar) | ESC (Pricing Order sayfaları), Premier of Victoria | HAYIR |
| Yatırım | Ticari kararlar konsorsiyumda; kapasite genişletme taahhüdü kira sözleşmesinde | Torys, PRNewswire | EVET |
| Kiralama/arazi | ~500 ha arazi yönetimi kiracıda; kira bedelleri Pricing Order kapsamı DIŞI (ESC yalnızca süreç incelemesi yapar) | ESC genel bakış belgesi | EVET |

**Gerekçe:** 3 alandan 2'si özerk, tarife bağımsız regülatörce tavanlı → 0.70. (PoM'un kendi ifadesi: "ülkenin en ağır regüle edilen limanı".)
**⚠️ CODEBOOK REVİZYON NOTU #13:** C1'de üç farklı kontrol tipi netleşti: (i) hiyerarşik vesayet (bakanlık onayı) — özerkliği düşürür; (ii) kamu hissedarının genel kurul hakkı (Rotterdam) — düşürmez; (iii) bağımsız regülatör tavanı (Melbourne) — İLGİLİ KARAR ALANINI özerklik dışı sayar. Üçlü tipoloji v2'ye giriyor; kavramsal olarak da Discussion'da değerli ("özerklik kimden bağımsızlık?").

## C2 — Ownership Hybridity → **0.95** ✅

| Alt kanıt | Bulgu (2019) | Kaynak |
|---|---|---|
| Operatör çoğulluğu | 3 bağımsız stevedor: DP World Melbourne, Patrick, VICT (ICTSI — Aralık 2016'da Webb Dock East'te faaliyete geçti, "limanın üçüncü stevedoru") | ESC genel bakış, FullyLoaded/Maritime Executive |
| Kamu operasyonu | Konteyner elleçlemede yok | ESC |

**Gerekçe:** ~%100 özel + ≥3 bağımsız operatör → 0.95.

## C3 — Multi-Level Coordination Density → **0.30 provizyonel** (2⚠️)

| Gösterge | Bulgu | Skor |
|---|---|---|
| 1. Kent–liman organı | Eyalet varlığı; belediye ile daimi organ kaydı yok (PoM topluluk istişaresi var ama kurumsallaşmış temsil organı doğrulanmadı) | 0 ⚠️ |
| 2. Ulusal koordinasyon | Ports Australia = sektör derneği (TÜRKLİM emsali: sayılmaz); ulusal liman koordinasyon organı aktif katılım kaydı yok | 0 ✅ |
| 3. Uluslararası ağ (aktif) | IAPH vb. aktif üyelik doğrulanmadı | ⚠️ |
| 4. Yazılı kriz protokolü | Port Management Act kapsamında yasal Safety and Environment Management Plan (SEMP) yükümlülüğü — yazılı, yasal plan; çok-aktörlü kriz koordinasyonu kapsamı teyit edilecek | 1 ⚠️ |

## C4 — Compound Lock-In → **0.55** (saf finansal kilit profili)

**(a) Düzenleyici katılık → 0.33** ✅ (⚠️ ikinci reform ihtimali)
2005–2019 penceresinde 1 büyük reform: 2016 Delivering Victorian Infrastructure (Port of Melbourne Lease Transaction) Act + Pricing Order rejimi. Başarısız girişim kaydı yok. → 0.33. (2012 liman lisans ücreti düzenlemesi ikinci reform sayılırsa 0'a iner — doküman turunda netleşecek.)

**(b) Finansal kilit (Dal-A) → 1.0** ✅ — FİNANSALLAŞMA UCU DOĞRULANDI
50 yıllık kira, 1 Kasım 2016 → 2066; 2019'da kalan vade = **47 yıl** → >40 bandı = 1.0. Bedel: A$9,7 milyar; kiracı: Future Fund (Avustralya varlık fonu) + QIC + GIP + OMERS (Kanada emeklilik fonu) — kurumsal yatırımcı konsorsiyumu, CFP'nin "financialization" temasının saf örneği. Ek kilit unsuru: yasal yıllık liman lisans ücreti ~A$80M (TÜFE artışlı).
**Pencere dışı ama Ş2 için kritik not:** ESC'nin ilk 5 yıllık denetimi (2016–2021) "significant and sustained non-compliance" buldu — gelir gereksinimi A$300–650M abartılmış. Finansallaşmış landlord'un regülatörle çatışması → Ş2 robustness kodlaması ve Discussion hammaddesi.

**(c) Sosyal meşruiyet açığı → 0.33** ✅
1 belgelenmiş ihtilaf kümesi: **Aralık 2017 VICT/Webb Dock ablukası** — MUA/CFMEU pikedi, Victoria Yüksek Mahkemesi ihtiyati tedbirlerine rağmen süren eylem (tedbir VTHC ve CFMEU sekreterlerini de kapsadı), 1.000+ konteyner bloke, limanın üçüncü stevedoru fiilen kapandı, ~2 hafta. Küme kuralı: tek uyuşmazlık (işe iade/güvenlik kartı) → 1 küme = 0.33.

**Bileşik:** (0.33 + 1.0 + 0.33)/3 = **0.55**
**Analitik not:** Durban ile aynı "orta-yüksek" banda düşmüyor ama kompozisyon ZıT: Durban üç boyutta da kilitli; Melbourne'un kilidi NEREDEYSE TAMAMEN finansal boyutta. Bileşik endeksin alt boyut dekompozisyonu coding sheet'te korunacak — fsQCA bileşiği kullanır, Discussion dekompozisyonu anlatır.

## C5 — Social Value Integration → **0.05~0.40 açık** (⚠️×2)

| Gösterge | Bulgu | Skor |
|---|---|---|
| 1. Bağlayıcı çevre/topluluk mandatı | PoM özel şirket; ancak Port Management Act kapsamında yasal SEMP (çevre yönetim planı) yükümlülüğü → "bağlayıcı çevre yükümlülüğü" sayılabilir | ⚠️ (0/1) |
| 2. Paydaş temsil organı | Daimi topluluk/emek temsil organı yok | 0 ✅ |
| 3. Kirada sosyal/yeşil koşul | Kira paketinde ihracatçı koruması (fiyat kararı) var — ama bu KULLANICI koruması, topluluk/çevre koşulu değil; yeşil koşul kaydı doğrulanmadı | ⚠️ (0/1) |

**Provizyonel:** muhafazakâr 0.05, iyimser 0.40. Doküman turu kararı: SEMP'in kapsamı + kira sözleşmesi kamuya açık özetleri.

---

## ÖZET SATIR (provizyonel)
| C1 | C2 | C3 | C4 | C5 |
|----|----|----|----|-----|
| 0.70 ✅ | 0.95 ✅ | 0.30 ⚠️ | 0.55 ✅ | 0.05~0.40 ⚠️ |

## DÖRT PİLOT — KONFİGÜRASYON UZAYININ DÖRT KÖŞESİ
| Vaka | C1 | C2 | C3 | C4 | C5 | Profil |
|------|----|----|----|----|----|--------|
| Rotterdam | 0.95 | 0.95 | 0.95 | ~0.33 | 0.40 | Özerk-koordineli landlord |
| Mersin | 0.05 | 0.70 | 0.30 | ~0.25 | 0.05 | Otoritesiz tam-imtiyaz |
| Durban | 0.05 | 0.30 | 0.30 | ~0.85 | ~0.55 | Kilitli devlet-operatör |
| Melbourne | 0.70 | 0.95 | 0.30 | 0.55 | ~0.20 | Finansallaşmış özel landlord |

→ Dört satırın hiçbiri diğerinin kopyası değil; her koşulda varyasyon var. Codebook dört uçta da ÇALIŞTI (revizyonlarla). Pilot amacına ulaştı.

## MELBOURNE HOCAM-CHECK (2 karar)
1. Not #12: C1 öznesi = landlord işlevini yürüten aktör (kamu/özel fark etmez); Mersin-Melbourne ayrımı "üçüncü tarafa kiralama testi" ile — onay?
2. Not #13: Üçlü kontrol tipolojisi (vesayet / hissedar hakkı / bağımsız regülatör) — onay?

## BEKLEYEN TOPLAM KARAR KUYRUĞU
Mersin: 5 | Durban: 3 | Melbourne: 2 → **10 karar** → hepsi kapanınca Codebook v2 KİLİT + Design Doc v2 (Melbourne düzeltmesi dahil)
