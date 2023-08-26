# from hak.one.dict.cell.to_str import f as to_str
# from hak.one.dict.get_or_default import f as get_or_default
# from hak.one.dict.rate.is_a import f as is_rate
# from hak.one.dict.rate.to_float import f as to_float
# from hak.one.dict.rate.to_num import f as to_num
# from hak.one.string.colour.decolour import f as decol
from datetime import date
from hak.many.dicts.a_into_b import f as a_into_b
from hak.one.dict.rate.make import f as make_rate
from hak.one.get_datatype import f as detect_type
from hak.pf import f as pf
from hak.pxyf import f as pxyf
from hak.pxyz import f as pxyz
from hak.one.number.int.random.make import f as make_random_integer
from hak.one.string.random.make import f as make_random_string

# make_cell
# src.cell.make
f = lambda x: a_into_b({'datatype': detect_type(x['value'])}, x)

# def f(x):
#   _width = x['width']
#   _format = get_or_default(x, 'format', None)
#   _val_str = (
#     (
#       _format(x['value'])
#       if x['value'] else
#       ''
#     )
#     if _format else (
#       (
#         rate_to_str(x['value'])
#         if to_num(x['value']) else
#         ''
#       )
#       if is_rate(x['value']) else
#       to_str(x['value'])
#     )
#   )
  
#   _ = _width - len(decol(f'{_val_str:>{_width}}'))
#   left_pad = ' '*_
#   return left_pad + f'{_val_str:>{_width}}'

def t_0():
  x = {'value': 0, 'name': 'i'}
  y = {'value': 0, 'name': 'i', 'datatype': 'int'}
  return pxyf(x, y, f)

def t_a():
  # cell_dict
  x = {'value': 'a', 'name': 'A'}
  y = {'value': 'a', 'name': 'A', 'datatype': 'str'}
  return pxyf(x, y, f)

def t_rate():
  x = {'value': make_rate(1, 1, {'m': 1}), 'name': 'distance'}
  y = {
    'value': {'numerator': 1, 'denominator': 1, 'unit': {'m': 1}},
    'name': 'distance',
    'datatype': 'rate'
  }
  return pxyf(x, y, f)

def t_date():
  x = {'value': date(2022, 4, 5), 'name': 'date'}
  y = {'value': date(2022, 4, 5), 'name': 'date', 'datatype': 'date'}
  return pxyf(x, y, f)

def t_description():
  x = {'value': 'Purchased USD with AUD', 'name': 'description'}
  y = {
    'value': 'Purchased USD with AUD',
    'name': 'description',
    'datatype': 'str'
  }
  return pxyf(x, y, f)

def t_USD_rate():
  x = {'value': make_rate(5472, 1, {'USD': 1}), 'name': 'USD Rate'}
  y = {
    'value': {'numerator': 5472, 'denominator': 1, 'unit': {'USD': 1}},
    'name': 'USD Rate',
    'datatype': 'rate'
  }
  return pxyf(x, y, f)

def t_A_nabtrade_cash_AUD():
  x = {
    'value': make_rate(-7350.89, 1, {'AUD': 1}),
    'name': 'nabtrade_cash_AUD'
  }
  y = {
    'value': {'numerator': -735089, 'denominator': 100, 'unit': {'AUD': 1}},
    'name': 'nabtrade_cash_AUD',
    'datatype': 'rate'
  }
  return pxyf(x, y, f)

def t_rate_0():
  x = {'value': make_rate(0, 1, {'m': 1}), 'name': 'description'}
  y = {
    'value': {'numerator': 0, 'denominator': 1, 'unit': {'m': 1}},
    'name': 'description',
    'datatype': 'rate'
  }
  return pxyf(x, y, f)

def t_none():
  x = {'value': None, 'name': 'foo'}
  y = {'value': None, 'name': 'foo', 'datatype': 'none'}
  return pxyf(x, y, f)

def t_drift():
  _value = make_random_integer(-9, 9)
  _name = make_random_string()
  _x = {'value': _value, 'name': _name}
  x = {'value': _value, 'name': _name}
  y = {'value': _value, 'name': _name, 'datatype': 'int'}
  z = f(x)
  if _x != x: return pf(f'drift of original dict occurred; _x: {_x}; x: {x}')
  return pxyz(x, y, z)

def t():
  if not t_0(): return pf('!t_0')
  if not t_a(): return pf('!t_a')
  if not t_A_nabtrade_cash_AUD(): return pf('!t_A_nabtrade_cash_AUD') #
  if not t_date(): return pf('!t_date')
  if not t_description(): return pf('!t_description')
  if not t_rate_0(): return pf('!t_rate_0')
  if not t_rate(): return pf('!t_rate')
  if not t_USD_rate(): return pf('!t_USD_rate')
  if not t_none(): return pf('!t_none')
  if not t_drift(): return pf('!t_drift')
  return 1
