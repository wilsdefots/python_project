#!/usr/bin/env python
# coding: utf-8

# In[85]:


get_ipython().system('pip install yfinance==0.1.67')
get_ipython().system('pip install nbformat==5.9.2')


# In[96]:


get_ipython().system('pip install dict')
get_ipython().system('pip install graph_object')


# In[98]:


import yfinance as yf
import pandas as pd
import requests
from bs4 import BeautifulSoup
import plotly.graph_objects as go
from plotly.subplots import make_subplots


# In[62]:


def make_graph(stock_data, revenue_data, stock):
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, subplot_titles=("Historical Share Price", "Historical Revenue"), vertical_spacing = .3)
    stock_data_specific = stock_data[stock_data.Date <= '2021--06-14']
    revenue_data_specific = revenue_data[revenue_data.Date <= '2021-04-30']
    fig.add_trace(go.Scatter(x=pd.to_datetime(stock_data_specific.Date, infer_datetime_format=True), y=stock_data_specific.Close.astype("float"), name="Share Price"), row=1, col=1)
    fig.add_trace(go.Scatter(x=pd.to_datetime(revenue_data_specific.Date, infer_datetime_format=True), y=revenue_data_specific.Revenue.astype("float"), name="Revenue"), row=2, col=1)
    fig.update_xaxes(title_text="Date", row=1, col=1)
    fig.update_xaxes(title_text="Date", row=2, col=1)
    fig.update_yaxes(title_text="Price ($US)", row=1, col=1)
    fig.update_yaxes(title_text="Revenue ($US Millions)", row=2, col=1)
    fig.update_layout(showlegend=False,
    height=900,
    title=stock,
    xaxis_rangeslider_visible=True)
    fig.show()


# In[48]:


#Question1
Tesla= yf.Ticker("TSLA")
tesla_data = Tesla.history(period="max")
tesla_data.reset_index(inplace=True)
tesla_data.head()


# In[54]:


#Question2
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/revenue.htm"
tesla_data = requests.get(url).text
tesla_revenue = pd.read_html(url,match='Tesla Quarterly Revenue')[0]
new_names = {'Tesla Quarterly Revenue (Millions of US $)':'date',
                 'Tesla Quarterly Revenue (Millions of US $).1':'Revenue'}
tesla_revenue.rename(columns=new_names,inplace=True)
tesla_revenue.tail()


# In[55]:


tesla_revenue["Revenue"]=tesla_revenue["Revenue"].str.replace(",| \ $","")


# In[56]:


#Question2
read_html_pandas_data = pd.read_html(url)
tesla_revenue= read_html_pandas_data[1]
new_names = {'Tesla Quarterly Revenue (Millions of US $)':'date',
                 'Tesla Quarterly Revenue (Millions of US $).1':'Revenue'}
tesla_revenue.rename(columns=new_names,inplace=True)
tesla_revenue["Revenue"] = tesla_revenue["Revenue"].str.replace("$","").replace(",","")
tesla_revenue.tail()


# In[57]:


tesla_revenue["Revenue"] = tesla_revenue["Revenue"].str.replace("$","").replace(",","")
tesla_revenue.tail()


# In[58]:


#Question3
Gamestop = yf.Ticker("GME")
gme_data = Gamestop.history(period="max")
gme_data.reset_index(inplace=True)
gme_data.head()


# In[59]:


#Question4
url2 = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/stock.html"
gme_data  = requests.get(url2).text
gme_revenue = pd.read_html(url2, match='GameStop Quarterly Revenue')[0]
new_names2 = {'GameStop Quarterly Revenue (Millions of US $)':'date',
                 'GameStop Quarterly Revenue (Millions of US $).1':'Revenue'}
gme_revenue.rename(columns=new_names2,inplace=True)
gme_revenue["Revenue"] = gamestop_revenue["Revenue"].str.replace("$","").replace(",","")
gme_revenue.tail()


# In[60]:


#Question5
make_graph(tesla_data, tesla_revenue, 'Tesla')


# In[63]:


#Question6
make_graph(gme_data, gme_revenue, 'GameStop')


# In[ ]:





# In[ ]:





# In[ ]:




