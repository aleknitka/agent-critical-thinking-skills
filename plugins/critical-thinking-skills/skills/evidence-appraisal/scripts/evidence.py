#!/usr/bin/env python3
"""Score a claim's evidence strength 1-5. Offline, stdlib only."""
import argparse, json
TIER_BASE={"meta":5,"rct":4,"observational":3,"obs":3,"case":2,"expert":1.5,"blog":1}
BIAS_PEN={"low":0,"medium":0.5,"high":1}
def score(tier, recency_years, directness, bias):
    base=TIER_BASE[tier]
    rec=0
    if recency_years is not None and recency_years>2:
        if recency_years<=2: rec=0
        elif recency_years<=6: rec=0.25
        elif recency_years<=10: rec=0.5
        elif recency_years<=14: rec=0.75
        else: rec=1.0
    indirect=0.5 if directness=="indirect" else 0
    bpen=BIAS_PEN.get(bias,0)
    raw=base - rec - indirect - bpen
    return max(1.0,min(5.0,round(raw,2))), {"recency_penalty":rec,"indirect_penalty":indirect,"bias_penalty":bpen}
def main():
    p=argparse.ArgumentParser(description="Evidence appraisal — score a claim 1-5")
    p.add_argument("--claim",required=True,help="Claim sentence")
    p.add_argument("--source",default="",help="Source citation (DOI, title, etc.)")
    p.add_argument("--tier",required=True,choices=list(TIER_BASE.keys()),help="Source tier")
    p.add_argument("--n",type=int,default=None,help="Sample size")
    p.add_argument("--effect",default="",help="Effect size string, e.g. d=0.3 or 20%")
    p.add_argument("--recency",type=int,default=None,help="Years since publication/data")
    p.add_argument("--directness",choices=["direct","indirect"],default="direct")
    p.add_argument("--bias",choices=["low","medium","high"],default="low")
    p.add_argument("--json",action="store_true",help="JSON output")
    args=p.parse_args()
    tier=args.tier
    if tier=="obs": tier="observational"
    strength,mods=score(tier,args.recency,args.directness,args.bias)
    if strength>=4.5: interp="decision-grade; act and cite"
    elif strength>=3.5: interp="usable with one caveat; seek one replication"
    elif strength>=2.5: interp="suggestive; not decision-grade alone"
    elif strength>=1.5: interp="hypothesis only; seek better design"
    else: interp="anecdote/opinion; label as such"
    row={"claim":args.claim,"source":args.source,"tier":tier,"n":args.n,"effect":args.effect,"recency_years":args.recency,"directness":args.directness,"bias":args.bias,"strength":strength,"interpretation":interp,"modifiers":mods,"next_probe_suggestion":"find replication / prereg / direct outcome" if strength<4.5 else "monitor for contradictory meta-analysis"}
    if args.json:
        print(json.dumps(row,indent=2))
    else:
        print(f"Claim: {row['claim']}")
        print(f"Source: {row['source'] or '(none)'}  tier={tier}  n={args.n}  effect={args.effect}")
        print(f"Modifiers: recency -{mods['recency_penalty']}  indirect -{mods['indirect_penalty']}  bias -{mods['bias_penalty']}")
        print(f"Strength: {strength}/5 — {interp}")
        print(f"Next probe: {row['next_probe_suggestion']}")
if __name__=="__main__":
    main()
