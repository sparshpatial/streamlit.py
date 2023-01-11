import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""Simple Stock Price App""")

tickerSymbol ='APPL'

tickerData =yf.Ticker(tickerSymbol)

tickerDf =tickerData.history(period='id',starts='2010-5-31',end='2020-5-31')

st.bar_chart(tickerDf.Close)
st.bar_chart(tickerDf.Volume)