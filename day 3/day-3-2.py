import re
lines = []
with open('input.txt') as f:
    lines = f.readlines()
height = len(lines)
width = len(lines[0])
sum = 0

for line_num in range(height):
    for match in re.finditer(r'[\&\$\@\%\+\-\*\#\/\=]', lines[line_num]):
        touching_nums = []
        location = match.start()

        first_line = line_num - 1 if line_num != 0 else 0
        last_line = line_num + 1 if line_num != height-1 else 0
        
        for search_line_num in range(first_line, last_line+1):
            for num_match in re.finditer(r'(\d+)', lines[search_line_num]):
                for i in range (num_match.start(), num_match.end()):
                    if i >= location - 1 and i <= location + 1:
                        valid = True
                if valid:
                    touching_nums.append(int(num_match.group()))
                    valid = False

        if len(touching_nums) == 2:
            sum += touching_nums[0]*touching_nums[1]
           
print(sum)
