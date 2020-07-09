#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
from collections import deque

def main():
    N, M, K = [i for i in map(int, input().rstrip().split(' '))]
    A = deque([i for i in map(int, input().rstrip().split(' '))])
    B = deque([i for i in map(int, input().rstrip().split(' '))])
    
    print(A, B)
    
if __name__ == "__main__":
    main()


# In[ ]:




