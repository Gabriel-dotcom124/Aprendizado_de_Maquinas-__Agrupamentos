#2. Pré-processamento


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


!wget -q "https://raw.githubusercontent.com/andre-marcos-perez/ebac-course-utils/main/dataset/mall_customers.csv"

mall = pd.read_csv("./mall_customers.csv", sep= ",")

mall.head()

mall.info()

with sns.axes_style("whitegrid"):

  grafico = sns.pairplot(data= mall.drop("id", axis= 1), hue= "gender", palette= "pastel")

data = mall[["age", "income", "score"]]

data.head()