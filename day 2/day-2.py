import re
colors = {"red":12,"green":13,"blue":14}
sum = 0
with open('input.txt') as f:
    lines = f.readlines()

    for line in lines:
        num = int(re.search(r'\d+', line).group())
        # get max num red
        counts = []
        impossible = False
        for color in colors:
            count = re.findall(fr'(\d*) {color}', line)
            for entry in count:
                if int(entry) > colors[color]:
                    impossible = True

        if not impossible:
            sum += num
    print(sum)

        