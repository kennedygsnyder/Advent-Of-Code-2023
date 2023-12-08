from collections import Counter
with open('input.txt') as f:
  lines = f.readlines()

  hands = []
  for line in lines:
    bid = int(line[6:])
    hand = []
    for char in line[0:5]:
      if char == 'A':
        hand.append(14)
      elif char == 'K':
        hand.append(13)
      elif char == 'Q':
        hand.append(12)
      elif char == 'J':
        hand.append(11)
      elif char == 'T':
        hand.append(10)
      else:
        hand.append(int(char))

      card_counts = Counter(hand)
      num_unique_cards = len(card_counts)
      type = 1 #high card by default
      if num_unique_cards == 1:
        type = 7 #five of a kind
      elif num_unique_cards == 2:
        if card_counts.most_common()[0][1] == 4:
          type = 6 #four of a kind
        else:
          type = 5 #three of a kind
      elif num_unique_cards == 3:
        if card_counts.most_common()[0][1] == 3:
          type = 4 #three of a kind
        else:
          type = 3 #two pair
      elif num_unique_cards == 4:
        type = 2 #one pair

    hands.append([bid,type,hand])

hands = sorted(hands, key = lambda x: (x[1],x[2]))
total = 0
for i in range(len(hands)):
  total += (i+1)*hands[i][0]
print(total)

#get types of hands
