from src.classes import Rate
from datetime import date

from app import f as records_to_table

records = [
  {
    'date': date(2023, 1, 1),
    'cecil': {
      'robert': {'john': {'zenn': 0, 'rei': 1}, 'james': 2},
      'wendi': {'bec': {'theo': 3.126, 'max': 4}},
      'liz': 'boo!',
      'donald': True,
      'price': Rate(1, 2, {'$': 1, 'item': -1})
    }
  },
  {
    'date': date(2023, 1, 1),
    'cecil': {
      'robert': {'john': {'zenn': 7, 'rei': 8}, 'james': 9},
      'wendi': {'bec': {'theo': 10.124, 'max': 11}},
      'liz': 'who!',
      'donald': False,
      'price': Rate(2, 3, {'$': 1, 'item': -1})
    }
  },
  {
    'date': date(2023, 1, 1),
    'cecil': {
      'robert': {'john': {'zenn': 14, 'rei': 15}, 'james': 16},
      'wendi': {'bec': {'theo': 17.124, 'max': 18}},
      'liz': 'phew!',
      'donald': True,
      'price': Rate(4, 5, {'$': 1, 'item': -1})
    }
  }
]

print(records_to_table(records))
