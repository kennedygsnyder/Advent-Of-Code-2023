sum = 0
with open('input.txt') as f:
    lines = f.readlines()

    for line in lines:
        num_lists = line.split(":")[1].split("|")
        winning = [int(x) for x in num_lists[0].split()]
        have = [int(x) for x in num_lists[1].split()]

        matches = [num for num in have if num in winning]
        sum += 2**(len(matches)-1) if len(matches) > 0 else 0
print(sum)