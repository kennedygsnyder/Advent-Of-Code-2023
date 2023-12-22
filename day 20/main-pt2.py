from math import lcm, gcd
with open("input.txt") as f:
  lines = f.readlines()

ff_modules = {}
con_modules = {}
broadcaster_destinations = []
sends_to_mg = []

for i in range(len(lines)):
  line = lines[i]
  name, destinations = line[1:].strip().split(' -> ')
  destinations = destinations.split(', ')

  if name == 'roadcaster':
    print('broadcaster')
    broadcaster_destinations = line.strip().split(' -> ')[1].split(', ')

  if 'mg' in destinations:
    sends_to_mg.append(name)

  if line[0] == '%':
    ff_modules[name] = [0, destinations]
  elif line[0] == '&':
    #value, sources, source values, destinations
    con_modules[name] = [{}, destinations]

for i in range(len(lines)):
  line = lines[i]
  name, destinations = line[1:].strip().split(' -> ')
  destinations = destinations.split(', ')

  for destination in destinations:
    if destination in con_modules.keys() and name not in con_modules[destination][0].keys():
      con_modules[destination][0][name] = 0

def reset():
  for value in ff_modules.values():
    value[0] = 0

  for x in con_modules.values():
    for value in x[0].values():
      value = 0

def press_button(mg_high_from):
  turn_sent = 0

  pulses_queue = []
  pulse_count = 1
  for dest in broadcaster_destinations:
    pulses_queue.append(('broadcaster', 0, dest))

  while pulses_queue:
    source, pulse, dest = pulses_queue.pop(0)
    pulse_count += 1
    #print(pulse_count, source, '-low->' if pulse == 0 else '-high->', dest)
    
    if source == mg_high_from and pulse == 1 and dest == 'mg':
      print(pulse_count, source, '-low->' if pulse == 0 else '-high->', dest)
      turn_sent = pulse_count

    if dest in ff_modules.keys() and pulse == 0:
      for new_dest in ff_modules[dest][1]:
        pulses_queue.append((dest, 0 if ff_modules[dest][0] else 1, new_dest))
        
      ff_modules[dest][0] += 1
      ff_modules[dest][0] %= 2

    if dest in con_modules.keys():
      con_modules[dest][0][source] = pulse

      new_pulse = 0
      for source in con_modules[dest][0].values():
        if source == 0:
          new_pulse = 1
      for new_dest in con_modules[dest][1]:
        pulses_queue.append((dest, new_pulse, new_dest))
    #print(pulses_queue)
  return turn_sent


#mg receives from jg, rh, jm, hf
res = 0
while res == 0:
  res = press_button('jg')

results = []
for module in sends_to_mg:
  reset()
  res = 0
  i = 0
  while res == 0:
    res = press_button(module)
    i += 1
    
  results.append(i)

print(results)
lcm = 1
for i in results:
    lcm = lcm*i//gcd(lcm, i)
print(lcm)