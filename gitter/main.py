from hak.one.string.colour.bright.cyan import f as cy
from subprocess import run as sprun
from gitter.f_a import f as f_A
from gitter.f_m import f as f_M
from gitter.f_d import f as f_D

# main
def f():
  print(cy("Executing 'git pull'"))
  result = sprun(args=['git', 'pull'], capture_output=True, cwd='.')
  print(cy('result.stdout.decode():')+f' {result.stdout.decode()}')
  print(cy("Executing 'git status -s'"))
  result = sprun(args=['git', 'status', '-s'], capture_output=True, cwd='.')
  q_0=[_ for _ in result.stdout.decode().split("\n") if _]
  result = sprun(
    args=['git', 'ls-files', '--others', '--exclude-standard'],
    capture_output=True,
    cwd='.'
  )
  q_1=[f'?? {_}' for _ in result.stdout.decode().split("\n") if _]
  q = [_ for _ in (q_0+q_1) if not _.endswith('/')]
  d={}
  for j in q:
    z=3
    k, v=j[:z-1], j[z:]
    if k not in d: d[k]=set()
    d[k].add(v)
  __={'??': 'Added', ' D': 'Removed', ' M': 'Updated'}
  if ' M' in d: _=sorted(d[' M'])[0]; f_M(_)
  if '??' in d: _=sorted(d['??'])[0]; f_A(_)
  if ' D' in d: _=sorted(d[' D'])[0]; f_D(_)
  if any([_ in d for _ in [' M', '??', ' D']]): f()
