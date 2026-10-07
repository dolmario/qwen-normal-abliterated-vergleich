"""Own paired practice preparation/checker only. No HTTP, model or server access."""
from pathlib import Path
import json,argparse,hashlib
EXPECTED={
 'with_source':{'port':8091,'context':4096,'backup_serial':None,'source_ids':['A1','A2']},
 'without_source':{'port':None,'context':None,'backup_serial':None,'source_ids':[]}}
def validate(d,condition):
 expected=EXPECTED[condition]
 if not isinstance(d,dict) or set(d)!=set(expected):return False
 if condition=='with_source' and (type(d['port']) is not int or type(d['context']) is not int):return False
 return d==expected
def main():
 ap=argparse.ArgumentParser(description=__doc__);sub=ap.add_subparsers(dest='mode',required=True)
 p=sub.add_parser('prepare');p.add_argument('--output',required=True)
 c=sub.add_parser('check');c.add_argument('--condition',choices=list(EXPECTED),required=True);c.add_argument('--result',required=True)
 a=ap.parse_args()
 if a.mode=='prepare':
  out=Path(a.output).resolve()
  if out.exists():raise SystemExit('Existing output preserved; choose a new folder')
  source='Own synthetic source, not an actual installed server.\n[A1] The fictional learning service uses port8091.\n[A2] Its fictional configured context is4096tokens.\nThe backup power-supply serial number is not recorded.\n'
  prompt='This is a fictional learning service. Use only source facts supplied in this message. Tools, internet and previous chats are unavailable. Return only a JSON object with exactly port, context, backup_serial and source_ids. Unknown values must be actual JSON null, not strings. source_ids must list only supplied supporting source markers, in source order. Do not guess and do not call tools.\n'
  out.mkdir()
  (out/'MIT-QUELLE.txt').write_text(prompt+'\n'+source,encoding='utf-8')
  (out/'OHNE-QUELLE.txt').write_text(prompt+'\nNo source facts are supplied for this task.\n',encoding='utf-8')
  (out/'VORBEREITUNG.json').write_text(json.dumps({'synthetic':True,'files':['MIT-QUELLE.txt','OHNE-QUELLE.txt'],'model_calls':False,'HTTP_calls':False,'same_pair_prompt_per_condition':True},indent=2),encoding='utf-8')
  print('Two own harmless practice prompts prepared; no requests made.')
 else:
  data=json.loads(Path(a.result).read_text(encoding='utf-8-sig'))
  if not validate(data,a.condition):raise SystemExit('FAIL: exact required keys, types, null values or source markers differ')
  print('PASS: limited own synthetic contract, not general intelligence or causal abliteration effect.')
  print(hashlib.sha256(Path(a.result).read_bytes()).hexdigest())
if __name__=='__main__':main()
