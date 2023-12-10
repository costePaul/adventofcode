# with open('./2023/day03/input.txt', "r") as f:
with open('./2023/day03/test.txt', "r") as f:
    lines = f.read().split("\n")

NUMBERS = '0123456789'
symbols = NUMBERS+'.'

def find_full_number(lines, i,j, column_max, symb):
    index_start = j
    index_end = j
    if lines[i][j] not in NUMBERS:
        return 0
    while index_end<=column_max-1 and lines[i][index_end] in NUMBERS:
        index_end+=1
    while index_start>=0 and lines[i][index_start] in NUMBERS:
        index_start-=1
    print(i,j, lines[i][j], index_end, index_start)
    rez = int(lines[i][index_start+1:index_end])
    print(rez, 'tracked by', lines[i][j], 'retenu by ', symb)
    return rez

def find_near_numbers(lines,i, j, row_max, column_max):
    numbers = []
    if i==0:
        if j==0:
            if lines[0][1] in NUMBERS:
                numbers.append([0,1, lines[i][j]])
            if lines[1][0] in NUMBERS:
                numbers.append([1,0, lines[i][j]])
            elif lines[1][1] in NUMBERS:
                numbers.append([1,1, lines[i][j]])
        elif j==column_max-1:
            if lines[0][column_max-2] in NUMBERS:
                numbers.append([0,column_max-2, lines[i][j]])
            if lines[1][column_max-1] in NUMBERS:
                numbers.append([1,column_max-1, lines[i][j]])
            elif lines[1][column_max-2] in NUMBERS:
                numbers.append([1,column_max-2, lines[i][j]])
        else:
            if lines[0][j-1] in NUMBERS:
                numbers.append([0,j-1, lines[i][j]])
            if lines[0][j+1] in NUMBERS:
                numbers.append([0,j+1, lines[i][j]])
            if lines[1][j-1] in NUMBERS:
                numbers.append([1,j-1, lines[i][j]])
                if lines[1][j+1] in NUMBERS and lines[1][j] not in NUMBERS:
                    numbers.append([1,j+1, lines[i][j]])
            elif lines[1][j] in NUMBERS:
                numbers.append([1,j, lines[i][j]])
            elif lines[1][j+1] in NUMBERS:
                numbers.append([1,j+1, lines[i][j]])
    elif i==row_max-1:
        if j==0:
            if lines[row_max-1][1] in NUMBERS:
                numbers.append([row_max-1,1, lines[i][j]])
            if lines[row_max-2][0] in NUMBERS:
                numbers.append([row_max-2,0, lines[i][j]])
            elif lines[row_max-1][1] in NUMBERS:
                numbers.append([row_max-1,1, lines[i][j]])
        elif j==column_max-1:
            if lines[row_max-1][column_max-2] in NUMBERS:
                numbers.append([row_max-1,column_max-2, lines[i][j]])
            if lines[row_max-2][column_max-1] in NUMBERS:
                numbers.append([row_max-2,column_max-1, lines[i][j]])
            elif lines[row_max-1][column_max-2] in NUMBERS:
                numbers.append([row_max-1,column_max-2, lines[i][j]])
        else:
            if lines[row_max-1][j-1] in NUMBERS:
                numbers.append([row_max-1,j-1, lines[i][j]])
            if lines[row_max-1][j+1] in NUMBERS:
                numbers.append([row_max-1,j+1, lines[i][j]])
            if lines[row_max-2][j-1] in NUMBERS:
                numbers.append([row_max-2,j-1, lines[i][j]])
                if lines[row_max-2][j+1] in NUMBERS and lines[row_max-2][j] not in NUMBERS:
                    numbers.append([row_max-2,j+1, lines[i][j]])
            elif lines[row_max-2][j] in NUMBERS:
                numbers.append([row_max-2,j, lines[i][j]])
            elif lines[row_max-2][j+1] in NUMBERS:
                numbers.append([row_max-2,j+1, lines[i][j]])
    else:
        # print('on est dans le else') 
        # print(lines[i-1][j-1], lines[i-1][j], lines[i-1][j+1], lines[i][j-1], lines[i][j], lines[i][j+1], lines[i+1][j-1], lines[i+1][j], lines[i+1][j+1])
        # print('lines[i-1][j-1] in numbers', lines[i-1][j-1], numbers, lines[i-1][j-1] in numbers, type(lines[i-1][j-1]))
        if lines[i-1][j-1] in NUMBERS:
            # print('HG')
            numbers.append([i-1,j-1, lines[i][j]])
            if lines[i-1][j+1] in NUMBERS and lines[i-1][j] not in NUMBERS:
                numbers.append([i-1,j+1, lines[i][j]])
                # print('HD')
        elif lines[i-1][j] in NUMBERS:
            # print('H')
            numbers.append([i-1,j, lines[i][j]])
        elif lines[i-1][j+1] in NUMBERS:
            # print('HD')
            numbers.append([i-1,j+1, lines[i][j]])
        if lines[i][j-1] in NUMBERS:
            # print('G')
            numbers.append([i,j-1, lines[i][j]])
        if lines[i][j+1] in NUMBERS:
            # print('D')
            numbers.append([i,j+1, lines[i][j]])
        if lines[i+1][j-1] in NUMBERS:
            # print('BG')
            numbers.append([i+1,j-1, lines[i][j]])
            if lines[i+1][j+1] in NUMBERS and lines[i+1][j] not in NUMBERS:
                numbers.append([i+1,j+1, lines[i][j]])
                # print('BD')
        elif lines[i+1][j] in NUMBERS:
            numbers.append([i+1,j, lines[i][j]])
            # print('B')
        elif lines[i+1][j+1] in NUMBERS:
            numbers.append([i+1,j+1, lines[i][j]])
            # print('BD')
    return numbers

def part1(lines):
    row_max = len(lines)
    column_max = len(lines[0])
    indexes_to_count = []
    for i in range(row_max):
        for j in range(column_max):
            if lines[i][j] not in symbols:
                indexes_to_count.append([i,j])
    sum = 0
    numbers = []
    for point in indexes_to_count:
        i,j = point
        numbers.append(find_near_numbers(lines, i, j, row_max, column_max))
    for set_of_numbers in numbers:
        for number in set_of_numbers:
            i,j, symb = number
            # print('here')
            if i==0:
                if j==0:
                    sum+=find_full_number(lines, 0, 1, column_max, symb)
                    sum+=find_full_number(lines, 0, 1, column_max, symb)
                    sum+=find_full_number(lines, 1, 0, column_max, symb)
                elif j==column_max-1:
                    sum+=find_full_number(lines, 0, column_max-1, column_max, symb)
                    sum+=find_full_number(lines, 0, column_max-1, column_max, symb)
                    sum+=find_full_number(lines, 1, 0, column_max, symb)
                else:
                    sum+=find_full_number(lines, 0, j+1, column_max, symb)
                    sum+=find_full_number(lines, 0, j-1, column_max, symb)
                    sum+=find_full_number(lines, 1, j+1, column_max, symb)
                    sum+=find_full_number(lines, 1, j-1, column_max, symb)
                    sum+=find_full_number(lines, 1, j, column_max, symb)
            elif i==row_max-1:
                if j==0:
                    sum+=find_full_number(lines, row_max-1, 1, column_max, symb)
                    sum+=find_full_number(lines, row_max-1, 1, column_max, symb)
                    sum+=find_full_number(lines, row_max-2, 0, column_max, symb)
                elif j==column_max-1:
                    sum+=find_full_number(lines, row_max-1, column_max-1, column_max, symb)
                    sum+=find_full_number(lines, row_max-1, column_max-1, column_max, symb)
                    sum+=find_full_number(lines, row_max-2, 0, column_max, symb)
                else:
                    sum+=find_full_number(lines, row_max-1, j+1, column_max, symb)
                    sum+=find_full_number(lines, row_max-1, j-1, column_max, symb)
                    sum+=find_full_number(lines, row_max-2, j+1, column_max, symb)
                    sum+=find_full_number(lines, row_max-2, j-1, column_max, symb)
                    sum+=find_full_number(lines, row_max-2, j, column_max, symb)
            else:
                if j==0:
                    sum+=find_full_number(lines, i-1, 0, column_max, symb)
                    sum+=find_full_number(lines, i+1, 0, column_max, symb)
                    sum+=find_full_number(lines, i+1, 1, column_max, symb)
                    sum+=find_full_number(lines, i-1, 1, column_max, symb)
                    sum+=find_full_number(lines, i, 1, column_max, symb)
                elif j==column_max-1:
                    sum+=find_full_number(lines, i-1, column_max-1, column_max, symb)
                    sum+=find_full_number(lines, i+1, column_max-1, column_max, symb)
                    sum+=find_full_number(lines, i+1, column_max-2, column_max, symb)
                    sum+=find_full_number(lines, i-1, column_max-2, column_max, symb)
                    sum+=find_full_number(lines, i, column_max-2, column_max, symb)
                else:
                    sum+=find_full_number(lines, i+1, j+1, column_max, symb)
                    sum+=find_full_number(lines, i+1, j-1, column_max, symb)
                    sum+=find_full_number(lines, i+1, j, column_max, symb)
                    sum+=find_full_number(lines, i, j, column_max, symb)
                    sum+=find_full_number(lines, i, j+1, column_max, symb)
                    sum+=find_full_number(lines, i, j-1, column_max, symb)
                    sum+=find_full_number(lines, i-1, j-1, column_max, symb)
                    sum+=find_full_number(lines, i-1, j, column_max, symb)
                    sum+=find_full_number(lines, i-1, j+1, column_max, symb)
    return sum

a=part1(lines)
print(a)
assert a == 4361