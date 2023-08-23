from hak.pf import f as pf
from hak.pxyf import f as pxyf

from ...strings.block.hstack import f as hstack
from ..records_and_keypath.make_val_block import f as make_val_block

# make_children_block
f = lambda x: hstack([
  make_val_block({'records': x['records'], 'keypath': (x['field_name'], _k)})
  for _k
  in x['records'][0][x['field_name']].keys()
])

def t_a():
  x = {
    'records': [
      {'Name': 'Alice', 'Info': {'Age': 28, 'Country': 'USA'}}, 
      {'Name': 'Bob', 'Info': {'Age': 35, 'Country': 'Canada'}}, 
      {'Name': 'Charlie', 'Info': {'Age': 22, 'Country': 'UK'}},
    ],
    'field_name': 'Info'
  }
  y = [
    ' Age | Country ',
    '-----|---------',
    '  28 |     USA ',
    '  35 |  Canada ',
    '  22 |      UK ',
    '-----|---------'
  ]
  return pxyf(x, y, f)

def t():
  if not t_a(): return pf('!t_a')
  return 1
