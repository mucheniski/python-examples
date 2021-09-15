import pandas as pd
import matplotlib.pyplot as plt


def printLine():
    print()
    print("=" * 300)
    print()


childMortality = pd.read_csv("data/mortalidade-infantil.csv").head(10)

print(childMortality)

percent = childMortality['indicx']
city = childMortality['no_cidade']

printLine()

plt.title("Child Mortality Percent")
plt.xlabel("City")
plt.ylabel("Percent")
plt.bar(city, percent)
plt.show()

printLine()
