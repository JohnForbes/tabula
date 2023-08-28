from src.classes.cell import Cell
from hak.one.dict.rate.make import f as rate
from src.classes.table import Table
from src.classes.column import Column

# cell = Cell(value=rate(710, 113, {'a': 1}))
# print([str(cell)])
# print(cell.width)

# cell = Cell(value=True)
# print(str(cell))
# print(cell.width)

# print(isinstance(cell, Cell))

table = Table()
_a = 'aaa'
table.add_record({_a: 1, 'b': 2, 'c': 3})
table.add_record({_a: 4, 'b': 5, 'c': 6})
table.add_record({_a: 7, 'b': 8, 'c': 9})

# for c in table._cells:
#   print(c, table._cells[c])

# column = table.get_column(_a)
# print(column)

column = Column(_a, table)
# print(column.width)
# for c in column.cells:
#   print(c)

# print(column.width)


table.add_record({_a: 10, 'b': 11, 'c': 12})
# print()
# column = Column(_a, table)
# print(column.width)
# for c in column.cells:
#   print(c)

print(Column(_a, table))
print(Column('b', table))
