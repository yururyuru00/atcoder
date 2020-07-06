#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np

def main():
    args = input().rstrip().split(' ')
    N, M = int(args[0]), int(args[1])
    args = input().rstrip().split(' ')
    hw = np.array([int(i) for i in args])
    sum_hw = np.sum(hw)
    if(sum_hw > N):
        print('-1')
    else:
        print(N - sum_hw)
    
    
if __name__ == "__main__":
    main()


# In[ ]:




