with open('./2020/day08/input.txt', "r") as f:
    instructions = f.read().split("\n")
end = len(instructions)

accumulator = 0
index = 0
visited = []
while index not in visited:
    instru = instructions[index]
    visited.append(index)
    cmd, nb = instru[:3], int(instru[4:])
    if cmd == 'jmp':
        index += nb
    else:
        index += 1
        if cmd == 'acc':
            accumulator += nb
print(accumulator)

# Part 2
# we want to reach index == len(instructions)

def execute_part2(change_line_index):
    accumulator = 0
    index = 0
    visited = [len(instructions)]
    while index not in visited:
        instru = instructions[index]
        if index != change_line_index:
            visited.append(index)
            cmd, nb = instru[:3], int(instru[4:])
            if cmd == 'jmp':
                index += nb
            else:
                index += 1
                if cmd == 'acc':
                    accumulator += nb
        else:
            visited.append(index)
            cmd, nb = instru[:3], int(instru[4:])
            if cmd == 'nop':
                index += nb
            else:
                index += 1
                if cmd == 'acc':
                    accumulator += nb
                    print('pas le bon indice, c\'est un accumulateur ici')
    return index==len(instructions), accumulator

indexes_to_tweak = []
index = 0
for instru in instructions:
    if instru[:3]=='jmp' or instru[:3]=='nop':
        indexes_to_tweak.append(index)
    index += 1

for i in indexes_to_tweak:
    b, acc = execute_part2(i)
    if b:
        print(acc)