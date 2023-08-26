from src.functions.dict.cell.make import f as make_cell

class Table:
  def __init__(self):
    self._cells = {}
    self.row_count = 0
  
  def add_record(self, record):
    self.row_count += 1
    for (k, v) in record.items():
      self._cells[(k, self.row_count-1)] = make_cell({'value': v, 'field_name': k})
    
  def get_column(self, column_name):
    _cells = [
      self._cells[(column_name, i)]
      for i in range(self.row_count)
    ]

    return {
      'name': column_name,
      'cells': _cells
    }

t = Table()
t.add_record({'a': 1})
t.add_record({'a': 2, 'b': 'boo'})

print(t._cells)
print(t.row_count)

column_a = t.get_column('a')
print(column_a)