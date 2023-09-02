from hak.one.bool.is_a import f as is_bool
from hak.one.dict.rate.is_a import f as is_rate
from hak.one.dict.rate.to_str_frac import f as rate_to_str
from hak.one.dict.unit.to_str import f as unit_to_str
from hak.one.get_datatype import f as detect_type
from hak.one.is_0 import f as is_0
from hak.one.is_none import f as is_none
from hak.one.number.float.is_a import f as is_float
from hak.one.number.int.primes.prime_factors.get import f as get_prime_factors
from hak.one.string.colour.bright.green import f as green
from hak.one.string.colour.bright.red import f as red
from hak.one.string.colour.decolour import f as decol
from hak.pf import f as pf
from hak.pxyz import f as pxyz
from src.functions.dict.char_and_width.to_str import f as make_homogenous_line
from src.functions.dict.record_and_keypath.to_value import f as kp_to_val
from src.functions.dict.record.get_leaf_keypaths import f as get_leaf_keypaths
from src.functions.dict.value_and_width.to_str import f as fvw
from src.functions.ints.cell_value_widths.to_aggregate_width import f as aw
from src.functions.nodes.sort_children_by_nodepath import f as sort_by_nodepath
from src.functions.strings.block.hstack import f as hstack
from src.functions.strings.block.to_str import f as block_to_str
from src.functions.strings.block.vstack import f as vstack

def f(x): raise NotImplementedError('!26')

def dict_to_node_tree(x, root=None, nodes={}, table=None):
  if isinstance(x, dict):
    for k in x:
      nodes[k] = Node(k, table=table)
      if root:
        nodes[root].add_child(nodes[k])
      nodes = dict_to_node_tree(x[k], k, nodes, table)
  return nodes

class Cell:
  def __init__(self, value):
    self.value = value
    self.type = 'Rate' if isinstance(value, Rate) else detect_type(value)

  def __str__(self):
    v = self.value
    if  is_none(v): return ''
    if  is_rate(v): return rate_to_str(v)
    if  is_bool(v): return green('Y') if v else red('N')
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

def make_block(x):
  top_block = [f' {x.name:^{x.width}} ']
  return (
    vstack([top_block, hstack([c.block for c in sort_by_nodepath(x)])])
    if x.children else
    top_block
  )

get_width = lambda node: max(
  len(node.name),
  aw([c.width for c in node.children]),
  (
    node.table.get_column(node.nodepath).width
    if (node.nodepath, 0) in node.table.cells else
    0
  )
)

class Node:
  def __init__(self, name, table):
    self.name = name
    self.children = set()
    self.nodepath = tuple([name])
    self.table = table

  def add_child(self, child):
    self.children.add(child)
    child.nodepath = tuple(list(self.nodepath)+ list(child.nodepath))

  block = property(make_block)
  width = property(get_width)

div_int_by_rate = lambda u, v: Rate(u, 1, {'1': 0}) / v

def _g(a, b):
  if isinstance(a, float):
    decimal_place_count = len(str(a).split('.')[1].rstrip('0'))
    b *= 10**decimal_place_count
    a *= 10**decimal_place_count
    b = int(b)
    a = int(a)
  return a, b

class Rate:
  def __init__(self, numerator, denominator, unit):
    numerator, denominator = _g(numerator, denominator)
    denominator, numerator = _g(denominator, numerator)

    if numerator == 0: denominator = 1

    if isinstance(numerator, float):
      decimal_place_count = len(str(numerator).split('.')[1].rstrip('0'))
      numerator *= 10**decimal_place_count
      denominator *= 10**decimal_place_count
      numerator = int(numerator)
      denominator = int(denominator)

    self.numerator = numerator
    self.denominator = denominator
    self.unit = unit
    self.simplify()

  def simplify(self):
    numerator = self.numerator
    denominator = self.denominator
    unit = self.unit

    npf = get_prime_factors(numerator)
    dpf = get_prime_factors(denominator)

    common_factors = set(npf.keys()).intersection(set(dpf.keys()))

    while common_factors:
      common_factor = common_factors.pop()
      numerator //= common_factor
      denominator //= common_factor
      npf = get_prime_factors(numerator)
      dpf = get_prime_factors(denominator)
      common_factors = set(npf.keys()).intersection(set(dpf.keys()))
    self.numerator = numerator
    self.denominator = denominator
    self.unit = unit

  n = property(lambda self: self.numerator)
  d = property(lambda self: self.denominator)

  def __add__(u, v):
    if u.unit != v.unit:
      raise ValueError(f"u.unit: {u.unit} != v.unit: {v.unit}")
    return Rate(u.n * v.d + v.n * u.d, u.d * v.d, u.unit)

  def __truediv__(u, v):
    _unit = {k: 0 for k in sorted(set(u.unit.keys()) | set(v.unit.keys()))}

    for k in u.unit: _unit[k] += u.unit[k]
    for k in v.unit: _unit[k] -= v.unit[k]

    unit = {k: _unit[k] for k in _unit if _unit[k] != 0}

    return Rate(u.numerator*v.denominator, u.denominator*v.numerator, unit)

  def __str__(self):
    if self.denominator == 0: return f"undefined"
    if self.numerator == 0: return f""
    if self.denominator == 1: return f"{self.numerator}"
    return f"{self.numerator}/{self.denominator}"

  def __sub__(u, v):
    if u['unit'] != v['unit']:
      raise ValueError(f"u['unit']: {u['unit']} != v['unit']: {v['unit']}")
    return Rate(u.n * v.d - u.d * v.n, u.d * v.d, u.unit)

  def __mul__(u, v):
    _unit = {k: 0 for k in sorted(set(u.unit.keys()) | set(v.unit.keys()))}

    for k in u.unit: _unit[k] += u.unit[k]
    for k in v.unit: _unit[k] += v.unit[k]

    return Rate(
      u.numerator  *v.numerator,
      u.denominator*v.denominator,
      {k: _unit[k] for k in _unit if _unit[k] != 0}
    )

  def __eq__(u, v):
    _u = Rate(u.n, u.d, u.unit)
    _v = Rate(v.n, v.d, v.unit)
    return all([_u.n == _v.n, _u.d == _v.d, _u.unit == _v.unit])
  
  __abs__ = lambda s: Rate(abs(s.numerator), abs(s.denominator), s.unit)
  __float__ = lambda self: self.numerator / self.denominator

class Table:
  def __init__(s):
    s.cells = {}
    s.row_count = 0
    s.column_keypaths = set()
    s.last_record = None

  def add_record(s, record):
    record = {'α': record}
    s.column_keypaths |= get_leaf_keypaths(record, [], set())
    s.row_count += 1
    for kp in s.column_keypaths:
      v = kp_to_val({'record': record, 'keypath': kp})
      reference = (kp, s.row_count-1)
      s.cells[reference] = Cell(v)
    s.last_record = record
    
  def add_records(s, records):
    for r in records:
      s.add_record(r)

  get_column = lambda s, column_keypath: Column(s, column_keypath)

  columns = property(lambda s: [s.get_column(kp) for kp in s.column_keypaths])

  block = property(lambda s: hstack([
    c.block for c in sorted(s.columns, key=lambda x: x._keypath)
  ]))

  def __str__(s):
    root = list(s.last_record.keys())[0]
    nodes = dict_to_node_tree(s.last_record, table=s)
    header_str = block_to_str(nodes[root].block[1:])
    table_str = block_to_str(s.block)
    return '\n'.join([header_str, table_str])

def t_cell_a():
  x = Cell(0)
  y = ''
  z = str(x)
  return pxyz(x, y, z)

def t_cell_b():
  x = Cell('abc')
  y = 'abc'
  z = str(x)
  return pxyz(x, y, z)

def t_cell_c():
  x = Cell(123)
  y = '123'
  z = str(x)
  return pxyz(x, y, z)

def t_cell_d():
  x = Cell(1.3)
  y = '1.30'
  z = str(x)
  return pxyz(x, y, z)

def t_cell_e():
  x = Cell(True)
  y = green('Y')
  z = str(x)
  return pxyz(x, y, z)

def t_cell_f():
  x = Cell(False)
  y = red('N')
  z = str(x)
  return pxyz(x, y, z)

def t_cell_g():
  value = Rate(numerator=120, denominator=240, unit={'$': 1, 'm': -1})
  x = Cell(value)
  y = '1/2'
  z = str(x)
  return pxyz(x, y, z)

def t_cell():
  if not t_cell_a(): return pf('!t_cell_a')
  if not t_cell_b(): return pf('!t_cell_b')
  if not t_cell_c(): return pf('!t_cell_c')
  if not t_cell_d(): return pf('!t_cell_d')
  if not t_cell_e(): return pf('!t_cell_e')
  if not t_cell_f(): return pf('!t_cell_f')
  if not t_cell_g(): return pf('!t_cell_g')
  return 1

def t_column_a():
  from importlib import import_module
  _table = Table()
  x = {'table': _table, 'keypath': ('α', 'abc', 'def', 'ghi')}
  z = Column(**x)
  if not z._keypath == x['keypath']: return pf("!: z._keypath == x['keypath']")
  if not z._name == 'ghi': return pf("!: z._name == 'ghi'")
  if not z._table == _table: return pf("!: z._table == _table")
  if not z._type == None: return pf("!: z._type == None")
  if not z._unit == None: return pf("!: z._unit == None")
  if not z._include_heading == 0: return pf("!: z._include_heading == False")
  return 1

def t_column_b_column_name():
  x = {'table': Table(), 'keypath': ('α', 'abc', 'def', 'ghi')}
  z = Column(**x)
  result = all([z.w == len(x['keypath'][-1]), z.width == len(x['keypath'][-1])])
  return result

def t_column_b_decol_cell_strs():
  _table = Table()
  _table.add_record({'a': {'d': {'g': green('YY')}}})
  column = _table.get_column(('α', 'a', 'd', 'g'))
  result = column.w == 2
  return result

def t_column_b_unit_str_len():
  _table = Table()
  _table.add_record({'a': {'d': {'g': Rate(120, 240, {'$': 1, 'm': -1})}}})
  column = _table.get_column(('α', 'a', 'd', 'g'))
  result = column.w == len('$/m')
  return result

def t_column_b():
  if not t_column_b_column_name(): return pf('!t_b_column_name')
  if not t_column_b_decol_cell_strs(): return pf('!t_b_decol_cell_strs')
  if not t_column_b_unit_str_len(): return pf('!t_b_unit_str_len')
  return 1

def t_column_c():
  _table = Table()
  _table.add_record({'a': {'d': {'g': Rate(120, 240, {'$': 1, 'm': -1})}}})
  _table.add_record({'a': {'d': {'g': Rate(121, 240, {'$': 1, 'm': -1})}}})
  _table.add_record({'a': {'d': {'g': Rate(122, 240, {'$': 1, 'm': -1})}}})
  column = _table.get_column(('α', 'a', 'd', 'g'))
  cells = column._get_cells()
  return [str(c) for c in cells] == ['1/2', '121/240', '61/120']

def t_column_d():
  _table = Table()
  _table.add_record({'a': {'d': {'g': Rate(120, 240, {'$': 1, 'm': -1})}}})
  column = _table.get_column(('α', 'a', 'd', 'g'))
  return column.cells == column._get_cells()

def t_column_e_exclude_heading():
  _table = Table()
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

def t_column_e_include_heading():
  _table = Table()
  _rate = Rate(120, 240, {'$': 1, 'm': -1})
  record = {'a': {'d': {'g': _rate}}}
  _table.add_record(record)
  column = _table.get_column(('α', 'a', 'd', 'g'))
  column._include_heading = True
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

def t_column_e():
  if not t_column_e_exclude_heading(): return pf('!t_column_e_exclude_heading')
  if not t_column_e_include_heading(): return pf('!t_column_e_include_heading')
  return 1

def t_column_f():
  _table = Table()
  _table.add_record({'a': {'d': {'g': Rate(120, 240, {'$': 1, 'm': -1})}}})
  column = _table.get_column(('α', 'a', 'd', 'g'))
  return column.block == column._to_block()

def t_column_g():
  _table = Table()
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

def t_column():
  if not t_column_a(): return pf('!t_a')
  if not t_column_b(): return pf('!t_b')
  if not t_column_c(): return pf('!t_c')
  if not t_column_d(): return pf('!t_d')
  if not t_column_e(): return pf('!t_e')
  if not t_column_f(): return pf('!t_f')
  if not t_column_g(): return pf('!t_g')
  return 1

def t_node__init():
  _table = Table()
  node = Node('node_name', _table)
  if node.name != 'node_name': return pf("node.name != 'node_name'")
  if node.children != set(): return pf("node.children != set()")
  if node.nodepath != tuple(['node_name']):
    return pf("node.nodepath != tuple(['node_name'])")
  if node.table != _table: return pf("node.table != _table")
  return 1

def t_node__str(): return 0
def t_node_add_child(): return 0
def t_node_add_children(): return 0
def t_node_block(): return 0
def t_node_level(): return 0
def t_node_width(): return 0

def t_node():
  if not t_node__init(): return pf('!t_node__init')
  # if not t_node__str(): return pf('!t_node__str')
  # if not t_node_add_child(): return pf('!t_node_add_child')
  # if not t_node_add_children(): return pf('!t_node_add_children')
  # if not t_node_block(): return pf('!t_node_block')
  # if not t_node_level(): return pf('!t_node_level')
  # if not t_node_width(): return pf('!t_node_width')
  return 1

def t_rate_simplifies_at_init():
  x = {'numerator': 120, 'denominator': 240, 'unit': {'$': 1, 'm': -1}}
  y = Rate(1, 2, {'$': 1, 'm': -1})
  z = Rate(**x)
  return pxyz(x, y, z)

def t_rate_numerator_float():
  x = {'numerator': 0.120, 'denominator': 240, 'unit': {'$': 1, 'm': -1}}
  y = Rate(1, 2000, {'$': 1, 'm': -1})
  z = Rate(**x)
  return pxyz(x, y, z)

def t_rate_denominator_float():
  x = {'numerator': 120, 'denominator': 0.240, 'unit': {'$': 1, 'm': -1}}
  y = Rate(500, 1, {'$': 1, 'm': -1})
  z = Rate(**x)
  return pxyz(x, y, z)

def t_rate_a():
  x = {'numerator': 1, 'denominator': 2, 'unit': {'$': 1, 'm': -1}}
  y = '1/2'
  z = str(Rate(**x))
  return pxyz(x, y, z)

def t_rate_b():
  x = {'numerator': 0, 'denominator': 2, 'unit': {'$': 1, 'm': -1}}
  y = Rate(0, 1, {'$': 1, 'm': -1})
  z = Rate(**x)
  return pxyz(x, y, z)

def t_rate():
  if not t_rate_simplifies_at_init(): return pf('!t_rate_simplifies_at_init')
  if not t_rate_numerator_float(): return pf('!t_rate_numerator_float')
  if not t_rate_denominator_float(): return pf('!t_rate_denominator_float')
  if not t_rate_a(): return pf('!t_rate_a')
  if not t_rate_b(): return pf('!t_rate_b')
  return 1

def t_table__init__():
  table = Table()
  return all([
    table.cells == {},
    table.row_count == 0,
    table.column_keypaths == set()
  ])

def t_table_add_record():
  table = Table()
  record = {'a': {'b': Rate(1, 3, {'$': 1, 'm': -1})}}
  table.add_record(record)

  if table.column_keypaths != {('α', 'a', 'b')}:
    return pf("table.column_keypaths != {('α', 'a', 'b')}")

  if table.row_count != 1: return pf("table.row_count != 1")
  
  cell = table.cells[(('α', 'a', 'b'), 0)]
  
  if cell.value.numerator != 1: return pf('cell.value.numerator != 1')
  
  if cell.value.denominator != 3: return pf("cell.value.denominator != 3")
  
  if cell.value.unit != {'$': 1, 'm': -1}:
    return pf("cell.value.unit != {'$': 1, 'm': -1}")
  
  if table.last_record != {'α': record}:
    return pf("table.last_record != {'α': record}")

  return 1

def t_table_add_records():
  table = Table()
  records = [
    {'a': {'b': Rate(1, 3, {'$': 1, 'm': -1}), 'c': 'abc'}},
    {'a': {'b': Rate(2, 3, {'$': 1, 'm': -1}), 'c': 'ghi'}}
  ]
  table.add_records(records)
  return len(table.cells) == 4

def t_table___str__():
  table = Table()
  records = [
    {'a': {'b': Rate(1, 3, {'$': 1, 'm': -1}), 'c': 'abc'}},
    {'a': {'b': Rate(2, 3, {'$': 1, 'm': -1}), 'c': 'ghi'}}
  ]
  table.add_records(records)
  y = '\n'.join([
    '-----------',
    '     a     ',
    '-----------',
    '  b  |  c  ',
    '-----|-----',
    ' $/m |     ',
    '-----|-----',
    ' 1/3 | abc ',
    ' 2/3 | ghi ',
    '-----|-----'
  ])
  z = str(table)
  return y == z

def t_table_get_column():
  table = Table()
  records = [
    {'a': {'b': Rate(1, 3, {'$': 1, 'm': -1}), 'c': 'abc'}},
    {'a': {'b': Rate(2, 3, {'$': 1, 'm': -1}), 'c': 'ghi'}}
  ]
  table.add_records(records)
  column = table.get_column(('α', 'a', 'b'))
  return column.block == ['-----', ' $/m ', '-----', ' 1/3 ', ' 2/3 ', '-----']

def t_table_columns():
  table = Table()
  records = [
    {'a': {'b': Rate(1, 3, {'$': 1, 'm': -1}), 'c': 'abc'}},
    {'a': {'b': Rate(2, 3, {'$': 1, 'm': -1}), 'c': 'ghi'}}
  ]
  table.add_records(records)
  y_table_column_blocks = [
    ['-----', '     ', '-----', ' abc ', ' ghi ', '-----'],
    ['-----', ' $/m ', '-----', ' 1/3 ', ' 2/3 ', '-----'],
  ]
  
  z_table_column_blocks = set([str(c.block) for c in table.columns])

  return all([
    str(y_table_column_block) in z_table_column_blocks
    for y_table_column_block
    in y_table_column_blocks
  ])

def t_table_block():
  table = Table()
  records = [
    {'a': {'b': Rate(1, 3, {'$': 1, 'm': -1}), 'c': 'abc'}},
    {'a': {'b': Rate(2, 3, {'$': 1, 'm': -1}), 'c': 'ghi'}}
  ]
  table.add_records(records)
  y_blocks = [
    ['-----', '     ', '-----', ' abc ', ' ghi ', '-----'],
    ['-----', ' $/m ', '-----', ' 1/3 ', ' 2/3 ', '-----'],
    ['-----', '     ', '-----', ' abc ', ' ghi ', '-----'],
    ['-----', ' $/m ', '-----', ' 1/3 ', ' 2/3 ', '-----']
  ]
  c_blocks = [c.block for c in table.columns]
  for i in range(len(table.columns)):
    c = table.columns[i]
    if y_blocks[i] not in c_blocks:
      return pf(f'y_blocks[i] != c.block; {y_blocks[i]} != {c.block}')
  return 1

def t_table():
  if not t_table__init__(): return pf('!t_table__init__')
  if not t_table_add_record(): return pf('!t_table_add_record')
  if not t_table_add_records(): return pf('!t_table_add_records')
  if not t_table___str__(): return pf('!t_table___str__')
  if not t_table_get_column(): return pf('t_table_get_column')
  if not t_table_columns(): return pf('t_table_columns')
  if not t_table_block(): return pf('t_table_block')
  return 1

def t_dict_to_node_tree():
  x = {
    'alice': {
      'bob': {'frank': {'heidi': 0, 'ivan': 1}, 'niaj': 2},
      'carol': {'grace': {'judy': 3, 'michael': 4}},
      'dan': 5,
      'erin': 6,
    }
  }
  z = dict_to_node_tree(x)

  y_alices_children = {'bob', 'carol', 'dan', 'erin'}
  z_alices_children = set([c.name for c in z['alice'].children])
  if z_alices_children != y_alices_children: return pf([
    f'y_alices_children: {y_alices_children}',
    f'z_alices_children: {z_alices_children}'  
  ])

  y_bobs_children = {'frank', 'niaj'}
  z_bobs_children = set([c.name for c in z['bob'].children])
  if z_bobs_children != y_bobs_children: return pf([
    f'y_bobs_children: {y_bobs_children}',
    f'z_bobs_children: {z_bobs_children}'  
  ])

  y_franks_children = {'heidi', 'ivan'}
  z_franks_children = set([c.name for c in z['frank'].children])
  if z_franks_children != y_franks_children: return pf([
    f'y_franks_children: {y_franks_children}',
    f'z_franks_children: {z_franks_children}'  
  ])

  return 1

def t():
  if not t_cell(): return pf('!t_cell')
  if not t_dict_to_node_tree(): return pf('!t_dict_to_node_tree')
  if not t_node(): return pf('!t_node')
  if not t_rate(): return pf('!t_rate')
  if not t_column(): return pf('!t_column')
  if not t_table(): return pf('!t_table')
  return 1
