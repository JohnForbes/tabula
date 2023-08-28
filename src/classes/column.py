from src.functions.dict.char_and_width.to_str import f as make_homogenous_line
from src.functions.dict.value_and_width.to_str import f as make_line_value

class Column:
  def __init__(self, name, table):
    self._name = name
    self._unit = None
    self._type = None
    self._table = table

  def _get_width(self): return max([
    len(self._name),
    *[len(str(c)) for c in self.cells]
  ])

  width = property(_get_width)

  cells = property(
    lambda self: [
      self._table._cells[(self._name, r)]
      for r
      in range(self._table.row_count)
    ]
  )

  def to_block(self):
    w = self.width
    cell_strings = [f" {str(c):>{w}} " for c in self.cells]
    bar = make_homogenous_line({'char': '-', 'width': w})
    return [
      bar,
      make_line_value({'value': self._name, 'width': w}),
      bar,
      make_line_value({'value': self.cells[0].get_unit_str(), 'width': w}),
      bar,
      *cell_strings,
      bar,
    ]

  __str__ = lambda self: '\n'.join(self.to_block())

f = lambda: Column()
t = lambda: 1 # Functions externalised in functions directory
