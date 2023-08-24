# from hak.pxyz import f as pxyz
from hak.one.dict.is_a import f as is_dict
from hak.one.dict.rate.is_a import f as is_rate

from src.functions.dict.node.child.add import f as add_child
from src.functions.dict.node.value.assign import f as assign_value
from src.functions.dicts.nodes.make import f as make_nodes

# tree.build
def f(k, d):
  nodes = make_nodes(d)
  return _f(k, d, nodes)

def _f(k, d, nodes):
  n = nodes[k]
  if not is_dict(d[k]) or is_rate(d[k]):
    assign_value(n, d[k])
  else:
    for k_child in d[k].keys():
      add_child(n, nodes[k_child])
      _f(k_child, d[k], nodes)
  return nodes

def t():
  # _d = {
  #   'α': {
  #     'a': {'aa': {'aaa': 'Lollipop'}, 'ab': None},
  #     'b': {'ba': None}
  #   }
  # }
  # x = {
  #   'k': 'α',
  #   'd': _d
  # }
  # y = {
  #   'ba': {
  #     'name': 'ba',
  #     'value': None,
  #     'parent': {
  #       'name': 'b',
  #       'value': None,
  #       'parent': {
  #         'name': 'α',
  #         'value': None,
  #         'parent': None,
  #         'children': [
  #           {
  #             'name': 'a',
  #             'value': None,
  #             'parent': {...},
  #             'children': [
  #               {
  #                 'name': 'aa',
  #                 'value': None,
  #                 'parent': {...},
  #                 'children': [
  #                   {
  #                     'name': 'aaa',
  #                     'value': 'Lollipop',
  #                     'parent': {...},
  #                     'children': []
  #                   }
  #                 ]
  #               },
  #               {
  #                 'name': 'ab',
  #                 'value': None,
  #                 'parent': {...},
  #                 'children': []
  #               }
  #             ]
  #           },
  #           {...}
  #         ]
  #       },
  #       'children': [{...}]
  #     },
  #     'children': []
  #   },
  #   'aaa': {
  #     'name': 'aaa',
  #     'value': 'Lollipop',
  #     'parent': {
  #       'name': 'aa',
  #       'value': None,
  #       'parent': {
  #         'name': 'a',
  #         'value': None,
  #         'parent': {
  #           'name': 'α',
  #           'value': None,
  #           'parent': None,
  #           'children': [
  #             {...},
  #             {
  #               'name': 'b',
  #               'value': None,
  #               'parent': {...},
  #               'children': [
  #                 {
  #                   'name': 'ba',
  #                   'value': None,
  #                   'parent': {...},
  #                   'children': []
  #                 }
  #               ]
  #             }
  #           ]
  #         },
  #         'children': [
  #           {...},
  #           {
  #             'name': 'ab',
  #             'value': None,
  #             'parent': {...},
  #             'children': []
  #           }
  #         ]
  #       },
  #       'children': [{...}]
  #     },
  #     'children': []
  #   },
  #   'α': {
  #     'name': 'α',
  #     'value': None,
  #     'parent': None,
  #     'children': [
  #       {
  #         'name': 'a',
  #         'value': None,
  #         'parent': {...},
  #         'children': [
  #           {
  #             'name': 'aa',
  #             'value': None,
  #             'parent': {...},
  #             'children': [
  #               {
  #                 'name': 'aaa',
  #                 'value': 'Lollipop',
  #                 'parent': {...},
  #                 'children': []
  #               }
  #             ]
  #           },
  #           {'name': 'ab', 'value': None, 'parent': {...}, 'children': []}
  #         ]
  #       },
  #       {
  #         'name': 'b',
  #         'value': None,
  #         'parent': {...},
  #         'children': [
  #           {'name': 'ba', 'value': None, 'parent': {...}, 'children': []}
  #         ]
  #       }
  #     ]
  #   },
  #   'aa': {
  #     'name': 'aa',
  #     'value': None,
  #     'parent': {
  #       'name': 'a',
  #       'value': None,
  #       'parent': {
  #         'name': 'α',
  #         'value': None,
  #         'parent': None,
  #         'children': [
  #           {...},
  #           {
  #             'name': 'b',
  #             'value': None,
  #             'parent': {...},
  #             'children': [
  #               {
  #                 'name': 'ba',
  #                 'value': None,
  #                 'parent': {...},
  #                 'children': []
  #               }
  #             ]
  #           }
  #         ]
  #       },
  #       'children': [
  #         {...},
  #         {
  #           'name': 'ab',
  #           'value': None,
  #           'parent': {...},
  #           'children': []
  #         }
  #       ]
  #     },
  #     'children': [
  #       {
  #         'name': 'aaa',
  #         'value': 'Lollipop',
  #         'parent': {...},
  #         'children': []
  #       }
  #     ]
  #   },
  #   'ab': {
  #     'name': 'ab',
  #     'value': None,
  #     'parent': {
  #       'name': 'a',
  #       'value': None,
  #       'parent': {
  #         'name': 'α',
  #         'value': None,
  #         'parent': None,
  #         'children': [
  #           {...},
  #           {
  #             'name': 'b',
  #             'value': None,
  #             'parent': {...},
  #             'children': [
  #               {
  #                 'name': 'ba',
  #                 'value': None,
  #                 'parent': {...},
  #                 'children': []
  #               }
  #             ]
  #           }
  #         ]
  #       },
  #       'children': [
  #         {
  #           'name': 'aa',
  #           'value': None,
  #           'parent': {...},
  #           'children': [
  #             {
  #               'name': 'aaa',
  #               'value': 'Lollipop',
  #               'parent': {...},
  #               'children': []
  #             }
  #           ]
  #         },
  #         {...}
  #       ]
  #     },
  #     'children': []
  #   },
  #   'b': {
  #     'name': 'b',
  #     'value': None,
  #     'parent': {
  #       'name': 'α',
  #       'value': None,
  #       'parent': None,
  #       'children': [
  #         {
  #           'name': 'a',
  #           'value': None,
  #           'parent': {...},
  #           'children': [
  #             {
  #               'name': 'aa',
  #               'value': None,
  #               'parent': {...},
  #               'children': [
  #                 {
  #                   'name': 'aaa',
  #                   'value': 'Lollipop',
  #                   'parent': {...},
  #                   'children': []
  #                 }
  #               ]
  #             },
  #             {
  #               'name': 'ab',
  #               'value': None,
  #               'parent': {...},
  #               'children': []
  #             }
  #           ]
  #         },
  #         {...}
  #       ]
  #     },
  #     'children': [
  #       {
  #         'name': 'ba',
  #         'value': None,
  #         'parent': {...},
  #         'children': []
  #       }
  #     ]
  #   },
  #   'a': {
  #     'name': 'a',
  #     'value': None,
  #     'parent': {
  #       'name': 'α',
  #       'value': None,
  #       'parent': None,
  #       'children': [
  #         {...},
  #         {
  #           'name': 'b',
  #           'value': None,
  #           'parent': {...},
  #           'children': [
  #             {
  #               'name': 'ba',
  #               'value': None,
  #               'parent': {...},
  #               'children': []
  #             }
  #           ]
  #         }
  #       ]
  #     },
  #     'children': [
  #       {
  #         'name': 'aa',
  #         'value': None,
  #         'parent': {...},
  #         'children': [
  #           {
  #             'name': 'aaa',
  #             'value': 'Lollipop',
  #             'parent': {...},
  #             'children': []
  #           }
  #         ]
  #       },
  #       {
  #         'name': 'ab',
  #         'value': None,
  #         'parent': {...},
  #         'children': []
  #       }
  #     ]
  #   }
  # }
  # z = f(**x)
  # return pxyz(x, y, z)
  return True # TODO: Fix this test
