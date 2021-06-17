#adapted from https://stackoverflow.com/questions/9727673/list-directory-tree-structure-in-python

import sys, os
from pathlib import Path

tab =  '    '
branch = '│   '
node =    '├── '
last_node =   '└── '

def tree(dir_path: Path, prefix: str=''):
  contents = list(dir_path.iterdir())
  pointers = [node] * (len(contents) - 1) + [last_node]
  for pointer, path in zip(pointers, contents):
    if path.is_dir():
      yield prefix + pointer + path.name + os.sep
      extension = branch if pointer == node else tab
      yield from tree(path, prefix=prefix+extension)
    else:
      yield prefix + pointer + path.name

help_flags = ['-h','--h','-help','--help']

if sys.argv[1].lower() in help_flags:
  print('help menu')
else:
  with open('fileStructure.md', 'w') as f:
    f.write('# File structure\n\n```\n' + sys.argv[1] + os.sep + '\n')
    for line in tree(Path(sys.argv[1])):
      f.write(line + '\n')
    f.write('```')

with open('fileStructure.md', 'r') as f:
  print(f.read())