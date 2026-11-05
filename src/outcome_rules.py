"""Shared outcome-metric rules for ART-41 (codebook Section B; K22 windows, K23 mask, K24 pre-shock level)."""
import pandas as pd
RC = "portcalls_container_yoy_r4"; PRE_WEEKS = 8; PRE_TOL = 0.15; EARLY_WEEKS = 4

def halflife(after, target):
    hl = after[after[RC] >= target]
    return int((hl.iloc[0].week_start - after.iloc[0].week_start).days // 7) if not hl.empty else None

def metrics(wk, w0, w1, mask=False, k24=True):
    """Returns depth %, half-life (weeks), trough date, pre-window level, K24 flag, censored flag."""
    w0, w1 = pd.Timestamp(w0), pd.Timestamp(w1)
    win = wk[(wk.week_start >= w0) & wk[RC].notna()].reset_index(drop=True)
    inwin = win[win.week_start <= w1]
    if mask: inwin = inwin[~inwin.iso_week.isin([51, 52, 53, 1])]
    i = int(inwin[RC].idxmin()); tr = win.loc[i]; after = win.loc[i:].reset_index(drop=True)
    pre_s = wk[(wk.week_start < w0) & (wk.week_start >= w0 - pd.Timedelta(weeks=PRE_WEEKS))][RC].dropna()
    pre = float(pre_s.mean()) if len(pre_s) else float('nan')
    early = (tr.week_start - w0).days // 7 < EARLY_WEEKS
    flag = bool(k24 and pd.notna(pre) and abs(pre - 1) > PRE_TOL and early)
    if flag:
        depth = max(0.0, 100 * (1 - tr[RC] / pre))
        hlw = 0 if depth == 0 else halflife(after, tr[RC] + 0.5 * (pre - tr[RC]))
    else:
        depth = 100 * (1 - tr[RC]); hlw = halflife(after, tr[RC] + 0.5 * (1 - tr[RC]))
    cens = hlw is None
    if cens: hlw = int((after.iloc[-1].week_start - tr.week_start).days // 7)
    return round(depth, 1), hlw, str(tr.week_start.date()), (round(pre, 3) if pd.notna(pre) else None), flag, cens
