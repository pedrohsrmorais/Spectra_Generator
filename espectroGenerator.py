import pandas as pd
import numpy as np

import random

# imports próprios
from functions import func_s
from functions import func_maximum_abs

# -------------------------------------------------------------------- Números de onda
# Solicitar os valores do usuário
number_of_nm_minimum = int(input("Digite o menor número de onda: "))
number_of_nm_maximum = int(input("Digite o maior número de onda: "))
numeros_de_onda = {'minimum': number_of_nm_minimum, 'maximum': number_of_nm_maximum}

# Criar o DataFrame com os números de onda
dataframe_nm = pd.DataFrame(list(range(number_of_nm_minimum, number_of_nm_maximum + 1)), columns=['(nm)'])

# -------------------------------------------------------------------- Número de amostras
number_of_s = input("Digite o número de amostras: ")
number_of_c = int(number_of_s)
concentration = []

# Chama a função para obter a lista
list_s = func_s(number_of_c)

#-------------------------------------------------------------------------- CONCENTRAÇÕES

# Coleta as concentrações
for i in range(number_of_c):
    conc = float(input(f"Digite a concentração para a amostra {i + 1}: "))  
    concentration.append(conc)

# Adicionando colunas numeradas ao DataFrame
for i, item in enumerate(concentration, start=1):
    dataframe_nm[str(i)] = item  # Cria a coluna '1', '2', etc. e atribui o valor da concentração

#---------------------------------------------------------------------------- ABSORÇÕES

# Chamando a função func_maximum_abs para obter os valores de absorbância máxima
maximun_abs = func_maximum_abs(number_of_c, numeros_de_onda)

# Inicializar a coluna 'abs' com 0
dataframe_nm['abs'] = 0

for i, item in enumerate(maximun_abs, start=1):
    Sx = abs(dataframe_nm['(nm)'] - item)
    

    A = 0.2  # Altura do pico
    sigma = 80  # Largura do pico
    dataframe_nm[f'S{item}'] = A * np.exp(- (Sx ** 2) / (2 * sigma ** 2))


print(dataframe_nm)
dataframe = dataframe_nm

for i, item in enumerate(maximun_abs, start=1):
    eq = dataframe_nm[f'S{item}'] * dataframe_nm[f'{i}'] 
    dataframe_nm['abs'] = dataframe_nm['abs'] + eq  
    

    dataframe_nm = dataframe_nm.drop(columns=[f'S{item}'])
    dataframe_nm = dataframe_nm.drop(columns=[f'{i}'])

print("\n Máxima absorbancias e concentrações dos analitos:")
print(maximun_abs)
print(concentration)

# --------------------------------------------------------------------------------EXPORTANDO
dataframe_nm.to_excel('espectro_gerado.xlsx', index=False)
dataframe.to_csv('dados_para_adicao_do_padrao.csv', index=False)
