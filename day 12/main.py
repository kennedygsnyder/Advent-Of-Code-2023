import re
from itertools import product

def eval_line(line, nums):
  valid_group = True
  groups = list(filter(None, re.split(r'\.+', line)))
  if len(groups) == len(nums):
    for i in range(len(nums)):
      if len(groups[i]) != nums[i]:
        valid_group = False
  else:
    valid_group = False

  return valid_group

valid_options = 0
with open("input.txt") as f:
  lines = f.readlines()
  num_lines = len(lines)

  for i in range(len(lines)):
    line = lines[i]
    print(f'{i+1}/{num_lines}')
    existing_info = line.split()[0]
    configuration = [int(x) for x in line.split()[1].split(',')]
    #print(existing_info, configuration)
    num_unknown = existing_info.count('?')

    for possibility in product('#.', repeat=num_unknown):
      test_string = ''
      possibility = list(possibility)
      #print(possibility)
      for char in existing_info:
        if char == '?':
          test_string += possibility.pop(0)
        else:
          test_string += char
      #print(test_string)
    
      if eval_line(test_string, configuration): valid_options+=1

print(valid_options)