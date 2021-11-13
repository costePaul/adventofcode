with open('./2020/day09/input.txt', "r") as f:
    numbers = f.read().split("\n")

numbers = [int(number) for number in numbers]

def check(index):
    liste_previous = numbers[index-start_size:index]
    for number in liste_previous:
        if numbers[index]-number in liste_previous:
            # print(number-numbers[index], number, index, numbers[index])
            return True
    return False

start_size = 25
index = start_size
while check(index):
    index += 1
print(numbers[index])

goal = numbers[index]

for i in range(len(numbers)-1):
    size = numbers[i]+numbers[i+1]
    j = 2
    max_nb = max(numbers[i],numbers[i+1])
    min_nb = min(numbers[i],numbers[i+1])
    while size < goal:
        new_number = numbers[i+j]
        size += new_number
        j+=1
        if new_number > max_nb:
            max_nb = new_number
        elif new_number < min_nb:
            min_nb = new_number
    if size == goal:
        print(min_nb+max_nb)
