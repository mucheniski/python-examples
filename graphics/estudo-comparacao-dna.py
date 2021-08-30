entrada = open("dados/bacteria.fasta").read()
saida = open("bacteria.html", "w")

# Vetor é feito assim
contagem = {}
listaNucleotideos = ['A', 'T', 'C', 'G']

# Crio uma matriz com os valores de pares zerados para iniciar a contagem
for letra1 in listaNucleotideos:
    for letra2 in listaNucleotideos:
        contagem[letra1 + letra2] = 0

# Apenas para verificar a matriz
# print(contagem)

# Remover a quebra de letra1 para evitar erro na contagem
entrada = entrada.replace("\n", "")

# range cria uma lista de 0 até um valor definido, no caso o tamanho da entrada com len 
# Como estou indo de 2 em 2, preciso colocar o -1 aqui para que quando chegar no último
# não procure mais um porque o último não tem par
for dinucleotideoLetra in range(len(entrada)-1):
    # Percorro a entrada e comparo de duas em duas posições como exemplo AG com o
    # vetor de contagem, quando encontrar a combinação eu adicino mais um porque 
    # todos os valores estão zerados, assim contamos quantas combinações existem    
    contagem[entrada[dinucleotideoLetra] + entrada[dinucleotideoLetra+1]] += 1

print(contagem)

# html
indice = 1

for dinucleotideo in contagem:

    # Nível de transparencia vai de 0 a 100
    # Pego todos os valores e divido pelo maior valor, assim o que vai ficar mais
    # colorido vai ser o maior valor e o menor menos colorido
    transparencia = contagem[dinucleotideo] / max(contagem.values())

    saida.write("<div style='width:100px; border:1px solid #111; height:100px; float:left; background-color:rgba(0,0,255,"+str(transparencia)+"')>"+dinucleotideo+"</div> ")

    if indice % 4 == 0:
        saida.write("<div style='clear:both'></div>")
    
    indice += 1

saida.close()