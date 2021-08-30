import matplotlib.pyplot as plt

numeroBarra1 = [1, 3, 5, 7, 9]
tamanhoBarra1 = [2, 3, 7, 1, 0]

numeroBarra2 = [2, 4, 6, 8, 10]
tamanhoBarra2 = [5, 1, 3, 7, 4]

# Título do grafico
plt.title("Meu primeiro gráfico")

# Nomes dos eixos
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")

# Informar os valores para criar o gráfico de barras
plt.bar(numeroBarra1, tamanhoBarra1, label = "Grupo 1")
plt.bar(numeroBarra2, tamanhoBarra2, label = "Grupo 2")
plt.legend()
plt.show()