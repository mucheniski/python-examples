import pandas as pd
import matplotlib.pyplot as plt

expenditures = pd.read_csv("data/Despesas.csv")

# Soma dos valores agrupados pela categoria, o reset_index serve para manter indexado o dataframe
# em colunas que podem ser utilizadas para plotar o gráfico
totalization = expenditures.groupby('Categoria')['Valor'].sum().reset_index()

category = totalization['Categoria']
value = totalization['Valor']

# Plotando o grafico
plt.title("Expenditures")
plt.xlabel("Category")
plt.ylabel("Value")
plt.bar(category, value)
plt.show()