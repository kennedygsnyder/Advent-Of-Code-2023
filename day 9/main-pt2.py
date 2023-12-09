nodes = {}
with open('input.txt') as f:
  lines = f.readlines()

sum = 0
for line in lines:
  array = []
  curr_array = [int(x) for x in line.split(' ')]
  array.append(curr_array)

  while not all(x == 0 for x in curr_array):
    curr_array = []
    for i in range(len(array[-1])-1):
      curr_array.append(array[-1][i+1]-array[-1][i])
    array.append(curr_array)

  array[-1].insert(0,0)
  for i in range(len(array)-3,-1,-1):
    array[i].insert(0,array[i][0]-array[i+1][0])

  sum+= array[0][0]

print(sum)

