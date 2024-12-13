import random
import math


POPULATION_SIZE = 100
X_MIN = 0
X_MAX = 10
PRECISION = 2
TAXA_CRUZAMENTO = 0.7
TAXA_MUTACAO = 0.05

class Individuo:
    def __init__(self, x1 = None, x2 = None, fitness = None):
        self.x1 = x1
        self.x2 = x2
        self.f_objetivo = self.funcao_objetivo()
        self._fitness = fitness
        
        #aptidao = fitness
        
    @property
    def fitness(self):
        if self._fitness == None:
            raise ValueError("Valor de fitness nao foi atribuido")
        return self._fitness
    
    @fitness.setter
    def fitness(self, value):
        self._fitness = round(value, PRECISION)
        
    def funcao_objetivo(self):
        if self.x1 == None or self.x2 == None:
            raise ValueError("Valores de x1 e x2 nao foram atribuidos")
        return round(math.sqrt(self.x1)*math.sin(self.x1) * math.sqrt(self.x2)*math.sin(self.x2), PRECISION)
        
    
    def fitness(self):
        populacao_sorted = sorted(self.populacao, key=lambda x: x.f_objetivo, reverse=True)
        maximo = populacao_sorted[0].f_objetivo
        minimo = populacao_sorted[-1].f_objetivo
        
        return populacao_sorted
        
        
    
    """  def cruzamento(self, individuo2, taxa_cruzamento):
        # Crossover de média 
        x1_filho = (self.x1 + individuo2.x1) / 2
        x2_filho = (self.x2 + individuo2.x2) / 2
        return Individuo(x1_filho, x2_filho) """
        
    def __str__(self):
        return f"x1: {self.x1}, x2: {self.x2}, f_objetivo: {self.f_objetivo} fitness: {self.fitness}"
         
class Populacao:
    def __init__(self, populacao = []):
        self.populacao = populacao
        self.fitness = self.gen_fitness()
            
    
    def selecao(self):
    # Roleta
        pass

    def cruzamento(self):
        # Crossover de média
        pass
    
    def gen_fitness(self):
        dict_fitness = {}
        populacao_sorted = sorted(self.populacao, key=lambda x: x.f_objetivo, reverse=True)
        maximo = populacao_sorted[0].f_objetivo
        minimo = populacao_sorted[-1].f_objetivo
        
        def individual_fitness(rank_individuo):
            return minimo + (maximo - minimo) *  ((POPULATION_SIZE - rank_individuo) / (POPULATION_SIZE - 1))
            
        for i, individuo in enumerate(populacao_sorted):
            individuo.fitness = individual_fitness(i)
        
        return 
    
    def __str__(self):
        string_pop = ""
        for individuo in self.populacao:
            string_pop += str(individuo) + "\n"
        return f"{string_pop}"
            
class Geracao:
    def __init__(self, populacao, populacao_anterior = None):
        self.populacao = populacao
        self.populacao_anterior = populacao_anterior
        
    def __str__(self):
        return f"Populacao: {self.populacao}, Populacao Anterior: {self.populacao_anterior}"    
            
def populacao_inicial(tamanho_populacao):
    populacao = []
    for i in range(tamanho_populacao):
        x1 = round(random.uniform(X_MIN, X_MAX), PRECISION)
        x2 = round(random.uniform(X_MIN, X_MAX), PRECISION)
        populacao.append(Individuo(x1, x2))
    return populacao


populacao_teste = populacao_inicial(10)
print(populacao_teste[2])
pop = Populacao(populacao_teste)
print(pop)