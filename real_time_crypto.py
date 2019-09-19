#!/usr/bin/env python
# coding: utf-8

# In[35]:


import requests
from datetime import datetime


# In[2]:


TICKER_API_URL="https://api.coinmarketcap.com/v1/ticker/"


# In[29]:


def latest_price(crypto):
    response = requests.get(TICKER_API_URL+crypto)
    response_json = response.json()
    return float(response_json[0]['price_usd'])
            


# In[10]:


latest_price('bitcoin')


# In[33]:


threshold=1000


# In[ ]:


def main():


    last_price=-1
    while True:
        crypto='bitcoin'
        price=latest_price(crypto)
        if price<threshold:
            print('price is below than your threshold')
        now=datetime.now()
        now.strftime('%y-%m-%d %h:%m')
    if price!=last_price:
        print('bitcoin price:',price)
        last_price=price


# main()

# In[ ]:


main()


# In[ ]:




