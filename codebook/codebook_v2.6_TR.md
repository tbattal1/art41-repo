# ART-41 — Codebook v2.6 (KİLİT)
**Statü:** KİLİTLİ — 4 vakalık pilot + Batch 1-2 (Hamburg/Antwerp/Gdańsk/Valencia/Pire/Tanger Med) + Batch 3 Asya (Singapur/Şangay/Busan/Port Klang) + Batch 4 (Colombo/Jebel Ali) ile stres-testli; 16 HOCAM kararı (K1–K16) işlenmiş. Ağustos tam kodlaması bu sürümle yapılır; değişiklik ancak belgelenmiş gerekçeyle yeni sürüm olarak açılır (değişiklik günlüğü zorunlu, bkz. Bölüm E).
**Anti-DIPAN kuralı (mutlak):** Kaynağı belgelenmemiş hiçbir kod hücresi truth table'a giremez. Her kod = değer + kaynak + tarih + 1 cümle gerekçe. Kanıtsız hücre = MISSING; tahmin yasak.

---

## BÖLÜM A — KODLAMA KURALLARI

### Genel kurallar
1. **Kaynak hiyerarşisi:** (1) birincil hukuki metin (tüzük, kanun, imtiyaz şartnamesi) > (2) port authority resmi raporu > (3) WB Port Reform Toolkit 2025 / ESPO / ITF-OECD > (4) hakemli literatür > (5) sektör basını (yalnızca olay teyidi, sınıflandırma için değil).
2. **Zaman penceresi:** Koşullar 2019 sonu itibarıyla kodlanır (şok öncesi durum → nedensellik yönü). Reform sayımı penceresi SABİT: **2005–2019** (v2, Not#2). 2019 sonrası büyük governance değişimi coding sheet'e not edilir; Ş2 robustness kodlamasında dikkate alınır.
3. **Çelişen kaynak:** Hiyerarşide üstteki kazanır; çelişki coding sheet'e not edilir.
4. **Bilinmiyor ≠ 0.05:** Kanıtsız hücre MISSING; MISSING'li vaka yedekten değiştirilir.
5. **Düzeltme günlüğü:** Kodlayıcı (Claude dahil) kendi hatasını bulduğunda açık düzeltme kaydı düşer — Melbourne 99→50 yıl emsali; Singapur C4 0.11→0.33 emsali.

### C1 — Regulatory Autonomy
**ÖZNE KURALI (v2, Not#5+#12, K1+K9 onaylı):** C1'in öznesi = landlord/yönetim işlevini FİİLEN yürüten aktör — kamu ya da özel.
**Ayrım testi:** Aktör üçüncü taraf operatörlere kiralama/lisanslama yapıyor mu?
- Yapmıyor (tek-operatör imtiyazcısı, örn. MIP) → özne = kamu taraf (imtiyaz veren/regülatör); operatör serbestisi C2'ye yazılır.
- Yapıyor (örn. PoM, Rotterdam N.V.) → özne = o aktör.

**KONTROL TİPOLOJİSİ (v2, Not#1+#13, K10 onaylı):** Üç kontrol tipi ayrı muamele görür:
| Tip | Örnek | Etki |
|---|---|---|
| (i) Hiyerarşik vesayet (bakanlık onayı, genel bütçe) | Mersin kamu tarafı, TNPA/Transnet | Özerkliği düşürür |
| (ii) Kamu hissedarının genel kurul hakları | Rotterdam (belediye %70 + devlet %30) | DÜŞÜRMEZ |
| (iii) Bağımsız regülatör tavanı | Melbourne (ESC Pricing Order) | Yalnız İLGİLİ karar alanını özerklik dışı sayar |
| (iv) Sovereign-entegre füzyon (K16) | Jebel Ali (PCFC=DP World, Dubai devleti) | DÜŞÜRMEZ — dışsal merkezi onay yok, grup öz-yönetir |

**K16 — SOVEREIGN-ENTEGRE KONTROL (kontrol tipi iv) (v2.6, 08.07.2026, HOCAM onaylı):** Landlord/regülatör + operatör + sahip aynı sovereign devlet grubunda FÜZYON hâlindeyse (ör. Dubai devleti → PCFC + DP World, aynı başkan; sovereign=sahip), K9 özne-testi dejenere olur (ayrışacak taraf yok). Kararları onaylayacak DIŞSAL merkezi otorite bulunmadığından grup üç karar alanını da (tarife/yatırım/imtiyaz) öz-yönetir → vesayet YOK → **C1 = 0.95** (Jebel Ali). **Kritik ayrım:** ayrışma (Singapur: MPA≠PSA + bakanlık dışsal onay → tutelage → 0.50) vs füzyon (Dubai: sovereign yönlendirme = öz-yönetim → 0.95). Not: C2 yine K13 ile kodlanır (korporatize devlet operatörü → kamu-dominant, Jebel Ali 0.30).

**K13 — KORPORATİZE-YERLİ-DEVLET OPERATÖR AYRIMI (v2.3, 08.07.2026, HOCAM onaylı):**
Korporatize ama %100 (ya da çoğunluğu) yerli devlet sermayeli operatör + ayrı statutory-board/idari landlord-regülatör konfigürasyonunda (örn. PSA/Temasek + MPA; SIPG + municipal idare):
- **C1 öznesi = landlord/regülatör otorite** (K9 literal: operatör üçüncü tarafa kiralamaz, işletir → tek-operatör dalı → özne kamu taraf).
- **K10(ii) hissedar-relief YALNIZ hissedarlı korporatize LANDLORD'a uygulanır** (Rotterdam N.V.). Statutory board'a (MPA — hissedarı yok) ve landlord OLMAYAN operatöre (PSA) uygulanmaz.
- Devlet kontrolü pasif genel-kurul hakkı değil aktif hiyerarşik yön ise (SASAC atama + parti gözetimi, Şangay), tip (i) → özerkliği düşürür.
- **Gerekçe:** Korporatizasyon ≠ özelleştirme; C1 (özerklik) ile C2 (mülkiyet hibriditesi) konseptüel ayrımı korunur.

**Skor tablosu (üç karar alanı: tarife / yatırım / imtiyaz-kiralama):**
| Kanıt | Skor |
|---|---|
| Üçü de yönetim organında; vesayet yok | 0.95 |
| İkisi özerk; biri vesayet veya regülatör tavanında | 0.70 |
| Özerk tüzel kişilik var ama stratejik kararlar merkezi onaya tabi | 0.50 |
| Tüzel kişilik var, operasyonel kararlar dahi ulusal sistem içinde | 0.30 |
| Deconcentrated devlet dairesi / korporatize otorite yok | 0.05 |

### C2 — Ownership Hybridity
| Kanıt | Skor |
|---|---|
| Konteyner kapasitesinin >%80'i özel/karma VE ≥2 bağımsız operatör | 0.95 |
| >%80 özel ama tek dominant operatör | 0.70 |
| ~%40–60 karma | 0.50 |
| <%20 özel katılım (konteynerde kamu dominant ama başka yük türlerinde özel varlık VEYA biçimsel landlord yapı) | 0.30 |
| Tam kamu hizmet limanı (hiçbir segmentte anlamlı özel katılım yok) | 0.05 |
**v2 (Not#10, K8 onaylı):** Birincil metrik konteyner payı; çeşitlendirilmiş limanlarda dökme/sıvı özel payı coding sheet'te AYRI SÜTUN olarak tutulur (skoru değiştirmez, Discussion hammaddesi). Durban emsali: konteyner ~%100 kamu + özel dökme + biçimsel landlord → 0.30.
**Not:** Devlet sermayeli yabancı operatör (COSCO, DP World) "özel" sayılır; operatör tipi sütunda işaretlenir.
**K13 (v2.3, HOCAM onaylı):** Korporatize YERLİ-DEVLET mülkiyeti "özel" DEĞİL — kamu-dominant sayılır (≤0.30 bandı). Yukarıdaki COSCO/DP World notu YABANCI operatörün ev-sahibi limanda imtiyaz kazanmasına dairdir; bir ülkenin KENDİ ulusal devlet operatörüne (Temasek/PSA, SIPG) uygulanmaz. Korporatizasyon+kotasyon+azınlık-JV, kamu-dominant kontrolü değiştirmiyorsa 0.30 (Singapur/Şangay emsali).

### C3 — Multi-Level Coordination Density
Dört ikili gösterge, toplam/4:
1. Kurumsallaşmış kent–liman organı (ortak komite, hissedar-belediye organı dahil) — **not:** şehir-devlet/tek-belediye-mülkiyet konfigürasyonunda ayrı kent-liman organı yoksa (entegrasyon devlet-içi hiyerarşi) SAYILMAZ (Singapur/Şangay emsali, C3.2 dikey-hiyerarşi dışlamasıyla simetri).
2. Ulusal liman stratejisi/koordinasyon organına aktif katılım — **v2:** dikey hiyerarşi (bakanlık→KİT→liman) koordinasyon SAYILMAZ (Mersin/Durban emsali); sektör derneği üyeliği (TÜRKLİM, Ports Australia) SAYILMAZ. Yatay çok-paydaşlı çerçeve (tripartit ITM, bölgesel liman entegrasyonu) SAYILIR.
3. Uluslararası ağ üyeliği AKTİF (son 3 yılda belgelenmiş faaliyet; pasif üyelik sayılmaz)
4. Yazılı kriz/iş sürekliliği koordinasyon protokolü — **v2.1 (Not#14, K11 onaylı):** Evrensel yasal zorunluluk olan tesis-ölçekli planlar (ISPS, 5312 AMP, SEMP-tipi yasal planlar) SAYILMAZ — yargı alanındaki her limanda bulundukları için ayırt edici güç taşımazlar. Çıta: limana özgü + çok-aktörlü (belediye/diğer limanlar/hinterland) + yasal asgarinin ötesinde kurumsallaşma (emsal: Rotterdam FERM + CyberNautics + port-ISAC → 1; Mersin 5312 tesis planı → 0; Melbourne SEMP → 0; dijital-paylaşım PCS tek başına → 0)
**Skor:** 4/4=0.95, 3/4=0.70, 2/4=0.50, 1/4=0.30, 0/4=0.05

### C4 — Compound Lock-In (üç alt boyut, ağırlıksız ortalama)
**(a) Düzenleyici katılık (pencere 2005–2019):**
| Durum | Skor |
|---|---|
| ≥2 anlamlı reform | 0 |
| 1 reform | 0.33 |
| 1 reform + belgelenmiş başarısız/tıkanmış sonraki çerçeve reformu (Mersin: Limancılık Kanunu — K2 onaylı) | 0.67 |
| 0 reform (başarısız girişim olsun olmasın) | 1 |
| **Yasalaşmış-ama-uygulanmamış çekirdek reform** (Durban: 2005 Kanunu korporatizasyon emri, 16 yıl — K6 onaylı) | 1 |
**Not (reform tanımı):** "Anlamlı reform" = yapısal YÖNETİŞİM/mülkiyet reformu (korporatizasyon, landlord geçişi, imtiyaz-modeli restrukturasyonu). Altyapı/dijital/spatial-konsolidasyon (Singapur Tuas, digitalPORT@SG) SAYILMAZ; imtiyaz UZATMASI reform değil süreklilik (Port Klang 2010/2013 emsali).

**(b) Finansal kilit — İKİ DALLI (v2, Not#10b, K7 onaylı):**
- **Dal-A (imtiyazlı/kiralı limanlar):** Kapasite-ağırlıklı kalan imtiyaz süresi (2019): <10 yıl=0, 10–25=0.33, 25–40=0.67, >40=1. (Melbourne: 47 yıl → 1; Port Klang: ~32 yıl → 0.67.)
- **Dal-B (devlet-operatör limanlar):** KİT mali kısıtı — üç gösterge: belgelenmiş yatırım açığı / borç servisi baskısı / ekipman yaşı-yenileme açığı. 0 gösterge=0, 1=0.33, 2=0.67, 3=1. (Durban: 3/3 → 1; PSA/SIPG: 0/3 → 0.)
- Dal seçimi coding sheet'te gerekçelendirilir; karma yapılarda dominant yapı esas alınır.
- **K15 — YENİLENEBİLİR/ALAN-BAZLI KİRA SİSTEMİ (v2.5, 08.07.2026, HOCAM onaylı):** Landlord limanda sabit uzun imtiyaz YERİNE yenilenebilir/alan-bazlı kira sistemi varsa (örn. Busan: iskele-alanına göre sabit kira, aktif yeniden yapılandırma, rekabetçi yeniden-ihale) ve kesin kira süresi kaynaklanamıyorsa, C4b kalan-süre yerine **finansal-esneklik kanıtına** göre kodlanır. Batık terminal sermayesi (kilit yönü) ↔ yenilenebilir/renegotiable kira (esneklik yönü) dengesi. Busan emsali: batık capex + yenilenebilir kira → 0.33. Tahminî süre rakamı truth table'a GİRMEZ (anti-DIPAN).

**(c) Sosyal meşruiyet açığı (pencere 2015–2019):**
Belgelenmiş **operasyonel-etkili** ihtilaf KÜMELERİ: 0=0, 1=0.33, 2=0.67, ≥3=1.
**Küme tanımı (v2, Not#3):** Aynı taraflar + aynı talep + <12 ay = 1 olay.
**v2.2 (K12 onaylı — operasyonel kural):** C4c YALNIZ operasyonel kesinti üretebilecek/üretmiş akut ihtilafı ölçer (grev, abluka, throughput'u durduran protesto, imtiyaz iptaline yol açan uyuşmazlık). Süregelen çevre/hukuk davası (Hamburg Elbe dredging, dig-out port itirazları) operasyonel kesintiye dönüşmediyse C4c'ye GİRMEZ; coding sheet'te "yapısal ihtilaf (operasyonel-olmayan)" AYRI SÜTUNDA not edilir. Durban emsali: SDCEA muhalefeti dig-out'u erteletti + grev tehdidi → operasyonel-etkili, sayılır. (Not: finansal iflas/çöküş — Hanjin 2016 — ihtilaf değil, C4c'ye girmez.)
**Zaman notu (v2, Not#7):** Ana analizde 2019'a sabit; robustness'ta Ş2 için 2019–2023 penceresiyle yeniden kodlanır (yalnız C4c).

**Yön notu:** C4 kilitlenme ölçer; hipotez yönü açık bırakılır — fsQCA'nın asimetrik mantığına uygun; Introduction'da açık soru olarak çerçevelenir. (Bulgu: Singapur/Port Klang yüksek C4a + sıfır C4b/C4c = "istikrar-çünkü-optimize" ≠ "kilit-çünkü-tıkalı" — lock-in ↔ disfonksiyon ayrışması, Discussion ekseni.)

### C5 — Social Value Integration
Üç ikili gösterge, toplam/3:
1. Tüzük/kuruluş kanununda BAĞLAYICI çevre/topluluk mandatı (yükümlülük dili; yasal kamu görevi tanımı dahil — Durban emsali; İspanyol TRLPEMM çevre görevi + zorunlu memoria de sostenibilidad → 1)
2. Yönetişimde düzenli toplanan paydaş temsil organı (yasal PCC tipi komiteler dahil — fiilî işlerlik teyidiyle; İspanyol Consejo de Navegación y Puerto, TRLPEMM Md.34 → 1)
3. İmtiyaz/lisans şartlarında sosyal-yeşil koşul (yerel istihdam, B-BBEE, emisyon eşiği, shore power)
**Skor:** 3/3=0.95, 2/3=0.70, 1/3=0.40, 0/3=0.05
**v2 (Not#8):** Gönüllü CSR/yeşil programlar — ne kadar kapsamlı olursa olsun — yapısal entegrasyon SAYILMAZ (Mersin; Singapur MSGI; Malezya gönüllü yeşil-liman politikası emsali).
**v2 (Not#11, analitik):** C5 de jure kurumsallaşmayı, C4c de facto meşruiyeti ölçer; ikisinin ayrışması (Durban profili) çelişki değil BULGUDUR — Discussion belkemiği adayı.
**K14 — EVRENSEL BAĞLAYICI YEŞİL MANDAT (v2.4, 08.07.2026, HOCAM onaylı):** C5.3 için evrensel/ulusal **bağlayıcı** yeşil mandat (zorunlu shore power; ECA/SECA emisyon eşiği; AB rıhtım kükürt mandatı 2010'dan; Çin DECA; Kore Liman Hava Kalitesi Kanunu) SAYILIR. Gerekçe: C5 kurumsallaşmayı ölçer (ayırt-edicilik değil) — K11'in ayırt-edicilik çıtası C3.4/C3.1 içindi, C5 indikatörleri onu istemez. **Bilinen sonuç (kabul edilmiş):** AB rıhtım-mandatı (2010'dan bağlayıcı) tüm AB limanlarında C5.3=1 yapar → C5.3 AB alt-örnekleminde tekdüzeleşir (AB/ECA-limanı proxy'sine yaklaşır); C5 bileşik olduğundan (C5.1/C5.2 ayrıştırır) fsQCA korunur, ama Discussion'da şeffaf raporlanır. **Retroaktif:** Kodlanmış AB vakalarında C5.3 yeniden kontrol edildi (bkz. Bölüm F).

---

## BÖLÜM B — OUTCOME ÇIKARIM PROTOKOLÜ (KİLİT — 07.07.2026, Rotterdam Ş1 pilotuyla)
**KARAR:** Y = **YoY aynı-ISO-hafta oranı** (mevsimsellik-arındırılmış), 4 haftalık yuvarlanan ortalama. Gerekçe: Rotterdam gerçek verisinde LEVEL-raw Noel artefaktına, LEVEL-mask/seasonal erken-2020 kış çukuruna kandı; yalnız YoY gerçek COVID dibini (8 Haziran 2020) buldu. Karar veriyle sınandı.

1. **Veri:** IMF PortWatch liman-düzey günlük → ISO-haftalık (yalnız tam haftalar). Snapshot disiplini: ham veri bir kez çekilir, `art41_snapshots/`'e dondurulur, SHA256 damgalı; tüm analizler dondurulmuş dosyadan.
2. **YoY oranı:** ratio_t = değer(yıl, ISO-hafta) / değer(referans_yıl, aynı ISO-hafta). Referans: **Ş1 → 2019; Ş2 → 2022**. W53→W52 eşlemesi loglanır.
3. **Metrikler:** dip oranı (1−dip = düşüş derinliği %) → dip haftası → %95 eşiğine dönüş (ilk temas + 4 hafta sürdürülmüş) → yarı ömür.
4. **İki metrik sütunu:** toplam portcalls + portcalls_container ayrı raporlanır. fsQCA ana Y'si: [Ağustos'ta ikinci-vaka teyidiyle: konteyner mi toplam mı].
5. **LEVEL'in kaderi:** Ana tanım DEĞİL; robustness ekinde "tanım duyarlılığı".
6. **Repro zinciri:** Her metrik hücresi snapshot dosya adı + SHA + script sürümü (v5) ile belgelenir → GitHub.

**Bilinen zaaflar:** Referans-yılı duyarlılık testi (robustness); Ş2 referans çakışması 2022 ile çözüldü.

## BÖLÜM C — TEST VE ROBUSTNESS PAKETİ
(v1 ile aynı)
- C.1 Test-retest (5 vaka, ≥14 gün, hedef ≥%80) + şeffaf coding sheet
- C.2 Kalibrasyon çapa kaydırma (±1 kademe; P90/P50/P10 → P85/P50/P15)
- C.3 Consistency 0.75/0.80/0.85; PRI ≥0.70; leave-one-out; skewness >%80; simultaneous subset relations
- C.4 Y_COVID vs Y_RedSea ayrı koşular — örtüşme raporu
- C.5 Within-case: 2 tipik + 1 aykırı (opsiyonel)
- Referans: Oana & Schneider protokolü, R `QCA` + `SetMethods`

## BÖLÜM D — PİLOT + BATCH SONUÇ KAYDI
- Pilot 4/4 (Rotterdam, Mersin, Durban, Melbourne) — 07.07.2026
- Batch 1-2 (Hamburg, Antwerp, Gdańsk, Valencia, Pire, Tanger Med) — 08.07.2026
- **Batch 3 Asya (Singapur, Şangay, Busan, Port Klang) — 08.07.2026 → K13/K14/K15 üretildi**
- **Batch 4 (Colombo, Jebel Ali) — 08.07.2026 → 16/22 kodlu, K16 üretildi**
- Kalan: Batch 5-6 (LA, NY/NJ, Vancouver, Santos, Cartagena, Lagos)

## BÖLÜM E — DEĞİŞİKLİK GÜNLÜĞÜ
| Sürüm | Tarih | Değişiklik | Gerekçe | Onay |
|---|---|---|---|---|
| v1 | 07.07.2026 | İlk sürüm | — | — |
| v2 | 07.07.2026 | 13 pilot revizyon notu (özne, kontrol tipolojisi, C4a kademeleri, C4b iki dal, küme tanımı, KSS) | 4 vakalık pilot | K1–K10 |
| v2.1 | 07.07.2026 | C3.4: evrensel yasal tesis planları sayılmaz | Ayırt-edicilik; Not#8 simetri | K11 |
| v2.2 | 08.07.2026 | C4c yalnız operasyonel-etkili akut ihtilaf | Outcome operasyonel → meşruiyet açığı da operasyonel (Schneider & Wagemann condition specification) | K12 |
| **v2.3** | **08.07.2026** | **K13: korporatize-yerli-devlet operatör → C1 özne=landlord/regülatör; K10(ii) yalnız hissedarlı landlord'a; C2'de yerli devlet = kamu-dominant** | **Korporatizasyon ≠ özelleştirme; C1/C2 konseptüel ayrımı korunur (Singapur/Şangay)** | **K13** |
| **v2.4** | **08.07.2026** | **K14: C5.3'e evrensel bağlayıcı yeşil mandat (shore power, ECA/SECA eşiği, AB rıhtım-mandatı, DECA) girer** | **C5 kurumsallaşma ölçer, ayırt-edicilik değil; K11 çıtası C3 içindi (Şangay DECA)** | **K14** |
| **v2.5** | **08.07.2026** | **K15: landlord + yenilenebilir/alan-bazlı kira sistemi → C4b finansal-esneklik kanıtıyla (kalan-süre değil)** | **Codebook Dal-A sabit-imtiyaz varsayar; Busan yenilenebilir kira yapısal boşluk; tahminî süre yasak** | **K15** |
| **v2.6** | **08.07.2026** | **K16: sovereign-entegre kontrol tipi (iv) → füzyonda dış vesayet yok → C1=0.95 (Jebel Ali)** | **K10 tipolojisi Körfez füzyon-modelini kapsamıyordu; ayrışma↔füzyon ayrımı** | **K16** |
**Retroaktif etki (v2.1):** Mersin C3.4 0→teyit; Melbourne C3.4 1⚠️→0; Durban C3.4 ⚠️→0.
**Retroaktif etki (v2.4/K14):** bkz. Bölüm F.

## BÖLÜM F — K14 RETRO KAYDI (AB rıhtım-mandatı, 08.07.2026)
AB kükürt direktifi rıhtımda %0.1 (2010'dan bağlayıcı) → tüm AB limanlarında C5.3=1. Etki:
| Liman | Recorded C5 | K14 sonrası | Değişim | Güven |
|---|---|---|---|---|
| Rotterdam | 0.40 | 0.40 | — (C5.3 zaten 1: shore power/ESI/yeşil imtiyaz) | Yüksek |
| Hamburg | 0.70 | 0.70 | — (C5.3 zaten 1) | Yüksek |
| Antwerp | 0.70 | 0.70 | — (C5.3 zaten 1) | Yüksek |
| Valencia | 0.70 | 0.95 | ↑ (C5.1+C5.2 zaten 1; C5.3 eklendi) | Orta* |
| Gdańsk | 0.40 | 0.70 | ↑ (C5.3 eklendi) | Orta* |
| Pire | 0.05 | 0.40 | ↑ (0/3'ten; matematiksel kesin) | Yüksek |
*Valencia/Gdańsk: orijinal case dosyasındaki C5 kırılımıyla teyit bekliyor (eğer C5.3 zaten 1 idiyse değişmez).
