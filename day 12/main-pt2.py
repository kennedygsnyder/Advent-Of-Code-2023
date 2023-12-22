import re
from functools import cache

@cache
def eval_line(line, nums):
  line = line.strip('.')
  #print(line, nums)
  counts = 0
  groups = list(filter(None, re.split(r'[\.?]+', line)))
  if len(nums) == 0:
    return 0
  if len(line) < (sum(nums) + len(nums)-1):
    return 0
  
  q_index = line.find('?')
  if q_index == -1:
    if len(groups) > len(nums) or len(groups) < len(nums):
      return 0
    else:
      if all([len(groups[i]) == nums[i] for i in range(len(groups))]):
        return 1
      else:
        return 0
  
  if len(groups) == len(nums):
    if all([len(groups[i]) == nums[i] for i in range(len(groups))]):
      return 1

  groups = list(filter(None, re.split(r'[\.]+', line)))
  if len(groups) > 0 and not '?' in groups[0]:
    if len(groups[0]) == nums[0]:
      counts += eval_line('.'.join(groups[1:]), nums[1:])
  else:
    newline = ''
    i = 0
    while line[i] != '?':
      newline += (line[i])
      i+=1
    counts += eval_line(newline + '#' + line[i+1:], nums)
    counts += eval_line(newline + '.' + line[i+1:], nums)
  
  return counts

valid_options = 0
with open("input.txt") as f:
  lines = f.readlines()
  num_lines = len(lines)

  for i in range(len(lines)):
    line = lines[i]
    print(f'{i}/{num_lines}')
    existing_info = line.split()[0]
    existing_info = (existing_info + '?') * 4 + existing_info
    configuration = [int(x) for x in line.split()[1].split(',')]
    configuration = configuration * 5
    num_unknown = existing_info.count('?')

    num = eval_line(existing_info, tuple(configuration))
    valid_options += num

print(valid_options)