import numpy as np
import time
start_time = time.time()
with open("input.txt") as f:
  lines = f.readlines()

array = []
lookup = {"#": 2, "O": 1, ".": 0}

for line in lines:
  array.append(list(lookup[char] for char in line.strip()))
array = np.array(array)

def roll_west(array_tuple):
  array = np.array(array_tuple)
  for row in array:
    for i in range(len(row)):
      if row[i] == 1:
        curr_index = i
        while curr_index > 0 and row[curr_index-1] == 0:
          curr_index -= 1
        if curr_index != i:
          row[curr_index] = 1
          row[i] = 0
  return array

cache = []
def cycle(array_tuple):
  cached_index = -1
  if array_tuple in cache:
    cached_index = cache.index(array_tuple)

  array = list(array_tuple)
  for i in range(4):
    array = roll_west(tuple([tuple(row) for row in array]))
    array = np.rot90(array, k=1, axes=(1,0))
  
  cache.append(array_tuple)
  return array, cached_index

i = 0
num_cycles = 1000000000
cycle_found = False
array = np.rot90(array)

while i < num_cycles:
  array, cached_index = cycle(tuple([tuple(row) for row in array]))

  if not cycle_found and cached_index != -1:
    cycle_found = True
    cycle_length = i - cached_index
    remaining_cycles = num_cycles - i
    i += ((remaining_cycles-1) // cycle_length) * cycle_length
  i += 1

array = np.rot90(array, k=1, axes=(1,0))

total = 0
score = len(array)
for row in array:
  total += score * len([x for x in row if x == 1])
  score -= 1

print(total)
print(f'{(time.time() - start_time):.2f} seconds')