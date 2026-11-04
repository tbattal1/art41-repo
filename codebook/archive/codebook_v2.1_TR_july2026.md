# ART-41 — Codebook v2.1 (KİLİT)
**Statü:** KİLİTLİ — 4 vakalık pilotla stres-testli; 10 HOCAM kararı (07.07.2026) + K11 (07.07.2026) işlenmiş. Ağustos tam kodlaması bu sürümle yapılır; değişiklik ancak belgelenmiş gerekçeyle yeni sürüm olarak açılır (değişiklik günlüğü zorunlu, bkz. Bölüm E).
**Anti-DIPAN kuralı (mutlak):** Kaynağı belgelenmemiş hiçbir kod hücresi truth table'a giremez. Her kod = değer + kaynak + tarih + 1 cümle gerekçe. Kanıtsız hücre = MISSING; tahmin yasak.

---

## BÖLÜM A — KODLAMA KURALLARI

### Genel kurallar
1. **Kaynak hiyerarşisi:** (1) birincil hukuki metin (tüzük, kanun, imtiyaz şartnamesi) > (2) port authority resmi raporu > (3) WB Port Reform Toolkit 2025 / ESPO / ITF-OECD > (4) hakemli literatür > (5) sektör basını (yalnızca olay teyidi, sınıflandırma için değil).
2. **Zaman penceresi:** Koşullar 2019 sonu itibarıyla kodlanır (şok öncesi durum → nedensellik yönü). Reform sayımı penceresi SABİT: **2005–2019** (v2, Not#2). 2019 sonrası büyük governance değişimi coding sheet'e not edilir; Ş2 robustness kodlamasında dikkate alınır.
3. **Çelişen kaynak:** Hiyerarşide üstteki kazanır; çelişki coding sheet'e not edilir.
4. **Bilinmiyor ≠ 0.05:** Kanıtsız hücre MISSING; MISSING'li vaka yedekten değiştirilir.
5. **Düzeltme günlüğü:** Kodlayıcı (Claude dahil) kendi hatasını bulduğunda açık düzeltme kaydı düşer — Melbourne 99→50 yıl emsali.

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

### C3 — Multi-Level Coordination Density
Dört ikili gösterge, toplam/4:
1. Kurumsallaşmış kent–liman organı (ortak komite, hissedar-belediye organı dahil)
2. Ulusal liman stratejisi/koordinasyon organına aktif katılım — **v2:** dikey hiyerarşi (bakanlık→KİT→liman) koordinasyon SAYILMAZ (Mersin/Durban emsali); sektör derneği üyeliği (TÜRKLİM, Ports Australia) SAYILMAZ
3. Uluslararası ağ üyeliği AKTİF (son 3 yılda belgelenmiş faaliyet; pasif üyelik sayılmaz)
4. Yazılı kriz/iş sürekliliği koordinasyon protokolü — **v2.1 (Not#14, K11 onaylı):** Evrensel yasal zorunluluk olan tesis-ölçekli planlar (ISPS, 5312 AMP, SEMP-tipi yasal planlar) SAYILMAZ — yargı alanındaki her limanda bulundukları için ayırt edici güç taşımazlar. Çıta: limana özgü + çok-aktörlü (belediye/diğer limanlar/hinterland) + yasal asgarinin ötesinde kurumsallaşma (emsal: Rotterdam FERM + CyberNautics + port-ISAC → 1; Mersin 5312 tesis planı → 0; Melbourne SEMP → 0)
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

**(b) Finansal kilit — İKİ DALLI (v2, Not#10b, K7 onaylı):**
- **Dal-A (imtiyazlı/kiralı limanlar):** Kapasite-ağırlıklı kalan imtiyaz süresi (2019): <10 yıl=0, 10–25=0.33, 25–40=0.67, >40=1. (Melbourne: 47 yıl → 1.)
- **Dal-B (devlet-operatör limanlar):** KİT mali kısıtı — üç gösterge: belgelenmiş yatırım açığı / borç servisi baskısı / ekipman yaşı-yenileme açığı. 0 gösterge=0, 1=0.33, 2=0.67, 3=1. (Durban: 3/3 → 1.)
- Dal seçimi coding sheet'te gerekçelendirilir; karma yapılarda dominant yapı esas alınır.

**(c) Sosyal meşruiyet açığı (pencere 2015–2019):**
Belgelenmiş büyük ihtilaf KÜMELERİ (genişleme davası, ≥3 gün grev, kitlesel kampanya): 0=0, 1=0.33, 2=0.67, ≥3=1.
**Küme tanımı (v2, Not#3):** Aynı taraflar + aynı talep + <12 ay = 1 olay.
**Zaman notu (v2, Not#7):** Ana analizde 2019'a sabit; robustness'ta Ş2 için 2019–2023 penceresiyle yeniden kodlanır (yalnız C4c).

**Yön notu:** C4 kilitlenme ölçer; hipotez yönü açık bırakılır — fsQCA'nın asimetrik mantığına uygun; Introduction'da açık soru olarak çerçevelenir.

### C5 — Social Value Integration
Üç ikili gösterge, toplam/3:
1. Tüzük/kuruluş kanununda BAĞLAYICI çevre/topluluk mandatı (yükümlülük dili; yasal kamu görevi tanımı dahil — Durban emsali)
2. Yönetişimde düzenli toplanan paydaş temsil organı (yasal PCC tipi komiteler dahil — fiilî işlerlik teyidiyle)
3. İmtiyaz/lisans şartlarında sosyal-yeşil koşul (yerel istihdam, B-BBEE, emisyon eşiği, shore power)
**Skor:** 3/3=0.95, 2/3=0.70, 1/3=0.40, 0/3=0.05
**v2 (Not#8):** Gönüllü CSR programları — ne kadar kapsamlı olursa olsun — yapısal entegrasyon SAYILMAZ (Mersin emsali).
**v2 (Not#11, analitik):** C5 de jure kurumsallaşmayı, C4c de facto meşruiyeti ölçer; ikisinin ayrışması (Durban profili) çelişki değil BULGUDUR — Discussion belkemiği adayı.

---

## BÖLÜM B — OUTCOME ÇIKARIM PROTOKOLÜ (KİLİT — 07.07.2026, Rotterdam Ş1 pilotuyla)
**KARAR:** Y = **YoY aynı-ISO-hafta oranı** (mevsimsellik-arındırılmış), 4 haftalık yuvarlanan ortalama. Gerekçe: Rotterdam gerçek verisinde LEVEL-raw Noel artefaktına (21-28 Aralık), LEVEL-mask ve LEVEL-seasonal ise erken-2020 kış/Çin Yeni Yılı çukuruna (10 Şubat) kandı; yalnız YoY gerçek COVID dibini (8 Haziran 2020) buldu. Karar veriyle sınandı, sezgiyle değil.

1. **Veri:** IMF PortWatch liman-düzey günlük seriler → ISO-haftalık toplam (yalnız 7 günü tam haftalar). Snapshot disiplini: ham veri bir kez çekilir, `art41_snapshots/`'e dondurulur, SHA256 damgalı; tüm analizler dondurulmuş dosyadan (API backfill'e karşı tekrarlanabilirlik).
2. **YoY oranı:** ratio_t = değer(yıl, ISO-hafta) / değer(referans_yıl, aynı ISO-hafta). Referans yılı: **Ş1 → 2019; Ş2 → 2022** (Kızıldeniz-öncesi son temiz tam yıl; şok penceresinin referansı kirletmesini önler — iki şok tek felsefeyle ölçülür). W53→W52 eşlemesi loglanır.
3. **Metrikler (YoY oranı üzerinden):** dip oranı (1−dip = düşüş derinliği %) → dip haftası → %95 eşiğine dönüş (ilk temas + 4 hafta sürdürülmüş) → yarı ömür (ek metrik).
4. **İki metrik sütunu:** toplam portcalls + portcalls_container ayrı raporlanır (Rotterdam'da konteyner ~2× daha sert vuruldu — yük-türü asimetrisi Discussion malzemesi). fsQCA ana koşusunun Y'si: **[Ağustos'ta ikinci-vaka teyidiyle kesinleşecek: konteyner mi toplam mı]** — pilot notu bu tek alt-kalemi açık bırakıyor.
5. **LEVEL'in kaderi:** Ana tanım DEĞİL; robustness ekinde "tanım duyarlılığı" olarak raporlanır (C.2 yanına) — okuyucuya mevsimsellik-arındırmanın neden gerektiğini gösteren şeffaflık.
6. **Repro zinciri:** Her metrik hücresi snapshot dosya adı + SHA + script sürümü (v4) ile belgelenir → GitHub.

**Bilinen zaaflar ve karşılıkları (hakem-hazır):**
- Referans-yılı kutsallaştırma → robustness'ta referans-yılı duyarlılık testi (anormal 2019/2022'li limanlar için alternatif referans).
- Ş2 referans çakışması → 2022 referansıyla çözüldü (yukarıda madde 2).

## BÖLÜM C — TEST VE ROBUSTNESS PAKETİ
(v1 ile aynı — değişiklik yok)
- C.1 Test-retest (5 vaka, ≥14 gün, hedef ≥%80) + şeffaf coding sheet (GitHub/supplementary)
- C.2 Kalibrasyon çapa kaydırma (±1 kademe; P90/P50/P10 → P85/P50/P15)
- C.3 Consistency 0.75/0.80/0.85; PRI ≥0.70 (makas >0.20 = çelişkili); leave-one-out; skewness >%80 kontrolü; simultaneous subset relations
- C.4 Y_COVID vs Y_RedSea ayrı koşular — örtüşme raporu (iki sonuç da yayınlanabilir bulgu)
- C.5 Within-case: 2 tipik + 1 aykırı vaka (opsiyonel)
- Referans: Oana & Schneider protokolü, R `QCA` + `SetMethods` [referans cerrahisi kodlama aşamasında]

## BÖLÜM D — PİLOT SONUÇ KAYDI
- Pilot 4/4 tamamlandı (Rotterdam, Mersin, Durban, Melbourne) — 07.07.2026
- 13 revizyon notu üretildi, 10 HOCAM kararıyla işlendi → v2; Not#14/K11 ile → v2.1
- Kalan doğrulama kuyruğu Design Doc v2'de; kural değişikliği GEREKTİRMEZLER (yalnız hücre teyidi)

## BÖLÜM E — DEĞİŞİKLİK GÜNLÜĞÜ
| Sürüm | Tarih | Değişiklik | Gerekçe | Onay |
|---|---|---|---|---|
| v1 | 07.07.2026 | İlk sürüm | — | — |
| v2 | 07.07.2026 | 13 pilot revizyon notu (özne kuralları, kontrol tipolojisi, C4a kademeleri, C4b iki dal, küme tanımı, KSS kuralı) | 4 vakalık pilot stres testi | K1–K10 |
| v2.1 | 07.07.2026 | C3.4: evrensel yasal tesis planları sayılmaz (Not#14) | Ayırt edici güç: herkeste olan şey kimseyi ayırt etmez; Not#8 ile simetri (yasal asgari ↔ gönüllü jest, ikisi de kurumsal tercih değil) | K11 |
**Retroaktif etki (v2.1):** Mersin C3.4 0→teyit; Melbourne C3.4 1⚠️→0 (SEMP yasal asgari); Durban C3.4 ⚠️→0 (ad hoc müdahale + evrensel planlar). Kodlayıcının kendi önceki skoruna kural uygulaması = tutarlılık disiplini kaydı.
