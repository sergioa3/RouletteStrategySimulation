import random

#trying to simulate a different roulette strategy based on the idea that the first one blows up too fast by doubling everytime.
#the idea behing this one was to tradeoff absurd amounts of money needed to have a "confidently safe" amount of allowed losses in a row, by having slower gains. 

class persona:
    blanqueados = 0
    satisfechos = 0
    def __init__(self, d: int, meta_ganancia:int):
        self.dinero = d
        self.sig_apuesta = 1
        self.blanqueado = False
        self.satisfecho = False
        self.meta = meta_ganancia + d
        self.perdida_parcial = int(0)

    
    def get_perdida_parcial(self):
        return self.perdida_parcial
    def cambiar_perdida_parcial(self, p: int):
        self.perdida_parcial = p
    def get_dinero(self):
        return self.dinero
    def cambiar_dinero(self, d:int):
        self.dinero = d
    def get_sig_apuesta(self):
        return self.sig_apuesta
    def cambiar_sig_apuesta(self, a:int):
        self.sig_apuesta = a
    def get_blanqueado(self):
        return self.blanqueado
    def get_satisfecho(self):
        return self.satisfecho
    def get_meta(self):
        return self.meta
    def cambiar_satisfaccion(self):
        self.satisfecho = not self.get_satisfecho()
    def check_satisfacer(self):
        if self.get_dinero() >= self.get_meta():
            self.cambiar_satisfaccion()
    def cambiar_blanq(self):
        self.blanqueado = not self.get_blanqueado()
    def check_blanquear(self):
        if self.get_sig_apuesta() >= self.get_dinero():
            self.cambiar_blanq()
    @classmethod
    def get_blanqs(cls)->int:
        return cls.blanqueados
    @classmethod
    def suma_blanqueado(cls):
        cls.blanqueados = cls.get_blanqs() + 1
    @classmethod
    def get_satis(cls)->int:
        return cls.satisfechos
    @classmethod
    def suma_satisfecho(cls):
        cls.satisfechos = cls.get_satis() + 1
class clase_ruleta:
    posibilidades = []

    def __init__(self):
        self.cayo = True

    @classmethod
    def iniciar(cls):
        for i in range(38):
           cls.posibilidades.append(i)
    @classmethod
    def get_posibles(cls)->list:
        return cls.posibilidades
    
    def tirar(self)->int:
        return random.choice(clase_ruleta.get_posibles())
    
    def cambiar_cayo(self, r:bool):
        self.cayo = r
    def get_cayo(self)->bool:
        return self.cayo

    def jugar(self):
        tiro = self.tirar()
        #prendida  = en True
        result= True
        if tiro > 11:
            result = False
        self.cambiar_cayo(result)


def jueguelo(joe: persona, ruleta: clase_ruleta):
    a_ganar=0
    if ruleta.get_cayo():
        joe.cambiar_dinero(joe.get_dinero()+3*joe.get_sig_apuesta())
        joe.cambiar_sig_apuesta(1)
        joe.cambiar_perdida_parcial(0)
    if not ruleta.get_cayo():
        joe.cambiar_perdida_parcial(joe.get_perdida_parcial()+joe.get_sig_apuesta())
        a_ganar=joe.get_perdida_parcial()+1
        if a_ganar%2 == 0:
            joe.cambiar_sig_apuesta((a_ganar//2))
        if not a_ganar%2 == 0 : 
            joe.cambiar_sig_apuesta((a_ganar//2)+1)





def apostar(joe: persona, ruleta: clase_ruleta):
    joe.cambiar_dinero(joe.get_dinero()-joe.get_sig_apuesta())
    ruleta.jugar()
    jueguelo(joe, ruleta)
    
    
def noche(joe: persona, ruleta: clase_ruleta):
    cuantas_va = 0
    while not (joe.get_blanqueado() or joe.get_satisfecho()):
        apostar(joe,ruleta)
        joe.check_blanquear()
        joe.check_satisfacer()
        #print(ruleta.get_cayo())  
        #print(joe.get_dinero())
        cuantas_va +=1
        #print('p',joe.get_perdida_parcial())
        #print('sig_apuesta:',joe.get_sig_apuesta())
        #print('deberia subir a :',joe.get_sig_apuesta()*2+joe.get_dinero())
    if joe.get_blanqueado():
        persona.suma_blanqueado()
    if joe.get_satisfecho():
        persona.suma_satisfecho()
    #print(cuantas_va)  
        

def simulacion(dinero_inicial: int, meta_ganar:int, tamaño:int, ruleta: clase_ruleta)->list:
    resultados=[]
    for i in range(tamaño):
        player = persona(dinero_inicial, meta_ganar)
        noche(player, ruleta)
        resultados.append(player)
    return resultados

def analisis(dinero_inicial: int, meta_ganar:int, tamaño:int, ruleta: clase_ruleta)->dict:
    clase_ruleta.iniciar()
    resultados = simulacion(dinero_inicial, meta_ganar, tamaño, ruleta)
    neto = -tamaño*dinero_inicial
    '''blancos = 0
    ferchos = 0'''
    for pers in resultados:
        neto = neto + pers.get_dinero()
        '''if pers.get_blanqueado():
            blancos = blancos + pers.get_dinero()
        elif pers.get_satisfecho():
            ferchos = ferchos + pers.get_dinero()'''


    dicci = {'blanqueados:': persona.get_blanqs(), 'satisfechos:':persona.get_satis(), 'balance_promedio':(neto/tamaño),'balance_promedio_porc':((neto/tamaño)/dinero_inicial)}
    return dicci

def consola():
    dinero = int(input('Dinero inicial='))
    meta = int(input('Meta a sacar='))
    size = input('Tamaño de simulación=')
    if size == None:
        size = 10000
    elif not (size == None):
        size = int(size)
    
print(analisis(1024,1000,100000,clase_ruleta()))




#cayo = bool
#tiro = numero