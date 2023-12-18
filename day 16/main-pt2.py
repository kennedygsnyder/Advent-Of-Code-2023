import numpy as np
from functools import cache
with open('input.txt') as f:
  lines = f.readlines()

energized = []
items = []

for line in lines:
  items.append([char for char in line.strip()])

energized = np.zeros((len(items), len(items[0])), dtype=bool)
num_splits = 0
active_splits = 0

cache = {}
def traverse(point, dir):
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

max_total = 0

for row_num in range(len(lines)):
  energized = np.zeros((len(items), len(items[0])), dtype=bool)
  cache = {}
  traverse((row_num,0), 'E')
  total = 0
  for row in energized:
    total += sum([x == 1 for x in row])
  print(total)
  if total > max_total:
    max_total = total

  energized = np.zeros((len(items), len(items[0])), dtype=bool)
  cache = {}
  traverse((row_num,len(lines[0])-1), 'W')
  total = 0
  for row in energized:
    total += sum([x == 1 for x in row])
  print(total)
  if total > max_total:
    max_total = total

for col_num in range(len(lines[0])):
  energized = np.zeros((len(items), len(items[0])), dtype=bool)
  cache = {}
  print((0,col_num))
  traverse((0,col_num), 'S')
  total = 0
  for row in energized:
    total += sum([x == 1 for x in row])
  if total > max_total:
    max_total = total

  energized = np.zeros((len(items), len(items[0])), dtype=bool)
  cache = {}
  traverse((len(lines)-1, col_num), 'N')
  total = 0
  for row in energized:
    total += sum([x == 1 for x in row])
  if total > max_total:
    max_total = total

print(max_total)