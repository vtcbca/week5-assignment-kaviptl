#!/usr/bin/env python
# coding: utf-8

# In[6]:


import csv


# In[7]:


file1=open("c:\sqlite3\csv\kavi144.txt","w")
l=["om\n","sai\n","ram\n"]


# In[8]:


file1.write("hello\n")
file1.writelines(l)
file1.close()


# In[9]:


file2=open("c:\sqlite3\csv\kavi144.txt","r")
op=file2.readlines()
print(op)


# In[ ]:




