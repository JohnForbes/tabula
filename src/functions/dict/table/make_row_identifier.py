from hak.pxyf import f as pxyf
from src.functions.dict.cell.make import f as cell
from src.functions.dict.table.make import f as table
from src.functions.dict.table.insert_records import f as insert_records
from hak.one.number.int.random.make import f as u

f = lambda x: (max(x['row_order']) if x['row_order'] else -1)+1

t = lambda: pxyf(
  insert_records({
    'table': table(),
    'records': [
      {'a': u(-9, 9), 'b': u(-9, 9)},
      {'a': u(-9, 9), 'b': u(-9, 9)},
      {'a': u(-9, 9), 'b': u(-9, 9)}
    ]
  }),
  3,
  f
)
