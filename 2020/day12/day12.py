with open('./2020/day12/input.txt', "r") as f:
    orders = f.read().split("\n")
new_orders = []
for order in orders:
    new_orders.append((order[0],int(order[1:])))

pos = [0,0]
facing_nb = 1
facing_dir = 'E'
corresponding_table = [[['N','W','S','E'],['E','N','W','S'],['S','E','N','W'],['W','S','E','N']],\
    [['N','E','S','W'],['E','S','W','N'],['S','W','N','E'], ['W','N','E','S']]]
corresponding_table_nb = [[[0,3,2,1],[1,0,3,2],[2,1,0,3],[3,2,1,0]],[[0,1,2,3],[1,2,3,0],[2,3,0,1], [3,0,1,2]]]

for direction,size in new_orders:
    if direction == 'F':
        direction = facing_dir
    if direction == 'N':
        pos[0] += size
    elif direction == 'S':
        pos[0] -= size
    elif direction == 'E':
        pos[1]+= size
    elif direction == 'W':
        pos[1] -= size
    elif direction == 'L':
        facing_dir = corresponding_table[0][facing_nb][size//90]
        facing_nb = corresponding_table_nb[0][facing_nb][size//90]
    elif direction == 'R':
        facing_dir = corresponding_table[1][facing_nb][size//90]
        facing_nb = corresponding_table_nb[1][facing_nb][size//90]

print(pos, abs(pos[0])+abs(pos[1]))

# part 2
pos = [0,0]
waypoint = [1,10]

def find_facing_quarter():
    if waypoint[0]>=0:
        if waypoint[1]>=0:
            return 0
        else:
            return 1
    else:
        if waypoint[1]>=0:
            return 3
        else:
            return 2

def change_quarter(q1, q2, waypoint):
    diff = (q2-q1)%4
    if diff == 1:
        return [waypoint[1],-waypoint[0]]
    elif diff == 2:
        return [-waypoint[0],-waypoint[1]]
    elif diff == 3:
        return [-waypoint[1],waypoint[0]]

for direction,size in new_orders:
    if direction == 'F':
        pos[0] += waypoint[0]*size
        pos[1] += waypoint[1]*size
    elif direction == 'N':
        waypoint[0] += size
    elif direction == 'S':
        waypoint[0] -= size
    elif direction == 'E':
        waypoint[1]+= size
    elif direction == 'W':
        waypoint[1] -= size
    else:
        facing_quarter = find_facing_quarter()
        move = size//90
        if move == 2:
            new_quarter = (facing_quarter+2)%4
        elif (direction == 'R' and move==1) or (direction == 'L' and move==3):
            new_quarter = (facing_quarter-1)%4
        elif (direction == 'L' and move==1) or (direction == 'R' and move==3):
            new_quarter = (facing_quarter+1)%4
        waypoint = change_quarter(facing_quarter, new_quarter, waypoint)
        
print(pos, abs(pos[0])+abs(pos[1]))