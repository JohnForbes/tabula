from hak.one.bool.is_a import f as is_bool
from hak.one.dict.rate.is_a import f as is_rate
from hak.one.dict.rate.to_str_frac import f as rate_to_str
from hak.one.dict.unit.to_str import f as unit_to_str
from hak.one.get_datatype import f as detect_type
from hak.one.is_0 import f as is_0
from hak.one.is_none import f as is_none
from hak.one.number.float.is_a import f as is_float
from hak.one.string.colour.bright.green import f as g
from hak.one.string.colour.bright.red import f as r
from hak.one.string.colour.decolour import f as decol
from hak.pf import f as pf
from hak.pxyz import f as pxyz
from src.classes.rate import Rate

class Cell:
  def __init__(self, value):
    self.value = value
    self.type = 'Rate' if isinstance(value, Rate) else detect_type(value)

  def __str__(self):
    v = self.value
    if  is_none(v): return ''
    if  is_rate(v): return rate_to_str(v)
    if  is_bool(v): return g('Y') if v else r('N')
    if     is_0(v): return ''
    if is_float(v): return f"{v:.2f}"
    return str(v)

  get_unit_str = lambda self: (
    unit_to_str(self.value.unit)
    if self.type == 'Rate' else
    ''
  )
  
  width = property(lambda self: max([
    len(decol(str(self))),
    len(decol(self.get_unit_str())),
  ]))

f = lambda x: Cell(x)

def t_a():
  x = Cell(0)
  y = ''
  z = str(x)
  return pxyz(x, y, z)

def t_b():
  x = Cell('abc')
  y = 'abc'
  z = str(x)
  return pxyz(x, y, z)

def t_c():
  x = Cell(123)
  y = '123'
  z = str(x)
  return pxyz(x, y, z)

def t_d():
  x = Cell(1.3)
  y = '1.30'
  z = str(x)
  return pxyz(x, y, z)

def t_e():
  x = Cell(True)
  y = g('Y')
  z = str(x)
  return pxyz(x, y, z)

def t_f():
  x = Cell(False)
  y = r('N')
  z = str(x)
  return pxyz(x, y, z)

def t_g():
  value = Rate(numerator=120, denominator=240, unit={'$': 1, 'm': -1})
  x = Cell(value)
  y = '1/2'
  z = str(x)
  return pxyz(x, y, z)

def t():
  if not t_a(): return pf('!t_a')
  if not t_b(): return pf('!t_b')
  if not t_c(): return pf('!t_c')
  if not t_d(): return pf('!t_d')
  if not t_e(): return pf('!t_e')
  if not t_f(): return pf('!t_f')
  if not t_g(): return pf('!t_g')
  return 1
