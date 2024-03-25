
def ratibum(lista, a):
    for i in range(len(lista)-1):
        if(lista[i] > lista[i+1]):
            lista.append(lista[i])
            del(lista[i])
            a+=1
            if a == len(lista)-1:
                return 'Senha Correta'
            ratibum(lista, a)
        elif(lista[i] == lista[i+1]):
            return 'Senha incorreta'
    return 'Senha correta'
lista = [1, 2, 3, 4, 3, 5]
print(ratibum(lista, 1))