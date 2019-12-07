#!/usr/bin/env python
# coding: utf-8

# In[2]:


import os


# In[3]:


os.getcwd()


# In[4]:


os.mkdir("paper")


# In[7]:


lista = os.listdir("ddd")


# In[10]:


lista_s = []
for i in lista:
    lista_s.append(i.split(".")[0])


# In[11]:


print(lista_s)


# In[14]:


varia = ["dd", "prote", "liga", "rio"]


# In[16]:


os.chdir("paper")


# In[25]:


os.getcwd()


# In[24]:


os.chdir("..")


# In[26]:


for i in lista_s:
    os.mkdir(i)
    os.chdir(i)
    for k in varia:
        os.mkdir(k)
    os.chdir("..")


# In[ ]:




