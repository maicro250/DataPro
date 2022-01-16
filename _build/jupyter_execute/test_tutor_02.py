#!/usr/bin/env python
# coding: utf-8

# **本习题由李政创建，转载及其他形式合作请与我们联系（微信号`maicro42`)，未经授权严禁搬运及二次创作，侵权必究！**

# # numpy基本操作练习

# ## 导入numpy，并查看其版本

# In[1]:


import numpy as np
#print(np.__version__)


# ## 题目1：创建一个三行三列，元素全是1的矩阵。

# In[2]:


#np.array([[ 0., 0., 0.],
#          [ 0., 0., 0.],
#          [ 0., 0., 0.]])


# ## 题目2：创建5阶单位矩阵

# In[3]:


#result = np.diag([1,1,1,1,1])
#result


# ## 题目3：生成8行8列的二维数组，值为1-999随机数

# In[4]:


#data = np.random.randint(1, 999, [8, 8])
#data


# ## 题目4：找到每列的最大值

# In[5]:


#np.amax(data, axis=0)


# ## 题目5：找到每行的最大值

# In[6]:


#np.amin(data, axis=1)


# In[ ]:




