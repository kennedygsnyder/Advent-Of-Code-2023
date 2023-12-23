import numpy as np
import sys
sys.setrecursionlimit(10**6)
import time
start_time = time.time()

with open('day 23/input.txt') as f:
  lines = f.readlines()

lines = [line.strip() for line in lines]

grid = np.zeros((len(lines), len(lines[0])), dtype=int)

lookup = {'.':0, '#':1, '>':2, '<':3, 'v':4, '^':5}

start_pos = (0, lines[0].index('.'))
end_pos = (len(lines)-1, lines[-1].index('.'))

for i in range(len(lines)):
  grid[i] = [lookup[char] for char in lines[i]]

def get_neighbors(point, grid):
  y, x = point
  neighbors = [(y, x+1), (y, x-1), (y+1, x), (y-1, x)]
  valid_neighbors = []
  if grid[point] in [2,3,4,5]:
    neighbors = [neighbors[grid[point]-2]]
  for neighbor in neighbors:
    if grid[neighbor] != 1:
      valid_neighbors.append(neighbor)

  return valid_neighbors  

def paths(start_pos, end_pos, visited, path_length):
  if start_pos[0] - 5 > end_pos[0]:
    return 0
  
  if start_pos == end_pos:
    return path_length
  
  if start_pos not in visited:
    new_visited = visited.copy()
    new_visited.append(start_pos)

    results = []
    neighbors = get_neighbors(start_pos, grid)
    for neighbor in neighbors:
      results.append(paths(neighbor, end_pos, new_visited, path_length+1))
    return max(results)
  
  return 0

midpoints = np.where(grid[70] == 0)[0]

midpoint_maxes = []
for midpoint in midpoints:
  midpoint_maxes.append(paths(start_pos, (70, midpoint), [], 0))

end_maxes = []
for midpoint in midpoints:
  end_maxes.append(paths((70,midpoint), end_pos, [], 0))

final_totals = []
for i in range(len(midpoints)):
  final_totals.append(midpoint_maxes[i] + end_maxes[i])

print('Part 1:', max(final_totals))
print(f'{(time.time() - start_time):.2f} seconds')