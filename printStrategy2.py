def strategy2(n:int)->list:
    lista = [1]
    perdido = 0
    for y in range(n):
            x = lista[y]
            perdido = perdido + x
            a_subir = perdido + 1
            if a_subir%2 == 0:
                siguiente = (a_subir//2)
            if not a_subir%2 == 0 : 
                siguiente = (a_subir//2) + 1
            lista.append(siguiente)
    return lista

def sumarlos(n:int)->int:
    lista = strategy2(n)
    suma = 0
    for e in lista:
        suma = suma + e
    return suma 

def getSequence(n):
    n = n-1
    patron = strategy2(n)
    for f in range(len(patron)):
        print('{}:'.format(f+1), patron[f])
    print("Total necesario:",sumarlos(n))

getSequence(8)

    