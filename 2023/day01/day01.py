# with open('./2023/day01/test.txt', "r") as f:
with open('./2023/day01/input.txt', "r") as f:
    words = f.read().split("\n")

nums = '123456789'

def part1():
    sum = 0
    for word in words:
        rev_word = word[::-1]
        for char in word:
            if char in nums:
                sum+= int(char)*10
                break
        for char in rev_word:
            if char in nums:
                sum+= int(char)
                break
    return sum

print(part1())

valid_nums = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
valid_nums_rev = ['eno', 'owt', 'eerht', 'ruof', 'evif', 'xis', 'neves', 'thgie', 'enin']

def find_num(word, liste):
    for i in range(len(word)):
        if word[i] in nums:
                return int(word[i])
        for idx_num,num in enumerate(liste): 
            if word[i:i+len(num)] == num:
                return idx_num+1

def part2():
    sum = 0
    for word in words:
        rev_word = word[::-1]
        sum += find_num(word, liste = valid_nums) * 10 + find_num(rev_word, liste = valid_nums_rev)
    return sum

print(part2())