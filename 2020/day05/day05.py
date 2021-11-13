import math
import numpy as np

text = open('./2020/day05/input.txt')
lines = [line[:-1] for line in text]

def get_good_half(a,b, letter):
    if letter=='R':
        letter='B'
    elif letter=='L':
        letter='F'
    c = (b+a)/2
    # print(a,b,c, letter)
    if letter == 'B':
        return math.ceil(c), b
    if letter == 'F':
        return a, math.floor(c)

def get_coordinate(ticket):
    a = 0
    b = 127
    for i in range(7):
        a, b = get_good_half(a, b, ticket[i])
    x = 0
    y = 7 
    for i in range(7,10):
        x, y = get_good_half(x, y, ticket[i])
    return a,x

def get_id(row, column):
    return 8*row+column

def find_highest_id(data):
    return np.max(np.array([get_id(get_coordinate(ticket)[0], get_coordinate(ticket)[1]) for ticket in data]))

print(find_highest_id(lines))

def collect(data):
    mat = np.zeros((128,8))
    for ticket in data:
        row, column = get_coordinate(ticket)
        mat[row][column]=1
    output = []
    for i in range(128):
        for j in range(8):
            if mat[i][j]==0:
                output.append((i,j))
    return output

def sort(data):
    ids = [get_id(val[0],val[1]) for val in data]
    return [id for id in ids if id-1 not in ids and id+1 not in ids]

print(sort(collect(lines))[0])