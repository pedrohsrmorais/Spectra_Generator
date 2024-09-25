import random

# abs = S1*[a] + S2*[b]

def func_s(x):
    data_s = []
    for i in range(x):
        s = random.randint(1, 1000000)
        data_s.append(s)

    return data_s


# Definindo a função para gerar valores de absorbância máxima
def func_maximum_abs(x, numeros_de_onda):
    maximum_abs = []  
    
    for i in range(x):
        s = random.randint(numeros_de_onda['minimum'], numeros_de_onda['maximum'])
        maximum_abs.append(s)

    return maximum_abs