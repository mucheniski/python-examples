import matplotlib.pyplot as plt
import random

vetor = []

# Crio um loop de 0 a 100
# populo com um numero aleatório de 0 a 50
for i in range(100):
    numeroAleatorio = random.randint(0,1000)
    vetor.append(numeroAleatorio)

plt.boxplot(vetor)
plt.title("Boxplot")
plt.show()