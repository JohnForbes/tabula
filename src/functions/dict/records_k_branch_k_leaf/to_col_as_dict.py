from hak.one.dict.rate.make import f as rate
from hak.pf import f as pf
from hak.pxyf import f as pxyf
from hak.one.dict.unit.to_str import f as unit_to_str
from data.records import records_without_date as records_wout_date

# get_column
# records_k_branch_k_leaf_to_col_as_dict
f = lambda x: {
  'head': x['k_leaf'],
  'unit': unit_to_str(x['records'][0][x['k_branch']][x['k_leaf']]['unit']),
  'values': [r[x['k_branch']][x['k_leaf']] for r in x['records']]
}

def t_prices_apples():
  x = {'records': records_wout_date, 'k_branch': 'prices', 'k_leaf': 'apples'}
  y = {
    'head': 'apples',
    'unit': '$/apple',
    'values': [
      rate(1, 4, {'$': 1, 'apple': -1}),
      rate(3, 4, {'$': 1, 'apple': -1})
    ]
  }
  return pxyf(x, y, f)

def t():
  if not t_prices_apples(): return pf('!t_prices_apples')
  return True
