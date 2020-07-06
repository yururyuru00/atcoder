#!/usr/bin/env python
# coding: utf-8

# In[1]:


from collections import deque

global count

def dfs(S):
    global count
    val = int(S)
    if(val % 2019 == 0):
        count += 2

def main():
    global count
    count = 3
    args = input().rstrip().split(' ')
    S = args[0]
    dfs(S)
    dfs(S)
    print(count)

if __name__ == '__main__':
    main()


# In[ ]:




