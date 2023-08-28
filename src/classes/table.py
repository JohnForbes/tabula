from src.classes.cell import Cell
from src.classes.column import Column

class Table:
  def __init__(self):
    self._cells = {}
    self.row_count = 0
  
  def add_record(self, record):
    self.row_count += 1
    for (k, v) in record.items():
      self._cells[(k, self.row_count-1)] = Cell(v)
    
  get_column = lambda self, column_name: Column(column_name, self)

f = lambda: Table()
t = lambda: 1 # Functions externalised in functions directory
