from datetime import date
# from hak.one.dict.cell.to_str import f as to_str
# from hak.one.dict.get_or_default import f as get_or_default
# from hak.one.dict.rate.is_a import f as is_rate
from hak.one.dict.rate.make import f as make_rate
# from hak.one.dict.rate.to_float import f as to_float
# from hak.one.dict.rate.to_num import f as to_num
# from hak.one.dict.rate.to_str import f as rate_to_str
from hak.one.get_datatype import f as detect_type
# from hak.one.string.colour.decolour import f as decol
from hak.pf import f as pf
from hak.pxyz import f as pxyz

# make_cell
# src.cell.make
def f(value, datatype=None):
  y = {}
  y['value'] = value
  y['datatype'] = datatype or detect_type(value)
  return y

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
  x = 0
  y = {'value': 0, 'datatype': 'int'}
  z = f(x)
  return pxyz(x, y, z)

def t_a():
  # cell_dict
  x = {'value': 'a'}
  y = {'value': 'a', 'datatype': 'str'}
  z = f(**x)
  return pxyz(x, y, z)

def t_rate():
  x = make_rate(numerator=1, denominator=1, unit={'m': 1})
  y = {
    'value': {'numerator': 1, 'denominator': 1, 'unit': {'m': 1}},
    'datatype': 'rate'
  }
  z = f(x)
  return pxyz(x, y, z)

def t_date():
  x = {'value': date(2022, 4, 5)}
  y = {'value': date(2022, 4, 5), 'datatype': 'date'}
  z = f(**x)
  return pxyz(x, y, z)

def t_description():
  x = {'value': 'Purchased USD with AUD'}
  y = {'value': 'Purchased USD with AUD', 'datatype': 'str'}
  z = f(**x)
  return pxyz(x, y, z)

def t_USD_rate():
  x = {'value': make_rate(5472, 1, {'USD': 1})}
  y = {
    'value': {'numerator': 5472, 'denominator': 1, 'unit': {'USD': 1}},
    'datatype': 'rate'
  }
  z = f(**x)
  return pxyz(x, y, z)

def t_A_nabtrade_cash_AUD():
  x = {'value': make_rate(-7350.89, 1, {'AUD': 1})}
  y = {
    'value': {'numerator': -735089, 'denominator': 100, 'unit': {'AUD': 1}},
    'datatype': 'rate'
  }
  z = f(**x)
  return pxyz(x, y, z)

def t_rate_0():
  x = {'value': make_rate(numerator=0, denominator=1, unit={'m': 1})}
  y = {
    'value': {'numerator': 0, 'denominator': 1, 'unit': {'m': 1}},
    'datatype': 'rate'
  }
  z = f(**x)
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
  return True
