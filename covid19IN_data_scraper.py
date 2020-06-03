# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 21:37:50 2020

@author: Home
"""


import requests
import pandas as pd

url = 'https://www.mohfw.gov.in/'
html = requests.get(url).content
df_list = pd.read_html(html)
df = df_list[-1]
print(df)

df.to_csv("data.csv", index=False)

df = pd.read_csv('data.csv')

#df.drop(df.tail(4).index,inplace = True)
#df.drop(["37","38","39","40"].index, inplace = True)
df_out = df.iloc[:37]

df_out.to_csv("data_cleaned.csv", index=False)