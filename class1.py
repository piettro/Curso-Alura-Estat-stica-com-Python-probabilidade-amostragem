import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.special import comb
from scipy.stats import binom

'''
Em um concurso para preencher uma vaga de cientista de dados temos um total de 10 questões de múltipla escolha, 
com 3 alternativas possíveis em cada questão. Cada questão tem o mesmo valor. 
Suponha que um candidato resolva se aventurar sem ter estudado absolutamente nada. 
Ele resolve fazer a prova de olhos vendados e chutar todas as resposta. 
Assumindo que a prova vale 10 pontos e a nota de corte seja 5, 
obtenha a probabilidade deste candidato acertar 5 questões e também a probabilidade deste candidato 
passar para a próxima etapa do processo seletivo.
'''

n = 10
p = 1/3
q = (1 - p)
k = 5

probability = (comb(n,k) * (p ** k) * (q ** (n - k)))
print(f'O candidato tem {probability} de probabilidade para passar no processo seletvio')

probability = binom.pmf(k,n,p)
print(f'O candidato tem {probability} de probabilidade para passar no processo seletvio')

probability = binom.pmf(5, n, p) + binom.pmf(6, n, p) + binom.pmf(7, n, p) + binom.pmf(8, n, p) + binom.pmf(9, n, p) + binom.pmf(10, n, p)
print(f'O candidato tem {probability} de probabilidade para passar no processo seletvio')

probability = binom.pmf([5,6,7,8,9,10],n,p).sum()
print(f'O candidato tem {probability} de probabilidade para passar no processo seletvio')

probability = 1 - binom.cdf(4,n,p)
print(f'O candidato tem {probability} de probabilidade para passar no processo seletvio')

'''
Uma moeda, perfeitamente equilibrada, é lançada para o alto quatro vezes. Utilizando a distribuição binomial, 
obtenha a probabilidade de a moeda cair com a face coroa voltada para cima duas vezes.
'''
p = 1 / 2  
n = 4  
k = 2  

result = binom.pmf(k, n, p)


'''
Um dado, perfeitamente equilibrado, é lançado para o alto dez vezes. Utilizando a distribuição binomial, 
obtenha a probabilidade de o dado cair com o número cinco voltado para cima pelo menos três vezes.
'''
p = 1 / 6  
n = 10     
result = binom.sf(2, n, p)

print("{0:.2%}".format(result))

'''
Uma cidade do interior realiza todos os anos uma gincana para arrecadar fundos para o hospital da cidade. 
Na última gincana se sabe que a proporção de participantes do sexo feminino foi de 60%. O total de equipes, 
com 12 integrantes, inscritas na gincana deste ano é de 30. Com as informações acima responda: 
Quantas equipes deverão ser formadas por 8 mulheres?
'''
p = 0.6
n = 12
k = 8

probability = binom.pmf(k, n, p)
print(f'{round(probability * 100,2)}%')

teams = 30 * probability
teams = round(teams,0)
print(teams)

'''
Suponha que a probabilidade de um casal ter filhos com olhos azuis seja de 22%. 
Em 50 famílias, com 3 crianças cada uma, quantas podemos esperar que tenham dois filhos com olhos azuis?
'''

p = 0.22
n = 3
k = 2
N = 50

probability = binom.pmf(k, n, p)
mean = probability * N
print(probability)
print(mean)