from hak.pxyz import f as pxyz
from hak.pf import f as pf
from hak.one.dict.rate.make import f as make_rate

f = lambda value: {'value': value}

def t_0():
  x = 0
  y = {'value': 0}
  z = f(x)
  return pxyz(x, y, z)

def t_rate():
  x = make_rate(numerator=1, denominator=1, unit={'m': 1})
  y = {'value': {'numerator': 1, 'denominator': 1, 'unit': {'m': 1}}}
  z = f(x)
  return pxyz(x, y, z)

def t():
  if not t_0(): return pf('!t_0')
  if not t_rate(): return pf('!t_rate')
  return True
