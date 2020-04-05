import numpy as np

sudoku = np.zeros((9,9), dtype=int)

sudoku[0][0] = 5
sudoku[0][1] = 3
sudoku[0][4] = 7

sudoku[1][0] = 6
sudoku[1][3] = 1
sudoku[1][4] = 9
sudoku[1][5] = 5

sudoku[2][1] = 9
sudoku[2][2] = 8
sudoku[2][7] = 6

sudoku[3][0] = 8
sudoku[3][4] = 6
sudoku[3][8] = 3

sudoku[4][0] = 4
sudoku[4][3] = 8
sudoku[4][5] = 3
sudoku[4][8] = 1

sudoku[5][0] = 7
sudoku[5][4] = 2
sudoku[5][8] = 6

sudoku[6][1] = 6
sudoku[6][6] = 2
sudoku[6][7] = 8

sudoku[7][3] = 4
sudoku[7][4] = 1
sudoku[7][5] = 9
sudoku[7][8] = 5

sudoku[8][4] = 8
sudoku[8][7] = 7
sudoku[8][8] = 9

print(sudoku)

def horizontal(sero, pan, can):
    for j in range(9):
        if pan[sero][j] != 0:
            can[pan[sero][j] - 1] = 0

def vertical(garo, pan, can):
    for i in range(9):
        if pan[i][garo] != 0:
            can[pan[i][garo] - 1] = 0
            
def box(sero, garo, pan, can):
    x = 3 * int(sero / 3)
    y = 3 * int(garo / 3)
    for i in range(x, x+3):
        for j in range(y, y+3):
            if pan[i][j] != 0:
                can[pan[i][j] - 1] = 0
    
def search(pan):
    for i in range(9):
        for j in range(9):
            if pan[i][j] == 0:    
                can = np.ones(9, dtype=int)
                
                horizontal(i, pan, can)
                vertical(j, pan, can)
                box(i, j, pan, can)
                
                can_num = len(can[can==1])
                if can_num == 1:
                    print('[',i,',',j,'] =', can)
                    pan[i][j] = np.where(1 == can)[0] + 1
             
count = 0
# while True:
#     count += 1
#     print(count)
#     last_pan = np.array(sudoku)
#     search(sudoku)
#     if np.array_equal(sudoku, last_pan):
#         break

# print(sudoku)

a = 1
b = 2
c = 3

if a == 1 and b == 2 and c == 3:
    print("hi")

print("bye")
print("why")