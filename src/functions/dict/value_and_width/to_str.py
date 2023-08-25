from hak.one.string.colour.bright.green import f as g
from hak.one.string.colour.decolour import f as decolour
from hak.pf import f as pf
from hak.pxyf import f as pxyf

def f(x):
  v = str(x['value'])
  delta = len(v) - len(decolour(v))
  w = x['width'] + delta
  return f" {v:>{w}} "

t_int = lambda: pxyf({'value': 12, 'width': 10}, '         12 ', f)
t_yes = lambda: pxyf({'value': g('Y'), 'width': 4}, f"    {g('Y')} ", f)

def t():
  if not t_int(): return pf('!t_int')
  if not t_yes(): return pf('!t_yes')
  return 1
