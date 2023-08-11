from hak.one.get_datatype import f as detect_type
from hak.pxyz import f as pxyz
from hak.pf import f as pf
from hak.one.dict.rate.make import f as make_rate

def f(value, datatype=None):
  y = {}
  y['value'] = value
  y['datatype'] = datatype or detect_type(value)
  return y

def t_0():
  x = 0
  y = {'value': 0, 'datatype': 'int'}
  z = f(x)
  return pxyz(x, y, z)

def t_rate():
  x = make_rate(numerator=1, denominator=1, unit={'m': 1})
  y = {
    'value': {'numerator': 1, 'denominator': 1, 'unit': {'m': 1}},
    'datatype': 'rate'
  }
  z = f(x)
  return pxyz(x, y, z)

def t():
  if not t_0(): return pf('!t_0')
  if not t_rate(): return pf('!t_rate')
  return True
