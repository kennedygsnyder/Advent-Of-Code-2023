import numpy as np

with open('input.txt') as f:
  patterns = [x.split('\n') for x in ''.join(f.readlines()).split('\n\n')]
  
  lookup = {"#": 1, ".": 0}
  for pattern in patterns:
    for i in range(len(pattern)):
      pattern[i] = list(lookup[char] for char in pattern[i].split()[0])

def find_vertical_reflections(pattern):
  reflection_indices = [i for i in range(len(pattern[0])-1)]
  for row in pattern:
    new_valid_reflections = []
    for reflection_index in reflection_indices:
      left = reflection_index
      right = reflection_index+1
      valid_reflection = True
      while left >= 0 and right < len(row):
        if row[left] != row[right]:
          valid_reflection = False
          left = -1
        else:
          left -= 1
          right += 1
      if valid_reflection:
        new_valid_reflections.append(reflection_index)
      reflection_indices = new_valid_reflections
  return reflection_indices[0]+1 if reflection_indices else -1


summary = 0
for pattern in patterns:
  reflection = find_vertical_reflections(pattern)
  if reflection != -1:
    summary += reflection
  else:
    pattern = np.array(pattern).T.tolist()
    reflection = find_vertical_reflections(pattern)
    summary += 100 * reflection

print(summary)


      
