# -*- coding: utf-8 -*-
"""
Spyder Editor

 @author: anamcilie
 
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
path = r'D:\BM\DATA\PurpleAir\2_Ulaanbaatar monitors\Acceptable sensors\Monitors PurpleAir\Arkhangai_01 202108 202207'
data = pd.read_csv(path + '/Cleaned_Data_File_Arkhangai_01.csv')

# Exploratory Data Analysis

data.dtypes # find the datatypes of all variables
data.columns # list of all column names - original list
data.shape # Dimensions of original dataset (rows, columns)
print(data.head(10)) # first 10 rows of dataset
data.index # index - number of rows and columns
data.info() # information on datatypes and number of elements

# Convert the datatype of certain columns to float type 
data[['Datetime']] = data[['Datetime']].apply(pd.to_datetime)
# Convert the datatype of certain columns to float type 
data[['Temperature_F', 'PM2.5 ug/m3','Humidity_%']] = data[['Temperature_F', 'PM2.5 ug/m3','Humidity_%']].apply(pd.to_numeric)



############### Time Series ###################

# Line Plot - continous variables
#pm_conc = ['PM-1','PM-10','PM-2.5']
# Set the Date as Index
data['Datetime'] = pd.to_datetime(data['Datetime'])
data.index = data['Datetime']
del data['Datetime']
pm_conc = ['PM2.5 ug/m3']
plt.plot(data[pm_conc])
plt.xlabel('Datetime')
plt.ylabel('PM2.5 ug/m3')
plt.show()
plt.savefig(path + "\Timeseries_Zamiin tsagdaa_PLM.jpg")
    

# Time Series Analysis
data2 = data.set_index('Datetime')
data2.head(3)

data2['Month'] = data2.index.month
data2['Year'] = data2.index.year
data2.sample(30, random_state = 0)


# slicing and plotting at the same time
data2.loc['2021-08-01 00:00:00':'2021-09-30 23:59:00', 'PM2.5 ug/m3'].plot()
# save the cleaned data file to another .csv, in the same folder
data.to_csv(path + "\Season_Data_File.csv")


# store descriptive statistics in a different dataframe and .csv file
desc_stat = data.describe()
desc_stat.to_csv(path+'\Descriptive_Stats_Zamiin tsagdaa_PLM.csv')


# Basic Plots

data.boxplot()
plt.savefig(path + "\Boxplots_.jpg")

# Pair Plot
sns.pairplot(data)
plt.savefig(path + "\pairplot_Zamiin tsagdaa_PLM.jpg")



# Histogram
data.hist(figsize=(16, 20), bins=50, xlabelsize=8, ylabelsize=8)
plt.savefig(path + "\Histogram_Zamiin tsagdaa_PLM.jpg")



# mean values on a daily basis
#data2.resample('D').mean()
#data.to_csv(path + "\Daily avg_Arkhangai_01.csv")

