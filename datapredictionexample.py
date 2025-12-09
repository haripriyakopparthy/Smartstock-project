import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

# Correct file path with XLSX extension
file_path = r'item_dataset.xlsx'

# Read Excel file
data = pd.read_excel(file_path)

# First 15 rows display
print("First 15 rows:")
print(data.head(15))

# Check for null values and replace with 0 if any
if data.isnull().any().any():
    replace = data.columns[data.isnull().any()]
    data[replace] = data[replace].fillna(0)
    print("\nData after filling nulls:")
    print(data)
else:
    print("\nNo null values found.")

# --- Example: Simple prediction (dummy) ---
# Suppose you want to predict total value = Price * Quantity
if 'Price' in data.columns and 'Quantity' in data.columns:
    data['Total_Value'] = data['Price'] * data['Quantity']
    print("\nData with Total_Value column:")
    print(data.head(15))
    
    # Plot example
    plt.figure(figsize=(8,5))
    plt.bar(data['Item'], data['Total_Value'], color='skyblue')
    plt.xlabel('Item')
    plt.ylabel('Total Value')
    plt.title('Total Value per Item')
    plt.xticks(rotation=45)
    plt.show()
else:
    print("Columns 'Price' or 'Quantity' not found for prediction.")