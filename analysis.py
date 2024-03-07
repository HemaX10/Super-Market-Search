import pandas as pd 
import glob
import os


# # first problem

# #getting all files and read them 

csv_files = [file for file in os.listdir('E:\engenrring Hema\FYE\python course\pandas\problems\Pandas-Data-Science-Tasks-master\SalesAnalysis\Sales_Data\sales')]

dfs = []
for file in csv_files :
    df = pd.read_csv(f'E:\engenrring Hema\FYE\python course\pandas\problems\Pandas-Data-Science-Tasks-master\SalesAnalysis\Sales_Data\sales\{file}')
    dfs.append(df)

allData = pd.concat(dfs, ignore_index=True)

allData.to_csv('allData.csv' , index=False)



