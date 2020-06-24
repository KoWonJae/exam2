#!/usr/bin/env python
# coding: utf-8

# In[45]:


class Point:
    __x = 0
    __y = 0
            
    def __init__(self, a, b):
        self.x = a
        self.y = b
    
    def __add__(self, other):
        num = other.x
        num2 = other.y
        self.x = self.x + num
        self.y = self.y + num2
        return self.x, self.y
        
    
    def distance(self, another):
        num = pow(self.x - another.x, 2) + pow(self.y - another.y, 2)
        num2 = pow(num, 0.5)
        return num2
        

p1 = Point(1,1)     
p2 = Point(2,2)
print('add answer')
print(p1 + p2)

print('distance')
a = p1.distance(p2)
print(a)

