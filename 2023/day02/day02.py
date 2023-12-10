with open('./2023/day02/input.txt', "r") as f:
    lines = f.read().split("\n")

available = {'red':12, 'green': 13, 'blue': 14}

"Game 4: 2 green, 2 blue; 12 red, 9 green, 2 blue; 13 green, 15 red, 4 blue; 14 red, 3 green, 5 blue; 6 red, 1 green; 1 blue, 2 red, 2 green"

def parser(line):
    num,line = line.split(':')
    num = int(num.split(' ')[-1])
    tirages = line.split(';')
    for tirage in tirages:
        tirs = tirage.split(',')
        for tir in tirs:
            input = tir.strip()
            quantity,color = input.split(' ')
            if int(quantity) > available[color]:
                num = 0
                break
    # if num!=0:
        # print(num)
    return num
    
def part1(lines):
    sum = 0
    for line in lines:
        sum += parser(line)
    return sum

print(part1(lines))

def part2(lines):
    sum = 0
    for line in lines:
        minimal_set = {'red':0, 'green':0, 'blue':0}
        _,line = line.split(':')
        tirages = line.split(';')
        for tirage in tirages:
            tirs = tirage.split(',')
            for tir in tirs:
                input = tir.strip()
                quantity,color = input.split(' ')
                quantity = int(quantity)
                if quantity > minimal_set[color]:
                    minimal_set[color] = quantity
        sum += minimal_set['green']*minimal_set['blue']*minimal_set['red']
    return sum

print(part2(lines))
