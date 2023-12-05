count = 0
cards = []
with open('input.txt') as f:
    lines = f.readlines()

    for line in lines:
        num_lists = line.split(":")[1].split("|")
        winning = [int(x) for x in num_lists[0].split()]
        have = [int(x) for x in num_lists[1].split()]
        cards.append([winning, have, 1])

    while cards:
        card = cards.pop(0)
        matches = [num for num in card[1] if num in card[0]]
        for i in range(card[2]):
            count += 1
            for j in range(len(matches)):
                cards[j][2] += 1

print(count)