# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 20:41:14 2019

@author: kshamaj
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 19:00:21 2019

@author: kshamaj
"""

pwd

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns
#data cleaning............

#loading data
df=pd.read_csv('googleplaystore.csv')
df.columns
df.dtypes

df.columns
df.dtypes
#finding null values in the data
df.isnull().sum()
#dropping null values
df1=df.dropna(subset=['Rating','Type','ContentRating','AndroidVer','CurrentVer'])
df1.isnull().sum()
#data cleaning
df1['Price']=df1['Price'].apply(lambda x : x.strip('$'))

df1['Installs']=df1['Installs'].apply(lambda t : t.strip('+').replace(',', ''))


df1['Size']=df1['Size'].apply(lambda x:x.strip('M'))
df1['Size']=df1['Size'].apply(lambda x:x.strip('k'))
df1[df1['Size'] == 'Varies with device'] = 0

df1['Type']=pd.get_dummies(df1['Type'])
df1.columns
df1.dtypes
df1.ContentRating.unique()

#making the ready to apply ,model
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
LE=LabelEncoder()

df1['App'] = LE.fit_transform(df1['App'])

df1['ContentRating']= LE.fit_transform(df1['ContentRating'])



CategoryList = df1['Category'].unique().tolist() 
CategoryList = ['cat_' + word for word in CategoryList]
df1 = pd.concat([df1, pd.get_dummies(df1['Category'], prefix='cat')], axis=1)

df1.to_csv( "clean_data.csv", index=False, encoding='utf-8-sig')


df1.dtypes
#converting the data types
df1["Size"] = df1.Size.astype(float)
df1["Installs"] = df1.Installs.astype(int)
df1['Price']=df1.Price.astype(float)
df1['Reviews']=df1.Reviews.astype(int)

df1.to_csv( "clean_data.csv", index=False, encoding='utf-8-sig')



