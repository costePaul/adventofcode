text = open('./2020/day03/input.txt')
rows = [line[:-1] for line in text]
nb_row = len(rows)
pattern_size = len(rows[0])
open_square = '.'
tree = '#'
symbols = [open_square, tree]

# check if the top left corner is an open square
# print(rows[0][0] == symbols[0])

b = True
index = None
for i in range(nb_row):
    if pattern_size != len(rows[i]):
        b = False
        index = i
# print(b, index)

def index_of(value, set):
    index = 0
    for val in set:
        if val == value:
            return True, index
        index += 1
    return False, index

def look_for_tree(chara):
    b, index = index_of(chara, symbols)
    if b:
        return index
    else:
        print('invalid character in input :'+chara)

def build_chara_liste(r, d):
    liste = []
    la = nb_row/d
    int_la = int(la)
    if la == int_la:
        for i in range(int_la):
                liste.append(rows[i*d][(i*r)%pattern_size])
    else:
        for i in range(int_la+1):
            liste.append(rows[i*d][(i*r)%pattern_size])
    return liste

def count_trees(right, down):
    liste = build_chara_liste(right, down)
    tree_count = 0
    for chara in liste:
        if look_for_tree(chara):
            tree_count += 1
    return tree_count

def create_solution_liste(couples):
    liste = []
    for (a,b) in couples:
        liste.append(count_trees(a,b))
    return liste

# recursive for fun
def multiply_elements(value, liste):
    if liste == []:
        return value
    else: 
        return multiply_elements(value*liste[0], liste[1:])

values = [(1,1),(3,1),(5,1),(7,1),(1,2)]
print(multiply_elements(1,create_solution_liste(values)))