from hak.pf import f as pf
from hak.pxyf import f as pxyf

from src.functions.dict.column.to_str import f as column_to_str

# _f_a
def f(x):
  column_strings = [column_to_str(c) for c in x]
  return '\n'.join([
    '|'.join([
      column_strings[column_index].split('\n')[i]
      for column_index
      in range(len(x))
    ])
    for i
    in range(len(column_strings[0].split('\n')))
  ])

def t_a():
  x = [
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
  y = '\n'.join([
    '-----|------',
    ' abc |  ghi ',
    '-----|------',
    '     |      ',
    '-----|------',
    '     |      ',
    '   1 |   10 ',
    '   2 |  200 ',
    '   3 | 3000 ',
    '-----|------'
  ])
  return pxyf(x, y, f, new_line=1, show_as_lists=1)

def t_b():
  x = [
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
  y = '\n'.join([
    '-----|------|-----',
    ' abc |  ghi | jkl ',
    '-----|------|-----',
    '     |      |     ',
    '-----|------|-----',
    '     |      |   a ',
    '   1 |   10 |   b ',
    '   2 |  200 |   c ',
    '   3 | 3000 |   d ',
    '-----|------|-----'
  ])
  return pxyf(x, y, f, new_line=1, show_as_lists=1)

def t_c():
  x = [
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
  y = '\n'.join([
    '-----|------|-----',
    ' abc |  ghi | jkl ',
    '-----|------|-----',
    '     |      |     ',
    '-----|------|-----',
    '     |      |   a ',
    '   1 |   10 |   b ',
    '   2 |  200 |   c ',
    '   3 | 3000 |   d ',
    '-----|------|-----'
  ])
  return pxyf(x, y, f, new_line=1, show_as_lists=1)

def t_d():
  x = [
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
  y = '\n'.join([
    '-----|------|-----|------',
    ' abc |  ghi | jkl |  mno ',
    '-----|------|-----|------',
    '     |      |     |      ',
    '-----|------|-----|------',
    '     |      |   a |    a ',
    '   1 |   10 |   b |   bb ',
    '   2 |  200 |   c |  ccc ',
    '   3 | 3000 |   d | dddd ',
    '-----|------|-----|------'
  ])
  return pxyf(x, y, f, new_line=1, show_as_lists=1)

def t():
  if not t_a(): return pf('!t_a')
  if not t_b(): return pf('!t_b')
  if not t_c(): return pf('!t_c')
  if not t_d(): return pf('!t_d')
  return 1