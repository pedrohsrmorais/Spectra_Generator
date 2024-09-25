import pandas as pd

dataframe = pd.read_csv('dados_para_adicao_do_padrao.csv')
print("Trabalhando na seguinte base de dados:")
print(dataframe)

# ------------ Inputs
n_amostra = input("\nA adição será na amostra de que número? (ex: 1, 2, etc...) ")
n_aditions = int(input("\nQuantas adições serão realizadas? "))  
n_quantity = float(input("\nQual a quantidade adicionada em cada uma das adições? "))  

# Novas colunas para cada adição:
for i in range(n_aditions):
    dataframe[f'Adicao {i}'] = n_quantity

for i in range(n_aditions):
    if i == 0:
        dataframe[f'Adicao {i}'] += dataframe[n_amostra]

    if i > 0:
        dataframe[f'Adicao {i}'] += dataframe[f'Adicao {i - 1}']

print(dataframe)
