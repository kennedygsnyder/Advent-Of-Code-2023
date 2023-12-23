import numpy as np
import time
start_time = time.time()

with open('day 23/input.txt') as f:
  lines = f.readlines()

lines = [line.strip() for line in lines]

grid = np.zeros((len(lines), len(lines[0])), dtype=int)

lookup = {'.':0, '#':1, '>':0, '<':0, 'v':0, '^':0}

start_pos = (0, lines[0].index('.'))
end_pos = (len(lines)-1, lines[-1].index('.'))

for i in range(len(lines)):
  grid[i] = [lookup[char] for char in lines[i]]

def get_neighbors(point, visited):
  y, x = point
  neighbors = [(y, x+1), (y, x-1), (y+1, x), (y-1, x)]
  valid_neighbors = []

  for neighbor in neighbors:
    if neighbor[0] >= 0 and neighbor[1] >= 0 and neighbor[0] < len(grid[0]) and neighbor[1] < len(grid) and grid[neighbor] != 1 and neighbor not in visited:
      valid_neighbors.append(neighbor)

  return valid_neighbors  

def get_connected_intersections(start_point):
  start_nodes = [(x, 0, [start_point]) for x in get_neighbors(start_point, [])]
  final_nodes = []

  for node in start_nodes:
    point, path_length, visited = node
    visited.append(point)
    path_length += 1
    neighbors = get_neighbors(point, visited)
    point = neighbors[0]
    while len(neighbors) == 1:
      visited.append(neighbors[0])
      path_length += 1
      point = neighbors[0]
      neighbors = get_neighbors(neighbors[0], visited)
    
    final_nodes.append((point, path_length))
    
  return final_nodes

nodes = {}

for y in range(len(grid)):
  for x in range(len(grid[0])):
    if grid[y,x] == 0:
      if y == 0 or y == len(grid)-1 or len(get_neighbors((y,x), [])) > 2:
        nodes[y,x] = []

for point in nodes.keys():
  nodes[point] = get_connected_intersections(point)

travel_nodes = [(start_pos, 0, [])]
end_lengths = []
max_traveled = 0

while travel_nodes:
  new_travel_nodes = []

  for i in range(len(travel_nodes)):
    pos, path_length, visited = travel_nodes[i]
    if path_length > max_traveled:
      max_traveled = path_length

    if path_length * 1.2 >= max_traveled:
      if pos == end_pos:
        end_lengths.append(path_length)

      else:
        new_visited = visited.copy()
        new_visited.append(pos)

        neighbors = nodes[pos]
        
        for neighbor in neighbors:
          if neighbor[0] not in new_visited:
            new_travel_nodes.append((neighbor[0], path_length + neighbor[1], new_visited))
  
  travel_nodes = new_travel_nodes 
    
print('Part 2:', max(end_lengths))
print(f'{(time.time() - start_time):.2f} seconds')