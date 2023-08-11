from src.cell.make import f as make_cell
from hak.pxyz import f as pxyz
from hak.pf import f as pf
# from hak.one.bool.is_a import f as is_bool
# from hak.one.dict.get_or_zero import f as v_or_0
# from hak.one.dict.rate.is_a import f as is_a_rate
# from hak.one.dict.rate.to_str import f as rate_to_str
# from hak.one.number.float.is_a import f as is_float
# from hak.one.string.colour.bright.green import f as g
# from hak.one.string.colour.bright.red import f as r
# from hak.one.number.int.is_a import f as is_int

# to_str
f = lambda x: str(x['value'])

# def f(x):
#   if is_int(x['value']): return str(x['value'])

#   if is_a_rate(x['value']): return rate_to_str(x['value'])
#   if is_bool(x['value']): return g('Y') if x['value'] else r('N')
#   if x['value'] is None: return ' '
#   if x['value'] == 0: return ' '
#   if is_float(x['value']): return f"{x['value']:.2f}"
#   _val_str = str(x['value'])
#   _width = v_or_0(x, 'width')
#   return ' '*_width + f'{_val_str:>{_width}}'

def t_a():
  x = {'value': 'a'}
  y = 'a'
  z = f(make_cell(**x))
  return pxyz(x, y, z)

def t_0():
  x = {'value': 0}
  y = '0'
  z = f(make_cell(**x))
  return pxyz(x, y, z)

def t_10():
  x = {'value': 10}
  y = '10'
  z = f(make_cell(**x))
  return pxyz(x, y, z)

def t():
  if not t_a(): return pf('t_a failed')
  if not t_0(): return pf('t_0 failed')
  if not t_10(): return pf('t_10 failed')
  return True
