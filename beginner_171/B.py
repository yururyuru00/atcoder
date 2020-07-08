#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np

def main():
    args = input().rstrip().split(' ')
    N, K = int(args[0]), int(args[1])
    args = input().rstrip().split(' ')
    p = np.array([int(i) for i in args])
    
    p = np.sort(p)
    sum = 0
    for i in range(K):
        sum += p[i]
    print(sum)
    
if __name__ == "__main__":
    main()


# In[ ]:




