# -*- coding: utf-8 -*-
"""

@author: anamc
"""



import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
from datetime import datetime
import warnings                   # To ignore the warnings
warnings.filterwarnings("ignore")
import seaborn as sns
sns.set_style("white")
plt.style.use("seaborn")
# Use seaborn style defaults and set the default figure size
sns.set(rc={'figure.figsize':(14, 8)})
plt.rcParams['axes.labelsize'] = 16
plt.rcParams['axes.labelweight'] = 'bold'
plt.rcParams['axes.titlesize'] = 16
plt.rcParams['axes.titleweight'] = 'bold'
# sns.set() # setting to default settings
# plt.rcParams # set default matplotlib settings

# finding the current directory
abs_path = os.getcwd()
abs_path

# change to desired folder where .csv file is present - Use forward backslash
path = r'D:\Dropbox\Dropbox\A_CESEP Ana Ilie\Data Science AQ\AQ\BM\DATA\Validation\DATA Validation'

######        reference or DustTrack in this case      ##############
data_reference = pd.read_csv(path + '\Reference.csv')

######        IQ AirVisual Monitor (considered short as D3)         ##############
data_D3 = pd.read_csv(path + '/XLJAT9X_every_min.csv')


data_reference.info()
data_D3.info()


# Timestamp needs to be converted to datetime object (for time series manipulations)
data_reference['Datetime'] = pd.to_datetime(data_reference['Datetime'])
data_D3['Datetime'] = pd.to_datetime(data_D3['Datetime'])

data_merged = pd.merge(data_D3, data_reference, how='inner', on='Datetime')
data_merged.info()

#data_merged.to_csv(path + "\Output V_chamber&Vb_D3_Merged_Clean_File.csv")
#path

# Linear Regression 
from sklearn.linear_model import LinearRegression
X = data_merged['PM2_5(ug/m3)_y'].values
Y = data_merged['PM2_5(ug/m3)_x'].values
X = X.reshape(-1,1)
Y = Y.reshape(-1,1)

lin_regressor = LinearRegression()  # create object for the class
lin_regressor.fit(X, Y)  # perform linear regression
Y_pred = lin_regressor.predict(X)  # make predictions
r_sq = lin_regressor.score(X,Y) # R-square
coeff = lin_regressor.coef_
intercept = lin_regressor.intercept_

plt.scatter(X, Y, color = 'blue')
plt.plot(X, Y_pred, color='red')
plt.xlim(0)
plt.ylim(0)
plt.xlabel('PM2_5(ug/m3)  reference')
plt.ylabel('PM2_5(ug/m3) IQ AirVisual')
plt.title('Reference vs IQ AirVisual XLJAT9X')
#plt.text(X.min(),Y.max(), 'Equation: y = %0.2f x + (%0.2f)'% (coeff, intercept), bbox=dict(facecolor='white', alpha=0.8))
plt.text(X.min(),Y.max()-1,'R-squared = %0.2f' % r_sq, bbox=dict(facecolor='white', alpha=0.8))
plt.savefig(path+'\Linear Regression XLJAT9X.png', dpi=300, bbox_inches='tight')

plt.show()




























