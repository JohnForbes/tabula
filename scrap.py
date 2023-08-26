from src.classes.table import Table

t = Table()
t.add_record({'a': 1})
t.add_record({'a': 2, 'b': 'boo'})

print(t._cells)
print(t.row_count)

column_a = t.get_column('a')
print(column_a)