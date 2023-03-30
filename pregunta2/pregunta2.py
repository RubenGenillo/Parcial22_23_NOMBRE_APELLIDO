import MergeSort
#cambia lo del mergesort
def main():
    lista = [18, 50, 210, 80, 145, 333, 70, 30]
    for elemento in lista:
        #con el prgrama se refiere a la funcion???, voy a hacer así
        if elemento > 300:
            break
        if elemento % 10 == 0 and elemento < 200:
            print(elemento)
    lista = MergeSort.mergeSort(lista)
    try:
        return lista.index(145)
    except ValueError:
        return -1


if __name__ == "__main__":

    print(main())
    
