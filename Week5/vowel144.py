#!/usr/bin/env python
# coding: utf-8

# In[11]:


import csv


# In[12]:


file1=open("c:\sqlite3\csv\owel.txt","w")
v=["a\n","e\n","i\n","o\n","u\n"]


# In[13]:


file1.writelines(v)
file1.close()


# In[21]:


file2=open("c:\sqlite3\csv\owel.txt","r")
p=file2.readlines()
print(p)


# In[ ]:





# In[ ]:




