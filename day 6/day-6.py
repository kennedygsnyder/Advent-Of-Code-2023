times = []
distances = []

with open('input.txt') as f:
  lines = f.readlines()

  times = [int(x) for x in lines[0].split()[1:]]
  distances = [int(x) for x in lines[1].split()[1:]]
  
product = 1
for i in range(len(times)):
  time = times[i]
  distance = distances[i]
  num_possibilities = 0
  for i in range(time):
    if ((time - i)*i > distance):
      num_possibilities += 1
      
  product *= num_possibilities
print(product)

