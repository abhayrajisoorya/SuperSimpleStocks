import datetime
import csv
import os
import pandas as pd

class Trade:

    def __init__(self):
        self.path = '/Users/abhay/Desktop/trades.csv'

    # Record Trade with details
    def RecordTrade(self, symbol, price, quantity, indicator):

        timestamp = datetime.datetime.now()

        header = ['Timestamp', 'Symbol', 'Price', 'Quantity', 'Indicator']

        with open(self.path, 'a') as csvfile:
            writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)

            # Create header if file is a newly created
            if (os.stat(self.path).st_size == 0):
                writer.writerow(header)

            # Append information to file
            if type(symbol) is str and (type(price) is int or type(price) is float) and type(quantity) is int and type(indicator) is str:
                writer.writerow([timestamp, symbol, price, quantity, indicator])
                csvfile.close()
            else:
                print('Wrong data format for one or more arguments.')
                print('Symbol and Indicator are strings, price is a float, quantity is an integer.')
                print('Information not appended.')
                csvfile.close()
                quit()


    def CalcPrice(self, symbol):

        if not isinstance(symbol, str):
            print('Please enter a valid symbol')
            quit()

        # Handler for empty trade file
        if (os.stat(self.path).st_size == 0):
            print('No trades recorded in memory')
            quit()

        # Check if symbol has recorded trades
        data = pd.read_csv(self.path)
        if not any(data.Symbol == symbol):
            print('No trades recorded for this instrument')
            quit()
        else:
            # Obtain compressed symbol frame with trades relating to symbol
            SF = pd.DataFrame(data.loc[data['Symbol'] == symbol])
            SF['Timestamp'] = pd.to_datetime(SF['Timestamp'],format="%Y-%m-%d %H:%M:%S.%f")

            # Obtain information from last 15 minutes
            time_now = datetime.datetime.now()
            time_earlier = time_now - datetime.timedelta(minutes=15)

            SF_timed = SF[(SF['Timestamp'] > time_earlier) & (SF['Timestamp'] < time_now)]

            if SF_timed.shape[0] == 0:
                print('No trades recorded for this stock in the last 15 minutes.')
                quit()

            # Find VWAP from this final table

            VWAP = sum(SF_timed['Price']*SF_timed['Quantity'])/sum(SF['Quantity'])
            print('VWAP for ' + symbol + ' across recorded trades over the last 15 minutes is ' + str(VWAP))





a = Trade()
# Fake data - does not represent real time bid-asks or prices in anyway
a.RecordTrade('AAPL', 100, 100, 'S')
a.RecordTrade('AAPL', 100, 90, 'B')
a.RecordTrade('AAPL', 400, 100, 'S')
a.RecordTrade('GE', 100, 100, 'S')
a.RecordTrade('F', 100, 75, 'S')
a.RecordTrade('ORCL', 200, 80, 'B')

a.CalcPrice('AAPL')
a.CalcPrice('ORCL')