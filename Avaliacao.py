 #Avaliação
#4.1 WCSS


wcss = []


for k in range(1, 11):

  model = KMeans(n_clusters= k)
  model = model.fit(data)
  wcss.append(model.inertia_)


with sns.axes_style("whitegrid"):

  grafico = sns.lineplot(x= range(1, 11), y= wcss, marker= "8", palette= "pastel")
  grafico.set(title= "Metodo cotovelo", ylabel= "WCSS", xlabel= "Qtd. clusters");


model = KMeans(n_clusters= 4)
model = model.fit(data)


clusters = model.labels_
clustered_data = pd.concat([data, pd.DataFrame(clusters, columns=["clusters"])], axis= 1)

with sns.axes_style("whitegrid"):

  grafico = sns.pairplot(data= clustered_data, hue= "clusters", palette= "pastel")


model = KMeans(n_clusters= 6)
model = model.fit(data)


clusters = model.labels_
clustered_data = pd.concat([data, pd.DataFrame(clusters, columns=["clusters"])], axis= 1)

with sns.axes_style("whitegrid"):

  grafico = sns.pairplot(data= clustered_data, hue= "clusters", palette= "pastel")

model = KMeans(n_clusters= 5)
model = model.fit(data)


clusters = model.labels_
clustered_data = pd.concat([data, pd.DataFrame(clusters, columns=["clusters"])], axis= 1)

with sns.axes_style("whitegrid"):

  grafico = sns.pairplot(data= clustered_data, hue= "clusters", palette= "pastel")



