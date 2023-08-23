from hak.pf import f as pf
from hak.pxyf import f as pxyf

f = lambda x: f" {x['value']:>{x['width']}} "

t_int = lambda: pxyf({'value': 12, 'width': 10}, '         12 ', f)

def t():
  if not t_int(): return pf('!t_int')
  return 1
