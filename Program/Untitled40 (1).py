#!/usr/bin/env python
# coding: utf-8

# ##9.  Create text file on python by taking input from user. Read Python.txt file and Print it in Reverse. 

# In[ ]:


f=open("D:\\23BCA269\\sqlite3\\data\\python.txt","w")


# In[2]:


line=[]
while True:
    l=input()
    if l:
        line.append(l+'\n')
    else:
        break
python='\n'.join(line)


# In[3]:


f.close()


# In[4]:


f=open("D:\\23BCA269\\sqlite3\\data\\python.txt","r")


# In[5]:


for line in reversed(python):
    print(line)


# In[6]:


f.close()


# In[ ]:




