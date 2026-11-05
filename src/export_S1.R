# Export tables for Supplementary S1 (truth tables, solutions, necessity) from the primary data (v4).
# Run from the repository root after ART41_R1_analysis.R:  Rscript src/export_S1.R
suppressMessages(library(QCA)); conds <- c("C1","C2","C3","C4","C5")
dir.create("results/S1", showWarnings = FALSE)
tie <- function(dd, v = 0.501) { for (c in conds) dd[[c]] <- ifelse(abs(dd[[c]] - 0.5) < 1e-9, v, dd[[c]]); dd }
calibA <- function(dd, q = c(.9, .5, .1)) { dd$lossA_cov <- pmax(0, dd$depth_cov) * dd$hl_cov; dd$lossA_red <- pmax(0, dd$depth_red) * dd$hl_red
  dd$Ycov <- calibrate(dd$lossA_cov, type = "fuzzy", thresholds = quantile(dd$lossA_cov, q)); dd$Yred <- calibrate(dd$lossA_red, type = "fuzzy", thresholds = quantile(dd$lossA_red, q))
  dd$Ycov_n <- 1 - dd$Ycov; dd$Yred_n <- 1 - dd$Yred; dd }
raw <- read.csv("data/conditions_and_raw_outcomes_v4.csv"); rownames(raw) <- raw$port; d <- calibA(tie(raw))
cat("Outcome anchors (loss = depth x half-life; P90 / P50 / P10):\n")
for (v in c("lossA_cov","lossA_red")) cat(v, round(quantile(d[[v]], c(.9,.5,.1)), 2), "\n")
DIR <- list(Ycov = c(C1=1,C2=1,C3=1,C4=0,C5=1), Yred = c(C1=1,C2=1,C3=1,C4=0,C5=1), Ycov_n = c(C1=0,C2=0,C3=0,C4=1,C5=0), Yred_n = c(C1=0,C2=0,C3=0,C4=1,C5=0))
sol_rows <- data.frame()
for (o in names(DIR)) {
  tt <- truthTable(d, outcome = o, conditions = conds, incl.cut = 0.80, pri.cut = 0.70, show.cases = TRUE, complete = FALSE, sort.by = "incl")
  t <- tt$tt; t <- t[t$n > 0, ]; t$cases <- gsub(",", ", ", t$cases)
  write.csv(data.frame(row = rownames(t), t[, c(conds, "OUT", "n", "incl", "PRI", "cases")]), sprintf("results/S1/truth_table_%s.csv", o), row.names = FALSE)
  for (typ in c("conservative", "parsimonious", "intermediate")) {
    m <- tryCatch(switch(typ, conservative = minimize(tt, details = TRUE), parsimonious = minimize(tt, include = "?", details = TRUE),
                         intermediate = minimize(tt, include = "?", dir.exp = DIR[[o]], details = TRUE)), error = function(e) NULL)
    if (is.null(m)) { sol_rows <- rbind(sol_rows, data.frame(outcome = o, type = typ, model = "-", term = "none explained", inclS = NA, PRI = NA, covS = NA, covU = NA, cases = "")); next }
    sols <- if (!is.null(m$i.sol)) unlist(lapply(names(m$i.sol), function(nm) setNames(m$i.sol[[nm]]$solution, paste(nm, paste0("M", seq_along(m$i.sol[[nm]]$solution))))), recursive = FALSE)
            else setNames(m$solution, paste0("M", seq_along(m$solution)))
    for (mn in names(sols)) for (term in sols[[mn]]) {
      x <- pof(term, o, d, relation = "suf")$incl.cov; mem <- compute(term, d)
      sol_rows <- rbind(sol_rows, data.frame(outcome = o, type = typ, model = mn, term = term, inclS = x[1, "inclS"], PRI = x[1, "PRI"], covS = x[1, "covS"],
        covU = NA, cases = paste(rownames(d)[mem > 0.5], collapse = ", "))) } } }
write.csv(sol_rows, "results/S1/solutions.csv", row.names = FALSE)
nec <- data.frame()
for (o in names(DIR)) { s <- superSubset(d, outcome = o, conditions = conds, incl.cut = 0.85, cov.cut = 0.5)$incl.cov
  nec <- rbind(nec, data.frame(outcome = o, expression = rownames(s), s[, c("inclN", "RoN", "covN")])) }
single <- data.frame()
for (o in names(DIR)) for (cn in c(conds, paste0("~", conds))) { x <- pof(cn, o, d, relation = "nec")$incl.cov
  single <- rbind(single, data.frame(outcome = o, condition = cn, inclN = x[1, "inclN"], RoN = x[1, "RoN"], covN = x[1, "covN"])) }
write.csv(nec, "results/S1/necessity_supersubset.csv", row.names = FALSE); write.csv(single, "results/S1/necessity_single.csv", row.names = FALSE)
cat("S1 tables written to results/S1/\n")
