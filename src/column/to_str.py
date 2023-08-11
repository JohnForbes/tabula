from hak.pxyz import f as pxyz
from src.column.make import f as make_column
from src.column.width.get import f as get_width
from hak.pf import f as pf

def f(x):
  w = get_width(x) + 2

  if   x['datatype'] == 'int':
    value_strings = [f" {v:>{get_width(x)}} " for v in x['values']]

  elif any([x['datatype'] in {'date', 'str'}]):
    _values = [str(v) for v in x['values']]
    value_strings = [f" {v:>{get_width(x)}} " for v in _values]

  else:
    raise TypeError(f"Unexpected type: {x['datatype']}")
  
  return '\n'.join([
    '-'*w,
    f" {x['name']:>{get_width(x)}} ",
    '-'*w,
    *value_strings,
    '-'*w,
  ])

def t_a():
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

def t_b():
  x = make_column(
    'animal',
    [
      'dog',
      'cat',
      'fox'
    ]
  )
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

def t():
  if not t_a(): return pf('!t_a')
  if not t_b(): return pf('!t_b')
  return True
