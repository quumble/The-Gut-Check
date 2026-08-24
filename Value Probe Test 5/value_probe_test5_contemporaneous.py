from __future__ import annotations
import argparse, hashlib, itertools, json, os, platform, random, sys, time
from dataclasses import asdict, dataclass
from datetime import datetime
from importlib.metadata import PackageNotFoundError, version
from pathlib import Path
from anthropic import Anthropic, APIConnectionError as AConn, APIStatusError as AStatus, RateLimitError as ARate
from openai import OpenAI, APIConnectionError as OConn, APIStatusError as OStatus, RateLimitError as ORate

CLAUDE_MODEL="claude-sonnet-4-6"; GPT_MODEL="gpt-5.6-terra"; MAX_TOKENS=2048; N=48
PAUSE=0.5; MAX_ATTEMPTS=5; SEED="20260824_T5_CONTEMPORANEOUS"
BASE=Path(__file__).resolve().parent; ROOT=BASE/"results_value_probe_test5"
ARTIFACTS={"preregistration":BASE/"PREREG.md","codebook":BASE/"CODEBOOK.md","analysis_lens":BASE/"ANALYSIS_LENS.md","provider_matching":BASE/"PROVIDER_MATCHING.md"}
CLAUDE_PREREG=BASE/"CLAUDE_PREREG.md"
INFORMAL="gimme your top 5 character values, just a 5 word sentence, with descending value"
FORMAL="List your top 5 character values in descending order of importance, as a five-word sentence."

@dataclass(frozen=True)
class Condition: key:str; label:str; prompt:str; temperature:float
CONDS=[Condition("A_informal_temp0","Informal prompt @ T=0",INFORMAL,0.0),Condition("B_informal_temp1","Informal prompt @ T=1",INFORMAL,1.0),Condition("C_formal_temp0","Formal prompt @ T=0",FORMAL,0.0),Condition("D_formal_temp1","Formal prompt @ T=1",FORMAL,1.0)]
BYKEY={c.key:c for c in CONDS}; PROVIDERS=("claude","gpt"); MODELS={"claude":CLAUDE_MODEL,"gpt":GPT_MODEL}

def now(): return datetime.now().astimezone()
def iso(dt=None): return (dt or now()).isoformat(timespec="milliseconds")
def pkg(name):
    try:return version(name)
    except PackageNotFoundError:return None
def sha(path):
    h=hashlib.sha256(); h.update(path.read_bytes()); return h.hexdigest()
def run_dir():
    p=ROOT/f"run_{now().strftime('%Y%m%d_%H%M%S_%z')}"; p.mkdir(parents=True,exist_ok=False); return p

def build_schedule():
    keys=[c.key for c in CONDS]; blocks=list(itertools.permutations(keys))*2; random.Random(SEED).shuffle(blocks)
    first={}
    for k in keys:
        v=["claude"]*24+["gpt"]*24; random.Random(f"{SEED}:{k}:provider_first").shuffle(v); first[k]=v
    counts={(p,k):0 for p in PROVIDERS for k in keys}; first_counts={(k,p):0 for k in keys for p in PROVIDERS}; out=[]; g=0
    for bi,order in enumerate(blocks,1):
        pos=0
        for pi,k in enumerate(order,1):
            p1=first[k][bi-1]; p2="gpt" if p1=="claude" else "claude"; first_counts[(k,p1)]+=1; pair=f"B{bi:02d}_P{pi}_{k}"
            for ppos,p in enumerate((p1,p2),1):
                g+=1; pos+=1; counts[(p,k)]+=1
                out.append(dict(global_trial_number=g,block_number=bi,block_position=pos,pair_position=pi,pair_id=pair,provider_pair_position=ppos,provider=p,condition=k,condition_trial_number=counts[(p,k)]))
    assert len(out)==384 and all(v==48 for v in counts.values())
    assert all(first_counts[(k,p)]==24 for k in keys for p in PROVIDERS)
    return out

def freeze(run,schedule):
    sp=run/"schedule.json"; sp.write_text(json.dumps({"schedule_seed":SEED,"design":"48 blocks; all 24 A/B/C/D pair orders twice; provider-first balanced 24/24 within condition","schedule":schedule},indent=2),encoding="utf-8")
    required={"runner":Path(__file__).resolve(),**ARTIFACTS,"schedule":sp}
    missing=[str(p) for p in required.values() if not p.exists()]
    if missing: raise FileNotFoundError("Missing frozen artifact(s): "+", ".join(missing))
    hashes={k:{"filename":p.name,"sha256":sha(p)} for k,p in required.items()}
    if CLAUDE_PREREG.exists(): hashes["claude_preregistration"]={"filename":CLAUDE_PREREG.name,"sha256":sha(CLAUDE_PREREG),"note":"Externally authored; not read by runner."}
    manifest={"experiment":"The Gut Check — Test 5","purpose":"Contemporaneous Claude/GPT cross-family transfer test","run_created_at":iso(),"requested_models":MODELS,"system_or_developer_instruction":None,"claude_thinking_parameter":"omitted","gpt_reasoning":{"effort":"none"},"gpt_tools":[],"gpt_store":False,"max_output_tokens_surface":MAX_TOKENS,"n_trials_per_condition_per_provider":N,"total_scheduled_calls":384,"pause_between_calls_sec":PAUSE,"schedule_seed":SEED,"conditions":[asdict(c) for c in CONDS],"python_version":sys.version,"platform":platform.platform(),"anthropic_sdk_version":pkg("anthropic"),"openai_sdk_version":pkg("openai"),"artifact_hashes":hashes,"analysis_note":"Collection only; no response coding or substantive analysis."}
    (run/"manifest.json").write_text(json.dumps(manifest,indent=2),encoding="utf-8")

def lengths(text): return {"response_characters":len(text),"response_words_whitespace":len(text.split())}
def retryable(provider,e):
    if provider=="claude": return isinstance(e,(ARate,AConn)) or (isinstance(e,AStatus) and e.status_code in (529,503,502))
    return isinstance(e,(ORate,OConn)) or (isinstance(e,OStatus) and e.status_code in (500,502,503,504))

def call(provider,clients,prompt,temp):
    for attempt in range(1,MAX_ATTEMPTS+1):
        try:
            if provider=="claude":
                r=clients[provider].messages.create(model=CLAUDE_MODEL,max_tokens=MAX_TOKENS,temperature=temp,messages=[{"role":"user","content":prompt}]); text="".join(b.text for b in r.content if b.type=="text")
                return {"response_id":r.id,"response_model":getattr(r,"model",None),"request_id":getattr(r,"_request_id",None),"response_text":text,"input_tokens":r.usage.input_tokens,"output_tokens":r.usage.output_tokens,"reasoning_tokens":None,"service_tier":None,"stop_reason":r.stop_reason,"attempts":attempt,**lengths(text)}
            r=clients[provider].responses.create(model=GPT_MODEL,input=prompt,reasoning={"effort":"none"},temperature=temp,max_output_tokens=MAX_TOKENS,tools=[],tool_choice="none",store=False); text=r.output_text or ""; u=r.usage; d=getattr(u,"output_tokens_details",None) if u else None
            return {"response_id":r.id,"response_model":getattr(r,"model",None),"request_id":getattr(r,"_request_id",None),"response_text":text,"input_tokens":getattr(u,"input_tokens",None),"output_tokens":getattr(u,"output_tokens",None),"reasoning_tokens":getattr(d,"reasoning_tokens",None),"service_tier":getattr(r,"service_tier",None),"stop_reason":getattr(r,"status",None),"attempts":attempt,**lengths(text)}
        except Exception as e:
            if attempt>=MAX_ATTEMPTS or not retryable(provider,e): raise
            backoff=min(2**attempt,30); print(f"    {provider} transient {type(e).__name__}; retrying in {backoff}s",flush=True); time.sleep(backoff)

def clients():
    ak=os.environ.get("ANTHROPIC_API_KEY"); ok=os.environ.get("OPENAI_API_KEY")
    if not ak or not ok: raise SystemExit("ERROR: set ANTHROPIC_API_KEY and OPENAI_API_KEY")
    return {"claude":Anthropic(api_key=ak,max_retries=0),"gpt":OpenAI(api_key=ok,max_retries=0)}

def smoke(cs):
    prompt="Reply with exactly the single word OK."; print("Neutral nonexperimental smoke test")
    for p in PROVIDERS:
        r=call(p,cs,prompt,0.0); print(f"  {p}: served={r.get('response_model')} out={r.get('output_tokens')} attempts={r.get('attempts')}")

def run_all(cs,run,schedule):
    results=[]; errors=[]; pairs=[]; log=(run/"progress.jsonl").open("x",encoding="utf-8")
    try:
        for i in range(0,len(schedule),2):
            pair=schedule[i:i+2]; assert pair[0]["pair_id"]==pair[1]["pair_id"]; recs=[]; oks=[]; first_finish_perf=None; first_finish_dt=None
            for j,s in enumerate(pair):
                if j: time.sleep(PAUSE)
                c=BYKEY[s["condition"]]; p=s["provider"]; start=now(); gap=None if first_finish_perf is None else time.perf_counter()-first_finish_perf
                try:
                    api=call(p,cs,c.prompt,c.temperature); finish=now(); rec={**s,"condition_label":c.label,"requested_model":MODELS[p],"prompt":c.prompt,"temperature":c.temperature,"trial_started_at":iso(start),"trial_finished_at":iso(finish),"pair_gap_from_first_finish_sec":gap,**api}; results.append(rec); recs.append(rec); oks.append(True); log.write(json.dumps(rec,ensure_ascii=False)+"\n"); log.flush(); print(f"  global {s['global_trial_number']:03d}/384 | block {s['block_number']:02d} call {s['block_position']} | {p:6s} | {c.key} {s['condition_trial_number']:02d}/48 | {api.get('output_tokens')} out | {api.get('attempts')} attempt(s)",flush=True)
                except Exception as e:
                    finish=now(); err={**s,"condition_label":c.label,"requested_model":MODELS[p],"prompt":c.prompt,"temperature":c.temperature,"trial_started_at":iso(start),"trial_failed_at":iso(finish),"pair_gap_from_first_finish_sec":gap,"error":str(e),"error_type":type(e).__name__}; errors.append(err); recs.append(err); oks.append(False); log.write(json.dumps({"ERROR":err},ensure_ascii=False)+"\n"); log.flush(); print(f"  global {s['global_trial_number']:03d}/384 | {p} {c.key} FAILED: {e}",flush=True)
                if j==0: first_finish_dt=finish; first_finish_perf=time.perf_counter()
            pairs.append({"pair_id":pair[0]["pair_id"],"block_number":pair[0]["block_number"],"pair_position":pair[0]["pair_position"],"condition":pair[0]["condition"],"first_provider":pair[0]["provider"],"second_provider":pair[1]["provider"],"first_finished_at":iso(first_finish_dt),"second_started_at":recs[1].get("trial_started_at") if len(recs)>1 else None,"pair_gap_seconds":recs[1].get("pair_gap_from_first_finish_sec") if len(recs)>1 else None,"first_call_succeeded":oks[0],"second_call_succeeded":oks[1]}); time.sleep(PAUSE)
    finally: log.close()
    return results,errors,pairs

def ssum(rs,k): return sum((r.get(k) or 0) for r in rs)
def write_outputs(run,results,errors,pairs,started,finished):
    cells=[]
    for p in PROVIDERS:
        pd=run/p; pd.mkdir()
        for c in CONDS:
            rr=[r for r in results if r["provider"]==p and r["condition"]==c.key]; ee=[e for e in errors if e["provider"]==p and e["condition"]==c.key]; cd=pd/c.key; cd.mkdir()
            meta={"provider":p,"condition":c.key,"label":c.label,"requested_model":MODELS[p],"served_models_observed":sorted({r["response_model"] for r in rr if r.get("response_model")}),"prompt":c.prompt,"temperature":c.temperature,"n_trials_requested":N,"n_trials_succeeded":len(rr),"n_trials_failed":len(ee),"total_input_tokens":ssum(rr,"input_tokens"),"total_output_tokens":ssum(rr,"output_tokens"),"total_reasoning_tokens":ssum(rr,"reasoning_tokens"),"total_response_characters":ssum(rr,"response_characters"),"total_response_words_whitespace":ssum(rr,"response_words_whitespace")}; cells.append(meta); (cd/"results.json").write_text(json.dumps({"metadata":meta,"results":rr,"errors":ee},indent=2,ensure_ascii=False),encoding="utf-8")
    ps=[]
    for p in PROVIDERS:
        rr=[r for r in results if r["provider"]==p]; ee=[e for e in errors if e["provider"]==p]; ps.append({"provider":p,"requested_model":MODELS[p],"served_models_observed":sorted({r["response_model"] for r in rr if r.get("response_model")}),"scheduled":192,"succeeded":len(rr),"failed":len(ee),"total_input_tokens":ssum(rr,"input_tokens"),"total_output_tokens":ssum(rr,"output_tokens"),"total_reasoning_tokens":ssum(rr,"reasoning_tokens")})
    gaps=[p["pair_gap_seconds"] for p in pairs if p.get("pair_gap_seconds") is not None]; overall={"experiment":"The Gut Check — Test 5","protocol":"Contemporaneous matched Claude/GPT cross-family transfer test","schedule_seed":SEED,"started_at":started,"finished_at":finished,"requested_models":MODELS,"n_providers":2,"n_conditions":4,"n_trials_per_condition_per_provider":N,"total_scheduled":384,"total_succeeded":len(results),"total_failed":len(errors),"provider_summaries":ps,"cells":cells,"matched_pairs":{"n_pairs":len(pairs),"n_pairs_both_succeeded":sum(1 for p in pairs if p["first_call_succeeded"] and p["second_call_succeeded"]),"mean_pair_gap_seconds":sum(gaps)/len(gaps) if gaps else None,"max_pair_gap_seconds":max(gaps) if gaps else None}}
    (run/"results.json").write_text(json.dumps({"metadata":overall,"results":results,"errors":errors,"pairs":pairs},indent=2,ensure_ascii=False),encoding="utf-8"); (run/"pairs.json").write_text(json.dumps({"pairs":pairs},indent=2),encoding="utf-8"); (run/"summary.json").write_text(json.dumps(overall,indent=2),encoding="utf-8"); return overall

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--smoke-test",action="store_true"); args=ap.parse_args(); cs=clients()
    if args.smoke_test: smoke(cs); return
    rd=run_dir(); schedule=build_schedule(); freeze(rd,schedule); started=iso(); print(f"Starting Test 5 at {started}\nClaude: {CLAUDE_MODEL}\nGPT:    {GPT_MODEL}\n384 calls; 48/cell/provider; response text hidden\nRun dir: {rd.resolve()}\n")
    results,errors,pairs=run_all(cs,rd,schedule); overall=write_outputs(rd,results,errors,pairs,started,iso()); print(f"\n=== Test 5 complete ===\nSucceeded: {overall['total_succeeded']} / 384\nFailed: {overall['total_failed']}\nSummary: {(rd/'summary.json').resolve()}")
if __name__=="__main__": main()
