from datetime import date
from hak.one.dict.rate.make import f as rate
from hak.many.dicts.a_into_b import f as a_into_b

records_without_date = [
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

records_with_date = [
  a_into_b({'date': date(2023, 7, 27)}, records_without_date[0]),
  a_into_b({'date': date(2023, 7, 28)}, records_without_date[1])
]
