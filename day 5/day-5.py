seeds = []
keys = []
min = -1
with open('input.txt') as f:
    lines = f.readlines()

    seeds = [int(x) for x in lines[0].split()[1:]]

    raw_keys = [line.strip() for line in lines[2:] if (line[0].isdigit() or line[0] == "\n")]
    raw_keys.append('')

#get all keys
while len(raw_keys) > 0:
    new_key = []
    key = raw_keys.pop(0)
    while key != '' and len(raw_keys) != 0:
        new_key.append([int(x) for x in key.split()])
        key = raw_keys.pop(0)
    keys.append(new_key)
        
for seed in seeds:
    curr_location = seed
    for key in keys:
        new_location = 0
        for entry in key:
            if entry[1] <= curr_location and entry[1]+entry[2] >= curr_location:
                new_location = curr_location - entry[1] + entry[0]
        curr_location = new_location if new_location != 0 else curr_location
    if min == -1 or curr_location < min:
        min = curr_location

print(min)
    