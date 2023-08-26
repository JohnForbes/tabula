# ignore_overlength_lines
from hak.one.dict.rate.make import f as rate
from hak.pf import f as pf
from hak.pxyf import f as pxyf

from ...dict.records_and_function.to_underlined_row import f as f_a
from ...dict.records_k_branch_k_leaf.to_unit_cell_str import f as f_b

# f_units
# records_to_units_row_with_underline
f = lambda x: f_a({'records': x, 'function': f_b})

def t_a():
  x = [
    {
      'prices': {
        'apples': rate(1, 4, {'$': 1, 'apple': -1}),
        'bananas': rate(1, 2, {'$': 1, 'banana': -1})
      },
      'volumes': {
        'applezzz': rate(1, 1, {'apple': 1}),
        'bananazzz': rate(2, 1, {'banana': 1}),
        'pearzzzzzz': rate(3, 1, {'pear': 1})
      },
      'zloops': {'zloop': rate(7, 1, {'zloop': 1})}
    },
    {
      'prices': {
        'apples': rate(3, 4, {'$': 1, 'apple': -1}),
        'bananas': rate(1, 1, {'$': 1, 'banana': -1})
      },
      'volumes': {
        'applezzz': rate(4, 1, {'apple': 1}),
        'bananazzz': rate(5, 1, {'banana': 1}),
        'pearzzzzzz': rate(6, 1, {'pear': 1})
      },
      'zloops': {'zloop': rate(7, 1, {'zloop': 1})}
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
        'apples': rate(1, 4, {'$': 1, 'apple': -1}),
        'bananas': rate(2, 4, {'$': 1, 'banana': -1})
      },
      'volumes': {
        'applezzz': rate(1, 1, {'apple': 1}),
        'bananazzz': rate(2, 1, {'banana': 1}),
        'pearzzzzzz': rate(3, 1, {'pear': 1})
      },
      'zloops': {'zloop': rate(7, 1, {'zloop': 1})}
    },
    {
      'prices': {
        'apples': rate(3, 4, {'$': 1, 'apple': -1}),
        'bananas': rate(4, 4, {'$': 1, 'banana': -1})
      },
      'volumes': {
        'applezzz': rate(4, 1, {'apple': 1}),
        'bananazzz': rate(5, 1, {'banana': 1}),
        'pearzzzzzz': rate(6, 1, {'pear': 1})
      },
      'zloops': {'zloop': rate(7, 1, {'zloop': 1})}
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
