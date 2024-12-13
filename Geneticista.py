import random
import math

X_MIN = 0
X_MAX = 10
PRECISION = 2

class Individuo:
    def __init__(self, x1 = None, x2 = None):
        self.x1 = x1
        self.x2 = x2
        self.f_objetivo = self.funcao_objetivo()
        
        #aptidao = fitness
        
    def funcao_objetivo(self):
        if self.x1 == None or self.x2 == None:
            raise ValueError("Valores de x1 e x2 nao foram atribuidos")
        return round(math.sqrt(self.x1)*math.sin(self.x1) * math.sqrt(self.x2)*math.sin(self.x2), PRECISION)
        

    """  def cruzamento(self, individuo2, taxa_cruzamento):
        # Crossover de média 
        x1_filho = (self.x1 + individuo2.x1) / 2
        x2_filho = (self.x2 + individuo2.x2) / 2
        return Individuo(x1_filho, x2_filho) """
        
    def __str__(self):
        return f"x1: {self.x1}, x2: {self.x2}, f_objetivo: {self.f_objetivo}"
         
class Populacao:
    def __init__(self, taxa_mutacao, taxa_cruzamento):
        self.taxa_mutacao = taxa_mutacao
        self.taxa_cruzamento = taxa_cruzamento
        self.populacao = []
            
        def fitness(self):
            # Ranking Linear
            pass
        
        def selecao(self):
        # Roleta
            pass
    
        def cruzamento(self):
            # Crossover de média
            pass
            
def populacao_inicial(tamanho_populacao):
    populacao = []
    for i in range(tamanho_populacao):
        x1 = round(random.uniform(X_MIN, X_MAX), PRECISION)
        x2 = round(random.uniform(X_MIN, X_MAX), PRECISION)
        populacao.append(Individuo(x1, x2))
    return populacao

populacao_teste = populacao_inicial(10)
print(populacao_teste[5])