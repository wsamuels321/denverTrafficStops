#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt

dt = pd.read_csv("C:/Users/wsamuels/Python Projects/DataCSVs/Traff_stops.csv")


# In[8]:


len(dt)


# In[34]:


dt.head(10)


# In[9]:


list(dt)


# In[43]:


nh = dt['NEIGHBORHOOD_NAME'].value_counts()
probs = dt['PRIORITY_DESCRIPTION']
addr = dt['ADDRESS']
timeOfDay = dt['TIME_PHONEPICKUP']

#g = datetime.strptime(timeOfDay[5], '%Y-%m-%d %H:%M:%S.%f')
#timeOfDay[5].find(".")


# In[44]:


timeFormat = [] 
for x in timeOfDay:
    if x.find(".")>-1:
        timeFormat.append(datetime.strptime(x, '%Y-%m-%d %H:%M:%S.%f'))
    else:
        timeFormat.append(datetime.strptime(x, '%Y-%m-%d %H:%M:%S'))


# In[73]:


hour = []
for h in timeFormat:
    hour.append(str(h.hour))
hrFrame = pd.DataFrame({'hr':hour})
fr = hrFrame['hr'].value_counts()
g = fr.plot(kind='bar', figsize=(15,10), title='Traffic stops by Hour')
gif = g.get_figure()
gif.savefig('stopsHR.pdf')


# In[31]:


nh.head(1)


# In[33]:


probs


# In[21]:


plotDF= nh[:10]


# In[22]:


plotDF.plot(kind='bar')


# In[10]:


q =nh.plot(kind='bar', figsize=(30,10), title='Traffic stops per neighborhood')


# In[21]:


fig = q.get_figure()
fig.savefig('stops.pdf')


# In[ ]:




