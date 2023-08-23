from hak.pf import f as pf
from hak.pxyf import f as pxyf

# g
# f = lambda v, w: f' {v:>{w}} '
# def f(v, w): return f' {str(v):>{w}} '
f = lambda x: f" {str(x['value']):>{x['width']}} "

t_int = lambda: pxyf({'value': 12, 'width': 10}, '         12 ', f)

def t():
  if not t_int(): return pf('!t_int')
  return 1
