import re
with open('input.txt') as f:
  lines = f.readlines()

codes = lines[0].split(',')
boxes = []
for i in range(256):
  boxes.append({})

sum = 0
for code in codes:
  code_string = re.split(r'[=-]', code)[0]

  current_value = 0
  for char in code_string:
    current_value += ord(char)
    current_value *= 17
    current_value %= 256

  operator = '=' if '=' in code else '-'
  if operator == '=':
    num = int(re.split(r'[=-]', code)[1])
    boxes[current_value][code_string] = num
  else:
    if code_string in boxes[current_value].keys():
      del boxes[current_value][code_string]
  
print(boxes)
sum = 0
for i in range(len(boxes)):
  for j in range(len(boxes[i])):
    key, val = list(boxes[i].items())[j]
    sum += (i+1)*(j+1)*val

print(sum)