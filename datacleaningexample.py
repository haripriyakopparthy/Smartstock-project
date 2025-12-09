import pandas as pd
import numpy as np
import matplotlib 
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


#Read excel file
file_path=r'item_dataset.xlsx'
data=pd.read_excel(file_path)
print("first 15 rows")
print(data.head(15))
#clean columns
data.columns=data.columns.str.strip().str.lower().str.replace(" ","_")
col_to_clean=['quantity']
data['quantity']=(
    data['quantity'].replace([""," ","NA","N/A"],np.nan)
)
# convert to numeric
data['quantity']=pd.to_numeric(data['quantity'],errors='coerce')

data['quantity']=data['quantity'].fillna(0).astype(int)
data['quantity']=data['quantity'].fillna(0).astype(int)
print(data)

