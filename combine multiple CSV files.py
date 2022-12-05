# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 19:51:08 2022

@author: anamc
"""


import os
import glob
import pandas as pd
os.chdir("D:/Dropbox/Dropbox/A_CESEP Ana Ilie/Data Science AQ/AQ/BM/DATA/IQair VisualAir/2_Ulaanbaatar monitors/IQair Visual monitors/35r surguuli/csv")


#find all csv files in the folder
#use glob pattern matching -> extension = 'csv'
#save result in list -> all_filenames
extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
print(all_filenames);


#combine all files in the list
combined_csv = pd.concat(map(pd.read_csv, all_filenames), ignore_index=True)
#export to csv
combined_csv.to_csv( "combined_csv.csv", index=False, encoding='utf-8-sig')










