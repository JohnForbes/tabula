from hak.one.string.colour.bright.green import f as g
from hak.one.string.colour.decolour import f as decol
from hak.pf import f as pf
from src.classes.rate import f as Rate
from src.functions.dict.char_and_width.to_str import f as make_homogenous_line
from src.functions.dict.value_and_width.to_str import f as fvw

class Column:
  def __init__(self, table, keypath):
    self._keypath = keypath
    self._name = self._keypath[-1]
    self._table = table
    self._type = None
    self._unit = None
    self._include_heading = False

  w = property(
    lambda s: max([
      len(s._name),
      *[len(decol(str(c))) for c in s.cells],
      *[len(c.get_unit_str()) for c in s.cells]
    ])
  )
  width = property(lambda s: s.w)

  def _get_cells(self):
    result = []
    for r in range(self._table.row_count):
      d = self._table.cells
      kp = (self._keypath, r)
      if kp in d:
        cell = d[kp]
        result.append(cell)
    return result

  cells = property(_get_cells)

  def _to_block(self):
    w = self.width
    cell_strings = [fvw({'value': c, 'width': w}) for c in self.cells]
    bar = make_homogenous_line({'char': '-', 'width': w})
    heading = [bar, fvw({'value': self._name, 'width': w})]

    result_excl_heading = [
      bar,
      fvw({'value': self.cells[0].get_unit_str(), 'width': w}),
      bar,
      *cell_strings,
      bar,
    ]

    result_incl_heading = heading + result_excl_heading

    return result_incl_heading if self._include_heading else result_excl_heading

  block = property(_to_block)

  __str__ = lambda self: '\n'.join(self.block)

f = lambda x: Column(**x)

def t_a():
  from importlib import import_module
  _Table = import_module('src.classes.table').Table
  _table = _Table()
  x = {'table': _table, 'keypath': ('α', 'abc', 'def', 'ghi')}
  z = f(x)
  if not z._keypath == x['keypath']: return pf("!: z._keypath == x['keypath']")
  if not z._name == 'ghi': return pf("!: z._name == 'ghi'")
  if not z._table == _table: return pf("!: z._table == _table")
  if not z._type == None: return pf("!: z._type == None")
  if not z._unit == None: return pf("!: z._unit == None")
  if not z._include_heading == 0: return pf("!: z._include_heading == False")
  return 1

def t_b_column_name():
  from importlib import import_module
  _Table = import_module('src.classes.table').Table
  x = {'table': _Table(), 'keypath': ('α', 'abc', 'def', 'ghi')}
  z = f(x)
  result = all([z.w == len(x['keypath'][-1]), z.width == len(x['keypath'][-1])])
  del _Table
  return result

def t_b_decol_cell_strs():
  from importlib import import_module
  _Table = import_module('src.classes.table').Table
  _table = _Table()
  _table.add_record({'a': {'d': {'g': g('YY')}}})
  column = _table.get_column(('α', 'a', 'd', 'g'))
  result = column.w == 2
  del _table
  del _Table
  del column
  return result

def t_b_unit_str_len():
  from importlib import import_module
  _Table = import_module('src.classes.table').Table
  _table = _Table()
  _table.add_record({'a': {'d': {'g': Rate(120, 240, {'$': 1, 'm': -1})}}})
  column = _table.get_column(('α', 'a', 'd', 'g'))
  result = column.w == len('$/m')
  del _table
  del _Table
  del column
  return result

def t_b():
  if not t_b_column_name(): return pf('!t_b_column_name')
  # if not t_b_decol_cell_strs(): return pf('!t_b_decol_cell_strs')
  # if not t_b_unit_str_len(): return pf('!t_b_unit_str_len')
  return 1

def t_c():
  from importlib import import_module
  _Table = import_module('src.classes.table').Table
  _table = _Table()
  _table.add_record({'a': {'d': {'g': Rate(120, 240, {'$': 1, 'm': -1})}}})
  _table.add_record({'a': {'d': {'g': Rate(121, 240, {'$': 1, 'm': -1})}}})
  _table.add_record({'a': {'d': {'g': Rate(122, 240, {'$': 1, 'm': -1})}}})
  column = _table.get_column(('α', 'a', 'd', 'g'))
  cells = column._get_cells()
  return [str(c) for c in cells] == ['1/2', '121/240', '61/120']

def t_d():
  from importlib import import_module
  _Table = import_module('src.classes.table').Table
  _table = _Table()
  _table.add_record({'a': {'d': {'g': Rate(120, 240, {'$': 1, 'm': -1})}}})
  column = _table.get_column(('α', 'a', 'd', 'g'))
  return column.cells == column._get_cells()

def t_e_exclude_heading():
  from importlib import import_module
  _Table = import_module('src.classes.table').Table
  _table = _Table()
  _table.add_record({'a': {'d': {'g': Rate(120, 240, {'$': 1, 'm': -1})}}})
  _table.add_record({'a': {'d': {'g': Rate(121, 240, {'$': 1, 'm': -1})}}})
  _table.add_record({'a': {'d': {'g': Rate(122, 240, {'$': 1, 'm': -1})}}})
  column = _table.get_column(('α', 'a', 'd', 'g'))
  return column._to_block() == [
    '---------',
    '     $/m ',
    '---------',
    '     1/2 ',
    ' 121/240 ',
    '  61/120 ',
    '---------'
  ]

def t_e_include_heading():
  from importlib import import_module
  _Table = import_module('src.classes.table').Table
  _table = _Table()
  # record = {'a': {'heading': Rate(120, 240, {'$': 1, 'm': -1})}}
  _rate = Rate(120, 240, {'$': 1, 'm': -1})
  record = {'a': {'d': {'g': _rate}}}
  _table.add_record(record)
  column = _table.get_column(('α', 'a', 'd', 'g'))
  column._include_heading = True
  # _table.add_record({'a': {'heading': Rate(121, 240, {'$': 1, 'm': -1})}})
  # _table.add_record({'a': {'heading': Rate(122, 240, {'$': 1, 'm': -1})}})
  # column = _table.get_column(('α', 'a', 'heading'))
  y = [
    '-----',
    '   g ',
    '-----',
    ' $/m ',
    '-----',
    ' 1/2 ',
    '-----'
  ]
  z = column._to_block()
  return y == z or pf([f'y: {y}', f'z: {z}'])

def t_e():
  if not t_e_exclude_heading(): return pf('!t_e_exclude_heading')
  if not t_e_include_heading(): return pf('!t_e_include_heading')
  return 1

def t_f():
  from importlib import import_module
  _Table = import_module('src.classes.table').Table
  _table = _Table()
  _table.add_record({'a': {'d': {'g': Rate(120, 240, {'$': 1, 'm': -1})}}})
  column = _table.get_column(('α', 'a', 'd', 'g'))
  return column.block == column._to_block()

def t_g():
  from importlib import import_module
  _Table = import_module('src.classes.table').Table
  _table = _Table()
  _table.add_record({'a': {'d': {'g': Rate(120, 240, {'$': 1, 'm': -1})}}})
  _table.add_record({'a': {'d': {'g': Rate(121, 240, {'$': 1, 'm': -1})}}})
  _table.add_record({'a': {'d': {'g': Rate(122, 240, {'$': 1, 'm': -1})}}})
  column = _table.get_column(('α', 'a', 'd', 'g'))
  y = '\n'.join([
    '---------',
    '     $/m ',
    '---------',
    '     1/2 ',
    ' 121/240 ',
    '  61/120 ',
    '---------'
  ])
  z = str(column)
  return y == z

def t():
  if not t_a(): return pf('!t_a')
  if not t_b(): return pf('!t_b')
  if not t_c(): return pf('!t_c')
  if not t_d(): return pf('!t_d')
  if not t_e(): return pf('!t_e')
  if not t_f(): return pf('!t_f')
  if not t_g(): return pf('!t_g')
  return 1
