import pandas as pd
import matplotlib.pyplot as plt

pricesdf = pd.read_csv('../datasets/AnnualTicketSales.csv')
pricesdf = pricesdf.sort_values('AVERAGE TICKET PRICE', ascending=True)

plt.title('Price Average Through the Years')
plt.xlabel('Years')
plt.ylabel('Prices')
plt.plot(
    pricesdf['YEAR'], # Eixo X
    pricesdf['AVERAGE TICKET PRICE'], # Eixo Y
    'r.--', # cor e tipo da linha, vermelha pontilhada e com traços entre os pontos
    label='Price'
)

plt.legend()

# Saving the graphic
plt.savefig('../exported/ticketPrices.png')

plt.show()