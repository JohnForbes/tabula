from hak.one.directory.clean import f as clean_directory
from hak.test.do import f as do_test
from hak.test.final_line.check import f as check_final_line
from hak.test.line_lengths.check import f as check_line_lengths
from hak.test.oldest_file.print import f as print_oldest_file
from hak.one.directory.filepaths.get import f as get_filepaths
from hak.many.strings.filepaths.get_least_recently_modified import f as get_least_recently_modified

if __name__ == '__main__':
  print('|'+'-'*78+'|')
  clean_directory('.')
  z = do_test(False)
  print(z['message'])
  if z['result']:
    check_line_lengths()
    check_final_line()
    print_oldest_file()
  
  archived = get_filepaths('./archive', [])
  print(f'Oldest archived: {get_least_recently_modified(archived)}')
  print('|'+'-'*78+'|')
