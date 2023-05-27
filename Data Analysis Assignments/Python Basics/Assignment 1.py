#!/usr/bin/env python
# coding: utf-8

# ### 1. Write a Python program to print "Hello Python"?

# In[1]:


print("Hello Python")


# ### 2. Write a Python program to do arithmetical operations addition and division.?
# 

# In[2]:


# Taking input from users

a= int(input("Enter any number a:  "))
b= int(input("Enter any number b: "))
c= int(input("Enter any number c: "))
d= int(input("Enter any number d: "))

# for addition 
print("addition =",a+b)

# for division 

if c>0 :
    print("Division =",c/d)
else:
    print("division error")


# ### 3. Write a Python program to find the area of a triangle?
# 

# In[3]:


# Taking input from users

height= int(input("Enter height :  "))
base= int(input("Enter base :  "))

area=(1/2)*base*height

print("area of triange is: ",area)


# ### 4. Write a Python program to swap two variables?
# 

# In[6]:


a= 5
b=6
y=a 
a=b
b=y
print(a,b)

