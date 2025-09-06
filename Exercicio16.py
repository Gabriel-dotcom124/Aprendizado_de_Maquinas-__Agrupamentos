import sklearn
import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt


iris = sns.load_dataset("iris")
iris = iris.drop("species", axis= 1)

with sns.axes_style("whitegrid"):

  grafico = sns.pairplot(data= iris, palette= "pastel")

print(iris.isnull().sum())

iris = iris.fillna(iris.mean())

print(iris.isnull().sum())

from sklearn.preprocessing import StandardScaler


scaler = StandardScaler()

for col in numerical_cols:
  iris[col + "_std"] = scaler.fit_transform(iris[[col]])

display(iris.head())


iris_scaled = iris.filter(regex='_std$')

display(iris_scaled.head())



wcss = []

for k in range(1, 11):
  model = KMeans(n_clusters=k, random_state=42, n_init=10)
  wcss.append(model.inertia_)

print(wcss)



with sns.axes_style("whitegrid"):
  grafico = sns.lineplot(x=range(1, 11), y=wcss, marker="8", palette="pastel")
  grafico.set(title="Método do Cotovelo", ylabel="WCSS", xlabel="Quantidade de Clusters");
  plt.show()


n_clusters = 3

model = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
model.fit(iris_scaled)

clusters = model.labels_

iris['cluster'] = clusters

display(iris.head())

with sns.axes_style("whitegrid"):
  grafico = sns.pairplot(data= iris, hue= "cluster", palette= "pastel")

#Com base no gráfico de pares com as atribuições de clusters, podemos observar como os pontos de dados estão agrupados. Com 3 clusters, podemos ver agrupamentos distintos dos pontos de dados da íris, o que está alinhado com o fato de que o conjunto de dados da íris é conhecido por conter três espécies de flores de íris. Os clusters parecem separar as diferentes espécies de maneira razoavelmente boa com base nas características.

flor = np.array([5.1, 3.5, 1.4, 0.2])


cluster = model.predict(flor.reshape(1, -1))

print(f"A flor seria alocada ao grupo: {cluster[0]}")




