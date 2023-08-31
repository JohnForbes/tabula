from src.functions.dict.char_and_width.to_str import f as make_homogenous_line
from src.functions.dict.value_and_width.to_str import f as make_line_value

class Column:
  def __init__(self, table, keypath):
    self._keypath = keypath
    self._name = self._keypath[-1]
    self._table = table
    self._type = None
    self._unit = None
    self._include_heading = False

  w = property(
    lambda s: max([
      len(s._name),
      *[len(str(c)) for c in s.cells],
      *[len(c.get_unit_str()) for c in s.cells]
    ])
  )
  width = property(lambda s: s.w)

  def _get_cells(self):
    result = []
    for r in range(self._table.row_count):
      d = self._table.cells
      kp = (self._keypath, r)
      if kp in d:
        cell = d[kp]
        result.append(cell)
    return result

  cells = property(_get_cells)

  def _to_block(self):
    w = self.width
    cell_strings = [f" {str(c):>{w}} " for c in self.cells]
    bar = make_homogenous_line({'char': '-', 'width': w})

    heading = [
      bar,
      make_line_value({'value': self._name, 'width': w}),
      bar,
    ]

    result_excl_heading = [
      bar,
      make_line_value({'value': self.cells[0].get_unit_str(), 'width': w}),
      bar,
      *cell_strings,
      bar,
    ]

    result_incl_heading = heading + result_excl_heading

    return result_incl_heading if self._include_heading else result_excl_heading

  block = property(_to_block)

  __str__ = lambda self: '\n'.join(self.block)

f = lambda: Column()

