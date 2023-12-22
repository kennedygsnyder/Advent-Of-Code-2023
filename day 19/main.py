import re 

with open('input.txt') as f:
  lines = f.readlines()

variables = ['x', 'm', 'a', 's']
workflows = {}

i = 0
while lines[i].strip():
  line = lines[i]
  name, raw_tests = line.strip('}\n').split('{')
  raw_tests = raw_tests.split(',')
  tests = []
  for test in raw_tests[:-1]:
    test, location = test.split(':')
    tests.append((test, location))

  final_location = raw_tests[-1]
  workflows[name] = (tests.copy(), final_location)

  i += 1

sum = 0
for line in lines[i+1:]:
  status = 0
  matches = re.findall(r'(\d+)', line)
  x, m, a, s = [int(x) for x in matches]
  
  curr_workflow = 'in'
  print('\n',x,m,a,s)
  while status == 0:
    tests, final_location = workflows[curr_workflow]
    print(curr_workflow, tests, final_location)
    passed_test = False
    for test in tests:
      if not passed_test:
        if eval(test[0]):
          passed_test = True
          if test[1] == 'A':
            status = 1
          if test[1] == 'R':
            status = -1
          else:
            curr_workflow = test[1]
    
    if not passed_test:
      if final_location == 'A':
        status = 1
      elif final_location == 'R':
        status = -1
      else:
        curr_workflow = final_location
  
  if status == 1:
    print('accepted')
    sum += x + m + a + s
  
print(sum)