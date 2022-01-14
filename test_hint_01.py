#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def ts(n):
    hintmsg = {
            1:'输入：print(\"Hello world!\")',
            2:'输入：import pandas as pd',
    
            }
    if n in hintmsg.keys():
        print(hintmsg[n])
    else:
        print("提示信息（%d）获取失败。" % (n))

