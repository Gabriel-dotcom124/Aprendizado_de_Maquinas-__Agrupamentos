#5. Predição


#5.1 Estudos dos clusters


#Clusters 6

#Exemplo: Cluster 1 São clientes de alta renda e baixo potencial de compras que poderiam estar gastando mais no shopping.

with sns.axes_style("whitegrid"):

  grafico = sns.scatterplot(data= clustered_data.query("clusters == 1"), x= "age", y= "income", hue= "clusters", palette= "pastel")
  grafico.set(title= " Cluster 1 | Distribuição de Renda e Idade", xlabel= "Idade", ylabel= "Renda (U$)");
  grafico.get_legend().set_title("clustesr")


#Clusters 0 e 5

#São clientes com renda e potencial médio de compras que podem deixar de frequentar o shopping.

with sns.axes_style("whitegrid"):

  grafico = sns.scatterplot(data= clustered_data.query('clusters == 0 or clusters == 5'), x= "age", y= "income", hue= "clusters", palette= "pastel")
  grafico.set(title= "Clusters 0 e 5 | Distribuição de Renda e Idade", xlabel= "Idade (anos)", ylabel= "Renda (milhares de dólares)");
  grafico.get_legend().set_title("clusters")

#5.2 Predição

#Exemplo: Um cliente com 19 anos, 15.000 USD de renda anual e potencial de compra de 39:

cliente = np.array([19, 15, 39])

cluster = model.predict(cliente.reshape(1, -1))
print(clusters)


