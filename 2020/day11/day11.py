with open('./2020/day11/input.txt', "r") as f:
    original_seats = f.read().split("\n")

seats = original_seats
nb_rows = len(seats)
nb_columns = len(seats[0])

# part1
tolerance = 4
N = 1

def count_surrondings(nb,i,j):
    count = 0
    if nb == 1:
        for i_index in range(max(0,i-1),min(nb_rows,i+2)):
            for j_index in range(max(0,j-1),min(nb_columns,j+2)):
                if i_index != i or j_index != j:
                    if seats[i_index][j_index] == '#':
                        count += 1 
        return count
    else:
        for i_index in range(max(0,i-1),min(nb_rows,i+2)):
            for j_index in range(max(0,j-1),min(nb_columns,j+2)):
                row = i_index - i
                column = j_index - j
                if row or column:
                    distance = 1
                    row_index = i+distance*row
                    column_index = j+distance*column
                    seat = seats[row_index][column_index]    
                    while seat == '.' and row_index>=0 and column_index>=0 and row_index<nb_rows and column_index<nb_columns:
                        seat = seats[row_index][column_index]
                        distance+=1
                        row_index = i+distance*row
                        column_index = j+distance*column
                    if seat == '#':
                        count += 1
    return count

def update_data(nb):
    new_seats = []
    count_changes = 0
    count_occupied = 0
    count_non_occupied = 0
    for i in range(nb_rows):
        row = ''
        for j in range(nb_columns):
            seat = seats[i][j]
            if seat=='.':
                row += '.'
            else:
                cnt = count_surrondings(nb,i,j)
                if seat == 'L':
                    if cnt==0:
                        row+='#'
                        count_changes+=1
                        count_occupied+=1
                    else:
                        row+='L'
                        count_non_occupied+=1
                elif seat == '#':
                    if cnt>=tolerance:
                        row+='L'
                        count_changes+=1
                        count_non_occupied+=1
                    else:
                        row+='#'
                        count_occupied+=1
        new_seats.append(row)
    return new_seats, count_changes, count_occupied, count_non_occupied

seats, nb_changes, nb_occupied, nb_nn_occupied = update_data(N)
while nb_changes>0:
    seats, nb_changes, nb_occupied, nb_nn_occupied = update_data(N)
print(nb_occupied)

# part 2
tolerance = 5
N = 2
seats = original_seats

seats, nb_changes, nb_occupied, nb_nn_occupied = update_data(N)
while nb_changes>0:
    seats, nb_changes, nb_occupied, nb_nn_occupied = update_data(N)
print(nb_occupied)