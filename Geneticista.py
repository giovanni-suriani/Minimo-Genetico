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
        """ #Debugging purpose
            if self._fitness == None:
            print(f"valor de fitness nao foi atribuido")
            raise ValueError("Valor de fitness nao foi atribuido") """
        return self._fitness
    
    @fitness.setter
    def fitness(self, value):
        self._fitness = round(value, PRECISION)
        
    def funcao_objetivo(self):
        if self.x1 == None or self.x2 == None:
            raise ValueError("Valores de x1 e x2 nao foram atribuidos")
        return round(math.sqrt(self.x1)*math.sin(self.x1) * math.sqrt(self.x2)*math.sin(self.x2), PRECISION)
        
    def __str__(self):
        return f"x1: {self.x1}, x2: {self.x2}, f_objetivo: {self.f_objetivo} fitness: {self.fitness}"
    
    def __repr__(self):
        return self.__str__()
         
         
         
class Roleta:
    def __init__(self, roleta):
        self.rouleta = roleta
    
    def set_rouleta(self, populacao):
        total = sum([individuo.fitness for individuo in populacao])
        # Existe otimizacao que considdera o sort da populacao de acordo com o fit para fazer a busca, mas nao pensei rapido
        chance_individuo = lambda individuo: individuo.fitness / total
        self.roleta = {chance_individuo(populacao[0]): populacao[0]}
        for i in range(1, len(populacao), 1):
            self.roleta[chance_individuo(populacao[i]) + list(self.roleta.keys())[-1]] = populacao[i]
        return self.roleta            
        
    def girar(self):
        # retorna o individuo sorteado
        sorteado = round(random.uniform(0, 1), PRECISION)
        individual_chances = list(self.roleta.keys()) # chances of each individual
        def halve(i:int): # divide a lista de chances pela metade
            if sorteado < individual_chances[(len(individual_chances) / 2)]:
                # Testa o maior elemento dos restantes possiveis é o que tem a maior chance de ser sorteado (boa chance de ja ser um otimo no geral)
                if sorteado > individual_chances[(len(individual_chances) / 2) - 1]:
                    return self.roleta[individual_chances[(len(individual_chances) / 2)]]
                if sorteado < individual_chances[(len(individual_chances) / 2) - 1]:
                    individual_chances = individual_chances[:len(individual_chances) / 2]
                    
        return None
        
       
         
class Populacao:
    def __init__(self, populacao = []):
        self.populacao = populacao
        self.gen_fitness()
            
    def selecao(self):
        pass

    def cruzamento(self):
        # Crossover de média
        #x1_filho = (self.x1 + individuo2.x1) / 2
        #x2_filho = (self.x2 + individuo2.x2) / 2
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


populacao_teste = populacao_inicial(5)
print(populacao_teste[2])
pop = Populacao(populacao_teste)
print(pop)