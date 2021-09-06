import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

st.sidebar.header("Navigate")
option=st.sidebar.selectbox("Graph Selector", ('Home','OHLC','Candlestick','Vertex Line','Colored Bar'))

st.header(option)

if option=='Home':
    st.title("OHLC ENGINE - Dashboard")
    st.header("Project Under Northern Trust by Group 16")
    st.image("https://cdn.northerntrust.com/pws/nt/images/social-media/nt-2linestacked-logo-1200x628.png",width=200)

if option=='OHLC':
    dfm= pd.read_csv('stockdata.csv')
    sto=st.selectbox("Select Stock",('AAPL','MSFT','GOOG','GOOGL','ADSK','AMZN','FB','TSLA','TSM','NVDA','V','JPM','JNJ','BABA','WMT','UNH','BAC','MA','PG','HD'))
    st.text(sto)
    if sto=='AAPL':
        df1 = dfm[dfm['symbol'] == 'AAPL'].copy()
    if sto=='MSFT':
        df1 = dfm[dfm['symbol'] == 'MSFT'].copy()
    if sto=='GOOG':
        df1 = dfm[dfm['symbol'] == 'GOOG'].copy()
    if sto=='GOOGL':
        df1 = dfm[dfm['symbol'] == 'GOOGL'].copy()
    if sto=='ADSK':
        df1 = dfm[dfm['symbol'] == 'ADSK'].copy()
    if sto=='AMZN':
        df1 = dfm[dfm['symbol'] == 'AMZN'].copy()
    if sto=='FB':
        df1 = dfm[dfm['symbol'] == 'FB'].copy()
    if sto=='TSLA':
        df1 = dfm[dfm['symbol'] == 'TSLA'].copy()
    if sto=='TSM':
        df1 = dfm[dfm['symbol'] == 'TSM'].copy()
    if sto=='NVDA':
        df1 = dfm[dfm['symbol'] == 'NVDA'].copy()
    if sto=='V':
        df1 = dfm[dfm['symbol'] == 'V'].copy()
    if sto=='JPM':
        df1 = dfm[dfm['symbol'] == 'JPM'].copy()
    if sto=='JNJ':
        df1 = dfm[dfm['symbol'] == 'JNJ'].copy()
    if sto=='BABA':
        df1 = dfm[dfm['symbol'] == 'BABA'].copy()
    if sto=='WMT':
        df1 = dfm[dfm['symbol'] == 'WMT'].copy()
    if sto=='UNH':
        df1 = dfm[dfm['symbol'] == 'UNH'].copy()
    if sto=='BAC':
        df1 = dfm[dfm['symbol'] == 'BAC'].copy()
    if sto=='MA':
        df1 = dfm[dfm['symbol'] == 'MA'].copy()
    if sto=='PG':
        df1 = dfm[dfm['symbol'] == 'PG'].copy()
    if sto=='HD':
        df1 = dfm[dfm['symbol'] == 'HD'].copy()
    fig = go.Figure(data=go.Ohlc(x=df1['date'],
                    open=df1['open'],
                    high=df1['high'],
                    low=df1['low'],
                    close=df1['close']))
    
    fig.update_layout(
    title=f"{sto} stock Prizes",
    yaxis_title='Stock Price (USD per Shares)')
    fig.update_layout(height=700)

    st.plotly_chart(fig, use_container_width=True)

if option=='Candlestick':
    symbol = st.sidebar.text_input("Symbol",value='APPL', max_chars=5, type='default')
    dfm= pd.read_csv('stockdata.csv')
    df = dfm[dfm['symbol'] == 'AAPL'].copy()
    fig = go.Figure(data=go.Candlestick(x=df['date'],
                    open=df['open'],
                    high=df['high'],
                    low=df['low'],
                    close=df['close']))
    fig.update_layout(
    title=f"{symbol} stock Prizes",
    yaxis_title='Stock Price (USD per Shares)')
    fig.update_layout(height=700)

    st.plotly_chart(fig, use_container_width=True)

if option=='Vertex Line':
    sel=st.selectbox("Value",('High','Low','Open','Close'))
    st.subheader(sel)
    sto=st.selectbox("Select Stock",('AAPL','MSFT','GOOG','GOOGL','ADSK','AMZN','FB','TSLA','TSM','NVDA','V','JPM','JNJ','BABA','WMT','UNH','BAC','MA','PG','HD','ALL'))
    st.text(sto)
    dfm= pd.read_csv('stockdata.csv')
    if sto=='AAPL':
        df1 = dfm[dfm['symbol'] == 'AAPL'].copy()
    if sto=='MSFT':
        df1 = dfm[dfm['symbol'] == 'MSFT'].copy()
    if sto=='GOOG':
        df1 = dfm[dfm['symbol'] == 'GOOG'].copy()
    if sto=='GOOGL':
        df1 = dfm[dfm['symbol'] == 'GOOGL'].copy()
    if sto=='ADSK':
        df1 = dfm[dfm['symbol'] == 'ADSK'].copy()
    if sto=='AMZN':
        df1 = dfm[dfm['symbol'] == 'AMZN'].copy()
    if sto=='FB':
        df1 = dfm[dfm['symbol'] == 'FB'].copy()
    if sto=='TSLA':
        df1 = dfm[dfm['symbol'] == 'TSLA'].copy()
    if sto=='TSM':
        df1 = dfm[dfm['symbol'] == 'TSM'].copy()
    if sto=='NVDA':
        df1 = dfm[dfm['symbol'] == 'NVDA'].copy()
    if sto=='V':
        df1 = dfm[dfm['symbol'] == 'V'].copy()
    if sto=='JPM':
        df1 = dfm[dfm['symbol'] == 'JPM'].copy()
    if sto=='JNJ':
        df1 = dfm[dfm['symbol'] == 'JNJ'].copy()
    if sto=='BABA':
        df1 = dfm[dfm['symbol'] == 'BABA'].copy()
    if sto=='WMT':
        df1 = dfm[dfm['symbol'] == 'WMT'].copy()
    if sto=='UNH':
        df1 = dfm[dfm['symbol'] == 'UNH'].copy()
    if sto=='BAC':
        df1 = dfm[dfm['symbol'] == 'BAC'].copy()
    if sto=='MA':
        df1 = dfm[dfm['symbol'] == 'MA'].copy()
    if sto=='PG':
        df1 = dfm[dfm['symbol'] == 'PG'].copy()
    if sto=='HD':
        df1 = dfm[dfm['symbol'] == 'HD'].copy()
    if sto=='ALL':
        df1=dfm.copy()
    
    if sel=='High':
        fig = px.line(df1,x=df1['date'],y=df1['high'],color=df1['symbol'],title='High Stock Prices',markers= True)
        fig.update_layout(height=700)
        st.plotly_chart(fig, use_container_width=True)
    if sel=='Low':
        fig = px.line(df1,x=df1['date'],y=df1['low'],color=df1['symbol'],title='Low Stock Prices',markers= True)
        fig.update_layout(height=700)
        st.plotly_chart(fig, use_container_width=True)
    if sel=='Open':
        fig = px.line(df1,x=df1['date'],y=df1['open'],color=df1['symbol'],title='Opening Stock Prices',markers= True)
        fig.update_layout(height=700)
        st.plotly_chart(fig, use_container_width=True)
    if sel=='Close':
        fig = px.line(df1,x=df1['date'],y=df1['high'],color=df1['symbol'],title='Closing Stock Prices',markers= True)
        fig.update_layout(height=700)
        st.plotly_chart(fig, use_container_width=True)

if option=='Colored Bar':
    dfm= pd.read_csv('D:stockdata.csv')
    sto=st.selectbox("Select Stock",('AAPL','MSFT','GOOG','GOOGL','ADSK','AMZN','FB','TSLA','TSM','NVDA','V','JPM','JNJ','BABA','WMT','UNH','BAC','MA','PG','HD'))
    st.text(sto)
    if sto=='AAPL':
        df1 = dfm[dfm['symbol'] == 'AAPL'].copy()
    if sto=='MSFT':
        df1 = dfm[dfm['symbol'] == 'MSFT'].copy()
    if sto=='GOOG':
        df1 = dfm[dfm['symbol'] == 'GOOG'].copy()
    if sto=='GOOGL':
        df1 = dfm[dfm['symbol'] == 'GOOGL'].copy()
    if sto=='ADSK':
        df1 = dfm[dfm['symbol'] == 'ADSK'].copy()
    if sto=='AMZN':
        df1 = dfm[dfm['symbol'] == 'AMZN'].copy()
    if sto=='FB':
        df1 = dfm[dfm['symbol'] == 'FB'].copy()
    if sto=='TSLA':
        df1 = dfm[dfm['symbol'] == 'TSLA'].copy()
    if sto=='TSM':
        df1 = dfm[dfm['symbol'] == 'TSM'].copy()
    if sto=='NVDA':
        df1 = dfm[dfm['symbol'] == 'NVDA'].copy()
    if sto=='V':
        df1 = dfm[dfm['symbol'] == 'V'].copy()
    if sto=='JPM':
        df1 = dfm[dfm['symbol'] == 'JPM'].copy()
    if sto=='JNJ':
        df1 = dfm[dfm['symbol'] == 'JNJ'].copy()
    if sto=='BABA':
        df1 = dfm[dfm['symbol'] == 'BABA'].copy()
    if sto=='WMT':
        df1 = dfm[dfm['symbol'] == 'WMT'].copy()
    if sto=='UNH':
        df1 = dfm[dfm['symbol'] == 'UNH'].copy()
    if sto=='BAC':
        df1 = dfm[dfm['symbol'] == 'BAC'].copy()
    if sto=='MA':
        df1 = dfm[dfm['symbol'] == 'MA'].copy()
    if sto=='PG':
        df1 = dfm[dfm['symbol'] == 'PG'].copy()
    if sto=='HD':
        df1 = dfm[dfm['symbol'] == 'HD'].copy()
    fig = go.Figure(data=[
    go.Bar(name='Open', x=df1['date'], y=df1['open']),
    go.Bar(name='Close', x=df1['date'], y=df1['close']),
    go.Bar(name='High', x=df1['date'], y=df1['high']),
    go.Bar(name='Low', x=df1['date'], y=df1['low'])
    ])
    fig.update_layout(
    title=f"{sto} Stock",)
    fig.update_layout(barmode='stack')
    st.plotly_chart(fig, use_container_width=True)