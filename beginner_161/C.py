#!/usr/bin/env python
# coding: utf-8

# In[11]:


def main():
    args = input().rstrip().split(' ')
    N, K = int(args[0]), int(args[1])
    last_point = N % K
    print(min(last_point, abs(last_point-K)))
    
if __name__ == "__main__":
    main()


# In[ ]:




