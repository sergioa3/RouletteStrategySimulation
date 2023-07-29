import random
# importing the sys module 
import sys 
  
# the setrecursionlimit function is 
# used to modify the default recursion 
# limit set by python. Using this,  
# we can increase the recursion limit 
# to satisfy our needs 
#sys.setrecursionlimit(10**3)


#this was the first try to create the simulation 
# before knowing OOP



def ruleta()->int:
    lista=[]
    for i in range(38):
        lista.append(i)
    return random.choice(lista)

def jugar_ruleta()->bool:
    cayo = ruleta()
    result=True
    if cayo > 11:
        result = False
    return result


def prueba_sonido(n:int)->list:
    resultados = []
    for i in range(n):
        resultados.append(jugar_ruleta())
    return resultados
#print(prueba_sonido(15))

def encontrar_cuantas_puede_jugar(dinero: int)->int:
    respuesta=1
    if dinero < 1:
        return 0
    if dinero < 2:
        return 1
    i = 1
    while 2**i <= dinero:
        i+=1
    respuesta = i-1
    return respuesta
#print(encontrar_cuantas_puede_jugar(1024))

def hay_repetido(lista: list, elemento, limite: int)->bool:
        repe = False
        seguidas = 0

        r=0
        while r in range(len(lista)) and not repe:
            if lista[r] == elemento :
                seguidas += 1
            if not lista[r] == elemento:
                seguidas = 0
            if seguidas >= limite:
                repe = True
            r+=1
        return repe

def analisis(d: int, c:int)->dict:


    n = encontrar_cuantas_puede_jugar(d)
    
    resultados = prueba_sonido(c)
    blanqueado = hay_repetido(resultados, False, n)
    dicci = {'Puedes jugar maximo seguidas:':n, 'total resultados':resultados, 'Te Blanqueaste':blanqueado}
    
    return dicci

def simular (d: int, c:int, s:int)->dict:
    lista_grande =[]
    blanqueadas = 0
    for i in range(s):
        noche = analisis(d, c)
        if noche['Te Blanqueaste']==True:
            blanqueadas += 1
        lista_grande.append(noche)
    dicci = {'total:':lista_grande, 'blanqueadas':blanqueadas}
    return dicci





def consola():
    dinero = input('Cuanto dinero meterias:')
    dinero = int(dinero)
    print('Puedes perder {} seguidas!!!'.format(encontrar_cuantas_puede_jugar(dinero)))
    tamaño_simulacion = input('Cuantas vas a jugar')
    tamaño_simulacion = int(tamaño_simulacion)
    simulaciones = input('Cuantas veces lo deseas simular')
    simulaciones = int(simulaciones)
    
    simulacion = simular(dinero, tamaño_simulacion, simulaciones)
    b = simulacion['blanqueadas']
    porc = float(b)/float(simulaciones)*100
    print('Se blanquea en {} simulaciones, el {} porciento de las veces'.format(b, porc))

def iniciar():
    consola()
iniciar()


