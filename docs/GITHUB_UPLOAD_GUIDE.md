# GitHub'a Yükleme Rehberi (Hocam için, adım adım)

Bu klasör zaten bir git deposu — ilk commit atılmış durumda. Tek yapman gereken
onu GitHub'a bağlamak. İki yol var; **Yol A (web arayüzü) en kolayı.**

---

## Yol A — GitHub web arayüzüyle (kod satırı derdi yok)

1. github.com → sağ üst **+** → **New repository**
2. Repository name: `port-governance-shock-recovery` (ya da istediğin isim)
3. **Private** seç (submission öncesi gizli kalsın; kabul sonrası public yaparsın)
4. "Add a README" / "Add .gitignore" / "license" seçeneklerini **İŞARETLEME**
   (bizde zaten var, çakışmasın)
5. **Create repository** → açılan sayfada "…or push an existing repository" kutusundaki
   iki satırı kopyala. Sonra bu klasörde (terminalde) şunları çalıştır:

```bash
cd ~/Desktop/ART_41_RTBM_No_best_Model/art41-repo
git remote add origin https://github.com/<KULLANICI_ADIN>/port-governance-shock-recovery.git
git branch -M main
git push -u origin main
```

GitHub kullanıcı adı + parola/token isteyebilir. Parola yerine **Personal Access
Token** gerekir (github.com → Settings → Developer settings → Personal access
tokens → Fine-grained → repo erişimi ver). Token'ı parola alanına yapıştır.

---

## Yol B — GitHub Desktop (grafik arayüz, hiç komut yok)

1. desktop.github.com'dan GitHub Desktop indir, giriş yap
2. **File → Add Local Repository** → bu `art41-repo` klasörünü seç
3. **Publish repository** → Private işaretle → Publish
4. Bitti. Sonraki değişikliklerde sadece "Commit" + "Push" tıklarsın.

---

## Snapshot'ı eklemeyi UNUTMA (kritik!)

Şu an depoda `data/snapshots/` içinde sadece README var — asıl snapshot CSV'si
senin makinende (`art41_snapshots/port1114_S1_raw_20260707.csv`). Reproducibility
için onu depoya kopyalaman şart:

```bash
cp art41_snapshots/port1114_S1_raw_20260707.csv art41-repo/data/snapshots/
cd art41-repo
git add data/snapshots/port1114_S1_raw_20260707.csv
git commit -m "Add Rotterdam S1 raw snapshot (SHA 93af5ebc136e)"
git push
```

Bu dosya olmadan hakem sonuçları tekrar üretemez. Ağustos'ta 22 vaka çekildikçe
her snapshot aynı şekilde eklenecek.

---

## Zenodo bağlantısı (kabul sonrası, DOI için)

RTBM kabul verince: Zenodo → GitHub entegrasyonu ile repoyu bağla, "release"
oluştur → otomatik DOI. NSGA-III+SHAP makalende yaptığın gibi (concept + version
DOI). Böylece makale "Data and code available at [DOI]" satırıyla çıkar.

---

## Ne zaman public yapmalı?

- **Şimdi:** Private kalsın (kör hakemlik anonimliğini bozmasın — repoda adın var).
- **Submission'da:** RTBM çift-kör ise, anonim bir Zenodo/OSF linki ver ya da
  "available upon acceptance" de. Tek-körse doğrudan link verilebilir.
- **Kabul sonrası:** Public + Zenodo DOI.
