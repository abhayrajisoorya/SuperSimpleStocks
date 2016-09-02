from urllib.request import urlopen
import re
import math

class IndexCalculator:

    def __init__(self, tickers):
        self.prices = []
        self.list = tickers
        self.GetData()
        self.ComputeMean()

    def GetData(self):
        root = 'http://finance.google.com/finance/info?client=ig&q='

        for ticker in self.list:
            try:
                url = root+ticker
                data = str(urlopen(url).read())
                last_price = float(re.findall("\d+\.\d+", data.split(',')[3])[0])
                self.prices.append(last_price)
            except:
                pass

    def ComputeMean(self):
        product = 1
        for k in self.prices:
            product *= k

        index = math.pow(product, 1/len(self.prices))
        print('The current All Share Index for stocks in the given list is ' + str(index))


list = ['AAPL', 'GOOG', 'ORCL']
b = IndexCalculator(list)
