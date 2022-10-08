# -*- coding: utf-8 -*-
"""

@author: anamc
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
from datetime import datetime
from pandas import Series        # To work on series
import statsmodels
import warnings                   # To ignore the warnings
warnings.filterwarnings("ignore")
import seaborn as sns
sns.set_style("white")
plt.style.use("seaborn")
# Use seaborn style defaults and set the default figure size
sns.set(rc={'figure.figsize':(14, 8)})

# sns.set() # setting to default settings
# plt.rcParams # set default matplotlib settings


# finding the current directory
abs_path = os.getcwd()
abs_path

# change to desired folder where .csv file is present - Use forward backslash
path = r'D:\BM\DATA\IQair VisualAir\35r surguuli'
data = pd.read_csv(path + '/historical_hourly_data_GASYTU6.csv')

# Exploratory Data Analysis
data.dtypes # find the datatypes of all variables
data.columns # list of all column names - original list
data.shape # Dimensions of original dataset (rows, columns)
print(data.head(10)) # first 10 rows of dataset
data.index # index - number of rows and columns
data.info() # information on datatypes and number of elements

# store descriptive statistics in a different dataframe and .csv file
#desc_stat = data.describe()
#desc_stat.to_csv(path+'\Descriptive_Stats.csv')
#print(desc_stat)

# Convert the datatype of certain columns to float type 
data[['Datetime']] = data[['Datetime']].apply(pd.to_datetime)
    
#setting xticklabels
week = ['mon','tue','wed','thu','fri','sat','sun']
months = ['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']

data.info() # information on datatypes and number of elements

#  dropping Nan values
data = data.dropna()

#data = data.drop(columns=['Temperature_F'], axis = 1)

# Saving the cleaned file into the same folder
data.to_csv('bayan-Ulgii_01 (outside)_Clean.csv', index=False)