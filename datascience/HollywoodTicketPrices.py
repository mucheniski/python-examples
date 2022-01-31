import pandas as pd
import matplotlib.pyplot as plt

pricesdf = pd.read_csv('../datasets/AnnualTicketSales.csv')
pricesdf = pricesdf.sort_values('AVERAGE TICKET PRICE', ascending=True)

plt.title('Price Average Through the Years')

plt.plot(pricesdf['YEAR'], pricesdf['AVERAGE TICKET PRICE'])

plt.show()