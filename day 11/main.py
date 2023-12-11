galaxies = []
with open('input.txt') as f:
  lines = f.readlines()
  for line in lines:
    line = line.strip()
    x = 0
    if all([char == '.' for char in line]):
      galaxies.append('x'*len(line))
    else:
      galaxies.append(line)

#rotate
galaxies_expanded = []
for line in galaxies:
  galaxies_expanded.append('')

#get rows
for i in range(len(galaxies[0])):
  col = [row[i] for row in galaxies]

  if all([char in '.x' for char in col]):
    for j in range(len(galaxies)):
      galaxies_expanded[j] += ('x')
  else:
    for j in range(len(galaxies)):
      galaxies_expanded[j] += galaxies[j][i]

galaxies = galaxies_expanded

list_galaxies = []
for i in range(len(galaxies)):
  for j in range(len(galaxies[0])):
    if galaxies[i][j] == '#':
      list_galaxies.append([i,j])

from itertools import combinations
combinations = list(combinations(list_galaxies,2))
sum_dist = 0

for combo in combinations:
  galaxy_1, galaxy_2 = combo
  dist = 0
  x1 = min(galaxy_1[1], galaxy_2[1])
  x2 = max(galaxy_1[1], galaxy_2[1])
  y1 = min(galaxy_1[0], galaxy_2[0])
  y2 = max(galaxy_1[0], galaxy_2[0])
  while x1 < x2:
    if (galaxies[y1][x1] == 'x'):
      x1 += 1
      dist += 1000000
    else:
      x1 += 1
      dist += 1
  while y1 < y2:
    if (galaxies[y1][x1] == 'x'):
      y1 += 1
      dist += 1000000
    else:
      y1 += 1
      dist += 1
  sum_dist+= dist
print(sum_dist)