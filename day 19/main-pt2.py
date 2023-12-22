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

def get_all_states(rules, workflow, test_num):
  if workflow == 'A':
    return (rules,)
  if workflow == 'R':
    return ()
  
  info = workflows[workflow]
  tests, final_location = info
  results = []
    
  test = tests[test_num]
  results += get_all_states(rules + [test[0]], test[1], 0)
  
  next_workflow = final_location if test_num == len(tests) - 1 else workflow
  next_test_num = 0 if test_num == len(tests) - 1 else test_num + 1

  new_operator = '>=' if '<' in test[0] else '<='
  new_test = test[0][0] + new_operator + test[0][2:]

  results += get_all_states(rules + [new_test], next_workflow, next_test_num)

  return results

states = get_all_states([], 'in', 0)

sum = 0
i = 1
for state in states:
  print(f'{i}/{len(states)}')
  nums = {'x':[x for x in range(1,4001)], 'm': [x for x in range(1,4001)], 'a': [x for x in range(1,4001)], 's': [x for x in range(1,4001)]}
  for rule in state:
    var = rule[0]
    eq = 'x' + rule[1:]
    nums[var] = [x for x in nums[var] if eval(eq)]
  i+= 1
  sum += len(nums['x']) * len(nums['m']) * len(nums['a']) * len(nums['s'])

print(sum)