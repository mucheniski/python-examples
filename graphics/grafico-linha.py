import matplotlib.pyplot as plt

eixoX = [1, 2, 5]
eixoY = [2, 3, 7]

# Título do grafico
plt.title("Meu primeiro gráfico")

# Nomes dos eixos
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")

# Informar os valores para plotar e gerar o gráfico de linhas
plt.plot(eixoX, eixoY)

plt.show()