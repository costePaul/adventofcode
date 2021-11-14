import numpy as np
with open('./2020/day10/input.txt', "r") as f:
    voltages = f.read().split("\n")
voltages = [int(number) for number in voltages]
n = len(voltages)

count = 0
count_1 = 0
count_3 = 1 # because you count from the last plug to your computer, which is a +3
used = []
current_voltage = 0

while count < n:
    possibles = []
    values = []
    for num in voltages:
        if num not in used:
            diff = num-current_voltage
            if 1<=diff<=3:
                possibles.append(num)
                values.append(diff)
    sort_indexes = np.argsort(np.array(values))
    l = len(possibles)
    sorted_possibles = [current_voltage]
    for i in range(l):
        sorted_possibles.append(possibles[sort_indexes[i]])
    for i in range(l):
        diff = sorted_possibles[i+1]-sorted_possibles[i]
        if diff==1:
            count_1 += 1
        elif diff==3:
            count_3 += 1
    count += l
    current_voltage = sorted_possibles[-1]

print(count_1*count_3)

# Part 2
voltages.append(0)
sorted_voltages = np.sort(np.array(voltages))
max_volt = sorted_voltages[-1]
info = np.zeros(max_volt+1)
info[0]=1
index = 1
while index<max_volt+1:
    if index in voltages:
        s = max(0, index-3)
        info[index]=sum([info[i] for i in range(s,index)])
    index+=1

print(info[-1])