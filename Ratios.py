# Import necessary modules
import pandas_datareader.data as data
import datetime
import pandas as pd


# Define new initialization class
class FindRatios:

    # Instance start up method - initialize ticker object
    def __init__(self, symbol=None):
        if symbol == None:
            raise ValueError('There must be a ticker symbol. ' +
                       'Rerun method with symbol argument.')
            quit()
        self.ticker = symbol

        self.SourceData()
        self.ComputeRatios()

    # Source the data for stock from an appropriate API
    # Yahoo finance is used here
    def SourceData(self):
        start = datetime.datetime.now() - \
                datetime.timedelta(1000)
        end = datetime.datetime.now()

        # Source the OHLCV and corporate action data
        quotes = data.DataReader(self.ticker, 'yahoo', start, end)
        corp_action = data.DataReader(self.ticker, 'yahoo-actions',
                                      start, end)

        # Assign data to standard panda frames
        yesterday = datetime.datetime.now() - \
                    datetime.timedelta(1)

        self.prices_final = pd.DataFrame(quotes.ix[yesterday.date()])
        self.actions_final = pd.DataFrame(corp_action)



    def ComputeRatios(self):

        AF = self.actions_final
        AP = self.prices_final
        AP.columns = ['value']

        # Need to exclude stock splits from extraction and find last dividend
        if not any(AF.action == 'DIVIDEND'):
            print('No dividend data exists in last three years.')
            print('Ratios cannot be computed for this stock.')
            quit()

        else:
            all_dividends = pd.DataFrame(AF.loc[AF['action'] == 'DIVIDEND'])
            no_of_dividends =  all_dividends.shape[0]
            last_dividend = all_dividends['value'].iloc[0]
            last_price = AP.iloc[1]['value']

            self.div_yield = last_dividend/last_price

            if no_of_dividends >= 3:
                self.PE = last_price/all_dividends.iloc[:4]['value'].mean()
            else:
                self.PE = last_price/all_dividends.iloc[:no_of_dividends]['value'].mean()

            print('The P/E ratio for ' + self.ticker + ' is ' + str(self.PE))
            print('The dividend yield for ' + self.ticker + ' is ' + str(self.div_yield))

Apple = FindRatios('F')
Facebook = FindRatios('AAPL')
GE = FindRatios('GE')



