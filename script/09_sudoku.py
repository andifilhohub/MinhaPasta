def main():
    number_tab = int(input())
    tab = []
    i = 0 
    while i<number_tab*9:
        row_tab = [int(i) for i in input().split()]
        tab.append(row_tab)
        i+=1
    aux = 0
    new_tab = []
    for i in range(number_tab):
        LK = []
        for j in range(len(tab[0])):
            LK.append(tab[j+(aux)])
        new_tab.append(LK)
        aux+=len(tab[0])
        print(sudoku(new_tab[0]))
def sum_list(x):
    sum = 0
    for i in range(len(x)):
        sum+=x[i]
    return sum
def sudoku_horizontal(x):
    sum = 0
    aux = 0
    
    for j in range(len(x[0])):
        _list = []
        for i in range(len(x[0])):
            print(x[i])
            if x[i][j] not in _list:
                _list.append(x[i][j])
            else: return False
        if sum_list(x[i]) != 45:
            return False
        
    return True
def sudoku_vertical(x):
    return 0


                
        
    
    
    
main()