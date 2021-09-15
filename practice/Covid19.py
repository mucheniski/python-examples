import pandas as pd


def printLine():
    """
    Print a line
    """
    print()
    print("="*100)
    print()


covidData = pd.read_csv("data/boletim-covid.csv")


printLine()
print(covidData)
printLine()

# only not null values
print(covidData[covidData['notes'].notnull()])