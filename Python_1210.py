#!/usr/bin/env python
# coding: utf-8

# In[1]:


n=7
c=0
while(n):
    if(n>5):
        c=c+n-1
        n=n-1
    else:
        break
print(n)
print(c)


# In[2]:


str1="hello"
c=0
for x in str1:
   if(x!="l"):
       c=c+1
   else:
       pass
print(c)


# In[6]:


for i in range(0,2,-1):
    print("Hello")

