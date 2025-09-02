#1. Motivação


import numpy as np


def dist(a:np.array, b: np.array) -> float:
  return np.linalg.norm(a-b)


grupo_a = np.array([30, 40])
grupo_b = np.array([57, 90])


cliente = np.array([27, 50])

dist_a = dist(cliente, grupo_a)
dist_b = dist(cliente, grupo_b)


#1.1 K-Média


#O agrupamento de k-médias é uma abordagem que busca particionar um conjunto de dados em  k  grupos ou clusters. Cada objeto  x  do conjunto de dados é alocado ao grupo mais próximo, ou seja, ao grupo com a menor distância entre suas coordenadas e as do centro do grupo  xc  (centróide). De maneira geral, utiliza métodos iterativos para encontrar os centróides  xc , dado um número pré definido de clusters. O algoritmo parte de algumas definições:

#• defina a quantidade de clusters  k ;

#• defina a posição inicial dos centróides  xc ;

#• defina a um erro de movimentação de centróide  α ;


#E itera até que os centroides não se movimentem significativamente: Para cada valor  xi :

#Para cada valor  xc :

#Calcule a distância de  xi  a  xc  aloque  xi 

#para  xc  mais próximo Recalcule todos  xc  Se a distancia entre o antigo e o novo  xc  for maior que  α : Repita


#1.2 Pacote Scikit-Learn

from sklearn.cluster import KMeans

model = KMeans()

