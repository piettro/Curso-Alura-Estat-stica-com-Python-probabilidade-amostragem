import pandas as pd
import numpy as np
from scipy.stats import norm

norm_table = pd.DataFrame(
    [], 
    index=["{0:0.2f}".format(i / 100) for i in range(0, 400, 10)],
    columns = ["{0:0.2f}".format(i / 100) for i in range(0, 10)])

for index in norm_table.index:
    for column in norm_table.columns:
        Z = np.round(float(index) + float(column), 2)
        norm_table.loc[index, column] = "{0:0.4f}".format(norm.cdf(Z))

norm_table.rename_axis('Z', axis = 'columns', inplace = True)

print(norm_table.head())

'''
Em um estudo sobre as alturas dos moradores de uma cidade verificou-se que o conjunto de dados segue 
uma distribuição aproximadamente normal, com média 1,70 e desvio padrão de 0,1. 
Com estas informações obtenha o seguinte conjunto de probabilidades:

A. probabilidade de uma pessoa, selecionada ao acaso, ter menos de 1,80 metros.
'''

mean = 1.7
desv_pad = 0.1
x = 1.8

z = (x - mean) / desv_pad

probability = 0
print(f'The probability of person smaller than 1.8 metters is {round(probability * 100,2)}%')

probability = norm.cdf(z)
print(f'The probability of person smaller than 1.8 metters is {round(probability * 100,2)}%')

'''
B. probabilidade de uma pessoa, selecionada ao acaso, ter entre 1,60 metros e 1,80 metros.
'''

mean = 1.7
desv_pad = 0.1
x_sup = 1.8
x_inf = 1.6

z_sup = (x_sup - mean) / desv_pad
z_inf = (x_inf - mean) / desv_pad

probability_sup = norm.cdf(z_sup)
probability_inf = norm.cdf(z_inf)
probability = probability_sup - probability_inf
print(f'The probability of person beetween than 1.6 metters and 1.8 metters is {round(probability * 100,2)}%')

'''
C. probabilidade de uma pessoa, selecionada ao acaso, ter mais de 1,90 metros.
'''
mean = 1.7
desv_pad = 0.1
x_inf = 1.9

z_inf = (x_inf - mean) / desv_pad

probability_sup = 1
probability_inf = norm.cdf(z_inf)
probability = probability_sup - probability_inf
print(f'The probability of person taller than 1.9 metters is {round(probability * 100,2)}%')


'''
A aplicação de uma prova de estatística em um concurso apresentou um conjunto de notas normalmente distribuídas. 
Verificou-se que o conjunto de notas tinha média 70 e desvio padrão de 5 pontos.
Qual a probabilidade de um aluno, selecionado ao acaso, ter nota menor que 85?
'''

mean = 70
desv_pad = 5
x = 85
z = (x - mean) / desv_pad

probability = norm.cdf(z)
print(f'The probability of the random student has perfomance lower than 85 is {round(probability * 100,2)}%')

'''
O faturamento diário de um motorista de aplicativo segue uma distribuição aproximadamente normal, 
com média R$ 300,00 e desvio padrão igual a R$ 50,00. Obtenha as probabilidades de que, em um dia aleatório, o motorista ganhe:

1) Entre R$ 250,00 e R$ 350,00
2) Entre R$ 400,00 e R$ 500,00
'''

mean = 300
desv_pad = 50
z_inf = (250 - mean) / desv_pad
z_sup = (350 - mean) / desv_pad

probability = norm.cdf(z_sup) - norm.cdf(z_inf)
print("{0:.2%}".format(probability))

mean = 300
desv_pad = 50
z_inf = (400 - mean) / desv_pad
z_sup = (500 - mean) / desv_pad

probability = norm.cdf(z_sup) - norm.cdf(z_inf)
print("{0:.2%}".format(probability))