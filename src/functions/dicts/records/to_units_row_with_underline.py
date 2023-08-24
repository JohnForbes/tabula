# ignore_overlength_lines
from hak.one.dict.rate.make import f as make_rate
from hak.pxyf import f as pxyf
from hak.one.dict.rate.make import f as make_rate
from hak.pf import f as pf
from hak.pxyf import f as pxyf

from src.functions.dict.records_and_function.to_underlined_row import f as f_a
from src.functions.dict.records_k_branch_k_leaf.to_unit_cell_str import f as f_b

# f_units
# records_to_units_row_with_underline
f = lambda x: f_a({'records': x, 'function': f_b})

def t_a():
  x = [
    {
      'prices': {
        'apples': make_rate(1, 4, {'$': 1, 'apple': -1}),
        'bananas': make_rate(1, 2, {'$': 1, 'banana': -1})
      },
      'volumes': {
        'applezzz': make_rate(1, 1, {'apple': 1}),
        'bananazzz': make_rate(2, 1, {'banana': 1}),
        'pearzzzzzz': make_rate(3, 1, {'pear': 1})
      },
      'zloops': {'zloop': make_rate(7, 1, {'zloop': 1})}
    },
    {
      'prices': {
        'apples': make_rate(3, 4, {'$': 1, 'apple': -1}),
        'bananas': make_rate(1, 1, {'$': 1, 'banana': -1})
      },
      'volumes': {
        'applezzz': make_rate(4, 1, {'apple': 1}),
        'bananazzz': make_rate(5, 1, {'banana': 1}),
        'pearzzzzzz': make_rate(6, 1, {'pear': 1})
      },
      'zloops': {'zloop': make_rate(7, 1, {'zloop': 1})}
    }
  ]
  y = [
    '| $/apple | $/banana |    apple |    banana |       pear |  zloop |',
    '|---------|----------|----------|-----------|------------|--------|',
  ]
  return pxyf(x, y, f)

def t_b():
  x = [
    {
      'prices': {
        'apples': make_rate(1, 4, {'$': 1, 'apple': -1}),
        'bananas': make_rate(2, 4, {'$': 1, 'banana': -1})
      },
      'volumes': {
        'applezzz': make_rate(1, 1, {'apple': 1}),
        'bananazzz': make_rate(2, 1, {'banana': 1}),
        'pearzzzzzz': make_rate(3, 1, {'pear': 1})
      },
      'zloops': {'zloop': make_rate(7, 1, {'zloop': 1})}
    },
    {
      'prices': {
        'apples': make_rate(3, 4, {'$': 1, 'apple': -1}),
        'bananas': make_rate(4, 4, {'$': 1, 'banana': -1})
      },
      'volumes': {
        'applezzz': make_rate(4, 1, {'apple': 1}),
        'bananazzz': make_rate(5, 1, {'banana': 1}),
        'pearzzzzzz': make_rate(6, 1, {'pear': 1})
      },
      'zloops': {'zloop': make_rate(7, 1, {'zloop': 1})}
    }
  ]
  y = [
    '| $/apple | $/banana |    apple |    banana |       pear |  zloop |',
    '|---------|----------|----------|-----------|------------|--------|'
  ]
  return pxyf(x, y, f)

def t():
  if not t_a(): return pf('!t_a')
  if not t_b(): return pf('!t_b')
  return True
