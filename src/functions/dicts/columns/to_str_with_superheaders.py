from hak.pxyf import f as pxyf
from hak.one.list.remove_duplicates import f as remove_duplicates
from hak.pf import f as pf

from src.functions.dict.columns_and_paths.get_widths import f as get_path_W
from src.functions.strings.block.homogenise_line_lengths import f as h
from src.functions.dicts.columns.to_str_without_superheaders import f as f_a

# _f_b
def f(x):
  paths = remove_duplicates([p[0] for p in [c['path'] for c in x if c['path']]])
  path_widths = get_path_W({'paths': paths, 'columns': x})
  return '\n'.join(h([
    '-'+'-|-'.join([   '-'*path_widths[p]    for p in paths])+'-',
    ' '+' | '.join([f'{p:>{path_widths[p]}}' for p in paths])+' ',
    *f_a(x).split('\n')
  ]))

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
    '------------',
    '    numbers ',
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
    '------------|-----',
    '    numbers | let ',
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
    '------------|---------',
    '    numbers | letters ',
    '-----|------|---------',
    ' abc |  ghi |     jkl ',
    '-----|------|---------',
    '     |      |         ',
    '-----|------|---------',
    '     |      |       a ',
    '   1 |   10 |       b ',
    '   2 |  200 |       c ',
    '   3 | 3000 |       d ',
    '-----|------|---------'
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
    '------------|------------',
    '    numbers |    letters ',
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

def t_e():
  x = [
    {
      'name': 'a',
      'cells': [
        {'value': 0, 'type': 'int', 'name': 'a'},
        {'value': 3, 'type': 'int', 'name': 'a'},
        {'value': 6, 'type': 'int', 'name': 'a'}
      ],
      'path': ()
    },
    {
      'name': 'b',
      'cells': [
        {'value': 1, 'type': 'int', 'name': 'b'},
        {'value': 4, 'type': 'int', 'name': 'b'},
        {'value': 7, 'type': 'int', 'name': 'b'}
      ],
      'path': ()
    }
  ]
  y = '\n'.join([
    '--',
    '  ',
    '---|---',
    ' a | b ',
    '---|---',
    '   |   ',
    '---|---',
    '   | 1 ',
    ' 3 | 4 ',
    ' 6 | 7 ',
    '---|---'
  ])
  return pxyf(x, y, f, new_line=1, show_as_lists=1)

def t():
  if not t_a(): return pf('!t_a')
  if not t_b(): return pf('!t_b')
  if not t_c(): return pf('!t_c')
  if not t_d(): return pf('!t_d')
  if not t_e(): return pf('!t_e')
  return 1
