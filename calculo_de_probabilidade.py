import math

# A conta ficou mais facil pois eu transladei !!!


PRECISION = 3
ULTIMO_INDIVIDUO = round(2 * math.e - 2, PRECISION)


def round_result(res):
    return round(res, PRECISION)


def f_x(x):
    # Distribuicao de probabilidade
    res = 1 / (x + 2)
    return round_result(res)


def g_x(x):
    # Acumulada
    res = math.log(x + 2)
    return round_result(res)


def chance_x(x1, x2):
    # Chance de sair o individuo x2
    y1 = g_x(x1)
    y2 = g_x(x2)
    return round_result(y2 - y1)


def chance_cada_individuo(num_individuos):
    chance_individuos = []
    step = ULTIMO_INDIVIDUO / num_individuos
    walk = 0
    for i in range(0, num_individuos, 1):
        chance_individuos.append(chance_x(walk, walk + step))
        walk += step
    return chance_individuos

def chance_acumulada_individuo(num_individuo, chance_individuos):
    return round_result(sum(chance_individuos[:num_individuo]))


def message_to_print_chances(pos_individuo, walk, chance_individuo, acumulado):
    string = f"Individuo {pos_individuo}: x {walk}, g(x) = {chance_individuo}, acumulado = {acumulado}"
    return string

def print_chance_cada_individuo(chance_individuos, show_x = False):
    # para qualquer lista de individuos mostrar suas chances e numero de operacoes
    num_individuos = len(chance_individuos)
    step = round_result(ULTIMO_INDIVIDUO / num_individuos)
    walk = 0
    acumulado = 0
    for i in range(0, num_individuos, 1):
        walk = round_result(walk + step)
        acumulado = round_result(chance_individuos[i] + acumulado)
        #porcentagem_sobre_acumulado = round_result(chance_individuos[i]* 100 / acumulado)
        if show_x:
            print(f"Individuo {i}: x {walk}, g(x)% = {round_result(chance_individuos[i] * 100)}, 
                  acumulado = {acumulado}")
        else:
            print(f"Individuo {i}: g(x)% = {round_result(chance_individuos[i] * 100)}, acumulado = {acumulado}")
            
        #print(message_to_print_chances(i, walk, chance_individuos[i], acumulado))
        
def quebra_lista_meio(lista):
    return lista[:len(lista) // 2], lista[len(lista) // 2:]

def pegando_elemento_do_meio(lista):
    # Se a lista tiver tamanho par, pegar o elemento a esquerda, pq tanto faz, o padrao e pegar o da direita
    if len(lista) % 2 == 0:
        return lista[len(lista) // 2 - 1], len(lista) // 2 - 1
    return lista[len(lista) // 2], len(lista) // 2

def elementos_meio_individuos(chance_individuos, numero_divisoes):
    lista = chance_individuos
    print_chance_cada_individuo(lista)
    print(f"{' ' * 25} |\n{' ' * 25} V")
    for i in range(0, numero_divisoes, 1):
        lista_esq, lista_dir = quebra_lista_meio(lista)
        lista = lista_esq
        print_chance_cada_individuo(lista_esq)
        """ print(f"{' ' * 13} {' // ' * 6} ")
        print_chance_cada_individuo(lista_dir) """
        length_str = len(str(lista))
        #spaces = length_str // 2
        print(f"{' ' * 25} |\n{' ' * 25} V")


individuos_chances = chance_cada_individuo(10)
elementos_meio_individuos(individuos_chances, 2)

