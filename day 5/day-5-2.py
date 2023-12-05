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

keys.reverse()
match_found = False
i = 0
while not match_found:
    print(i)
    curr_location = i
    for key in keys:
        new_location = 0
        for entry in key:
            if entry[0] <= curr_location and entry[0]+entry[2] > curr_location:
                new_location = curr_location - entry[0] + entry[1]
                break
        curr_location = new_location if new_location != 0 else curr_location
    
    for j in range(0,len(seeds),2):
        if curr_location >= seeds[j] and curr_location < seeds[j]+seeds[j+1]:
            print(i)
            match_found = True
    i += 1

    