text = open('./2020/day02/input.txt')
passwords = [line for line in text]

def read_pwd(pwd):
    minNb = ''
    maxNb = ''
    still_first_nb = True
    still_second_nb = True
    for chara in pwd:
        if chara == '-':
            still_first_nb = False
        elif chara == ' ':
            still_second_nb = False
        elif still_first_nb:
            minNb += chara
        elif still_second_nb:
            maxNb += chara
        else:
            return int(minNb), int(maxNb), chara, pwd[len(minNb+maxNb)+5:]
    
def count_occurence(letter, pwd):
    count = 0
    for chara in pwd:
        if chara==letter:
            count += 1
    return count

def is_valid_1(pwd):
    min_nb, max_nb, letter, pwd = read_pwd(pwd)
    letter_count = count_occurence(letter, pwd)
    if min_nb <= letter_count <= max_nb:
        return 1
    else:
        return 0

def is_valid_2(pwd):
    x, y, letter, pwd = read_pwd(pwd)
    pos1 = pwd[x-1] == letter
    pos2 = pwd[y-1] == letter
    if pos1 and not(pos2):
        return 1
    elif pos2 and not(pos1):
        return 1
    else:
        return 0

def count_valid_passwords_1(set):
    count = 0
    for password in set:
        count += is_valid_1(password)
    return count

def count_valid_passwords_2(set):
    count = 0
    for password in set:
        count += is_valid_2(password)
    return count

print(count_valid_passwords_1(passwords))
print(count_valid_passwords_2(passwords))