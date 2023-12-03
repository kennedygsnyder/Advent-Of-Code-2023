import re
lines = []
with open('input.txt') as f:
    lines = f.readlines()
height = len(lines)
width = len(lines[0])
sum = 0

for line_num in range(height):
    for match in re.finditer(r'\d+', lines[line_num]):
        valid = False
        start = match.start()
        end = match.end()

        first_line = line_num - 1 if line_num != 0 else 0
        last_line = line_num + 1 if line_num != height-1 else height-1
        
        first_char = start - 1 if start != 0 else 0
        last_char = end if end != width else width
        for search_line_num in range(first_line, last_line+1):
            for char in lines[search_line_num][first_char:last_char+1]:
                if char in "&$@%+-*#/=":
                    valid = True
        if valid:
            sum += int(match.group())

print(sum)
