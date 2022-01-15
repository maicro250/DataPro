#!/usr/bin/env python
# coding: utf-8

# **本习题由李政创建，转载及其他形式合作请与我们联系（微信号`maicro42`)，未经授权严禁搬运及二次创作，侵权必究！**

# # matplotlib、numpy基本操作练习

# ## 导入基础模块：matplotlib、mpl_toolkits、numpy。

# In[1]:


import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np


# ## 示例1：初始化3D图形显示区，并调用numpy生成数据。

# In[2]:


get_ipython().run_line_magic('matplotlib', 'notebook')


# In[3]:


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
theta = np.linspace(0, 2 * np.pi, 100)
y = 10*np.cos(theta)
z = 10*np.sin(theta)
for i in range(1):
    phi = i*np.pi/9
    ax.plot(y*np.sin(phi)+10*np.sin(phi), y*np.cos(phi)+10*np.cos(phi), z)

