import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
#sample data
x=np.arange(1,11)
y=np.random.randint(10,100,size=10)
#LINE Plot
plt.figure(figsize=(6,4))
plt.plot(x,y,marker='o',color='b',linestyle='--',label='line plot')
plt.title('Line plot example')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.legend(loc='upper right')
#Bar Chat
plt.figure(figsize=(6,4))
plt.bar(x,y,color='orange')
plt.title('Bar plot example')
plt.xlabel('Bar x-axis')
plt.ylabel('Bar y-axis')
# Scatter Chart
plt.figure(figsize=(6,6))
plt.scatter(x,y,color='blue')
plt.title('Scatter plot example')
plt.xlabel('Scatter x-axis')
plt.ylabel('Scatter y-axis')
plt.show()