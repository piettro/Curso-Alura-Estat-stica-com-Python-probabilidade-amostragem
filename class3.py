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

'''
O Inmetro verificou que as lâmpadas incandescentes da fabricante XPTO apresentam uma vida útil normalmente distribuída, 
com média igual a 720 dias e desvio padrão igual a 30 dias. Calcule a probabilidade de uma lâmpada, escolhida ao acaso, durar:

1) Entre 650 e 750 dias
2) Mais que 800 dias
3) Menos que 700 dias
'''

mean = 720
desv_pad = 30

# Item A
z_inf = (650 - mean) / desv_pad
z_sup = (750 - mean) / desv_pad

probability = norm.cdf(z_sup) - norm.cdf(z_inf)
print("{0:.2%}".format(probability))

# Item B
Z = (800 - mean) / desv_pad

probability = 1 - norm.cdf(Z)
print("{0:.2%}".format(probability))

# Item C
Z = (700 - mean) / desv_pad

probability = norm.cdf(Z)
print("{0:.2%}".format(probability))

'''
Utilizando a tabela padronizada, ou o ferramental disponibilizado pelo Python, 
encontre a área sob a curva normal para os valores de Z abaixo:

1) Z < 1,96
2) Z > 2,15
3) Z < -0,78
4) Z > 0,59
'''

# Item A
probability = norm.cdf(1.96)
print("{0:0.4f}".format(probability))

# Item B
probability = 1 - norm.cdf(2.15)
# ou -> probabilidade = norm.sf(2.15)
print("{0:0.4f}".format(probability))

# Item C
probability = norm.cdf(-0.78)
print("{0:0.4f}".format(probability))

# Item D
probability = 1 - norm.cdf(0.59)
# ou -> probabilidade = norm.sf(0.59)
print("{0:0.4f}".format(probability))