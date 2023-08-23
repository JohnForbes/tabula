from hak.one.dict.rate.is_a import f as is_rate
from hak.one.dict.rate.make import f as make_rate
from hak.one.dict.rate.to_str_frac import f as to_str_frac
from hak.one.dict.unit.to_str import f as unit_to_str
from hak.one.string.colour.bright.red import f as red
from hak.one.string.colour.decolour import f as decol
from hak.pf import f as pf
from hak.pxyz import f as pxyz

from src.functions.dict.cell.make import f as make_cell
from src.functions.dict.cell.to_str import f as to_str

# width
def f(x):
  v = x['value']
  header_word_widths = [len(i) for i in x['field_name'].split('_')]
  unit_width = len(unit_to_str(v['unit'])) if is_rate(v) else 0
  val_str = to_str_frac(v) if x['datatype'] == 'rate' else to_str(x)
  value_str_width = len(decol(val_str))
  return max([*header_word_widths, value_str_width, unit_width])

def t_00():
  x = make_cell(100, 'foo')
  y = 3
  z = f(x)
  return pxyz(x, y, z)

def t_0():
  x = make_cell(**{'value': False, 'field_name': 'a'})
  y = 1
  z = f(x)
  return pxyz(x, y, z)

def t_1():
  x = make_cell(**{'value': 'a', 'field_name': 'aa'})
  y = 2
  z = f(x)
  return pxyz(x, y, z)

def t_2():
  x = make_cell(**{'value': red('-'), 'field_name': 'is_revenue'})
  y = len('revenue')
  z = f(x)
  return pxyz(x, y, z)

def t_quantity_short_unit():
  x = make_cell(**{
    'value': make_rate(12.34, 1, {'m': 1}),
    'field_name': 'length'
  })
  y = len('length')
  z = f(x)
  return pxyz(x, y, z)

def t_quantity_long_unit():
  x = make_cell(**{
    'value': make_rate(
      12.34,
      1,
      {'lightyear': 1}
    ),
    'field_name': 'length'
  })
  y = len('lightyear')
  z = f(x)
  return pxyz(x, y, z)

def t_rate():
  x = make_cell(**{
    'value': make_rate(547200, 735089, {'USD': 1, 'AUD': -1}),
    'field_name': 'rate_USD_per_AUD'
  })
  y = len('547200/735089')
  z = f(x)
  return pxyz(x, y, z)

def t():
  if not t_00(): return pf('!t_00')
  if not t_0(): return pf('!t_0')
  if not t_1(): return pf('!t_1')
  if not t_2(): return pf('!t_2')
  if not t_quantity_short_unit(): return pf('!t_quantity_short_unit')
  if not t_quantity_long_unit(): return pf('!t_quantity_long_unit')
  if not t_rate(): return pf('!t_rate')
  return True
