#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np

def main():
    args1, args2 = input().rstrip().split(' '), input().rstrip().split(' ')
    N, M = int(args1[0]), int(args1[1])
    items = np.array([int(val) for val in args2])
    items = np.sort(items)[::-1]
    items_sum = np.sum(items)
    bottom = items_sum / 4. / M
    
    if(items[M-1] >= bottom):
        print('Yes')
    else:
        print('No')
    
if __name__ == "__main__":
    main()


# In[ ]:




