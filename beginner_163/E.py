#!/usr/bin/env python
# coding: utf-8

# In[10]:


import numpy as np
from collections import deque

def main():
    args = input().rstrip().split(' ')
    N = int(args[0])
    args = input().rstrip().split(' ')
    A = np.array([float(val) for val in args])
    A_ = np.copy(A)
    for i in range(N):
        A_[i] += i/N
    que = deque([int(val) for val in range(N)])
    top = np.argsort(-A_)
    
    Ans = 0
    for i in top:
        print('{} '.format(i))
        l, r = abs(que[0]-i), abs(que[-1]-i)
        if(l > r):
            Ans += A[i] * l
            que.popleft()
        else:
            Ans += A[i] * r
            que.pop()
        print(que)
        print(Ans)
    print(Ans)
    
if __name__ == "__main__":
    main()


# In[ ]:




