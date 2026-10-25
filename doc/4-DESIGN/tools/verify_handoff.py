#!/usr/bin/env python3
"""Validate TPX design inputs, mappings and freshness; does not test an app."""
from pathlib import Path
import json, re, sys, urllib.parse
sys.dont_write_bytecode=True
from build_context import ROOT,DESIGN,VERSION,build
checks=[]
def ok(condition,label):
 if not condition:raise AssertionError(label)
 checks.append(label)
def txt(name):return (DESIGN/name).read_text()
def rows(text,pattern):
 return [line.strip('|').split('|') for line in text.splitlines() if re.match(r'^\| '+pattern+r' \|',line)]
def seq(actual,prefix,n,width=3):return actual==[f'{prefix}-{i:0{width}}' for i in range(1,n+1)]
def first(table):return [row[0].strip() for row in table]
def part(text,a,b):return text.split(a,1)[1].split(b,1)[0]
expected,counts,snapshots=build();pack=txt('08-claude-design-context.md')
ok(pack==expected,'standalone pack is current, including source checksums')
ok(counts['context_bytes']<256*1024,'context under256KiB')
screens=rows((ROOT/'doc/2-PRD/02-screen-inventory.md').read_text(),r'S-\d{3}')
ok(seq(first(screens),'S',63),'63 source Screen IDs')
sids=set(first(screens));fids={f'F-{i:03}' for i in range(1,22)}
components=rows(txt('04-component-inventory.md'),r'CMP-\d{3}')
ok(seq(first(components),'CMP',56),'56 stable component IDs')
cids=set(first(components));uses={c[0].strip():set(re.findall(r'S-\d{3}',c[6])) for c in components}
for cid,refs in uses.items():ok(bool(refs) and refs<=sids,cid+' valid screen usage')
flow=txt('03-screen-flow-requirements.md')
for pattern,prefix,n in [(r'US-\d{3}','US',21),(r'UF-\d{3}','UF',13),(r'UC-\d{3}','UC',28)]:ok(seq(first(rows(flow,pattern)),prefix,n),prefix+' contiguous/unique mapping')
screen_targets=rows(part(flow,'## 6.','## 7.'),r'S-\d{3}')
ok(seq(first(screen_targets),'S',63),'63 screen targets')
for row in screen_targets:
 sid=row[0].strip();refs=set(re.findall(r'CMP-\d{3}',row[5]))
 ok(refs and refs<=cids,sid+' valid required components')
 ok(refs=={c for c,ss in uses.items() if sid in ss},sid+' screen/component mapping agrees both ways')
 ok(bool(re.search(r'UC-\d{3}',row[6])),sid+' scenario mapping')
ok('CMP-036' not in next(r[5] for r in screen_targets if r[0].strip()=='S-033'),'admin login has no internal data table')
coverage=rows(txt('09-design-coverage-plan.md'),r'S-\d{3}');cells=[]
surfaces=['WEB_DESKTOP','WEB_MOBILE','APP_IOS','APP_ANDROID','ADMIN_DESKTOP','ADMIN_COMPACT']
ok(seq(first(coverage),'S',63),'63 coverage rows')
for row in coverage:
 sid=row[0].strip();actual={s for s,c in zip(surfaces,row[2:]) if c.strip()=='Expected'}
 required=set(surfaces[:4] if int(sid[2:])<=32 else surfaces[4:])
 ok(actual==required,sid+' exact required surfaces')
 cells.extend((sid,s) for s in actual)
ok(len(cells)==190 and len(set(cells))==190,'190 distinct expected screen/surface cells')
journeys=txt('13-detailed-journeys.md');cases=txt('14-flow-case-matrix.md')
jids=re.findall(r'^## (J-\d{3}) —',journeys,re.M)
ok(seq(jids,'J',25),'25 journey sections')
case_rows=rows(cases,r'FC-\d{3}');ok(seq(first(case_rows),'FC',100),'100 case rows')
caseids=set(first(case_rows));seen_screens=set();seen_features=set()
for jid,body in zip(jids,re.split(r'^## J-\d{3} —[^\n]*\n',journeys,flags=re.M)[1:]):
 ok(len(re.findall(r'^\d+\. ',body,re.M))>=4 and 'Điểm kết thúc / recovery:' in body,jid+' action/recovery structure')
 refs=set(re.findall(r'S-\d{3}',body));ok(refs and refs<=sids,jid+' valid screens');seen_screens|=refs
 ok(set(re.findall(r'FC-\d{3}',body))<=caseids,jid+' valid case refs')
for row in rows(journeys,r'J-\d{3}'):seen_features|=set(re.findall(r'F-\d{3}',row[2]))
ok(seen_features==fids,'journeys cover21feature groups')
ok(seen_screens==sids,'journeys reference all63logical screens')
for row in case_rows:
 ok(len(row)==6,row[0].strip()+' case table width')
 ok(bool(re.search(r'S-\d{3}',row[1])) and set(re.findall(r'S-\d{3}',row[1]))<=sids,row[0].strip()+' actor/screen anchors')
 ok(all(row[i].strip() for i in [2,3,4]) and 'Expected' in row[5],row[0].strip()+' trigger/result/status')
 ok(row[4].strip() in pack,row[0].strip()+' expectation embedded')
ac_count=0
index=(ROOT/'doc/2-PRD/09-acceptance-criteria.md').read_text()
for path in sorted((ROOT/'doc/2-PRD/04-detailed-feature-specs').glob('F-*.md')):
 body=path.read_text();acs=re.findall(r'^- \*\*(AC-F-\d{3}-\d{2})\*\* (.+)$',body,re.M);ac_count+=len(acs)
 ok([a for a,b in acs]==[f'AC-{path.stem}-{i:02}' for i in range(1,len(acs)+1)],path.stem+' stable AC sequence')
 for acid,content in acs:ok(acid in pack and content in pack and acid in index,acid+' source/pack/index retained')
ok(ac_count==116,'116 source AC')
ok(seq(first(rows((ROOT/'doc/2-PRD/06-api-contract-map.md').read_text(),r'API-\d{3}')),'API',119),'119 draft API IDs')
ok(seq(first(rows(txt('15-action-contract-gaps.md'),r'AG-\d{3}')),'AG',16),'16 action-gap records')
# Check actual current rules instead of relying only on the count of files or frames.
wallet=next(r for r in components if r[0].strip()=='CMP-027')
ok('available+held_order+pending_withdrawal' in wallet[-1],'cash wallet includes order hold and withdrawal pending separately')
ok('HOLD' in txt('00-design-brief.md') and 'CAPTURE' in txt('00-design-brief.md') and 'RELEASE' in txt('00-design-brief.md'),'brief has joint hold lifecycle')
ok('giữ nguyên ORDER_EARN' in txt('00-design-brief.md') and 'D-100' in txt('00-design-brief.md'),'brief retains earned points on post-complete refund')
ok('OQ-050' in flow and 'OQ-042' in flow and 'Branch A' in flow and 'Branch B' in flow,'pending policies have explicit alternative frame requirements')
ok('OQ-048/049 đã đóng' in flow,'answered clarifications not reopened')
for fragment in ['Hoàn sau complete có thu hồi earn tương ứng','OQ-049 chưa chốt','P-013–019 chưa được user duyệt.','Total=available+pending;','P-008 chặn dispatch/complete','Cash timing OQ-048 chưa chốt.']:
 for path in DESIGN.glob('*.md'):
  if path.name.startswith(('11-','12-')):continue
  ok(fragment not in path.read_text(),path.name+' no stale selected-policy assertion')
ok('Design System Package' in txt('01-claude-design-prompt.md') and 'UI Workflow Package' in txt('01-claude-design-prompt.md'),'copyable prompt requests both packages')
ok('journey-case-map' in txt('07-claude-design-output-contract.md'),'output contract requires case evidence')
ok('- [x]' not in txt('05-design-review-checklist.md'),'actual design review still unchecked')
for name in ['system','mockups']:ok(not [p for p in (DESIGN/name).rglob('*') if p.is_file() and p.name not in ['.gitkeep','.DS_Store']],name+' no fabricated output')
# Recompute the color arithmetic quoted in the DS brief.
def lum(h):
 v=[int(h[i:i+2],16)/255 for i in (1,3,5)];v=[c/12.92 if c<=.04045 else ((c+.055)/1.055)**2.4 for c in v]
 return sum(c*w for c,w in zip(v,[.2126,.7152,.0722]))
def ratio(a,b):
 lo,hi=sorted([lum(a),lum(b)]);return round((hi+.05)/(lo+.05),2)
ok([ratio('#FFFFFF','#309953'),ratio('#FFFFFF','#F9A01B'),ratio('#FFFFFF','#237B3F'),ratio('#142118','#F9A01B')]==[3.62,2.08,5.28,7.99],'documented contrast arithmetic')
links=0
for path in [*DESIGN.glob('*.md'),ROOT/'PROJECT_STATUS.md',ROOT/'README.md',ROOT/'doc/5-DELIVERY/12-traceability-matrix.md']:
 for target in re.findall(r'(?<!!)\[[^\]\n]+\]\(([^)\n]+)\)',path.read_text()):
  target=target.strip('<>')
  if urllib.parse.urlparse(target).scheme or target.startswith('#'):continue
  dest=urllib.parse.unquote(target.split('#')[0]);links+=1;ok((path.parent/dest).exists(),str(path.relative_to(ROOT))+' link '+dest)
decisions=rows((ROOT/'doc/1-BRD/01-decision-log.md').read_text(),r'D-\d{3}')
ok(seq(first(decisions),'D',101),'101 decision records')
tasks=rows((ROOT/'doc/5-DELIVERY/04-task-status.md').read_text(),r'T-\d{3}')
ok(seq(first(tasks),'T',len(tasks)),'task IDs continuous and unique')
summary=(ROOT/'PROJECT_STATUS.md').read_text()
for state in ['Todo','Ready','Running','Review','Done','Blocked']:
 match=re.search(r'^\| '+state+r' \| (\d+) \|$',summary,re.M)
 ok(match is not None and int(match[1])==sum(r[3].strip()==state for r in tasks),'project/task summary agrees for '+state)
appfiles=sorted(str(p.relative_to(ROOT/'code')) for p in (ROOT/'code').rglob('*') if p.is_file() and p.name!='.DS_Store')
ok(appfiles==['README.md','apps/.gitkeep','packages/.gitkeep','tools/.gitkeep'],'no application skeleton introduced')
print(json.dumps({'status':'PASS','brief_version':VERSION,'checks':len(checks),'local_links':links,**counts,'pending_priority_policies':['OQ-050','OQ-042'],'actual_design_output':'Pending','product_tests':'Not performed'},ensure_ascii=False,indent=2))
