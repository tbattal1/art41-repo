# ============================================================================
# ART-41 — fsQCA ANALİZ (QCA + SetMethods)
# Çerçeve: A (eşit-sonuçluluk/"no best model") + B (şok-koşulluluğu) + C (tipoloji)
# Kalibrasyon: A primary (triangle-loss) + B robustness (additive)
# Gereksinim: install.packages(c("QCA","SetMethods"))
# ============================================================================
library(QCA); library(SetMethods)

# ---- 1. VERİ: 5 koşul + ham outcome metrikleri (KONTEYNER, iki şok) ---------
d <- data.frame(
  C1 = c(0.95,0.70,0.70,0.50,0.30,0.70,0.50,0.05,0.50,0.30,0.50,0.50,0.30,0.95,0.70,0.70,0.70,0.30,0.30,0.05,0.30,0.70),
  C2 = c(0.95,0.95,0.95,0.70,0.95,0.30,0.95,0.70,0.30,0.30,0.95,0.95,0.70,0.30,0.95,0.95,0.95,0.95,0.70,0.30,0.95,0.95),
  C3 = c(0.95,0.70,0.70,0.50,0.70,0.30,0.70,0.05,0.50,0.50,0.70,0.30,0.30,0.30,0.50,0.50,0.50,0.50,0.30,0.30,0.30,0.30),
  C4 = c(0.33,0.22,0.33,0.11,0.22,0.44,0.33,0.33,0.33,0.11,0.22,0.56,0.22,0.00,0.67,0.44,0.33,0.33,0.22,0.89,0.22,0.44),
  C5 = c(0.40,0.70,0.70,0.70,0.95,0.40,0.40,0.05,0.40,0.40,0.40,0.05,0.05,0.05,0.70,0.40,0.70,0.40,0.05,0.95,0.05,0.40),
  depth_cov = c(14.4,17.8,6.1,29.5,10.2,13.1,-14.6,0.1,11.2,5.5,11.7,62.7,23.5,-8.6,13.8,16.8,26.8,15.9,12.4,14.7,38.9,18.6),
  hl_cov    = c(6,16,2,3,1,2,0,1,10,1,2,4,4,0,2,1,1,6,13,1,2,5),
  depth_red = c(14.4,19.4,12.5,17.2,-0.5,15.7,2.2,29.4,7.1,1.8,-5.1,2.0,2.9,5.3,26.6,6.9,50.3,3.5,-19.8,16.1,32.4,15.1),
  hl_red    = c(3,3,3,2,0,2,1,5,2,1,0,2,1,2,2,1,2,1,0,2,1,1),
  row.names = c("Rotterdam","Hamburg","Antwerp","Gdansk","Valencia","Piraeus",
                "TangerMed","Mersin","Singapore","Shanghai","Busan","PortKlang",
                "Colombo","JebelAli","LA","NYNJ","Vancouver","Santos",
                "Cartagena","Durban","Lagos","Melbourne")
)
conds <- c("C1","C2","C3","C4","C5")
# fsQCA: tam 0.5 degeri sorunlu (ne iceride ne disarida) -> 0.501 (Ragin 2008)
d[conds] <- lapply(d[conds], function(x) ifelse(x==0.5, 0.501, x))

# ---- 2. OUTCOME KALİBRASYONU -----------------------------------------------
# A (primary): resilience-loss = max(0,depth) * half-life ; DÜŞÜK kayıp -> YÜKSEK direnç
lossA <- function(dep,hl) pmax(0,dep)*hl
d$lossA_cov <- lossA(d$depth_cov,d$hl_cov)
d$lossA_red <- lossA(d$depth_red,d$hl_red)
# azalan kalibrasyon: eşikler DESC (P90>P50>P10) => yüksek kayıp = dışlanır
d$Ycov <- calibrate(d$lossA_cov, type="fuzzy", thresholds=quantile(d$lossA_cov,c(.9,.5,.1)))
d$Yred <- calibrate(d$lossA_red, type="fuzzy", thresholds=quantile(d$lossA_red,c(.9,.5,.1)))

# B (robustness): additive-normalize (derinlik+hız eşit ağırlık), ARTAN
resB <- function(dep,hl){
  r1 <- 1-(dep-min(dep))/(max(dep)-min(dep))   # direnç (sığ dip)
  r2 <- 1-(hl-min(hl))/(max(hl)-min(hl))        # toparlanma (hızlı)
  0.5*r1+0.5*r2
}
d$Ycov_B <- calibrate(resB(d$depth_cov,d$hl_cov), type="fuzzy",
                      thresholds=quantile(resB(d$depth_cov,d$hl_cov),c(.1,.5,.9)))
d$Yred_B <- calibrate(resB(d$depth_red,d$hl_red), type="fuzzy",
                      thresholds=quantile(resB(d$depth_red,d$hl_red),c(.1,.5,.9)))

# negasyon sütunları (~Y = kırılganlık)
d$Ycov_n <- 1-d$Ycov; d$Yred_n <- 1-d$Yred

# ============================================================================
# 3. NECESSITY  — (A: ~C4 yarı-gerekli? / kesin gerekli var mı?)
# ============================================================================
cat("\n########## NECESSITY (incl.cut=0.85) ##########\n")
for(out in c("Ycov","Yred","Ycov_n","Yred_n")){
  cat("\n== outcome:",out,"==\n")
  print(superSubset(d, outcome=out, conditions=conds, incl.cut=0.85, cov.cut=0.5))
}
# C2 skewness uyarısı: nrow(d[d$C2>0.5,])/nrow(d) -> trivial-necessity kontrolü
cat("\nC2>0.5 oranı (skewness):", round(mean(d$C2>0.5),2),
    " | ~C4>0.5 oranı:", round(mean((1-d$C4)>0.5),2), "\n")

# ============================================================================
# 4. SUFFICIENCY  — truth table + minimize
#    A) DİRENÇ (Y): eşit-sonuçluluk beklenir (temiz tek-yol yok)
#    E-altbulgu) KIRILGANLIK (~Y): Durban lock-in yolu (RedSea)
# ============================================================================
dir_exp <- c(C1=1,C2=1,C3=1,C4=0,C5=1)   # teori: iyi-yönetişim + lock-in yokluğu -> direnç

run_suff <- function(out, label){
  cat("\n########## SUFFICIENCY:",label,"(",out,") ##########\n")
  tt <- truthTable(d, outcome=out, conditions=conds,
                   incl.cut=0.80, pri.cut=0.70, show.cases=TRUE, sort.by="incl")
  print(tt)
  cat("\n-- Parsimonious --\n");   print(tryCatch(minimize(tt, include="?", details=TRUE, show.cases=TRUE), error=function(e) e$message))
  cat("\n-- Intermediate --\n");   print(tryCatch(minimize(tt, include="?", dir.exp=dir_exp, details=TRUE, show.cases=TRUE), error=function(e) e$message))
}
run_suff("Ycov",  "COVID direnç")
run_suff("Yred",  "RedSea direnç")
run_suff("Ycov_n","COVID kırılganlık")
run_suff("Yred_n","RedSea kırılganlık")

# ============================================================================
# 5. ROBUSTNESS (B kalibrasyonu) — anahtar sonuçlar tekrar
# ============================================================================
cat("\n########## ROBUSTNESS: B kalibrasyonu ##########\n")
for(out in c("Ycov_B","Yred_B")){
  cat("\n== NEC",out,"==\n"); print(superSubset(d, outcome=out, conditions=conds, incl.cut=0.85, cov.cut=0.5))
  cat("\n== SUFF ~",out," (kırılganlık) ==\n")
  d$tmp <- 1-d[[out]]
  print(truthTable(d, outcome="tmp", conditions=conds, incl.cut=0.80, pri.cut=0.70, show.cases=TRUE, sort.by="incl"))
}

# ============================================================================
# 6. XY PLOTLAR  (A: equifinality diversity | ~C4 necessity | Durban path)
# ============================================================================
# ~C4 (lock-in yokluğu) -> direnç necessity XY
pdf("ART41_XYplots.pdf", width=7, height=6)
XYplot(1-d$C4, d$Ycov, data=d, jitter=TRUE, main="~C4 (no lock-in) -> COVID direnc (NEC)")
XYplot(1-d$C4, d$Yred, data=d, jitter=TRUE, main="~C4 (no lock-in) -> RedSea direnc (NEC)")
# Durban lock-in yolu -> RedSea kırılganlık (SUFF)
d$path_dur <- pmin(1-d$C1,1-d$C2,1-d$C3,d$C4,d$C5)
XYplot(d$path_dur, d$Yred_n, data=d, jitter=TRUE, main="c1c2c3C4C5 -> RedSea kirilganlik (SUFF)")
dev.off()
cat("\n>> XY plotlar: ART41_XYplots.pdf\n")

# ============================================================================
# 7. C — TİPOLOJİ (2. katman): dirençli vakaların yönetişim çeşitliliği
# ============================================================================
cat("\n########## TİPOLOJİ: yüksek-dirençli vakalar (Y>0.6) çeşitliliği ##########\n")
cat("\n-- COVID dirençli --\n"); print(d[d$Ycov>0.6, conds])
cat("\n-- RedSea dirençli --\n"); print(d[d$Yred>0.6, conds])
cat("\n(A tezi: dirençli limanlar yönetişimce ÇEŞİTLİ -> eşit-sonuçluluk)\n")

# kaydet
write.csv(d, "ART41_fsqca_calibrated.csv")
cat("\n>> Kalibre matris: ART41_fsqca_calibrated.csv\n")
