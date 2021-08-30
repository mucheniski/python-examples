import matplotlib.pyplot as plt

numeroBarra = [1, 2, 3, 4, 5]
tamanhoBarra = [2, 3, 7, 1, 0]

# Título do grafico
plt.title("Meu primeiro gráfico")

# Nomes dos eixos
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")

# Informar os valores para criar o gráfico de barras
plt.bar(numeroBarra, tamanhoBarra)
plt.show()