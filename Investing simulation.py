#!/usr/bin/env python
# coding: utf-8

# In[ ]:


## starting with $10,000 and adding an additional $10,000 annually
##what is the probability that you will have at least $1,000,000 after 30 years of investing,
## with an expected return of 10%


# In[1]:


## import needed libaries 
import numpy as np
from pandas import Series, DataFrame
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
import locale
locale.setlocale(locale.LC_ALL, '')


# In[2]:


## start with a simple static appraoch
## Problem is this does not model real world. It is not realistic we earn 10% every year
startValue = 10000
time = 30
rate = 0.1
annualAdd = 10000


# In[3]:


for year in range(time):
    
    ##calculates ending balance
    endValue = startValue * (1 + rate) + annualAdd
    
    ##prints ending balance after every year
    print(locale.currency(endValue, grouping=True))
    
    ##set next starting balance equal to current balance
    startValue = endValue


# In[4]:


## next I added market volatility instead of a simple fixed rate of return. I kept expected rate of return at 10%
##I chose a 20% market volatility.  volatlity added or subtracted on top off expected rate at 10%
## so we could see a range of returns for the year from -10% to 30%

startValue = 10000
expected_return = 0.1
volatility = 0.2
time = 30
annualAdd = 10000
print("\tRate for Year", "\t\tEnding Balance".rjust(18))
for year in range(time):
    adjustedRate = np.random.normal(expected_return, volatility)
    endValue = startValue * (1 + adjustedRate) + annualAdd
    print("\t{}".ljust(10).format(round(adjustedRate,4)),
         "\t{}".rjust(15).format(locale.currency(endValue, grouping=True)))
    startValue = endValue


# In[5]:


## This is a loop to run the simulation done in the previous cell.  I did 10,000 iterations
## storing the results using Pandas DataFrame.  DataFrame will have 10,000 columns and 30 rows


sim = DataFrame()
iterations = 10000

for x in range(iterations):
    expected_return = 0.1
    volatility = 0.2
    time = 30
    startValue = 10000
    annualAdd = 10000
    runningTable = []
    for i in range(time):
        endValue = round(startValue * (1 + np.random.normal(expected_return,volatility)) + annualAdd,2)
        runningTable.append(endValue)
        startValue = endValue
        
    sim[x] = runningTable


# In[6]:


## now that I have 10000 simulations in a table.  I sliced out the first 10 simulations to see what the data looks like.
## columns are the simulation number, rows are the ending balance for the year 

first_ten = list(range(10))
sim[first_ten]


# In[ ]:




