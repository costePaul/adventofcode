import numpy as np

with open('./2020/day13/input.txt', "r") as f:
    info = f.read().split("\n")
t = int(info[0])
info = info[1].split(",")

buses = [int(value) for value in info if value != 'x']

next_arrival = [num-t%num for num in buses]

array_next_arrival = np.array(next_arrival)
waiting_time = np.min(array_next_arrival)

bus_number = buses[np.argmin(np.array(next_arrival))]
print(waiting_time*bus_number)

#part2
# count = 0
# requirement = []
# for number in info:
#     if number != 'x':
#         requirement.append((count, int(number)))
#     count+=1

# max_bus_number = 0
# offset_of_the_max = 0
# for offset, bus_number in requirement:
#         if bus_number > max_bus_number:
#             max_bus_number = bus_number
#             offset_of_the_max = offset

# nb_requirements = len(requirement)
# t=100000000000000

# while (t-offset_of_the_max)%max_bus_number!=0:
#     t+=1
# print('c bon')
# b = True
# t0 = t
# while b:
#     nb_requirements_fullfilled = 0
#     for offset, bus_number in requirement:
#         if (t+offset)%bus_number == 0:
#             nb_requirements_fullfilled += 1
#     if nb_requirements_fullfilled == nb_requirements:
#         b = False
#     if (t-t0)%1000000 == 0:
#         print(t)
#     t+=offset_of_the_max
# print(t-1)

# 780601154795940

with open('./2020/day13/input.txt', "r") as f:
    LINES = f.readlines()
busses = ["x" if x == "x" else int(x) for x in LINES[1].split(",")]

def part2():
    mods = {bus: -i % bus for i, bus in enumerate(busses) if bus != "x"}
    # print(mods)
    vals = list(reversed(sorted(mods)))
    val = mods[vals[0]]
    r = vals[0]
    for b in vals[1:]:
        while val % b != mods[b]:
            val += r
        r *= b
    return val
# print(part2())
