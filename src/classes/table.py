from src.classes.cell import Cell
from src.classes.column import Column
from src.functions.strings.block.hstack import f as hstack
from src.functions.strings.block.vstack import f as vstack
from src.functions.strings.block.to_str import f as block_to_str
from src.functions.dict.record.get_leaf_keypaths import f as get_leaf_keypaths
from src.functions.dict.record_and_keypath.to_value import f as kp_to_val
from src.functions.dict.to_node_tree import f as dict_to_node_tree

class Table:
  def __init__(s):
    s.cells = {}
    s.row_count = 0
    s.column_keypaths = set()
  
  def add_tuple(s, keys, tuple):
    d = {keys[i]: tuple[i] for i in range(len(keys))}
    s.add_record(d)

  def add_record(s, record):
    record = {'α': record}
    s.column_keypaths |= get_leaf_keypaths(record)
    s.row_count += 1
    for kp in s.column_keypaths:
      v = kp_to_val({'record': record, 'keypath': kp})
      reference = (kp, s.row_count-1)
      s.cells[reference] = Cell(v)
    s.last_record = record
    
  def add_records(s, records):
    for r in records:
      s.add_record(r)

  get_column = lambda s, column_keypath: Column(s, column_keypath)

  columns = property(lambda s: [s.get_column(kp) for kp in s.column_keypaths])

  block = property(lambda s: hstack([
    c.block for c in sorted(s.columns, key=lambda x: x._keypath)
  ]))

  def __str__(s):
    root = list(s.last_record.keys())[0]
    nodes = dict_to_node_tree(s.last_record, table=s)
    header_str = block_to_str(nodes[root].block[1:])
    table_str = block_to_str(s.block)
    return '\n'.join([header_str, table_str])

f = lambda: Table()
