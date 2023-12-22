import numpy as np

with open("input.txt") as f:
  lines = f.readlines()

instructions = []
for line in lines:
  line = line.strip()
  line = line.split()
  instructions.append([line[0], int(line[1])])

width = 1
height = 1
for instr in instructions:
  if instr[0] == 'R':
    width += instr[1]
  if instr[0] == 'D':
    height += instr[1]

grid = np.zeros((2*height, 2*width), dtype=int)

curr_point = [height, width]
boundary_points = []
while instructions:
  grid[tuple(curr_point)] = 1
  boundary_points.append(curr_point.copy())
  if instructions[0][1] > 0:
    if instructions[0][0] == 'R':
      curr_point[1] += 1
    elif instructions[0][0] == 'L':
      curr_point[1] -= 1
    elif instructions[0][0] == 'U':
      curr_point[0] -= 1
    elif instructions[0][0] == 'D':
      curr_point[0] += 1
    instructions[0][1] -= 1
  else:
    instructions.pop(0)


#flood fill
fill_start_point = [0,0]
for i in range(len(grid)):
  row = grid[i]
  if sum(row) == 2:
    indices = [i for i in range(len(row)) if row[i] == 1]
    if indices[1] - indices[0] > 1:
      fill_start_point = [i, indices[0]+1]

queue = [fill_start_point]
while queue:
  curr_point = queue.pop(0)
  grid[tuple(curr_point)] = 1
  neighbors = [[0,1],[0,-1],[1,0],[-1,0]]
  neighbors = [[curr_point[0]+n[0], curr_point[1]+n[1]] for n in neighbors]
  for n in neighbors:
    if grid[tuple(n)] == 0 and n not in queue:
      queue.append(n)

print(sum(sum(grid)))