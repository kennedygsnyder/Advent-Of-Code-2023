import numpy as np

with open('input.txt') as f:
  patterns = [x.split('\n') for x in ''.join(f.readlines()).split('\n\n')]
  
  lookup = {"#": 1, ".": 0}
  for pattern in patterns:
    for i in range(len(pattern)):
      pattern[i] = list(lookup[char] for char in pattern[i].split()[0])

def find_vertical_reflections(pattern):
  reflection_indices = [(i, False) for i in range(len(pattern[0])-1)]
  for row in pattern:
    new_valid_reflections = []
    for item in reflection_indices:
      reflection_index, error_used = item
      left = reflection_index
      right = reflection_index+1
      valid_reflection = True
      while left >= 0 and right < len(row):
        if row[left] != row[right]:
          if error_used:
            valid_reflection = False
            left = -1
          else:
            error_used = True
            left -= 1
            right += 1
        else:
          left -= 1
          right += 1

      if valid_reflection:
        new_valid_reflections.append((reflection_index, error_used))
      reflection_indices = new_valid_reflections
  for item in reflection_indices:
    if item[1] == True:
      return item[0]+1
  return -1


summary = 0
for pattern in patterns:
  reflection = find_vertical_reflections(pattern)
  if reflection != -1:
    summary += reflection
  else:
    pattern = np.array(pattern).T.tolist()
    reflection = find_vertical_reflections(pattern)
    summary += 100 * reflection
  print(reflection)

print(summary)


      
