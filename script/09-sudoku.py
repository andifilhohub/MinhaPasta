#--------------------------------------------------#
#--                                              --#
#--               Anderson Filho                 --#
#--                12011ECP032                   --#
#--                                              --#   
#--------------------------------------------------#


def main ():
    n = int(input())
    
    all_table = []
    for j in range(n):
        tab_sudoku = []
        for i in range(9):
            tab_sudoku.append([int (i) for i in input().split()])
        all_table.append(tab_sudoku)
    for i in range(n):
        print(check(all_table[i]))
def check(array,n = 9):
    for i in range(n):
        for j in range(n):
            num = array[i][j]
            for h in range(n):
                if h == j:
                    continue
                elif array[i][h] == array[i][j]:
                    return False
    for i in range(n):
        for j in range(n):
            num = array[j][i]
            for h in range(n):
                if h == j:
                    continue
                elif array[h][i] == array[j][i]:
                    return False
    return True

def check_3x3(array, n = 9):
    
    new_array = []
    
    indx_row = 0
    for a in range(3):
        new_row = []
        for arr in range(3):
            indx_colum = 0
            for row  in range(3):
                new_colum = []
                for colum in range(3):
                    new_colum.apend(array[row+indx_row][colum+indx_colum])
                new_row.append(new_colum)
            indx_colum+=3
        indx_row += 3
    return new_array


main()
