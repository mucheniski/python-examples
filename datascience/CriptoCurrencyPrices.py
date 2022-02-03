# Show the prices of the best criptocurrencies
#
# Author: Diego Mucheniski

import pandas as pd
import matplotlib.pyplot as plt

pricesdf = pd.read_csv('../datasets/Top 100 Cryptocurrency 2022.csv')
pricesdf = pricesdf[['Crypto Name', 'Price']]

# Remove all caracters and convert to int
pricesdf['Price'] = pricesdf['Price'].str.replace('$','', regex=True).str.replace(',','', regex=True).str.replace('.','', regex=True)
pricesdf['Price'] = pricesdf['Price'].astype(int)

# Sort by price
pricesdf = pricesdf.sort_values('Price', ascending=False)

pricesdf = pricesdf.head()

# Ploting the graphic
plt.title('Price Average of CriptoCurrency')
plt.xlabel('Price')
plt.ylabel('Crypto Name')
plt.plot(
    pricesdf['Crypto Name'], # Eixo X
    pricesdf['Price'], # Eixo Y
    label='Price'
)

plt.legend()

# Saving the graphic
# plt.savefig('../exported/ticketPrices.png')

plt.show()