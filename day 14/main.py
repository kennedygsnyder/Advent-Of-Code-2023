import numpy as np
with open("input.txt") as f:
  lines = f.readlines()

array = []
lookup = {"#": 2, "O": 1, ".": 0}

for line in lines:
  array.append(list(lookup[char] for char in line.strip()))

array = np.array(array).T.tolist()

for row in array:
  for i in range(len(row)):
    if row[i] == 1:
      curr_index = i
      while curr_index > 0 and row[curr_index-1] == 0:
        curr_index -= 1
      if curr_index != i:
        row[curr_index] = 1
        row[i] = 0


array = np.array(array).T.tolist()
total = 0
score = len(array)
for row in array:
  total += score * len([x for x in row if x == 1])
  score -= 1

print(total)


