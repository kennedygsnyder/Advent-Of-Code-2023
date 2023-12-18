import numpy as np
from functools import cache
with open('input.txt') as f:
  lines = f.readlines()

  print(lines)

energized = []
items = []

for line in lines:
  energized.append([0 for char in line.strip()])
  items.append([char for char in line.strip()])

print(energized)
print(items)
num_splits = 0
active_splits = 0

cache = {}
def traverse(point, dir):
  global num_splits
  global active_splits
  num_splits += 1
  active_splits += 1
  print(active_splits,'/',num_splits)

  curr_point = list(point)
  while curr_point[0] >= 0 and curr_point[1] >= 0 and curr_point[0] < len(items) and curr_point[1] < len(items[0]):
    energized[curr_point[0]][curr_point[1]] = 1
    if items[curr_point[0]][curr_point[1]] == '|':
      if tuple(curr_point) in cache and dir in cache[tuple(curr_point)]:
        return
      elif tuple(curr_point) in cache:
        cache[tuple(curr_point)].append(dir)
      if dir == 'E':
        traverse((curr_point[0]-1,curr_point[1]),'N')
        curr_point[0] += 1
        dir = 'S'
      elif dir == 'W':
        traverse((curr_point[0]+1,curr_point[1]),'S')
        curr_point[0] -= 1
        dir = 'N'
      elif dir == 'S':
        curr_point[0] += 1
      elif dir == 'N':
        curr_point[0] -= 1
    elif items[curr_point[0]][curr_point[1]] == '-':
      if tuple(curr_point) in cache and dir in cache[tuple(curr_point)]:
        return
      elif tuple(curr_point) in cache:
        cache[tuple(curr_point)].append(dir)
      else:
        cache[tuple(curr_point)] = [dir]
      if dir == 'E':
        curr_point[1] += 1
      elif dir == 'W':
        curr_point[1] -= 1
      elif dir == 'S':
        traverse((curr_point[0],curr_point[1]-1),'W')
        curr_point[1] += 1
        dir = 'E'
      elif dir == 'N':
        traverse((curr_point[0],curr_point[1]+1),'E')
        curr_point[1] -= 1
        dir = 'W'
    elif items[curr_point[0]][curr_point[1]] == '.':
      if dir == 'E':
        curr_point[1] += 1
      elif dir == 'W':
        curr_point[1] -= 1
      elif dir == 'S':
        curr_point[0] += 1
      elif dir == 'N':
        curr_point[0] -= 1
    elif items[curr_point[0]][curr_point[1]] == '/':
      if dir == 'E':
        curr_point[0] -= 1
        dir = 'N'
      elif dir == 'W':
        curr_point[0] += 1
        dir = 'S'
      elif dir == 'S':
        curr_point[1] -= 1
        dir = 'W'
      elif dir == 'N':
        curr_point[1] += 1
        dir = 'E'
    elif items[curr_point[0]][curr_point[1]] == '\\':
      if dir == 'E':
        curr_point[0] += 1
        dir = 'S'
      elif dir == 'W':
        curr_point[0] -= 1
        dir = 'N'
      elif dir == 'S':
        curr_point[1] += 1
        dir = 'E'
      elif dir == 'N':
        curr_point[1] -= 1
        dir = 'W'

  active_splits -= 1

try:
  traverse((0,0), 'E')
except: 
  print('ugh')

total = 0
print(np.array(energized))
for row in energized:
  total += sum([x == 1 for x in row])

print(total)