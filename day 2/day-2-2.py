import re
colors = ["red","green","blue"]
sum = 0
with open('input.txt') as f:
    lines = f.readlines()

    for line in lines:
        num = int(re.search(r'\d+', line).group())
        # get max num red
        counts = []
        impossible = False
        for color in colors:
            count = [int(x) for x in re.findall(fr'(\d*) {color}', line)]
            counts.append(max(count))
        sum += counts[0]*counts[1]*counts[2]

    print(sum)

    