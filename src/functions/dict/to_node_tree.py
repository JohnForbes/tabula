from src.classes.node import Node
from hak.pf import f as pf

# dict_to_node_tree
def f(x, root=None, nodes={}, table=None):
  if isinstance(x, dict):
    for k in x:
      nodes[k] = Node(k, table=table)
      if root:
        nodes[root].add_child(nodes[k])
      nodes = f(x[k], k, nodes, table)
  return nodes

def t():
  x = {
    'alice': {
      'bob': {'frank': {'heidi': 0, 'ivan': 1}, 'niaj': 2},
      'carol': {'grace': {'judy': 3, 'michael': 4}},
      'dan': 5,
      'erin': 6,
    }
  }
  z = f(x)

  y_alices_children = {'bob', 'carol', 'dan', 'erin'}
  z_alices_children = set([c.name for c in z['alice'].children])
  if z_alices_children != y_alices_children: return pf([
    f'y_alices_children: {y_alices_children}',
    f'z_alices_children: {z_alices_children}'  
  ])

  y_bobs_children = {'frank', 'niaj'}
  z_bobs_children = set([c.name for c in z['bob'].children])
  if z_bobs_children != y_bobs_children: return pf([
    f'y_bobs_children: {y_bobs_children}',
    f'z_bobs_children: {z_bobs_children}'  
  ])

  y_franks_children = {'heidi', 'ivan'}
  z_franks_children = set([c.name for c in z['frank'].children])
  if z_franks_children != y_franks_children: return pf([
    f'y_franks_children: {y_franks_children}',
    f'z_franks_children: {z_franks_children}'  
  ])

  return 1
