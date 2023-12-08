sum = 0
words = {"one":'1',"two":'2',"three":'3',"four":'4',"five":'5',"six":'6',"seven":'7',"eight":'8',"nine":'9',"zero":'0'}

with open('input.txt') as f:
    lines = f.readlines()

    for line in lines:
        values = []
        for i in range(len(line)):
            if line[i].isnumeric(): 
                values.append(line[i])
            for j in range(3,6):
                if line[i:i+j] in words:
                    values.append(words[line[i:i+j]])
        sum += int(values[0] + values[-1])
    print(sum)

    