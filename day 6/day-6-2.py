with open('input.txt') as f:
  lines = f.readlines()

  time = int(''.join([char for char in lines[0] if char.isnumeric()]))
  distance = int(''.join([char for char in lines[1] if char.isnumeric()]))

product = 1
num_possibilities = 0
for i in range(time):
  if ((time - i)*i > distance):
    num_possibilities += 1
    
print(num_possibilities)