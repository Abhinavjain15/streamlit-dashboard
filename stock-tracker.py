import streamlit as st
import yfinance as yf
import datetime

st.title("Stock Tracker Dashboard")

col1, col2 = st.columns(2)

ticker_symbol = st.text_input("Enter the stock symbol", "AAPL")
stock_data = yf.Ticker(ticker_symbol)
company_name = stock_data.info.get("longName", "Name not available")

with col1:
    start_date = st.date_input("Enter Start date", datetime.date(2025, 6, 1))
with col2:
    end_date = st.date_input("Enter End date", datetime.date(2025, 7, 1))

stoch_df = stock_data.history(start=start_date, end=end_date)

st.write(
    f"""
## {company_name} ({ticker_symbol})
    """
)
st.dataframe(stoch_df)
st.write(
    """
### Daily Closing Line chart
    """
)
st.line_chart(stoch_df.Close)
st.write(
    """
### Volume of Shares Traded
    """
)
st.line_chart(stoch_df.Volume)
