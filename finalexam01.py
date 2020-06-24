#!/usr/bin/env python
# coding: utf-8

# In[40]:


def pi(a):
    ans = 0.0
    i = 1
    while i <= a:
        ans += pow(-1,(i+1))/(2*i-1)
        i = i+1
    return 4*ans

i = 1
print('i         m(i)')
while i <= 901:
    print('{0}       {1}'.format(i, pi(i)))
    i += 100

