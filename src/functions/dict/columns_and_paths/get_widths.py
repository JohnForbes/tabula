from src.functions.dict.column.width.get import f as get_col_width
from src.functions.ints.cell_value_widths.to_aggregate_width import f as aw
from hak.pf import f as pf
from hak.pxyf import f as pxyf

# get_path_widths
f = lambda x: {
  p: max(
    aw([get_col_width(c) for c in x['columns'] if c['path'][0] == p]),
    len(p)
  )
  for p in x['paths']
}

def t_a():
  x = {
    'paths': ['numbers'],
    'columns': [
      {
        'name': 'abc',
        'cells': [
          {'name': 'abc', 'type': 'int', 'value': 0},
          {'name': 'abc', 'type': 'int', 'value': 1},
          {'name': 'abc', 'type': 'int', 'value': 2},
          {'name': 'abc', 'type': 'int', 'value': 3}
        ],
        'path': ('numbers',)
      },
      {
        'name': 'ghi',
        'cells': [
          {'name': 'ghi', 'type': 'int', 'value': 0},
          {'name': 'ghi', 'type': 'int', 'value': 10},
          {'name': 'ghi', 'type': 'int', 'value': 200},
          {'name': 'ghi', 'type': 'int', 'value': 3000}
        ],
        'path': ('numbers',)
      }
    ]
  }
  y = {'numbers': 10}
  return pxyf(x, y, f)

def t_b():
  x = {
    'paths': ['numbers', 'let'],
    'columns': [
      {
        'name': 'abc',
        'cells': [
          {'name': 'abc', 'type': 'int', 'value': 0},
          {'name': 'abc', 'type': 'int', 'value': 1},
          {'name': 'abc', 'type': 'int', 'value': 2},
          {'name': 'abc', 'type': 'int', 'value': 3}
        ],
        'path': ('numbers',)
      },
      {
        'name': 'ghi',
        'cells': [
          {'name': 'ghi', 'type': 'int', 'value': 0},
          {'name': 'ghi', 'type': 'int', 'value': 10},
          {'name': 'ghi', 'type': 'int', 'value': 200},
          {'name': 'ghi', 'type': 'int', 'value': 3000}
        ],
        'path': ('numbers',)
      },
      {
        'name': 'jkl',
        'cells': [
          {'name': 'jkl', 'type': 'str', 'value': 'a'},
          {'name': 'jkl', 'type': 'str', 'value': 'b'},
          {'name': 'jkl', 'type': 'str', 'value': 'c'},
          {'name': 'jkl', 'type': 'str', 'value': 'd'}
        ],
        'path': ('let',)
      }
    ]
  }
  y = {'numbers': 10, 'let': 3}
  return pxyf(x, y, f)

def t_c():
  x = {
    'paths': ['numbers', 'letters'],
    'columns': [
      {
        'name': 'abc',
        'cells': [
          {'name': 'abc', 'type': 'int', 'value': 0},
          {'name': 'abc', 'type': 'int', 'value': 1},
          {'name': 'abc', 'type': 'int', 'value': 2},
          {'name': 'abc', 'type': 'int', 'value': 3}
        ],
        'path': ('numbers',)
      },
      {
        'name': 'ghi',
        'cells': [
          {'name': 'ghi', 'type': 'int', 'value': 0},
          {'name': 'ghi', 'type': 'int', 'value': 10},
          {'name': 'ghi', 'type': 'int', 'value': 200},
          {'name': 'ghi', 'type': 'int', 'value': 3000}
        ],
        'path': ('numbers',)
      },
      {
        'name': 'jkl',
        'cells': [
          {'name': 'jkl', 'type': 'str', 'value': 'a'},
          {'name': 'jkl', 'type': 'str', 'value': 'b'},
          {'name': 'jkl', 'type': 'str', 'value': 'c'},
          {'name': 'jkl', 'type': 'str', 'value': 'd'}
        ],
        'path': ('letters',)
      }
    ]
  }
  y = {'numbers': 10, 'letters': 7}
  return pxyf(x, y, f)

def t_d():
  x = {
    'paths': ['numbers', 'letters'],
    'columns': [
      {
        'name': 'abc',
        'cells': [
          {'name': 'abc', 'type': 'int', 'value': 0},
          {'name': 'abc', 'type': 'int', 'value': 1},
          {'name': 'abc', 'type': 'int', 'value': 2},
          {'name': 'abc', 'type': 'int', 'value': 3}
        ],
        'path': ('numbers',)
      },
      {
        'name': 'ghi',
        'cells': [
          {'name': 'ghi', 'type': 'int', 'value': 0},
          {'name': 'ghi', 'type': 'int', 'value': 10},
          {'name': 'ghi', 'type': 'int', 'value': 200},
          {'name': 'ghi', 'type': 'int', 'value': 3000}
        ],
        'path': ('numbers',)
      },
      {
        'name': 'jkl',
        'cells': [
          {'name': 'jkl', 'type': 'str', 'value': 'a'},
          {'name': 'jkl', 'type': 'str', 'value': 'b'},
          {'name': 'jkl', 'type': 'str', 'value': 'c'},
          {'name': 'jkl', 'type': 'str', 'value': 'd'}
        ],
        'path': ('letters',)
      },
      {
        'name': 'mno',
        'cells': [
          {'name': 'mno', 'type': 'str', 'value': 'a'},
          {'name': 'mno', 'type': 'str', 'value': 'bb'},
          {'name': 'mno', 'type': 'str', 'value': 'ccc'},
          {'name': 'mno', 'type': 'str', 'value': 'dddd'}
        ],
        'path': ('letters',)
      }
    ]
  }
  y = {'numbers': 10, 'letters': 10}
  return pxyf(x, y, f)

def t():
  if not t_a(): return pf('!t_a')
  if not t_b(): return pf('!t_b')
  if not t_c(): return pf('!t_c')
  if not t_d(): return pf('!t_d')
  return 1
