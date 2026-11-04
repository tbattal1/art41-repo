# =============================================================================
# ART-41 — "No Best Model, Only Best Matches" — fsQCA analysis, revision R1 (Nov 2026)
# R 4.3.3, QCA 3.25, admisc 0.41. No other packages required.
# Inputs : data/conditions_and_raw_outcomes_v3.csv  (22 ports; C1..C5 as coded, pre tie-break;
#          raw outcome metrics: trough depth % and recovery half-life (weeks) for the two shocks,
#          computed by src/july_variants.py on data/snapshots/july2026/ with the acute-phase
#          windows of codebook rule K22: COVID 2020-01-01..2020-09-30, Red Sea 2023-11-19..2024-11-18)
#          data/window_variants/cond_JUL_*.csv   (same conditions, outcomes under alternative windows;
#          used only in the window-sensitivity block of Section 6)
#          data/exposure/exposure_table.csv        (remote conditions E_C, E_R — see codebook v2.8 §C)
# Outputs: results/*.txt and results/*.csv
# Run from the repository root:  Rscript src/ART41_R1_analysis.R
# =============================================================================
suppressMessages(library(QCA))
dir.create("results", showWarnings = FALSE)
sink("results/ART41_R1_analysis_output.txt", split = TRUE)
cat("ART-41 R1 analysis —", format(Sys.time(), "%Y-%m-%d %H:%M %Z"), "\n")
cat(R.version.string, "| QCA", as.character(packageVersion("QCA")), "| admisc", as.character(packageVersion("admisc")), "\n\n")

# ---- 1. Data --------------------------------------------------------------------------------
raw <- read.csv("data/conditions_and_raw_outcomes_v3.csv", stringsAsFactors = FALSE)
rownames(raw) <- raw$port
conds <- c("C1","C2","C3","C4","C5")
ex <- read.csv("data/exposure/exposure_table.csv", stringsAsFactors = FALSE); rownames(ex) <- ex$port
stopifnot(all(rownames(raw) %in% rownames(ex)))

# ---- 2. Calibration -------------------------------------------------------------------------
# Conditions: qualitative anchors in the codebook; cells at exactly 0.50 cannot be assigned to a
# truth-table row and are recoded to 0.501 (Ragin 2008). The alternative 0.499 is run in §6.
tie <- function(dd, v = 0.501) { for (c in conds) dd[[c]] <- ifelse(abs(dd[[c]] - 0.5) < 1e-9, v, dd[[c]]); dd }
# Outcome A (primary): resilience-loss = max(0, depth) x half-life; direct method, anchors P90/P50/P10
# (descending: high loss = non-member). Outcome B (robustness): additive composite.
calibA <- function(dd, q = c(.9, .5, .1)) {
  dd$lossA_cov <- pmax(0, dd$depth_cov) * dd$hl_cov; dd$lossA_red <- pmax(0, dd$depth_red) * dd$hl_red
  dd$Ycov <- calibrate(dd$lossA_cov, type = "fuzzy", thresholds = quantile(dd$lossA_cov, q))
  dd$Yred <- calibrate(dd$lossA_red, type = "fuzzy", thresholds = quantile(dd$lossA_red, q))
  dd$Ycov_n <- 1 - dd$Ycov; dd$Yred_n <- 1 - dd$Yred; dd
}
resB <- function(dep, hl) { 0.5 * (1 - (dep - min(dep)) / (max(dep) - min(dep))) + 0.5 * (1 - (hl - min(hl)) / (max(hl) - min(hl))) }
d <- calibA(tie(raw))
d$Ycov_B <- calibrate(resB(d$depth_cov, d$hl_cov), type = "fuzzy", thresholds = quantile(resB(d$depth_cov, d$hl_cov), c(.1, .5, .9)))
d$Yred_B <- calibrate(resB(d$depth_red, d$hl_red), type = "fuzzy", thresholds = quantile(resB(d$depth_red, d$hl_red), c(.1, .5, .9)))
d$E_C <- ex[rownames(d), "E_C"]; d$E_R <- ex[rownames(d), "E_R"]
d$E_C <- ifelse(abs(d$E_C - 0.5) < 0.002, 0.499, d$E_C)      # Antwerp 0.4998 (documented knife-edge case)
d$E_R[is.na(d$E_R)] <- 0.40                                      # NY-NJ: Q pending; 0.40 and 0.70 give identical results (§7)
write.csv(round(d[, c(conds, "Ycov", "Yred", "Ycov_B", "Yred_B", "E_C", "E_R")], 3), "results/calibrated_matrix_R1.csv")
cat("Calibrated matrix written. Diversity:", length(unique(apply(d[, conds] > 0.5, 1, paste, collapse = ""))), "of 32 rows observed.\n")

# ---- 3. Directional expectations (Table 4.x) ------------------------------------------------
DIR_RES  <- c(C1 = 1, C2 = 1, C3 = 1, C4 = 0, C5 = 1)   # resilience
DIR_FRAG <- c(C1 = 0, C2 = 0, C3 = 0, C4 = 1, C5 = 0)   # fragility = complements (K19)

# ---- 4. Necessity -----------------------------------------------------------------------------
cat("\n########## NECESSITY (incl.cut = 0.85, cov.cut = 0.5) ##########\n")
for (out in c("Ycov", "Yred", "Ycov_n", "Yred_n")) { cat("\n== outcome:", out, "==\n"); print(superSubset(d, outcome = out, conditions = conds, incl.cut = 0.85, cov.cut = 0.5)) }
cat("\nSkewness (share of cases > 0.5):\n"); print(round(sapply(d[, c(conds, "Ycov", "Yred")], function(x) mean(x > 0.5)), 2))

# ---- 5. Sufficiency: conservative (headline) + intermediate ---------------------------------
suff <- function(dd, out, dir, label) {
  cat("\n########## SUFFICIENCY:", label, "(", out, ") ##########\n")
  tt <- truthTable(dd, outcome = out, conditions = conds, incl.cut = 0.80, pri.cut = 0.70, show.cases = TRUE, sort.by = "incl"); print(tt)
  cat("\n-- Conservative (headline) --\n");  print(tryCatch(minimize(tt, details = TRUE, show.cases = TRUE), error = function(e) e$message))
  cat("\n-- Parsimonious --\n");            print(tryCatch(minimize(tt, include = "?", details = TRUE, show.cases = TRUE), error = function(e) e$message))
  cat("\n-- Intermediate (dir.exp:", paste(names(dir), dir, sep = "=", collapse = ","), ") --\n")
  print(tryCatch(minimize(tt, include = "?", dir.exp = dir, details = TRUE, show.cases = TRUE), error = function(e) e$message))
}
suff(d, "Ycov",   DIR_RES,  "COVID resilience");   suff(d, "Yred",   DIR_RES,  "Red Sea window resilience")
suff(d, "Ycov_n", DIR_FRAG, "COVID fragility");    suff(d, "Yred_n", DIR_FRAG, "Red Sea window fragility")

# ---- 6. Robustness (Table 4.y) --------------------------------------------------------------
paths <- list(covid_cons = "~C1*C2*~C3*~C4*~C5", covid_int = "~C1*C2*~C3*~C5", redsea_cons = "~C1*~C2*~C3*C4*C5", redsea_int = "~C1*~C2*~C3*C4")
pofrow <- function(dd, expr, out) { x <- pof(expr, out, dd, relation = "suf")$incl.cov; sprintf("%.3f / %.3f / %.3f", x[1, "inclS"], x[1, "PRI"], x[1, "covS"]) }
consol <- function(dd, out) { tt <- tryCatch(truthTable(dd, outcome = out, conditions = conds, incl.cut = 0.80, pri.cut = 0.70), error = function(e) NULL)
  if (is.null(tt)) return("(no truth table)"); tryCatch(paste(minimize(tt)$solution[[1]], collapse = " + "), error = function(e) "none explained") }
rob <- data.frame()
addrow <- function(dd, label) { rob <<- rbind(rob, data.frame(perturbation = label, covid_path = pofrow(dd, paths$covid_cons, "Ycov_n"), covid_solution = consol(dd, "Ycov_n"),
  redsea_path = pofrow(dd, paths$redsea_cons, "Yred_n"), redsea_solution = consol(dd, "Yred_n"), stringsAsFactors = FALSE)) }
addrow(d, "baseline")
for (v in c(0.78, 0.67)) { dd <- d; dd["Durban", "C4"] <- v; addrow(dd, sprintf("Durban C4 = %.2f", v)) }
for (v in c(0.50, 0.70)) { dd <- raw; dd["Cartagena", "C1"] <- v; addrow(calibA(tie(dd)), sprintf("Cartagena C1 = %.2f", v)) }
addrow(calibA(tie(raw, 0.499)), "tie-break 0.499")
addrow(calibA(tie(raw), c(.85, .5, .15)), "outcome anchors P85/P50/P15")
addrow(calibA(tie(raw), c(.75, .5, .25)), "outcome anchors P75/P50/P25")
dB <- d; dB$Ycov_n <- 1 - dB$Ycov_B; dB$Yred_n <- 1 - dB$Yred_B; addrow(dB, "calibration B (additive)")
# Window sensitivity (K22/K23): same conditions, outcomes recomputed on the July 2026 snapshots under
# alternative measurement windows. J0 = windows de facto used in the submitted version (recovered
# empirically, see codebook K22); A2 = A1 + holiday mask; A3 = Red Sea start 15 Dec 2023;
# F1/F2/F3 = full stated windows (to Dec 2021 / Jun 2025), F2 with holiday mask, F3 with 19 Nov start.
wv <- c(J0_exact = "J0: de facto submitted windows (24 Feb-4 Oct 2020; 26 Nov 2023-26 Sep 2024)",
        A2_acute_mask = "A2: A1 + ISO-week 51-53/1 masked", A3_acute_Dec = "A3: Red Sea start 15 Dec 2023",
        F1_full = "F1: full windows (to 31 Dec 2021 / 1 Oct 2023-30 Jun 2025)", F2_full_mask = "F2: F1 + holiday mask",
        F3_full_Nov19 = "F3: F1 with Red Sea start 19 Nov 2023", NOV2026_A1_acute = "V1: A1 windows on the Nov 2026 PortWatch re-pull")
for (k in names(wv)) { w <- read.csv(sprintf("data/window_variants/cond_%s.csv", if (grepl("^NOV", k)) k else paste0("JUL_", k)), stringsAsFactors = FALSE); rownames(w) <- w$port
  addrow(calibA(tie(w)), wv[[k]]) }
cat("\n########## ROBUSTNESS ##########\n"); print(rob, row.names = FALSE); write.csv(rob, "results/robustness_table.csv", row.names = FALSE)
cat("\n-- Leave-one-out (outcome recalibrated on 21 cases) --\n")
loo <- data.frame()
for (cs in rownames(raw)) { dd <- calibA(tie(raw[rownames(raw) != cs, ])); loo <- rbind(loo, data.frame(dropped = cs, covid_path = pofrow(dd, paths$covid_cons, "Ycov_n"), redsea_path = pofrow(dd, paths$redsea_cons, "Yred_n"))) }
print(loo, row.names = FALSE); write.csv(loo, "results/leave_one_out.csv", row.names = FALSE)

# ---- 7. Two-step: remote exposure conditions (Section 4.6) -----------------------------------
cat("\n########## TWO-STEP: EXPOSURE ##########\n")
for (pr in list(c("E_C", "Ycov_n"), c("E_R", "Yred_n"))) {
  s <- pof(pr[1], pr[2], d, relation = "suf")$incl.cov; n <- pof(pr[1], pr[2], d, relation = "nec")$incl.cov
  cat(sprintf("Step 1  %s -> %s : sufficiency incl %.3f PRI %.3f cov %.3f | necessity inclN %.3f RoN %.3f covN %.3f\n", pr[1], pr[2], s[1, "inclS"], s[1, "PRI"], s[1, "covS"], n[1, "inclN"], n[1, "RoN"], n[1, "covN"]))
}
ctx <- data.frame(port = rownames(d), E_C = round(d$E_C, 2), frag_covid = round(d$Ycov_n, 2), E_R = round(d$E_R, 2), frag_redsea = round(d$Yred_n, 2),
                  ctx_C = ifelse(d$E_C > 0.5, "high", "low"), ctx_R = ifelse(d$E_R >= 0.7, "exposed", ifelse(d$E_R >= 0.4, "partial", "unexposed")))
print(ctx, row.names = FALSE); write.csv(ctx, "results/two_step_contexts.csv", row.names = FALSE)
cat("\nStep 2 (descriptive; no within-context minimisation — K17d). Locked paths within contexts:\n")
for (sub in list(list(d[d$E_C > 0.5, ], "high E_C", "covid_cons", "Ycov_n"), list(d[d$E_C <= 0.5, ], "low E_C", "covid_cons", "Ycov_n"),
                 list(d[d$E_R >= 0.7, ], "exposed E_R", "redsea_cons", "Yred_n"), list(d[d$E_R < 0.4, ], "unexposed E_R", "redsea_cons", "Yred_n")))
  cat(sprintf("  %-14s n=%2d  %s : %s\n", sub[[2]], nrow(sub[[1]]), sub[[3]], tryCatch(pofrow(sub[[1]], paths[[sub[[3]]]], sub[[4]]), error = function(e) "n/a")))
cat("\nSix-condition conservative solutions (information only; exceeds case-to-condition benchmark):\n")
for (pr in list(c("E_C", "Ycov_n"), c("E_R", "Yred_n"))) { tt <- tryCatch(truthTable(d, outcome = pr[2], conditions = c(conds, pr[1]), incl.cut = 0.80, pri.cut = 0.70), error = function(e) NULL)
  cat("  ", pr[2], ":", if (is.null(tt)) "n/a" else tryCatch(paste(minimize(tt)$solution[[1]], collapse = " + "), error = function(e) "none explained"), "\n") }
dd <- d; dd["NYNJ", "E_R"] <- 0.70; s <- pof("E_R", "Yred_n", dd, relation = "suf")$incl.cov
cat(sprintf("\nSensitivity NY-NJ E_R = 0.70: E_R -> Yred_n incl %.3f PRI %.3f (contexts unchanged for all other ports)\n", s[1, "inclS"], s[1, "PRI"]))
sink()
cat("Done. See results/.\n")
