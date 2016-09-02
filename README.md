# SuperSimpleStocks
Recruiting exercise for a company

Attached are three .py files that calculate the quantities required as per the question. This document provides an overview on how to use these files; please also refer to Assumptions.doc, which provides brief notes on assumptions used.

Ratios.py:
This addresses parts (a) and (b) of the first question.

The code is written in class format, so the appropriate syntax to use is: FindRatios(X) where ‘X’ is the ticker string of the required stock. E.g. FindRatios(‘F’); FindRatios(‘ORCL’) etc.

The console output should be a statement for both the required ratios for the respective ticker.

Trader.py:
This addresses part (c) and (d) of the first question.

Code is again written in class format, so the appropriate syntax to use is:
A = Trade(), which initialises the class
A.RecordTrade(‘AAPL’, 100,  90, ‘S’) records a sell trade for 90 stocks of Apple at 100 price., into a local csv file (path).
A.CalcPrice(‘AAPL’) then calculated Apple’s 15 min VWAP from the information recorded into the csv file.

Note: A.CalcPrice(X) returns a VWAP for X ONLY if there is data existing in the csv – so one would first have to record some trades before calling this method.

IndexCalculator.py:
This addresses the second question

The appropriate syntax is IndexCalculator(X) where X is a list of stock ticker strings, across which the index needs to be calculated.

