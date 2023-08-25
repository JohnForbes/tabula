# from hak.one.dict.get_or_zero import f as v_or_0
# from hak.one.number.int.is_a import f as is_int
from hak.one.bool.is_a import f as is_bool
from hak.one.dict.rate.is_a import f as is_rate
from hak.one.dict.rate.make import f as rate
from hak.one.dict.rate.to_str_frac import f as rate_to_str
from hak.one.is_0 import f as is_0
from hak.one.is_none import f as is_none
from hak.one.number.float.is_a import f as is_float
from hak.one.string.colour.bright.green import f as g
from hak.one.string.colour.bright.red import f as r
from hak.pf import f as pf
from hak.pxyf import f as pxyf

from src.functions.dict.cell.make import f as cell

# src.cell.to_str
# to_str
def f(x):
  v = x['value']
  if  is_none(v): return ' '
  if  is_rate(v): return rate_to_str(v)
  if  is_bool(v): return g('Y') if v else r('N')
  if     is_0(v): return ' '
  if is_float(v): return f"{v:.2f}"
  return str(v)

# def f(x):
#   if is_int(x['value']): return str(x['value'])

#   if is_bool(x['value']): return g('Y') if x['value'] else r('N')
#   if x['value'] is None: return ' '
#   if x['value'] == 0: return ' '
#   if is_float(x['value']): return f"{x['value']:.2f}"
#   _val_str = str(x['value'])
#   _width = v_or_0(x, 'width')
#   return ' '*_width + f'{_val_str:>{_width}}'

t_0 = lambda: pxyf(cell({'value':     0, 'field_name':   'i'}),    ' ', f)
t_a = lambda: pxyf(cell({'value':     1, 'field_name':   'b'}),    '1', f)
t_b = lambda: pxyf(cell({'value':    10, 'field_name':   'i'}),   '10', f)
t_c = lambda: pxyf(cell({'value':   '0', 'field_name':   'b'}),    ' ', f)
t_d = lambda: pxyf(cell({'value':   'a', 'field_name':   'A'}),    'a', f)
t_e = lambda: pxyf(cell({'value':   1.0, 'field_name': 'foo'}), '1.00', f)
t_f = lambda: pxyf(cell({'value':  None, 'field_name': 'foo'}),    ' ', f)
t_g = lambda: pxyf(cell({'value':  True, 'field_name':   'B'}), g('Y'), f)
t_h = lambda: pxyf(cell({'value': False, 'field_name':   'B'}), r('N'), f)

t_i = lambda: pxyf(
  cell({'value': rate(2, 1, {'a': 1}), 'field_name': 'a'}),
  '2',
  f
)

t_j = lambda: pxyf(
  cell({'value': rate(710, 113, {'a': 1}), 'field_name': 'foo'}),
  '710/113',
  f
)


def t():
  if not t_a(): return pf('t_a failed')
  if not t_0(): return pf('t_0 failed')
  if not t_b(): return pf('t_b failed')
  if not t_c(): return pf('t_c failed')
  if not t_d(): return pf('t_d failed')
  if not t_e(): return pf('t_e failed')
  if not t_f(): return pf('t_f failed')
  if not t_g(): return pf('t_g failed')
  if not t_h(): return pf('t_h failed')
  if not t_i(): return pf('t_i failed')
  if not t_j(): return pf('t_j failed')
  return 1
