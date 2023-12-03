sum = 0

with open('input.txt') as f:
    lines = f.readlines()

    for line in lines:
        ints = [char for char in line if char.isdigit()]
        sum += int(ints[0]+ints[-1])

print(sum)
    