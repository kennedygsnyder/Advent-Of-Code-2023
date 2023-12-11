nodes = {}
with open('input.txt') as f:
  lines = f.readlines()

for i in range(len(lines)):
  for j in range(len(lines[i])):
    if lines[i][j] == 'S':
      start_row = i
      start_col = j

curr_row = start_row
curr_col = start_col
length = 0

from_dir = ''
boundary_points = []

while (lines[curr_row][curr_col] != 'S' or length == 0):
  boundary_points.append([curr_row, curr_col])
  curr_val = lines[curr_row][curr_col]
  length += 1
  #starting point
  if lines[curr_row][curr_col] == 'S':
    #up
    if curr_row > 0 and lines[curr_row-1][curr_col] in '|7F':
      curr_row -= 1 
      from_dir = 'S'
    #down
    elif curr_row < len(lines)-1 and lines[curr_row+1][curr_col] in '|LJ':
      curr_row += 1 
      from_dir = 'N'
    #right
    elif curr_col < len(lines[0])-1 and lines[curr_row][curr_col+1] in '-J7':
      curr_col += 1
      from_dir = 'W'
    #left
    elif curr_col > 0 and lines[curr_row][curr_col-1] in '-LF':
      curr_col += 1
      from_dir = 'E'

  else:
    if from_dir == 'S':
      match curr_val:
        case 'F':
          curr_col += 1
          from_dir = 'W'
        case '7':
          curr_col -= 1
          from_dir = 'E'
        case '|':
          curr_row -= 1
          from_dir = 'S'

    elif from_dir == 'N':
      match curr_val:
        case 'L':
          curr_col += 1
          from_dir = 'W'
        case 'J':
          curr_col -= 1
          from_dir = 'E'
        case '|':
          curr_row += 1
          from_dir = 'N'
    elif from_dir == 'W':
      match curr_val:
        case 'J':
          curr_row -= 1
          from_dir = 'S'
        case '7':
          curr_row += 1
          from_dir = 'N'
        case '-':
          curr_col += 1
          from_dir = 'W'
    elif from_dir == 'E':
      match curr_val:
        case 'L':
          curr_row -= 1
          from_dir = 'S'
        case 'F':
          curr_row += 1
          from_dir = 'N'
        case '-':
          curr_col -= 1
          from_dir = 'E'

import numpy as np
def shoelace(x_y):
    x_y = np.array(x_y)
    x_y = x_y.reshape(-1,2)

    x = x_y[:,0]
    y = x_y[:,1]

    S1 = np.sum(x*np.roll(y,-1))
    S2 = np.sum(y*np.roll(x,-1))

    area = .5*np.absolute(S1 - S2)

    return area

area = shoelace(boundary_points)
print(area-len(boundary_points)//2+1)