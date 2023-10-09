#!/usr/bin/env python
# coding: utf-8

# In[65]:


# Importing the libraries 
import numpy as np 
from scipy import optimize
import pandas
import csv
import matplotlib
import matplotlib.pyplot as plt

#Define the objective function
def objective(x, a, b, c, f): 
   return (a*x) + (b*x**2)+ (c*x**3) + f
  
# Importing the dataset 
dataframe = pd.read_csv('growth curve 2.0.csv') 
data = dataframe.values
print(data) 


# In[66]:


#Verify the dataset
x, y = data[:, 0], data[:, 1] 
print(x)
print(y)


# In[67]:


#Draw the scatter plot and start setting up the parameters for curve-fitting
plt.scatter(x, y)
popt, _= optimize.curve_fit(objective, x, y)
a, b, c, f = popt


# In[68]:


plt.scatter(x, y)

#Curve-fitting
x_line = np.arange(min(x), max(x), 1)
y_line = objective(x_line, a, b, c, f)
plt.plot(x_line, y_line, '--', color = 'red')
plt.show()
print(a, b, c, f) #Output the coefficients


# In[ ]:





# In[ ]:




