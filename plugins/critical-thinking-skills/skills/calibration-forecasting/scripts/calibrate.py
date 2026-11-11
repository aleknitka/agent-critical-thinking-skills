#!/usr/bin/env python3
"""Brier score + calibration bins. Offline, stdlib only."""
import argparse, json, pathlib
def brier(forecasts):
    if not forecasts:
        return None,None
    n=len(forecasts)
    b=sum((f["p"]-f["o"])**2 for f in forecasts)/n
    baseline=0.25
    skill=1 - b/baseline if baseline else 0
    return b,skill
def calibration(forecasts,bins=5):
    edges=[i/bins for i in range(bins+1)]
    out=[]
    for i in range(bins):
        lo,hi=edges[i],edges[i+1]
        bucket=[f for f in forecasts if (lo <= f["p"] < hi) or (i==bins-1 and f["p"]==hi)]
        if bucket:
            mean_p=sum(f["p"] for f in bucket)/len(bucket)
            freq=sum(f["o"] for f in bucket)/len(bucket)
            out.append({"bin":f"{lo:.1f}-{hi:.1f}","n":len(bucket),"mean_p":round(mean_p,3),"observed_freq":round(freq,3),"gap":round(mean_p-freq,3)})
        else:
            out.append({"bin":f"{lo:.1f}-{hi:.1f}","n":0,"mean_p":None,"observed_freq":None,"gap":None})
    return out
DEMO=[{"p":0.9,"o":1},{"p":0.7,"o":1},{"p":0.6,"o":0},{"p":0.8,"o":1},{"p":0.3,"o":0},{"p":0.55,"o":1},{"p":0.75,"o":0},{"p":0.85,"o":1},{"p":0.4,"o":0},{"p":0.65,"o":1}]
def main():
    p=argparse.ArgumentParser(description="Calibration & Brier scorer")
    p.add_argument("--forecasts",default="",help="JSON file or JSON array string of {p,o}")
    p.add_argument("--demo",action="store_true",help="Use demo forecasts")
    p.add_argument("--json",action="store_true")
    p.add_argument("--markdown",action="store_true",help="Markdown table output")
    args=p.parse_args()
    data=None
    if args.demo:
        data=DEMO
    elif args.forecasts:
        path=pathlib.Path(args.forecasts)
        if path.exists():
            import json as js
            data=js.loads(path.read_text())
        else:
            data=json.loads(args.forecasts)
    else:
        p.error("provide --forecasts or --demo")
    forecasts=[]
    for f in data:
        forecasts.append({"p":float(f["p"]),"o":int(f["o"])})
    b,skill=brier(forecasts)
    cal=calibration(forecasts)
    out={"n":len(forecasts),"forecasts":forecasts,"brier":round(b,4) if b is not None else None,"skill_vs_0.5":round(skill,3) if skill is not None else None,"calibration":cal}
    if args.json:
        print(json.dumps(out,indent=2))
    elif args.markdown:
        print(f"Brier: {out['brier']}  Skill vs 0.5: {out['skill_vs_0.5']}  n={out['n']}")
        print("| bin | n | mean p | observed | gap |")
        print("|---|---|---|---|---|")
        for r in cal:
            print(f"| {r['bin']} | {r['n']} | {r['mean_p']} | {r['observed_freq']} | {r['gap']} |")
    else:
        print(f"Brier: {out['brier']}  Skill vs 0.5: {out['skill_vs_0.5']}  n={out['n']}")
        for r in cal:
            print(f"  {r['bin']}: n={r['n']}  mean_p={r['mean_p']}  observed={r['observed_freq']}  gap={r['gap']}")
if __name__=="__main__":
    main()
