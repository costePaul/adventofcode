text = open('./2020/day01/input.txt')
numbers = [int(line) for line in text]

def find_pair(set,target):
    for x in set:
        for y in set:
            if x+y==2020:
                return x*y
    
def find_triplets(set, target):
    for x in set:
        for y in set:
            for z in set:
                if x+y+z==2020:
                    return x*y*z

print(find_pair(numbers,2020))
print(find_triplets(numbers,2020))
