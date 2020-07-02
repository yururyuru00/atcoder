#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np




def main():
    args = input().rstrip().split(' ')
    N, M, K= int(args[0]), int(args[1]), int(args[2])
    friend, block = [], []
    for i in range(N):
        args = input().rstrip().split(' ')
        friend.append([int(args[0]), int(args[1])])
    for i in range(N):
        args = input().rstrip().split(' ')
        block.append([int(args[0]), int(args[1])])
        
    print('{} {} {}\n{}\n{}'.format(N, M, K, friend, block))
    
    
if __name__ == "__main__":
    main()


# In[ ]:




