import matplotlib.pyplot as plt

numeroBarra1 = [1, 3, 5, 7, 9]
tamanhoBarra1 = [2, 3, 7, 1, 0]
tamanhoHexagonos = [2000, 400, 580, 200, 300]

# Título do grafico
plt.title("Meu primeiro gráfico")

# Nomes dos eixos
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")

# Informar os valores para criar o gráfico de pontos 
plt.scatter(
    numeroBarra1, 
    tamanhoBarra1, 
    label="Meus pontos", 
    color="r", 
    marker="h",
    s=tamanhoHexagonos
)

# Imprime um grafico de linhas
plt.plot(
    numeroBarra1, 
    tamanhoBarra1,
    color="#6E6E6E",
    linestyle="--"
)

# Exibir as legendas
plt.legend()

# plt.show()
# plt.savefig("grafico-salvo-pelo-savefig.png")

# Alterando o padrão dpi da png
plt.savefig("grafico-salvo-pelo-savefig.png", dpi=300)

# Salvar em PDF melhora a qualidade da figura
# plt.savefig("grafico-salvo-pelo-savefig.pdf")