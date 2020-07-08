#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np

def main():
    N = int(input().rstrip())-1
    N_b = N
    
    for i in range(100000):
        N = N / 26
        if(N<1):
            break
    N = N_b
    
    ary = np.array([26**j for j in reversed(range(i+1))])
    for j in range(i+1):
        if(j==0):
            idx = int(N / ary[j])
            N = N - ary[j]*idx
            print(chr(96+idx), end='')
        else:
            idx = int(N / ary[j])
            N = N - ary[j]*idx
            print(chr(97+idx), end='')
    
if __name__ == "__main__":
    main()


# In[ ]:




