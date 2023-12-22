with open("input.txt") as f:
  lines = f.readlines()

ff_modules = {}
con_modules = {}
broadcaster_destinations = []

for i in range(len(lines)):
  line = lines[i]
  name, destinations = line[1:].strip().split(' -> ')
  destinations = destinations.split(', ')

  if line[0:11] == 'broadcaster':
    broadcaster_destinations = line.strip().split(' -> ')[1].split(', ')

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

def press_button():
  low_pulses_sent = 1
  high_pulses_sent = 0

  pulses_queue = []
  for dest in broadcaster_destinations:
    pulses_queue.append(('broadcaster', 0, dest))

  while pulses_queue:
    source, pulse, dest = pulses_queue.pop(0)

    if pulse == 0:
      low_pulses_sent += 1
    else:
      high_pulses_sent += 1

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
  return low_pulses_sent, high_pulses_sent

low_sum = 0
high_sum = 0
for i in range(1000):
  low, high = press_button()
  low_sum += low
  high_sum += high

print(low_sum, high_sum, low_sum * high_sum)