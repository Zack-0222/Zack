#!/usr/bin/env python
# coding: utf-8

# Step1: getting to know notebooks

# In[1]:


# this cell contains code
3 + 7


# step2: variables

# In[ ]:


# variable is name for a value/some infomation


# In[3]:


age = 31


# In[4]:


print(age)


# In[5]:


my_age = 28


# In[6]:


print(my_age)


# In[7]:


name = 'Zackkkk'


# In[8]:


print(name)


# In[9]:


print('my name is:', name)


# In[10]:


print('my name is:', name,'and i am',my_age)


# In[11]:


your_name = 'balala'


# In[12]:


print(your_name)


# In[13]:


print('in three years i will be',my_age+3)


# In[14]:


my_age_plus3 = my_age +3


# In[15]:


print('in three years i will be',my_age_plus3)


# In[16]:


# notebooks do return value without printing 
len(your_name)


# In[17]:


# not in nootbooks
print(len(your_name))


# In[19]:


your_name[1]


# In[20]:


your_name[0:3]


# In[21]:


# what are the value assigned to the variables :x ,y, swap

x = 1
y = 3
swap = x
x = y
y = swap


# In[23]:


print('x=',x,'y=',y,'swap=',swap)


# # data types and type conversion
# ## common data types: integers, floats, strings
# ## convert one to the other
# 

# In[24]:


52


# In[25]:


type(52)


# In[26]:


type(age)


# In[27]:


fitness = 'average'
type(fitness)


# In[28]:


fitness = 'average + 2'
type(fitness)


# In[30]:


first_name = 'Zack'
last_name = 'Yo'
print(first_name+last_name)


# In[31]:


print(first_name +'_' +last_name)


# In[32]:


print(first_name * 10)


# In[33]:


# convert integer to string so we can get number of digits
len(str(52))


# In[34]:


# convert string to integer so we can add
age = '36'
age_plus3 = int(age) + 3
print(age_plus3)
type(age_plus3)


# In[38]:


# floats: decimal number
temp = 37.4
type(temp)
print(temp + 2)
print(temp/2)
type(temp + 2)


# In[39]:


# convert integer/string to float
age = 36
type(age)
float(age)


# In[40]:


ph = '7.4'
type(ph)


# In[42]:


float_ph = float(ph)


# In[43]:


print(float_ph)


# In[45]:


# exersize

first = 1.0
second ='1'
third = '1.1'

# which operation will reture the float 2.0?
print(first + float (second)) # correct
print(float(second) + float (third)) # 2.1 (float)
print(first+int(third)) # raise error (cannot do float + str)
print(first+int(float(third))) # correct
print(int(first)+ int(float(third))) # 2 (integer)
print(2.0*second) # cannot mutiply string with float


# In[ ]:




