from hak.pf import f as pf
from hak.pxyf import f as pxyf

# from src.functions.dict.table.bar.make import f as make_bar

# make_bar
make_bar = lambda x: (
  "|-"+'-|-'.join(['-'*x['widths'][k] for k in x['names']])+"-|"
)

# src.table.head.make
def f(x):
  if 'units' in x:
    if all([x['units'][k] == '' for k in x['units']]):
      del x['units']

  units = None
  if 'units' in x:
    units = x['units']

  names = x['names']
  _widths = x['widths']

  sp = ' '
  
  result = '\n'.join([
    "| "+' | '.join([
      f"{_f.split('_')[i]:>{_widths[_f]}}" if len(_f.split('_')) > i else
      f"{sp:>{_widths[_f]}}"
      for _f in names
    ])+" |"
    for i in range(max([len(_f.split('_')) for _f in names]))
  ])

  unit_section = ''

  if units:
    bar = make_bar({'widths': _widths, 'names': names})
    unit_section += '\n'+bar+'\n'
    unit_section += '\n'.join([
      "| "+
      ' | '.join([f'{str(units[n]):>{_widths[n]}}' for n in names]) +
      " |"
    ])
  
  return result + unit_section

def t_0():
  x = {'names': list('abcde')}
  x['widths'] = {k: 2 for k in x['names']}
  y = '|  a |  b |  c |  d |  e |'
  return pxyf(x, y, f)

def t_1():
  x = {
    'widths': {
      'a': 2,
      'is_revenue': len('revenue'),
      'balance_equity_retained_earnings': 8,
    },
    'names': ['a', 'is_revenue', 'balance_equity_retained_earnings'],
  }

  y = '\n'.join([
    '|  a |      is |  balance |',
    '|    | revenue |   equity |',
    '|    |         | retained |',
    '|    |         | earnings |',
  ])
  return pxyf(x, y, f, new_line=1)

def t_2():
  x = {
    'widths': {
      'a': len('lightyear'),
      'is_revenue': len('revenue'),
      'balance_equity_retained_earnings': 8,
    },
    'names': ['a', 'is_revenue', 'balance_equity_retained_earnings'],
    'units': {
      'a': 'lightyear',
      'is_revenue': 'boolean',
      'balance_equity_retained_earnings': 'AUD'
    }
  }
  y = '\n'.join([
    '|         a |      is |  balance |',
    '|           | revenue |   equity |',
    '|           |         | retained |',
    '|           |         | earnings |',
    '|-----------|---------|----------|',
    '| lightyear | boolean |      AUD |',
  ])
  return pxyf(x, y, f, new_line=1)

def t():
  if not t_0(): return pf('t_0 failed')
  if not t_1(): return pf('t_1 failed')
  if not t_2(): return pf('t_2 failed')
  return 1
