from hak.one.string.is_a import f as is_str
from hak.pxyf import f as pxyf
from hak.pf import f as pf

f = lambda x: is_str(x) and '\n' not in x

t_false = lambda: pxyf(0, 0, f)
t_true = lambda: pxyf('abc', 1, f)

def t():
  if not t_false(): return pf('!t_false')
  if not t_true(): return pf('!t_true')
  return 1
