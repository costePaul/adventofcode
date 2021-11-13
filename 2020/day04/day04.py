text = open('./2020/day04/input.txt')
lines = [line[:-1] for line in text]

liste_pass = []
accumulate = ''
for line in lines:
    if line == '':
        liste_pass.append(accumulate)
        accumulate = ''
    else:
        accumulate += line+' '
liste_pass.append(accumulate)
nb_passport = len(liste_pass)
# print(liste_pass)

liste_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']
liste_numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
liste_letters = ['a', 'b', 'c', 'd', 'e', 'f']
liste_eye_color = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']


def get_indicators(passport):
    output = []
    for pattern in liste_fields:
        output.append(int(pattern in passport))
    return output

def attribute_score(passport):
    indicators = get_indicators(passport)
    score = 0
    for i in range(len(indicators)):
        indicator = indicators[i]
        score += indicator*2**i
    return score

def assess_validity_score(passport):
    score = attribute_score(passport)
    return score == 127 or score == 128+127

def count_valids1(data):
    count = 0
    for passport in data:
        count += int(assess_validity_score(passport))
    return count

print(count_valids1(liste_pass))

# Part2

def get_ending_index_pattern(pattern, text):
    len_pattern =  len(pattern) # =4
    for i in range(len(text)):
        j=0
        b = (text[i+j] == pattern[j])
        while b and j<len_pattern:
            b = text[i+j] == pattern[j]
            j+=1
        if b:
            index = i
            return index+len_pattern          

def find_corresponding_value(pattern, passport):
    index = get_ending_index_pattern(pattern+':', passport)
    output = ''
    for i in range(index, len(passport)):
        chara = passport[i] 
        if chara == ' ':
            return output
        else:
            output += chara

def valid_byr(passport):
    byr = int(find_corresponding_value('byr', passport))
    return 1920 <= byr <= 2002

def valid_iyr(p):
    iyr = int(find_corresponding_value('iyr', p))
    return 2010 <= iyr <= 2020

def valid_eyr(p):
    eyr = int(find_corresponding_value('eyr', p))
    return 2020 <= eyr <= 2030

def valid_hgt(p):
    ght = find_corresponding_value('hgt', p)
    taille = len(ght)
    if taille == 5:
        return (150<=int(ght[:3])<=193) and (ght[3:]=='cm')
    elif taille == 4:
        return (59<=int(ght[:2])<=76) and (ght[2:]=='in')
    else:
        return False

def valid_hcl(p):
    hcl = find_corresponding_value('hcl', p)
    if hcl[0]=='#':
        hcl=hcl[1:]
        count = 0
        for chara in hcl:
            if chara in liste_numbers:
                count+=1
            elif chara in liste_letters:
                count+=1
            else:
                print(chara)
        if count == 6:
            return True
    return False

def valid_ecl(p):
    ecl = find_corresponding_value('ecl', p)
    return (ecl in liste_eye_color)

def valid_pid(p):
    pid = find_corresponding_value('pid', p)
    if len(pid)==9:
        for chara in pid:
            if not (chara in liste_numbers):
                return False
        return True
    return False

def assess_validity_fields(passport):
    # we know that at least the 7 fields are present
    p = passport
    return valid_byr(p) and valid_ecl(p) and valid_eyr(p) and valid_hcl and valid_iyr(p) and valid_pid(p) and valid_hgt(p)

def count_valids(data):
    count = 0
    for passport in data:
        if assess_validity_score(passport):
            count += int(assess_validity_fields(passport))
    return count

print(count_valids(liste_pass))

####################### debug ##########################
# data = liste_pass
# # print(data)
# for passport in data:
#     score = attribute_score(passport)
#     p = passport
#     print('\n', 'P=', p)
#     print('score :',score, 'score_is_ok ', assess_validity_score(passport))
#     if assess_validity_score(passport):
#         print('byr:',valid_byr(p), 'iyr:', valid_iyr(p), 'eyr:', valid_eyr(p), 'hgt:', valid_hgt(p), 'hcl:', valid_hcl(p), 'ecl:', valid_ecl(p), 'pid:', valid_pid(p))
#         val_fields = assess_validity_fields(passport)
#         print('is_full_OK :',val_fields)



####################################################
# More consice solution using regex and dictionnaries

import re

keys = {
    "byr": r"byr:\s*(19[2-9]\d|200[0-2])\b",  # (Birth Year) - four digits; at least 1920 and at most 2002.
    "iyr": r"iyr:\s*20(1\d|20)\b",  # (Issue Year) - four digits; at least 2010 and at most 2020.
    "eyr": r"eyr:\s*20(2\d|30)\b",  # (Expiration Year) - four digits; at least 2020 and at most 2030.
    "hgt": r"hgt:\s*(1([5-8]\d|9[0-3])cm|(59|6\d|7[0-6])in)",  # (Height) - a number followed by either cm or in:
    # "If cm, the number must be at least 150 and at most 193.
    # "If in, the number must be at least 59 and at most 76.
    "hcl": r"hcl:\s*#[0-9a-f]{6}\b",  # (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    "ecl": r"ecl:\s*(amb|blu|brn|gry|grn|hzl|oth)\b",  # (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    "pid": r"pid:\s*\d{9}\b",  # (Passport ID) - a nine-digit number, including leading zeroes.
    # "cid", # (Country ID) - ignored, missing or not.
}

with open('./2020/day04/input.txt', "r") as f:
    passports = f.read().split("\n\n")

num_keys_valid = sum([all([k in p for k in keys]) for p in passports])
print(f"Part 1: {num_keys_valid}")

num_data_valid = sum([all([re.search(keys[k], p) for k in keys]) for p in passports])
print(f"Part 2: {num_data_valid}")