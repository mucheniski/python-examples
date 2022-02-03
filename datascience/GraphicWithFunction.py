import pandas as pd
import matplotlib.pyplot as plt

pricesdf = pd.read_csv('../datasets/AnnualTicketSales.csv')
pricesdf = pricesdf.sort_values('AVERAGE TICKET PRICE', ascending=True)

def plotAndSaveGraphic(title, labelX, labelY, xaxis, yaxis, labelGraphic, graphicPath):
    """
    Show graphic
    :param title, labelY, labelX, xaxis, yaxis, labelGraphic, graphicPath
    """
    plt.title(title)
    plt.xlabel(labelX)
    plt.ylabel(labelY)
    plt.plot(
        xaxis,
        yaxis,
        'r.--',  # cor e tipo da linha, vermelha pontilhada e com traços entre os pontos
        label=labelGraphic
    )
    plt.legend()

    # Saving the graphic
    plt.savefig(graphicPath)

    plt.show()


plotAndSaveGraphic('Price Average Through the Years',
            'Years',
            'Prices',
            pricesdf['YEAR'],
            pricesdf['AVERAGE TICKET PRICE'],
            'Price',
            '../exported/functionGraphic.png'
)
