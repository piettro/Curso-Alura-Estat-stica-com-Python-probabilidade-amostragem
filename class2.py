import numpy as np
from scipy.stats import poisson
'''
Um restaurante recebe em média 20 pedidos por hora. 
Qual a chance de que, em determinada hora escolhida ao acaso, o restaurante receba 15 pedidos?
'''

mean = 20
k = 15

probability = ((np.e ** -mean) * (mean ** k)) / (np.math.factorial(k))
print(f'The probability is {round(probability * 100,2)}%')

probability = poisson.pmf(k,mean)
print(f'The probability is {round(probability * 100,2)}%')


'''
O número médio de clientes que entram em uma padaria por hora é igual a 20. 
Obtenha a probabilidade de, na próxima hora, entrarem exatamente 25 clientes.
'''

mean = 20
k = 25

probability = ((np.e ** -mean) * (mean ** k)) / (np.math.factorial(k))
print(f'The probability is {round(probability * 100,2)}%')

probability = poisson.pmf(k,mean)
print(f'The probability is {round(probability * 100,2)}%')