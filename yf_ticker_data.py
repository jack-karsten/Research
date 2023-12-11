#!/usr/bin/env python
# coding: utf-8

# In[5]:


import yfinance as yf

def get_ticker_data(ticker_name, period_length):
    """
    Fetches data for a given ticker from Yahoo Finance.

    Parameters:
    ticker_name (str): The ticker symbol for which to fetch data.

    Returns:
    DataFrame: The fetched ticker data.
    """
    ticker = yf.Ticker(ticker_name)
    # Fetch historical data, adjust as needed
    data = ticker.history(period=period_length)
    return data


# In[ ]:




