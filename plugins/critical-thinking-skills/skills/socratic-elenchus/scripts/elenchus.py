#!/usr/bin/env python3
"""Generate Socratic probes for a term + definition. Offline, stdlib only."""
import argparse, json

def probes(term, definition, counterexample=""):
    t=term.strip()
    d=definition.strip()
    probes_list=[]
    probes_list.append({"type":"necessary_condition","question":f"What must be true for something to count as {t}? Is that true in your definition?","hint":"List necessary conditions separately before combining."})
    probes_list.append({"type":"sufficient_condition","question":f"What would be sufficient for {t}? Does your definition cover clear cases while excluding near-misses?","hint":"Test with a positive and a negative exemplar."})
    probes_list.append({"type":"counterexample_over","question":f"Can you name something that satisfies \"{d}\" but should NOT count as {t}?","hint":"Over-inclusive counterexample — the definition is too broad."})
    probes_list.append({"type":"counterexample_under","question":f"Can you name something that IS {t} but fails \"{d}\"?","hint":"Under-inclusive counterexample — the definition is too narrow."})
    probes_list.append({"type":"boundary","question":f"What is a boundary case for {t} that your definition should handle explicitly?","hint":"e.g. angry daily user for 'engagement'."})
    probes_list.append({"type":"operationalize","question":f"How would you measure or decide {t} in practice under your definition? What would two judges count or observe?","hint":"State a counting/observation rule; agreement test on cases A/B."})
    probes_list.append({"type":"revision","question":f"Revise: can you restate {t} in one sentence that survives the counterexamples above?","hint":"One sentence, necessary + sufficient; avoid examples/synonyms."})
    if counterexample:
        probes_list.append({"type":"counterexample_given","question":f'You offered counterexample "{counterexample}" — how does it break the definition, and what revision does it force?',"hint":"Classify as over/under-inclusive and patch exactly that."})
    operational=f"Operational definition draft: count/observe ___ when {t} defined as '{d}' → threshold/rule ___ → judge-agreement test on cases A/B."
    return {"term":t,"definition":d,"counterexample":counterexample,"probes":probes_list,"operational_prompt":operational}

def main():
    p=argparse.ArgumentParser(description="Socratic elenchus probe generator")
    p.add_argument("--term",required=True,help="Vague term to clarify")
    p.add_argument("--definition",required=True,help="Current definition sentence")
    p.add_argument("--counterexample",default="",help="Known counterexample (optional)")
    p.add_argument("--json",action="store_true")
    args=p.parse_args()
    out=probes(args.term,args.definition,args.counterexample)
    if args.json:
        print(json.dumps(out,indent=2))
    else:
        print(f"Term: {out['term']}")
        print(f"Definition: {out['definition']}")
        if out["counterexample"]:
            print(f"Counterexample: {out['counterexample']}")
        print()
        for i,pr in enumerate(out["probes"],1):
            print(f"{i}. [{pr['type']}] {pr['question']}")
            print(f"   hint: {pr['hint']}")
        print(f"\n{out['operational_prompt']}")

if __name__=="__main__":
    main()
