import pandas as pd

df = pd.DataFrame({'Item':['Soap','chacolates','books','pens','laptop','Mobile'],
                 'Quantity':[50,10,50,30,70,60],
                 'Price':[55,15,45,5,80,45],
                 'Sales':[3000,5000,4500,1000,500,150]})
import matplotlib 
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

# Histogram for Price
plt.figure(figsize=(8, 6))
plt.hist(df['Price'], bins=5, color='skyblue', edgecolor='black')
plt.title('Distribution of Price')
plt.xlabel('Price')
plt.ylabel('Frequency')

# Histogram for Quantity
plt.figure(figsize=(8, 6))
plt.hist(df['Quantity'], bins=5, color='lightgreen', edgecolor='black')
plt.title('Distribution of Quantity')
plt.xlabel('Quantity')
plt.ylabel('Frequency')
plt.show()