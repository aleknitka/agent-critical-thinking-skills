#!/usr/bin/env python3
"""Bayesian update: prior → LR → posterior. Offline, stdlib only."""
import argparse, json
def posterior_from(prior, lr):
    if not 0 < prior < 1:
        raise ValueError("prior must be in (0,1)")
    if lr <= 0:
        raise ValueError("LR must be >0")
    prior_odds=prior/(1-prior)
    post_odds=prior_odds*lr
    post=post_odds/(1+post_odds)
    return post, prior_odds, post_odds
def main():
    p=argparse.ArgumentParser(description="Bayes: prior → LR → posterior")
    p.add_argument("--prior",type=float,help="Prior probability in (0,1)")
    p.add_argument("--prior-odds",type=float,help="Prior odds (alternative to --prior)")
    p.add_argument("--lr",type=float,help="Likelihood ratio P(E|H)/P(E|~H)")
    p.add_argument("--lrs",default="",help="Comma-separated LRs for sequential update, e.g. 4,0.5,2")
    p.add_argument("--sensitivity",type=float,help="Sensitivity P(pos|H)")
    p.add_argument("--specificity",type=float,help="Specificity P(neg|~H)")
    p.add_argument("--hit-rate",type=float,help="Alias for sensitivity")
    p.add_argument("--false-alarm",type=float,help="P(pos|~H) = 1 - specificity")
    p.add_argument("--base-rate",action="store_true",help="Also show naive posterior (prior 0.5) for comparison")
    p.add_argument("--json",action="store_true")
    args=p.parse_args()
    if args.prior_odds is not None:
        prior=args.prior_odds/(1+args.prior_odds)
    elif args.prior is not None:
        prior=args.prior
    else:
        p.error("provide --prior or --prior-odds")
    lr=args.lr
    if lr is None:
        sens=args.sensitivity if args.sensitivity is not None else args.hit_rate
        spec=args.specificity
        fa=args.false_alarm
        if sens is not None and spec is not None:
            if not 0 < spec < 1: p.error("specificity in (0,1)")
            fa_calc=1-spec
            lr=sens/fa_calc if fa_calc!=0 else float("inf")
        elif sens is not None and fa is not None:
            lr=sens/fa if fa!=0 else float("inf")
        elif args.lrs:
            pass
        else:
            p.error("provide --lr or --sensitivity/--specificity or --lrs")
    lrs=[]
    if args.lrs:
        lrs=[float(x.strip()) for x in args.lrs.split(",") if x.strip()]
        if lr is not None:
            lrs=[lr]+lrs
    elif lr is not None:
        lrs=[lr]
    cur=prior
    steps=[]
    for i, cur_lr in enumerate(lrs):
        post, prior_odds, post_odds = posterior_from(cur, cur_lr)
        steps.append({"step":i+1,"prior":cur,"lr":cur_lr,"prior_odds":prior_odds,"posterior_odds":post_odds,"posterior":post})
        cur=post
    final=steps[-1]
    prod=1
    for x in lrs: prod*=x
    naive=prod/(1+prod)
    gap_pp=round((naive - final["posterior"])*100,2) if args.base_rate else None
    out={"prior":prior,"lrs":lrs,"steps":steps,"posterior":final["posterior"],"posterior_odds":final["posterior_odds"],"product_lr":prod,"naive_posterior":naive,"base_rate_gap_pp":gap_pp}
    if args.json:
        print(json.dumps(out,indent=2))
    else:
        print(f"Prior: {prior}  (odds {prior/(1-prior):.4f})")
        for s in steps:
            print(f"  Step {s['step']}: LR {s['lr']}  prior {s['prior']:.4f} → posterior {s['posterior']:.4f} (odds {s['posterior_odds']:.4f})")
        print(f"Final posterior: {final['posterior']:.4f}")
        print(f"Naive posterior (prior 0.5): {naive:.4f}  — gap {gap_pp} pp" if args.base_rate else "")
if __name__=="__main__":
    main()
