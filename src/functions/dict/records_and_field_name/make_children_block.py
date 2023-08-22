from src.functions.strings.block.hstack import f as hstack
# from misc.val_block.make import f as make_val_block
from ..records_and_keypath.make_val_block import f as make_val_block
from hak.pxyz import f as pxyz
from hak.pf import f as pf

# make_children_block
def f(x):
  records = x['records']
  field_name = x['field_name']
  return hstack([
    make_val_block({'records': records, 'keypath': (field_name, _k)})
    for _k
    in records[0][field_name].keys()
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
  z = f(x)
  return pxyz(x, y, z)

def t():
  if not t_a(): return pf('!t_a')
  return True
