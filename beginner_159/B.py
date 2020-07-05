#!/usr/bin/env python
# coding: utf-8

# In[26]:


import numpy as np

def judge(s):
    l = len(s)
    for i in range(int(l/2)):
        if(s[i] != s[l-1-i]):
            return False
    return True

def main():
    args = input().rstrip().split(' ')
    S = np.array([c for c in args[0]])
    l = len(S)
    s1 = np.array([S[i] for i in range(0, int(l/2))])
    s2 = np.array([S[i] for i in range(int(l/2)+1, l)])
    if(judge(S) and judge(s1) and judge(s2)):
        print('Yes')
    else:
        print('No')
    
    
if __name__ == "__main__":
    main()


# In[ ]:




