
#Series
import pandas as pd
data=pd.Series([10,20,30,40,50])
print(data)

import pandas as pd
data=pd.Series(['mohan','sai','bharath','chakri'])
print(data)

import pandas as pd
names = ["Alice", "Bob", "Charlie", "David", "Eva"]
name_series = pd.Series(names)
print(name_series)

import pandas as pd
data=pd.Series(['mohan','sai','bharath','chakri'],index=([10,11,12,13]))
print(data)

import pandas as pd

student_names = ["mohan", "sai", "Chakri", "raju", "bharath"]

index_values = [5 + i * 2 for i in range(len(student_names))]

student_series = pd.Series(student_names, index=index_values)

print(student_series)

import pandas as pd
freq=pd.Series(['neeraja','xyz','uvw','klm'],\
               index=[i for i in range(5,12,2)])
print(freq)

#Data Frame
import pandas as pd
df=pd.DataFrame({'item':['soap','chocolates','pens','books'],
                 'quantity' : [50,10,50,30],
                 'price':[55,15,45,5],
                 'sales':[100,200,50,300]})
print(df)

import pandas as pd
df=pd.DataFrame({'Item ':['Soap','chacolates','books','pens','mobiles','laptop'],
                 'Quantity ':[50,10,50,30,40,60],
                 'Price':[55,15,45,5,40,20]})
df['sales'] =[40,20,30,20,34,18]
#accessing or viewing the data
print(df)
print(df.head(3))
print(df.tail())
print(df.columns)
print(df.shape)
print(df.index)
print(df[0:3])

import pandas as pd
df=pd.DataFrame({'Item':['Soap','chacolates','books','pens','mobiles','laptop'],
                 'Quantity':[50,10,50,30,40,60],
                 'Price':[55,15,45,5,40,20]})
df['sales'] =[40,20,30,20,34,18]
print(df)
print("select row by iloc:\n",df.iloc[[0,1,2]])
print("select row by iloc:\n",df.loc[0,'sales'],"\n")
print(df[df['Quantity'] > 40])

import pandas as pd
df=pd.DataFrame({'Item':['Soap','chacolates','books','pens','laptop','Mobile'],
                 'Quantity':[50,10,50,30,70,60],
                 'Price':[55,15,45,5,80,45],
                 'Sales':[3000,5000,4500,1000,500,150]})
print("select row by loc:\n",df.loc[2,'Sales'],"\n")
print(df[(df['Quantity'] > 40) & (df['Sales'] > 3000)])

#Aggregate Functions
import pandas as pd
df=pd.DataFrame({'Item ':['Soap','chacolates','books','pens','laptop','Mobile'],
                                     'Quantity ':[50,10,50,30,70,60],
                                     'Price':[55,15,45,5,80,45],
                                     'Sales':[3000,5000,4500,1000,500,150]})
print(df)
print("Sum of Sales : ",df['Sales'].sum())
print("Count of Sales : ",df['Sales'].count())
print("Average of Sales : ",df['Sales'].mean())
print("Minimum of Sales : ",df['Sales'].min())
print("Min value: ",min(df['Sales']))
print("Max of Sales : ",df['Sales'].max())
print("Max value: ",max(df['Sales']))
print(df['Sales'].agg(['mean','min','max','count','sum']))

import pandas as pd
df=pd.DataFrame({'Item':['Soap','chacolates','books','pens','laptop','Mobile'],
                 'Quantity':[50,10,50,30,70,60],
                 'Price':[55,15,45,5,80,45],
                 'Sales':[3000,5000,4500,1000,500,150]})

df['lowStock'] = df['Quantity'] < 30
print(df)

#Sorting
import pandas as pd
df=pd.DataFrame({'Item':['Soap','chacolates','books','pens','laptop','Mobile'],
                 'Quantity':[50,10,50,30,70,60],
                 'Price':[55,15,45,5,80,45],
                 'Sales':[3000,5000,4500,1000,500,150]})

df['lowStock'] = df['Quantity'] < 30
#df = df.drop('Price', axis=1)

df_sorted = df.sort_values(by='Sales')
print(df_sorted)
df_sorted = df.sort_values(by='Price')
print(df_sorted)

import pandas as pd
df=pd.DataFrame({'Item ':['Soap','chacolates','books','pens','laptop','Mobile'],
                 'Quantity':[50,10,50,30,70,60],
                 'Price':[55,15,45,5,80,45],
                 'Sales':[3000,5000,4500,1000,500,150]})
print(df)
df_sorted = df.sort_values(by='Price', ascending=False)
print(df_sorted)

#Concating
import pandas as pd
df1=pd.DataFrame({'Item':['Detergent','Rice'],
                  'Quantity':[40,60]})
df2=pd.DataFrame({'Item':['Soap','Oil'],
                  'Quantity':[30,50]})
print(df1)
print(df2)
print(pd.concat([df1,df2]))

#Merging and Concat
import pandas as pd
df1=pd.DataFrame({'Item':['Detergent','Rice'],
                  'Quantity':[40,60],})

df2=pd.DataFrame({'Item':['Soap','Oil'],
                  'Quantity':[30,50]})

print("Concat vertical \n",pd.concat([df1,df2]))
print("Concat Horizontal \n",pd.concat([df1,df2],axis=1))

# Sorting by Sales
df_sorted_sales = df.sort_values(by='Sales', ascending=False)
print("\nDataFrame sorted by Sales (Descending):")
print(df_sorted_sales)

# Filtering for items with low stock
# Ensure the 'lowStock' column exists before filtering
if 'lowStock' not in df.columns:
    df['lowStock'] = df['Quantity'] < 30
low_stock_items = df[df['lowStock'] == True]
print("\nItems with low stock:")
print(low_stock_items)

# Filtering for items within a price range
price_range_items = df[(df['Price'] >= 10) & (df['Price'] <= 50)]
print("\nItems within price range (10-50):")
print(price_range_items)

# Dropping the 'lowStock' column
# Ensure the 'lowStock' column exists before dropping
if 'lowStock' in df.columns:
    df_no_lowstock = df.drop('lowStock', axis=1)
    print("\nDataFrame after dropping 'lowStock' column:")
    print(df_no_lowstock)
else:
    print("\n'lowStock' column not found in the DataFrame.")
    print(df)
    
# Calculating total sales
total_sales = df['Sales'].sum()
print(f"\nTotal Sales: {total_sales}")

# Calculating average price
average_price = df['Price'].mean()
print(f"Average Price: {average_price}")