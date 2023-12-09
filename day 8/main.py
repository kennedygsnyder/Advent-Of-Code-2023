nodes = {}
with open('input.txt') as f:
  lines = f.readlines()

  instructions = [char for char in lines[0].strip()]
  print(instructions)

  for line in lines[2:]:
    nodes[line[0:3]] = [line[7:10],line[12:15]]

curr_node = 'AAA'
i = 0
count = 0
while curr_node != 'ZZZ':
  print(curr_node)
  if i >= len(instructions):
    i = 0
  instruction = instructions[i]
  if instruction == 'R':
    curr_node = nodes[curr_node][1]
  else:
    curr_node = nodes[curr_node][0]
  i += 1
  count+= 1
print(count)