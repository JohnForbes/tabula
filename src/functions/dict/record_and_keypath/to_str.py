from datetime import date
from hak.one.dict.rate.make import f as make_rate
from hak.pxyz import f as pxyz

from src.functions.dict.column.make_from_values import f as make_from_values
from src.functions.dict.column.to_str import f as column_to_str

def f(x):
  keypath = x['keypath']
  k_0 = keypath[0] # 'dates'
  k_1 = keypath[1] # 'date'
  column = make_from_values(k_1, [x['record'][k_0][k_1]], k_0)
  return column_to_str(column)

def t():
  x = {
    'record': {
      'dates': {'date': date(2023, 1, 1)},
      'prices': {
        'apples': make_rate(1, 4, {'$': 1, 'apple': -1}),
        'bananas': make_rate(2, 4, {'$': 1, 'banana': -1})
      }
    },
    'keypath': ('dates', 'date')
  }
  y = '\n'.join([
    '------------',
    '       date ',
    '------------',
    '            ',
    '------------',
    ' 2023-01-01 ',
    '------------',
  ])
  z = f(x)
  return pxyz(x, y, z, new_line=1)

if __name__ == '__main__':
  print(t())
