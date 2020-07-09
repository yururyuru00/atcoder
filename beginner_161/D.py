#!/usr/bin/env python
# coding: utf-8

# In[15]:


from collections import deque

def dump_neighbor(val):
    if(val == 0):
        return [val, val+1]
    elif(val == 9):
        return [val-1, val]
    else:
        return [val-1, val, val+1]

def dfs(d, K):
    for i in range(K):
        val = d.popleft()
        neighbors = dump_neighbor(val%10)
        for neighbor in neighbors:
            d.append(val*10 + neighbor)
    print(val)
    

if __name__ == "__main__":
    K = int(input().rstrip())
    d = deque([val for val in range(1,10)])
    dfs(d, K)


# In[ ]:




