import heapq

def is_in_bounds(point):
  if point[0] >= 0 and point[0] < len(heat_losses) and point[1] >= 0 and point[1] < len(heat_losses[0]):
    return True
  return False

def get_neighbors(node, straight_moved, dir):
  neighbors = []
  r, c = node
  if straight_moved < max_consecutive:
    if dir == 'E':
      neighbors.append([[r, c+1], straight_moved + 1, dir])
    if dir == 'W':
      neighbors.append([[r, c-1], straight_moved + 1, dir])
    if dir == 'N':
      neighbors.append([[r-1, c], straight_moved + 1, dir])
    if dir == 'S':
      neighbors.append([[r+1, c], straight_moved + 1, dir])
    
  if straight_moved >= min_consecutive:
    if dir in ['E', 'W']:
      neighbors.append([[r-1,c], 1, 'N'])
      neighbors.append([[r+1,c], 1, 'S'])
    if dir in ['N', 'S']:
      neighbors.append([[r,c-1], 1, 'W'])
      neighbors.append([[r,c+1], 1, 'E'])

  neighbors = [neighbor for neighbor in neighbors if is_in_bounds(neighbor[0])]
  return neighbors

reached_end = False
visited = []
queue = []
heat_losses = []
nodes = {}
max_dist = 1000000000
min_consecutive = 4
max_consecutive = 10

with open("input.txt") as f:
  lines = f.readlines()

for line in lines:
  heat_losses.append([int(x) for x in line.strip()])

for i in range(len(heat_losses)):
  for j in range(len(heat_losses[0])):
    nodes[i,j] = {}
    for dir in ['E', 'W', 'S', 'N']:
      for k in range(max_consecutive):
        nodes[i,j][dir, k+1] = (max_dist, '')

heapq.heappush(queue, (0, (0,0), 0, 'E', '0-0>'))
heapq.heappush(queue, (0, (0,0), 0, 'S', '0-0>'))

i = 0
while queue:
  dist, node, straight_moved, dir, path = heapq.heappop(queue)

  visited.append(node)
  neighbors = get_neighbors(node, straight_moved, dir)

  for neighbor in neighbors:
    new_node, new_straight_moved, new_dir = neighbor
    new_dist = dist + heat_losses[new_node[0]][new_node[1]]
    new_path = path+str(new_node[0])+'-'+str(new_node[1])+'>'
    new_state = (new_dist, new_node, new_straight_moved, new_dir, new_path)

    min_dist = nodes[tuple(neighbor[0])][new_dir, new_straight_moved][0]
    if new_dist < min_dist:
      nodes[tuple(neighbor[0])][new_dir, new_straight_moved] = (min(new_dist, min_dist), new_path)
      heapq.heappush(queue, new_state)
  
  i += 1

min_travel = min([value[0] for value in nodes[len(heat_losses)-1, len(heat_losses[0])-1].values()])
print(min_travel)
