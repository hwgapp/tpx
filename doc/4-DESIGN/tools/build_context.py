#!/usr/bin/env python3
"""Build the standalone TPX design input from repository sources; no app code."""
from pathlib import Path
import argparse, hashlib, json, os, re, urllib.parse
ROOT=Path(__file__).resolve().parents[3]
DESIGN=ROOT/'doc/4-DESIGN'
VERSION='0.4'
DATE='2026-10-25'
SECTIONS=[('A. Brief sản phẩm và brand','00-design-brief.md'),('B. Design system requirements','02-design-system-requirements.md'),('C. Story/screen/flow/state và policy branches','03-screen-flow-requirements.md'),('D.56component requirements','04-component-inventory.md'),('E. Hai output packages và evidence contract','07-claude-design-output-contract.md'),('J.25detailed journeys','13-detailed-journeys.md'),('K.100case requirements','14-flow-case-matrix.md'),('L. Action/capability gaps và disposition','15-action-contract-gaps.md')]
PRIMARY=['doc/1-BRD/01-decision-log.md','doc/1-BRD/04-business-rules.md','doc/3-TECHNICAL/08-technical-decisions.md','doc/3-TECHNICAL/02-data-model.md']+[f'doc/2-PRD/{n}' for n in ['00-prd-overview.md','01-feature-inventory.md','02-screen-inventory.md','03-user-flows.md','05-route-map.md','06-api-contract-map.md','07-permission-matrix.md','11-review-decisions.md','12-domain-states.md','13-financial-rules.md','16-review-round-1.md']]
def section(text,name):
 marker='## '+name+'\n'
 if marker not in text:raise ValueError('Missing section '+name)
 return text.split(marker,1)[1].split('\n## ',1)[0].strip()
def promote_for_embedding(text):
 return re.sub(r'^(#{1,4}) ',lambda m:'#'*(len(m[1])+2)+' ',text,flags=re.M)
def relocate(text,source):
 def link(m):
  label,target=m[1],m[2]
  if urllib.parse.urlparse(target).scheme or target.startswith('#'):return m[0]
  path,sep,anchor=target.partition('#')
  dest=(source.parent/urllib.parse.unquote(path)).resolve()
  return '['+label+']('+os.path.relpath(dest,DESIGN)+(sep+anchor if sep else '')+')'
 return re.sub(r'\[([^\]\n]*)\]\(([^)\n]+)\)',link,text)
def embed(title,path):
 return '\n\n---\n\n## '+title+'\n\n'+promote_for_embedding(relocate(path.read_text(),path))+'\n'
def build():
 specs=sorted((ROOT/'doc/2-PRD/04-detailed-feature-specs').glob('F-*.md'))
 if len(specs)!=21:raise ValueError('Expected21feature specs')
 counts={'features':len(specs),'feature_AC':0,'logical_screens':63,'components':56,'journeys':25,'cases':100,'surface_cells':190}
 text=f'''# TPX — Context độc lập cho Claude Design

> Brief v{VERSION} · {DATE}. Đính kèm với prompt01. Nội dung nguồn đã nhúng; link repo chỉ để truy vết, không yêu cầu truy cập máy người dùng. Đây là input, chưa có design output hoặc app implementation.

Tạo Design System Package và UI Workflow Package. Phạm vi21feature groups/63screens/56CMP/25J/100FC/190screen×surface cells; source AC bên dưới là116. D-093–100 và review mới nhất ưu tiên trên proposals cũ. OQ-048/049 đã đóng; OQ-050/OQ-042 còn mở và có yêu cầu branch frames. Các P khác có trạng thái từng phần, không mặc định tất cả pending hoặc approved.

Quyền tự chọn visual typography/layout/tokens trong brand #309953/#F9A01B; không tự chốt business. Copy UI tiếng Việt, annotations tách riêng. Giao actual editable artifacts và evidence theo output contract, không chỉ mô tả chữ.
'''
 text+=embed('0. Review mới nhất — cash/points holds và refund giữ earned points',ROOT/'doc/2-PRD/16-review-round-1.md')
 for title,name in SECTIONS[:5]:text+=embed(title,DESIGN/name)
 text+='\n\n---\n\n## F.21source user stories và toàn bộ feature acceptance criteria\n\n[C] là phần đã chốt; [P] đọc trạng thái tại review register. Một feature có nhiều action; không chỉ thiết kế câu user story đầu tiên.\n'
 for index,path in enumerate(specs,1):
  body=path.read_text();title=body.splitlines()[0].removeprefix('# ')
  acs=re.findall(r'^- \*\*(AC-F-\d{3}-\d{2})\*\* (.+)$',body,re.M);counts['feature_AC']+=len(acs)
  text+='\n### US-'+f'{index:03}'+' / '+title+'\n\n'+section(body,'User Story')+'\n\nHành vi:\n\n'+section(body,'Scope và hành vi')+'\n\nInput/validation:\n\n'+section(body,'Dữ liệu vào và validation')+'\n\nAcceptance criteria:\n\n'+'\n'.join('- **'+aid+'** '+content for aid,content in acs)+'\n'
 for title,name in [('G. Review register — confirmed/mixed/proposal theo nguồn','11-review-decisions.md'),('H. Tiền/điểm và source invariants','13-financial-rules.md'),('I. Domain states và guards draft','12-domain-states.md')]:text+=embed(title,ROOT/'doc/2-PRD'/name)
 for title,name in SECTIONS[5:]:text+=embed(title,DESIGN/name)
 sources=[ROOT/p for p in PRIMARY]+specs+[DESIGN/name for title,name in SECTIONS]
 sources=list(dict.fromkeys(sources))
 snapshots=[(str(p.relative_to(ROOT)),hashlib.sha256(p.read_bytes()).hexdigest()) for p in sources]
 text+='\n\n---\n\n## M. Source snapshots\n\nHash nguồn tại lần build; không phải actual design assets. Refresh pack khi nguồn thay đổi.190required cells suy ra trực tiếp từ Screen/surface set trong sectionC; không cần mở link bên ngoài để biết màn nào phải có platform nào.\n\n| Source | SHA256 |\n| --- | --- |\n'+'\n'.join('| '+p+' | '+sha+' |' for p,sha in snapshots)+'\n'
 counts['source_snapshots']=len(snapshots);counts['context_bytes']=len(text.encode())
 if counts['feature_AC']!=116:raise ValueError('Expected116feature AC; update brief/version/counts when sources change')
 if counts['context_bytes']>=256*1024:raise ValueError('Context exceeds256KiB; reduce repetition without dropping requirements')
 return text,counts,snapshots
if __name__=='__main__':
 parser=argparse.ArgumentParser();parser.add_argument('--check',action='store_true');args=parser.parse_args()
 content,counts,_=build();dest=DESIGN/'08-claude-design-context.md'
 if args.check:
  if not dest.exists() or dest.read_text()!=content:raise SystemExit('STALE: run python3 doc/4-DESIGN/tools/build_context.py')
 else:dest.write_text(content)
 print(json.dumps({'status':'CURRENT' if args.check else 'BUILT','brief_version':VERSION,**counts},ensure_ascii=False))
