from src.classes.table import Table
from src.classes.record import Record
from hak.one.dict.rate.make import f as rate
from datetime import date

table = Table()
record = Record({
  'integer': 10,
  'string': 'abc',
  'price': rate(1, 2, {'$': 1, 'item': -1}),
  'date': date.today()
})

print(record)

table.add_record(record)

print(table.column_names)

print(table.header)
print(table.columns['integer'])
