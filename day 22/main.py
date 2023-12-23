import numpy as np

with open('day 22/input.txt') as f:
  lines = f.readlines()

bricks = []
maxes = [0,0,0]

for line in lines:
  brick_ends = [[int(y) for y in x.split(',')] for x in line.strip().split('~')]
  
  for i in range(3):
    maxes[i] = max(maxes[i], brick_ends[0][i]+1, brick_ends[1][i]+1)
  
  brick = []
  x1, y1, z1 = brick_ends[0]
  x2, y2, z2 = brick_ends[1]
  for x in range(min(x1, x2), max(x1, x2)+1):
    for y in range(min(y1, y2), max(y1, y2)+1):
      for z in range(min(z1, z2), max(z1, z2)+1):
        brick.append((x,y,z))

  bricks.append(brick)

def sim_blocks(original_bricks):
  bricks = original_bricks.copy()
  grid = np.zeros(maxes, dtype=int)
  grid[:,:,0] = -1

  brick_num = 1
  for brick in bricks:
    for x,y,z in brick:
      grid[x,y,z] = brick_num

    brick_num += 1

  block_fell = True
  while block_fell:
    block_fell = False
    for i in range(len(bricks)):
      can_move_down = True
      for point in bricks[i]:
        if grid[point[0], point[1], point[2] - 1] not in [0, i+1]:
          can_move_down = False
      
      if can_move_down:
        block_fell = True
        grid[grid == i+1] = 0
        bricks[i] = [(point[0], point[1], point[2] - 1) for point in bricks[i]]
        for point in bricks[i]:
          grid[point] = i + 1

  return bricks

bricks = sim_blocks(bricks)

movable = 0
for i in range(len(bricks)):
  test_bricks = bricks.copy()
  test_bricks.pop(i)
  shifted_bricks = sim_blocks(test_bricks)
  if shifted_bricks == test_bricks:
    movable += 1

print('Part 1:', movable)
