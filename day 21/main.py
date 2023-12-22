import numpy as np

def setup(filename):
  with open(filename) as f:
    lines = f.readlines()
  
  grid = np.zeros((len(lines), len(lines[0])-1))
  for y in range(len(lines)):
    for x in range(len(lines[0])-1):
      if lines[y][x] == '#':
        grid[y][x] = 1
      elif lines[y][x] == 'S':
        starting_point = (y,x)
  
  return np.array(grid), starting_point

def get_valid_neighbors(point, grid):
  y, x = point
  neighbors = [(y, x+1), (y, x-1), (y+1, x), (y-1, x)]
  valid_neighbors = []
  grid_size = len(grid)
  for neighbor in neighbors:
    if grid[tuple(x % grid_size for x in neighbor)] == 0:
      valid_neighbors.append(neighbor)

  return valid_neighbors

def traverse(filename, max_steps):
  grid, starting_point = setup(filename)

  queue = [(starting_point, 0)]
  parity = max_steps % 2
  visited = set()
  ending_points = set()

  while queue:
    point, steps_taken = queue.pop(0)

    if steps_taken % 2 == parity:
      ending_points.add(point)

    if steps_taken < max_steps:
      neighbors = get_valid_neighbors(point, grid)

      for neighbor in neighbors:
        if neighbor not in visited:
          visited.add(neighbor)
          queue.append((neighbor, steps_taken+1))
  
  return(len(ending_points))

def polynomial_calc(filename, num_steps):
  x = []
  y = []
  for i in range(4):
    x.append(i+.5)
    steps = 65 + i*131
    y.append(traverse(filename, steps))

  model = np.poly1d(np.polyfit(x, y, 2))
  num_steps_x = num_steps//131 + .5
  return round(model(num_steps_x))

print('Part 1:', traverse('input.txt', 64))
print('Part 2:', polynomial_calc('input.txt', 26501365))