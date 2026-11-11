#!/usr/bin/env python3
"""Steelman + red-team scaffold. Offline, stdlib only."""
import argparse, json
VECTORS=[
 ("Evidence","Weakest empirical link; what would an expert cite against it?","Cite the study that most undermines the claim and explain why."),
 ("Logic","Hidden premise / equivocation / correlation-as-cause","State the unstated warrant and test it."),
 ("Incentives","Who benefits if the claim is believed?","Name the incentive and the evidence it could distort."),
 ("Alternative explanation","What else produces the same observation?","One rival mechanism with equal fit."),
 ("Cost","What does the claim cost if wrong?","Money, trust, optionality, irreversibility."),
]
def build(claim, position, vectors=5):
    claim=claim.strip()
    rival=position.strip() if position else f"It is not the case that {claim.lower().rstrip('.')}"
    steelman={
        "claim_neg": rival,
        "premises": [
            f"Strongest evidence consistent with \"{rival}\" (state best source).",
            f"Mechanism that would make \"{rival}\" true (causal story).",
            f"Scope condition where \"{rival}\" holds more than the original claim."
        ],
        "concession_owed": "One sub-point the original claim should concede to the rival (be specific).",
        "charity_test": "Would a smart proponent of the rival sign this steelman as fair?"
    }
    attacks=[]
    for i,(name,q,prompt) in enumerate(VECTORS[:vectors]):
        attacks.append({"vector":name,"question":q,"prompt":prompt,"severity":"triage: fatal / serious / survivable","fix_hint":"Fix or price this vector before defending."})
    falsifier=f"I abandon \"{claim}\" if ___ (observable threshold) by ___ (date), and I name now the result I would be tempted to explain away: ___."
    return {"claim":claim,"rival":rival,"steelman":steelman,"attacks":attacks,"falsifier_template":falsifier}
def main():
    p=argparse.ArgumentParser(description="Steelman & red-team scaffold")
    p.add_argument("--claim",required=True,help="Claim to stress-test")
    p.add_argument("--position",default="",help="Explicit rival claim (optional)")
    p.add_argument("--vectors",type=int,default=5,help="Number of attack vectors (1-5)")
    p.add_argument("--json",action="store_true")
    args=p.parse_args()
    n=max(1,min(5,args.vectors))
    out=build(args.claim,args.position,n)
    if args.json:
        print(json.dumps(out,indent=2))
    else:
        print(f"Claim: {out['claim']}")
        print(f"Rival (¬P): {out['rival']}")
        print("\nSteelman — strongest ¬P:")
        for pr in out["steelman"]["premises"]:
            print(f"  - {pr}")
        print(f"  concession: {out['steelman']['concession_owed']}")
        print(f"  test: {out['steelman']['charity_test']}")
        print("\nRed-team vectors:")
        for a in out["attacks"]:
            print(f"  [{a['vector']}] {a['question']}")
            print(f"    → {a['prompt']}")
        print(f"\nFalsifier (pre-commit): {out['falsifier_template']}")
if __name__=="__main__":
    main()
