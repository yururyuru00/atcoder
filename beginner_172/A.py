#!/usr/bin/env python
# coding: utf-8

# In[19]:


def main():
    S = input().rstrip()
    T = input().rstrip()
    
    c = 0
    for s, t in zip(S, T):
        print(s, t)
        if(s != t):
            c += 1
    print(c)
    
if __name__ == "__main__":
    main()


# In[ ]:




