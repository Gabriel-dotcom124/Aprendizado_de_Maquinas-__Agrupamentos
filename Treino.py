#3. Treino

#3.1 Algoritimo


model = KMeans(n_clusters= 5)
model = model.fit(data)
model.__dict__

clusters = model.labels_
clusters = pd.DataFrame(clusters, columns=["clusters"])
clusters.head()

clustered_data = pd.concat([data, clusters], axis= 1)
clustered_data.head()

with sns.axes_style("whitegrid"):

  grafico = sns.pairplot(data= clustered_data, hue= "clusters", palette= "pastel")

clusters_centers = model.cluster_centers_
clusters_centers = pd.DataFrame(clusters_centers, columns=["age", "income", "score"])
clusters_centers.head()

with sns.axes_style("whitegrid"):

  fig, ax = plt.subplots()
  sns.scatterplot(data= clustered_data, x= "income", y= "score", hue= "clusters", palette= "pastel", ax= ax)
  sns.scatterplot(data= clusters_centers, x= "income", y= "score", color= "black", ax= ax)


