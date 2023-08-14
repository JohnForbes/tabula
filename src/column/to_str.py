from datetime import date
from hak.pf import f as pf
from hak.pxyz import f as pxyz
from src.column.make_from_values import f as make_column
from src.column.width.get import f as get_width

def f(x):
  w = get_width(x) + 2

  _datatype = x['cells'][0]['datatype']

  if   _datatype == 'int':
    cell_strings = [f" {c['value']:>{get_width(x)}} " for c in x['cells']]

  elif any([_datatype in {'date', 'str'}]):
    _cells = [str(c['value']) for c in x['cells']]
    cell_strings = [f" {v:>{get_width(x)}} " for v in _cells]

  else:
    raise TypeError(f"Unexpected type: {_datatype}")
  
  return '\n'.join([
    '-'*w,
    f" {x['name']:>{get_width(x)}} ",
    '-'*w,
    *cell_strings,
    '-'*w,
  ])

def t_0():
  x = make_column('a', [0])
  y = '\n'.join([
    '---',
    ' a ',
    '---',
    ' 0 ',
    '---',
  ])
  z = f(x)
  return pxyz(x, y, z, new_line=1)

def t_1():
  x = make_column('abc', [0, 10, 23])
  y = '\n'.join([
    '-----',
    ' abc ',
    '-----',
    '   0 ',
    '  10 ',
    '  23 ',
    '-----',
  ])
  z = f(x)
  return pxyz(x, y, z, new_line=1)

def t_2():
  x = make_column('ab', [0, 100, 2300])
  y = '\n'.join([
    '------',
    '   ab ',
    '------',
    '    0 ',
    '  100 ',
    ' 2300 ',
    '------',
  ])
  z = f(x)
  return pxyz(x, y, z, new_line=1)

def t_3():
  x = make_column('apples', [_**_ for _ in range(10)])
  y = '\n'.join([
    '-----------',
    '    apples ',
    '-----------',
    '         1 ',
    '         1 ',
    '         4 ',
    '        27 ',
    '       256 ',
    '      3125 ',
    '     46656 ',
    '    823543 ',
    '  16777216 ',
    ' 387420489 ',
    '-----------'
  ])
  z = f(x)
  return pxyz(x, y, z, new_line=True)

def t_4():
  x = make_column('animal', ['dog', 'cat', 'fox'])
  y = '\n'.join([
    '--------',
    ' animal ',
    '--------',
    '    dog ',
    '    cat ',
    '    fox ',
    '--------',
  ])
  z = f(x)
  return pxyz(x, y, z, new_line=True)

def t_date():
  x = make_column(
    'date',
    [date(2023, 1, 1), date(2023, 4, 8), date(2023, 12, 31)]
  )
  y = '\n'.join([
    '------------',
    '       date ',
    '------------',
    ' 2023-01-01 ',
    ' 2023-04-08 ',
    ' 2023-12-31 ',
    '------------',
  ])
  z = f(x)
  return pxyz(x, y, z, new_line=1)

def t_str():
  x = make_column('animal', ['dog', 'cat', 'fox'])
  y = '\n'.join([
    '--------',
    ' animal ',
    '--------',
    '    dog ',
    '    cat ',
    '    fox ',
    '--------',
  ])
  z = f(x)
  return pxyz(x, y, z, new_line=1)

def t():
  if not t_0(): return pf('!t_0')
  if not t_1(): return pf('!t_1')
  if not t_2(): return pf('!t_2')
  if not t_3(): return pf('!t_3')
  if not t_4(): return pf('!t_4')
  if not t_date(): return pf('!t_date')
  if not t_str(): return pf('!t_str')

  # if not t_00(): return pf('!t_00')
  # if not t_01(): return pf('!t_01')
  # if not t_date(): return pf('!t_date')
  # if not t_common_path(): return pf('!t_common_path')
  # if not t_numbers_let_paths(): return pf('!t_numbers_let_paths')
  # if not t_numbers_letters_paths(): return pf('!t_numbers_letters_paths')
  # if not t_numbers_letters_paths_2(): return pf('!t_numbers_letters_paths_2')
  return True
