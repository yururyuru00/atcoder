#!/usr/bin/env python
# coding: utf-8

# In[9]:


def main():
    args = input().rstrip().split(' ')
    N, A, B = int(args[0]), int(args[1]), int(args[2])
    unit = int(N/(A+B))
    rem = N % (A+B)
    if(rem > A):
        brem = A
    else:
        brem = rem
    print(A*unit + brem)
    
if __name__ == "__main__":
    main()


# In[ ]:




