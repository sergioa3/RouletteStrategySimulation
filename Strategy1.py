import random

#I first learned OOP by doing this simulation, it just felt way more natural compared to program and design to no OOP
#obviously this does not have the best programming practices since it was my first try at OOP and during my first years of Python and 
# programming in general.



class personas:
    blanqueados = 0
    satisferchos = 0
    def __init__(self, d: int, meta_ganancia:int):
        self.dinero = d
        self.sig_apuesta = 1
        self.blanqueado = False
        self.satisfecho = False
        self.meta = meta_ganancia + d

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
    def suma_blanqueadito(cls):
        cls.blanqueados = cls.get_blanqs() + 1
    @classmethod
    def get_satis(cls)->int:
        return cls.satisfechos
    @classmethod
    def suma_satisferchito(cls):
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
        result=True
        if tiro > 11:
            result = False
        self.cambiar_cayo(result)


def jueguelo(joe: personas, ruleta: clase_ruleta):
    if ruleta.get_cayo():
        joe.cambiar_dinero(joe.get_dinero()+3*joe.get_sig_apuesta())
        joe.cambiar_sig_apuesta(1)
    if not ruleta.get_cayo():
        joe.cambiar_sig_apuesta(2*joe.get_sig_apuesta())

def apostar(joe: personas, ruleta: clase_ruleta):
    joe.cambiar_dinero(joe.get_dinero()-joe.get_sig_apuesta())
    ruleta.jugar()
    jueguelo(joe, ruleta)
    
def noche(joe: personas, ruleta: clase_ruleta):
    
    while not (joe.get_blanqueado() or joe.get_satisfecho()):
        apostar(joe,ruleta)
        joe.check_blanquear()
        joe.check_satisfacer()    
    if joe.get_blanqueado() :
        personas.suma_blanqueadito()
    if joe.get_satisfecho():
        personas.suma_satisferchito()
        
        

def simulacion(dinero_inicial: int, meta_ganar:int, tamaño:int, ruleta: clase_ruleta)->list:
    resultados=[]
    for i in range(tamaño):
        player = personas(dinero_inicial, meta_ganar)
        noche(player, ruleta)
        resultados.append(player)
    return resultados

def analisis(dinero_inicial: int, meta_ganar:int, tamaño:int, ruleta: clase_ruleta)->dict:
    clase_ruleta.iniciar()
    resultados = simulacion(dinero_inicial, meta_ganar, tamaño, ruleta)
    neto = -tamaño*dinero_inicial
    blancos = 0
    satisfechos = 0
    for pers in resultados:
        neto = neto + pers.get_dinero()
        if pers.get_blanqueado():
            blancos = blancos + pers.get_dinero()
        elif pers.get_satisfecho():
            satisfechos = satisfechos + pers.get_dinero()


    dicci = {'blanqueados:': personas.get_blanqs(), 'satisfechos:':personas.get_satis(), 'balance_promedio':(neto/tamaño),\
         'balance_promedio de blanqs':blancos/personas.get_blanqs(), 'balance_promedio de satisfechos':satisfechos/personas.get_satis()}
    return dicci

print(analisis(1024,1000,100000,clase_ruleta()))
    
#cayo = bool
#tiro = numero