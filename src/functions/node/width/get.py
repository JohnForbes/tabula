from src.functions.ints.cell_value_widths.to_aggregate_width import f as w

# get_width
f = lambda x: max(
  len(x.name),
  w([c.width for c in x.children]),
  (
    x.table.get_column(x.nodepath).width
    if (x.nodepath, 0) in x.table.cells else
    0
  )
)
