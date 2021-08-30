# Dados coletados no DataSus
# Crescimento da população de 1980-2016

import matplotlib.pyplot as plt

# Ler o arquivo
dados = open("dados/populacao_brasileira.csv").readlines()

# Criar os vetores de eixos
eixoAnos = []
eixoPopulacao = []

# Navegar pelos dados len pega o tamanho de dados, e range cria uma lista que vai de 0 até o tamanho dos dados em len
# Util para poder ignorar a primeira linha
for i in range(len(dados)):
        if i != 0: # Ignorar a primeira linha que é o cabeçalho da planilha
            linha = dados[i].split(";") # Divido a linha em um array de 2 posições linha[0,1]
            eixoAnos.append(int(linha[0]))
            eixoPopulacao.append(int(linha[1]))


# é importante armazenar os valores no banco como números, por isso foram convertidos
# print(eixoAnos)
# print(eixoPopulacao)

plt.bar(eixoAnos, eixoPopulacao, color="#0000FF")
plt.plot(eixoAnos, eixoPopulacao, color="k")
plt.title("Crescimento da população Brasileira 1980-2016")
plt.xlabel("Ano")
plt.ylabel("População x 100.000.000")
plt.show()