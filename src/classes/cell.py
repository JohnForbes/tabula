from hak.one.bool.is_a import f as is_bool
from hak.one.dict.rate.is_a import f as is_rate
from hak.one.dict.rate.to_str_frac import f as rate_to_str
from hak.one.get_datatype import f as detect_type
from hak.one.is_0 import f as is_0
from hak.one.is_none import f as is_none
from hak.one.number.float.is_a import f as is_float
from hak.one.string.colour.bright.green import f as g
from hak.one.string.colour.bright.red import f as r
from hak.one.string.colour.decolour import f as decol
from hak.one.dict.unit.to_str import f as unit_to_str

class Cell:
  def __init__(self, value):
    self.value = value
    self.type = detect_type(value)

  def __str__(self):
    v = self.value
    if  is_none(v): return ''
    if  is_rate(v): return rate_to_str(v)
    if  is_bool(v): return g('Y') if v else r('N')
    if     is_0(v): return ''
    if is_float(v): return f"{v:.2f}"
    return str(v)

  get_unit_str = lambda self: (
    unit_to_str(self.value['unit'])
    if self.type == 'rate' else
    ''
  )
  
  width = property(lambda self: len(decol(str(self))))

f = lambda: Cell()
t = lambda: 1 # Functions externalised in functions directory
