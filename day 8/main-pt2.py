nodes = {}
with open('input.txt') as f:
  lines = f.readlines()

  instructions = [char for char in lines[0].strip()]
  print(instructions)

  for line in lines[2:]:
    nodes[line[0:3]] = [line[7:10],line[12:15]]

curr_nodes = [node for node in nodes.keys() if node[2] == 'A']
counts = []
for curr_node in curr_nodes:
  i = 0
  count = 0
  print(curr_node)
  while curr_node[2] != 'Z':
    if i >= len(instructions):
      i = 0
    instruction = instructions[i]
    if instruction == 'R':
      curr_node = nodes[curr_node][1]
    else:
      curr_node = nodes[curr_node][0]
    i += 1
    count+= 1
  counts.append(count)

print(counts)
from math import lcm, gcd
lcm = 1
for i in counts:
    lcm = lcm*i//gcd(lcm, i)
print(lcm)