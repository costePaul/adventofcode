with open('./2020/day15/input.txt', "r") as f:
    said = f.read().split(",")

def mirror(liste):
    if len(liste) == 1 or liste==[]:
        return liste
    return [liste[-1]]+mirror(liste[:-1])

counter = len(said)
said = [int(n) for n in said]
# said = [0,3,6]
d = {}
for i,val in enumerate(said):
    pass

rev = mirror(said)
print(said, rev)

def gen_new_nb(said, rev):
    # print(said, rev)
    i = said[-1]
    if i not in said[:-1]:
        return 0
    else:
        cnt = 1
        for j in rev[1:]:
            if i==j:
                return cnt
            else:
                cnt+=1

N=15
N=2019
N=30000000
while counter<N+1:
    if counter % 1000 == 0:
        print(counter)
    new = gen_new_nb(said, rev)
    said.append(new)
    rev = [new]+rev
    # print(said)
    counter+=1

# print(said)
print(said[N])
