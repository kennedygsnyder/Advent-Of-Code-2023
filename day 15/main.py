with open('input.txt') as f:
  lines = f.readlines()

codes = lines[0].split(',')

sum = 0
for code in codes:
  current_value = 0
  for char in code:
    current_value += ord(char)
    current_value *= 17
    current_value %= 256
  
  sum += current_value
print(sum)