from hak.one.dict.rate.is_a import f as is_rate
from hak.one.dict.rate.make import f as rate
from hak.one.dict.rate.to_str_frac import f as to_str_frac
from hak.one.dict.unit.to_str import f as unit_to_str
from hak.one.string.colour.bright.red import f as red
from hak.one.string.colour.decolour import f as decol
from hak.pf import f as pf
from hak.pxyf import f as pxyf

from src.functions.dict.cell.make import f as cell
from src.functions.dict.cell.to_str import f as to_str

# width
def f(x):
  v = x['value']
  header_word_widths = [len(i) for i in x['name'].split('_')]
  unit_width = len(unit_to_str(v['unit'])) if is_rate(v) else 0
  val_str = to_str_frac(v) if x['datatype'] == 'rate' else to_str(x)
  value_str_width = len(decol(val_str))
  return max([*header_word_widths, value_str_width, unit_width])

t_00 = lambda: pxyf(cell({'value': 100, 'name': 'foo'}), 3, f)
t_0 = lambda: pxyf(cell({'value': False, 'name': 'a'}), 1, f)
t_1 = lambda: pxyf(cell({'value': 'a', 'name': 'aa'}), 2, f)

t_2 = lambda: pxyf(
  cell({'value': red('-'), 'name': 'is_revenue'}),
  len('revenue'),
  f
)

t_quantity_short_unit = lambda: pxyf(
  cell({'value': rate(12.34, 1, {'m': 1}), 'name': 'length'}),
  len('length'),
  f
)

t_quantity_long_unit = lambda: pxyf(
  cell({'value': rate(12.34, 1, {'lightyear': 1}), 'name': 'length'}),
  len('lightyear'),
  f
)

t_rate = lambda: pxyf(
  cell({
    'value': rate(547200, 735089, {'USD': 1, 'AUD': -1}),
    'name': 'rate_USD_per_AUD'
  }),
  len('547200/735089'),
  f
)

def t():
  if not t_00(): return pf('!t_00')
  if not t_0(): return pf('!t_0')
  if not t_1(): return pf('!t_1')
  if not t_2(): return pf('!t_2')
  if not t_quantity_short_unit(): return pf('!t_quantity_short_unit')
  if not t_quantity_long_unit(): return pf('!t_quantity_long_unit')
  if not t_rate(): return pf('!t_rate')
  return 1
