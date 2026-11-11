#!/usr/bin/env python3
"""Route prompt to critical skills via 5 buckets. Offline, stdlib only."""
import argparse, json, re
SKILLS=[
 ("evidence-appraisal","sharper_judgment","evidence source credible trust claim strength citation study paper data source type tier", "Evaluate how much a source/claim is worth — scorecard + strength 1-5"),
 ("argument-mapping","sharper_judgment","argument valid follow warrant backing logic premise conclusion therefore hence claim grounds Toulmin", "Map whether reasons support the claim — Toulmin + validity tag"),
 ("fallacy-bias-spotting","sharper_judgment","fallacy bias systematic error de-bias reasoning sound cognitive fallacy", "Name the failure mode — 40-item scan + de-bias"),
 ("bayesian-updating","stronger_options","prior base rate Bayes Bayesian likelihood ratio posterior update how much evidence probability odds", "Prior → LR → posterior + base-rate flag"),
 ("socratic-elenchus","better_question","define meaning vague term precisely operationalize concept clarity definition what do you mean", "Socratic chain → operational definition"),
 ("steelman-red-team","broader_perspectives","steelman red team counter strongest counter strawman dissent falsify prove wrong other side", "Steelman strongest rival + red-team attack + falsifier"),
 ("calibration-forecasting","stronger_options","confidence calibrate forecast Brier accurate overconfident bet prediction track record", "Brier-scored forecasts + calibration curve"),
 ("decision-analysis","stronger_options","decision expected value EV utility choose option bet sensitivity analysis which option", "EV sheet + sensitivity + probe"),
]
BUCKETS={
 "sharper_judgment":["credible","source","evidence quality","valid","fallacy","bias","warrant","argument","trust","proof","claim strength","source quality"],
 "better_question":["define","what do you mean","vague","ambiguous","concept","precisely","operationalize","clarify","question","meaning"],
 "broader_perspectives":["other side","counter","steelman","red team","dissent","alternative view","strawman","adversarial","rival"],
 "stronger_options":["prior","base rate","Bayes","update","confidence","forecast","Brier","expected value","choose","bet","uncertainty","decision"],
 "more_ideas":["generate","brainstorm","ideas","creative"],
}
def score_text(text):
    low=text.lower()
    bucket_scores={}
    for b,cues in BUCKETS.items():
        s=sum(1 for c in cues if c.lower() in low)
        bucket_scores[b]=s / max(1,len(cues)/2)
    skill_scores=[]
    for slug,bucket,keywords,desc in SKILLS:
        hits=sum(1 for kw in keywords.split() if kw.lower() in low)
        bonus=bucket_scores.get(bucket,0)*0.5
        score=hits + bonus
        skill_scores.append((slug,bucket,score,desc))
    skill_scores.sort(key=lambda x: x[2], reverse=True)
    for k in bucket_scores:
        bucket_scores[k]=min(1.0, round(bucket_scores[k]*2,3))
    return bucket_scores, skill_scores
def main():
    p=argparse.ArgumentParser(description="Thinking router — critical track")
    p.add_argument("--text",default="",help="Prompt to route")
    p.add_argument("--list",action="store_true",help="List catalog")
    p.add_argument("--json",action="store_true")
    p.add_argument("--verbose",action="store_true")
    p.add_argument("--top",type=int,default=3)
    args=p.parse_args()
    if args.list:
        out=[{"slug":s,"bucket":b,"keywords":k,"desc":d} for s,b,k,d in SKILLS]
        if args.json:
            print(json.dumps(out,indent=2))
        else:
            for r in out:
                print(f"- {r['slug']} [{r['bucket']}] — {r['desc']}")
        return
    if not args.text:
        p.error("provide --text or --list")
    buckets, ranked = score_text(args.text)
    short=[r for r in ranked if r[2]>0][:3]
    if len(short)<2:
        short=ranked[:2]
    out={"text":args.text,"buckets":buckets,"ranked":[{"rank":i+1,"slug":r[0],"bucket":r[1],"score":round(r[2],3),"desc":r[3]} for i,r in enumerate(ranked)],"shortlist":[{"rank":i+1,"slug":r[0],"bucket":r[1],"why":r[3]} for i,r in enumerate(short)]}
    if args.json:
        print(json.dumps(out,indent=2))
    else:
        print(f"Buckets: {buckets}")
        print("Ranked:")
        for i,r in enumerate(ranked,1):
            print(f"  {i}. {r[0]} [{r[1]}] score {r[2]:.2f} — {r[3]}")
        print("Shortlist:")
        for r in short:
            print(f"  - {r[0]} — {r[3]}")
if __name__=="__main__":
    main()
