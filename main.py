import yfinance as yf
import streamlit as st

st.write("""
# Stock Price App
Shown are the stock ***opening price*** and ***volume*** of Microsoft
""")


# #define the ticker symbol
tickerSymbol = 'MSFT'
#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)

#get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2020-5-31')


st.line_chart(tickerDf.Open)
st.line_chart(tickerDf.Volume)
