#!/usr/bin/env python
# coding: utf-8

# In[5]:


import numpy as np

def main():
    args = input().rstrip().split(' ')
    N = int(args[0])
    args = input().rstrip().split(' ')
    A = np.array([int(val) for val in args])
    sup = np.zeros(N-1, dtype=np.int)
    
    for a in A:
        sup[a-1] += 1
    for val in sup:
        print(val)
    print(0)
    
if __name__ == "__main__":
    main()


# In[ ]:




