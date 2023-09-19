import pandas_datareader.data as wb
import pandas as pd
import numpy as np
import datetime 
import os 
import yfinance as yfin

#ment to u
#explority data analysis of stock priceses, to practice visualizationas and Pandas 
# focus on bank stocks and see how they progress throughout the financail crisis all the way to early 2016
# 2008-2009 economic crash 

########
# DATA #
########
start = "2006-01-01" # date range 
end = "2016-01-01"
#Tickers for Each Bank: Bank of America - BAC , CitiGroup - C, Goldman Sachs - GS , JPMorgan Chase - JPM, Morgan Stanley MS, Wells Fargo - WFC
yfin.pdr_override()
# Bank of America
BAC = wb.get_data_yahoo("BAC", start, end)
# CitiGroup
C = wb.DataReader('C', start, end)
# Goldman Sachs
GS = wb.DataReader('GS', start, end)
# JPMorgan Chase
JPM =wb.DataReader('JPM', start, end)
# Morgan Stanley 
MS = wb.DataReader('MS', start, end)
# Wells Fargo 
WFC = wb.DataReader('WFC', start, end)
print(C.head())

tickers = ['BAC', 'C', 'GS', 'JPM', 'MS', 'WFC']
print(tickers)

# help(pd.concat)
# CONCANTENATE the Bank Dataframes 
bank_stocks = pd.concat([BAC, C, GS, JPM, MS, WFC], axis = 1, keys=tickers)
print(bank_stocks)

# SET column name levels
bank_stocks.columns.names = ['Bank Ticker', 'Stock Info']
print(bank_stocks.head())

print(bank_stocks.xs('BAC', level = 'Bank Ticker', axis = 1).pct_change())

#######
# EDA #
####### exploratory data analysis
# resources: 
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.xs.html
# https://pandas.pydata.org/pandas-docs/stable/user_guide/advanced.html

# max Close price for each bank stock throughout, time periods
max = bank_stocks.xs(key='Close', level='Stock Info', axis=1).max()
print(max)

# new empty DataFrame 
returns = pd.DataFrame()

# returns for each bank stocks
# pct_change() on Close column to create return values 

for tick in tickers:
    returns[]
# returns.pct_change()