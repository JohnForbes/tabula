from hak.one.list.is_a import f as is_list
from hak.one.string.is_a import f as is_string
from hak.pf import f as pf
from hak.pxyf import f as pxyf

def f(x):
  if not is_list(x): return pf('!is_list')
  for item in x:
    if not is_string(item): return 0
  return all([j == len(x[0]) for j in [len(x_i) for x_i in x]])

t_1 = lambda: pxyf(['111' for _ in range(4)], 1, f)
t_0 = lambda: pxyf(['111', '1111', '11', '111'], 0, f)

def t():
  if not t_1(): return pf('!t_1')
  if not t_0(): return pf('!t_0')
  return 1
