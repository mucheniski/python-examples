import matplotlib.pyplot as plt
import pandas as pd

familyAges = pd.read_csv("data/familyAges.csv")

print(familyAges)
print(familyAges['name'])
# names = ['Brune', 'Diego', 'Pati', 'Matheus', 'Dirce', 'Lau']
# ages = [30, 34, 27, 29, 54, 64]

names = familyAges['name']
ages = familyAges['age']

plt.title("Ages of family")

plt.xlabel("Names")
plt.ylabel("Ages")

plt.bar(names, ages)
plt.show()