import numpy as np
import string

with open('./2020/day06/input.txt', "r") as f:
    groups = f.read().split("\n\n")

answers = [group.split("\n") for group in groups]

def count_diff_answers_part1(group):
    indicator = np.zeros(26)
    count = 0
    for answer in group:
        for chara in answer:
            letter_index = string.ascii_lowercase.index(chara)
            if not indicator[letter_index]:
                count+=1
                indicator[letter_index] = 1
    return count

def sum(k,list):
    if list == []:
        return k
    else:
        return sum(k+list[0], list[1:])

print(sum(0,[count_diff_answers_part1(group) for group in answers]))

#part2

def count_diff_answers_part2(group):
    indicator = np.zeros(26)
    count = 0
    for answer in group:
        for chara in answer:
            letter_index = string.ascii_lowercase.index(chara)
            indicator[letter_index] += 1
    for letter in range(26):
        if indicator[letter] == len(group):
            count+=1
    return count

print(sum(0,[count_diff_answers_part2(group) for group in answers]))