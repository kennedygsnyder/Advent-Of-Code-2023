import numpy as np

with open("input.txt") as f:
  lines = f.readlines()

instructions = []
for line in lines:
  line = line.split('#')[1].strip().strip(')')
  instructions.append([int(line[5]), int(line[0:5], 16)])

curr_point = [0, 0]
boundary_points = [[0,0]]
answer = 0
while instructions:
  dir, num = instructions.pop(0)
  if dir == 0:
    curr_point[1] += num
  elif dir == 2:
    curr_point[1] -= num
  elif dir == 3:
    curr_point[0] -= num
  elif dir == 1:
    curr_point[0] += num
  boundary_points.append(curr_point.copy())
  answer += num

area = 0
for i in range(len(boundary_points)):
  a = boundary_points[i]
  b = boundary_points[(i+1) % len(boundary_points)]
  area += a[1] * b[0] - a[0] * b[1]

area = int(abs(area) / 2)
square_area = int(area - answer / 2 + 1)

answer += square_area
print(answer)    