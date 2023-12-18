import heapq

max_dist = 1000000000

def is_in_bounds(point):
  if point[0] >= 0 and point[0] < len(heat_losses) and point[1] >= 0 and point[1] < len(heat_losses[0]):
    return True
  return False

with open("input.txt") as f:
  lines = f.readlines()

heat_losses = []
nodes = {}

for line in lines:
  heat_losses.append([int(x) for x in line.strip()])

for i in range(len(heat_losses)):
  for j in range(len(heat_losses[0])):
    nodes[i,j] = {'E': {1: max_dist, 2: max_dist, 3: max_dist}, 
                  'W': {1: max_dist, 2: max_dist, 3: max_dist}, 
                  'S': {1: max_dist, 2: max_dist, 3: max_dist}, 
                  'N': {1: max_dist, 2: max_dist, 3: max_dist}} 

def get_neighbors(node, straight_moved, dir):
  neighbors = []
  r, c = node
  if straight_moved < 3:
    if dir == 'E':
      neighbors.append([[r, c+1], straight_moved + 1, dir])
    if dir == 'W':
      neighbors.append([[r, c-1], straight_moved + 1, dir])
    if dir == 'N':
      neighbors.append([[r-1, c], straight_moved + 1, dir])
    if dir == 'S':
      neighbors.append([[r+1, c], straight_moved + 1, dir])
    
  if dir in ['E','W']:
    neighbors.append([[r-1,c], 1, 'N'])
    neighbors.append([[r+1,c], 1, 'S'])
  if dir in ['N', 'S']:
    neighbors.append([[r,c+1], 1, 'E'])
    neighbors.append([[r,c-1], 1, 'W'])

  neighbors = [neighbor for neighbor in neighbors if is_in_bounds(neighbor[0])]
  return neighbors


reached_end = False
visited = []
queue = []
heapq.heappush(queue, (0, (0,0), 0, 'E'))

i = 0
while queue:
  dist, node, straight_moved, dir = heapq.heappop(queue)

  if node == [len(heat_losses)-1, len(heat_losses[0])-1]:
    queue = []
  
  visited.append(node)
  neighbors = get_neighbors(node, straight_moved, dir)

  for neighbor in neighbors:
    new_node, new_straight_moved, new_dir = neighbor
    new_dist = dist + heat_losses[new_node[0]][new_node[1]]
    new_state = (new_dist, new_node, new_straight_moved, new_dir)
    
    min_dist = nodes[tuple(neighbor[0])][new_dir][new_straight_moved]
    if new_dist < min_dist:
      nodes[tuple(neighbor[0])][new_dir][new_straight_moved] = min(new_dist, min_dist)
      heapq.heappush(queue, new_state)
  
  i += 1

min_travel = max_dist
for key, value in nodes[len(heat_losses)-1, len(heat_losses[0])-1].items():
  travel = min(value.values())
  min_travel = min(min_travel, travel)

print(min_travel)