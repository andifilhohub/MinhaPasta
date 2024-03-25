from itertools import permutations

def main (password):
    #password = [int (i) for i in input().split()]  #4 5 6 7 1 2 3  5 6 7 8 0 1 2 3
    def bigger_smaller(mylist): # function to find the largest number and smallest number in the password
        num_bigger = 0
        num_smaller = 1000
        for i in range(len(mylist)):
            if mylist[i] < num_smaller:
                num_smaller = mylist[i]
            elif mylist[i] > num_bigger:
                num_bigger = mylist[i]
        return num_smaller,num_bigger
    def check_pass(mylist): #function to check if the password is valid
        for i in range(len(rotation(mylist))-1):
           
            if rotation(mylist)[i] > rotation(mylist)[i+1]:
                return False
        return True
                
    def rotation(mylist): #function to rotate the password 
        while  mylist[0] != bigger_smaller(mylist)[0]:
            mylist.append(mylist[0])
            del(mylist[0])
            #print(mylist)
        return mylist #return the rotated list (password)
    if check_pass(password): #calling the function check_pass to check
        return True
    else: return False


def rafaelnoia(senha):
    def lis_cres (lista):
        contador = 1                 
        for i in range (len(lista)-1):
            if lista[i] < lista[i+1]:
                contador = contador + 1
        if contador == len(lista):
            return True
        else: return False
    def ra_ti_bum (lista):
        if lis_cres(lista):
            return True
        for i in range (len(lista)):
            lista.append(lista[0])
            del(lista[0])
            if lis_cres(lista):
                return True
        return False
    #senha = [int(i) for i in input().split()]
    if ra_ti_bum(senha):
        return True
    else: return False
# Gera todas as permutações de uma lista de 1 a 7 com tamanho 7
combinations = list(permutations(range(1, 8), 7))

# Imprime as combinações
combo = [int(i) for i in input().split()]
if main(list(combo)) != rafaelnoia(list(combo)):
    print(main(list(combo)))
    print(rafaelnoia(list(combo)))
    print('diferente')
else: 
    print('ok')
    if main(list(combo)) and rafaelnoia(list(combo)):
        print('Klift, Kloft, Still, a porta se abriu')
    else:
        print('Senha incorreta')