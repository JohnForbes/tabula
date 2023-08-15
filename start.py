from hak.one.dict.rate.make import f as make_rate
from archive.dicts.records.to_nested_table import f as to_nested_table
from src.table.make import f as make_table
from src.table.insert_records import f as insert_records
from src.table.to_str import f as table_to_str

table = make_table()
table = insert_records(
    table, [
      {
        'apples': make_rate(1, 4, {'$': 1, 'apple': -1}),
        'bananas': make_rate(2, 4, {'$': 1, 'banana': -1})
      },
      {
        'apples': make_rate(3, 4, {'$': 1, 'apple': -1}),
        'bananas': make_rate(4, 4, {'$': 1, 'banana': -1})
      },
    ]
  )
table_str = table_to_str(table)
print(table_str)

# x = [
#   {
#     # 'dates': {'date': 'blergh'},
#     'prices': {
#       'apples': make_rate(1, 4, {'$': 1, 'apple': -1}),
#       'bananas': make_rate(2, 4, {'$': 1, 'banana': -1})
#     },
#     'volumes': {
#       'applezzz': make_rate(1, 1, {'apple': 1}),
#       'bananazzz': make_rate(2, 1, {'banana': 1}),
#       'pearzzzzzz': make_rate(3, 1, {'pear': 1})
#     },
#     'zloops': {'zloop': make_rate(7, 1, {'zloop': 1})}
#   },
#   {
#     'dates': {'date': make_rate(1, 1, {'day': 1})},
#     'prices': {
#       'apples': make_rate(3, 4, {'$': 1, 'apple': -1}),
#       'bananas': make_rate(4, 4, {'$': 1, 'banana': -1})
#     },
#     'volumes': {
#       'applezzz': make_rate(4, 1, {'apple': 1}),
#       'bananazzz': make_rate(5, 1, {'banana': 1}),
#       'pearzzzzzz': make_rate(6, 1, {'pear': 1})
#     },
#     'zloops': {'zloop': make_rate(7, 1, {'zloop': 1})}
#   }
# ]
# y = '\n'.join([
#   "|--------------------|-----------------------------------|--------|",
#   "|             prices |                           volumes | zloops |",
#   "|---------|----------|----------|-----------|------------|--------|",
#   "|  apples |  bananas | applezzz | bananazzz | pearzzzzzz |  zloop |",
#   "|---------|----------|----------|-----------|------------|--------|",
#   "| $/apple | $/banana |    apple |    banana |       pear |  zloop |",
#   "|---------|----------|----------|-----------|------------|--------|",
#   "|    0.25 |     0.50 |     1.00 |      2.00 |       3.00 |   7.00 |",
#   "|    0.75 |     1.00 |     4.00 |      5.00 |       6.00 |   7.00 |",
#   "|---------|----------|----------|-----------|------------|--------|",
# ])
# z = to_nested_table(x)
# print(z)
