

"""

@author: anamc
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
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
path = r'D:BM\DATA\Validation\DATA Validation\Merged files'
data = pd.read_csv(path+'/TVUM769_Reference_Merged_File.csv')

data.info()

from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from math import sqrt

x1 = data['PM2_5(ug/m3) TVUM769']
ref_port = data['PM2_5(ug/m3) ref']

# list to store results
results_df = [None] * 30

import scipy
def rsquared(x, y):
    """ Return R^2 where x and y are array-like."""
    slope, intercept, r_value, p_value, std_err = scipy.stats.linregress(x, y)
    return r_value**2

# r2
results_df[0] = rsquared(x1, ref_port)


print('\n Coefficient of Determination - R2 for Port1: ', results_df[0])


# mean squared error - mse
results_df[1] = mean_squared_error(x1, ref_port)

print('\n Mean Squared Error - MSE for Port1: ', results_df[1])


# root mean squared error - rmse
results_df[2] = sqrt(mean_squared_error(x1, ref_port))

print('\n Root Mean Squared Error - RMSE for Port1: ', results_df[2])


# absolute mean error - mae
results_df[3] = mean_absolute_error(x1, ref_port)

print('\n Mean Absolute Error - MAE for Port1: ', results_df[3])


# absolute mean bias error - mbe
results_df[4] = abs(np.mean(x1) - np.mean(ref_port))

print('\n Mean Bias Error - MBE for Port1:', results_df[4])

def nrmse(actual, reference):
    """ Normalized Mean Squared Error """
    return np.sum(np.square(actual-reference))/np.sum(np.square(actual - actual.mean()))

results_df[5] = nrmse(x1,ref_port)

print('\n Normalized Mean Square Error - NMSE for Port1:', results_df[5])


#df = pd.DataFrame(results_df, columns=['r2_port1', 'r2_port2', 'r2_port3', 'r2_port4', 'r2_port5'])
df = pd.DataFrame(results_df)
df = df.T
df.T.to_csv(path+'/TVUM769 statistical validation results.csv', index=False)






































