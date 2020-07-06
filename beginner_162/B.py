#!/usr/bin/env python
# coding: utf-8

# In[13]:



def func_sum_(fast, N):
    last = fast * int(N / fast)
    return int((fast + last) / 2. * (last / fast))
    

def main():
    args = input().rstrip().split(' ')
    N = int(args[0])
    sum_ = int((N+1) * N / 2)
    print(sum_ - (func_sum_(3, N) + func_sum_(5, N) - func_sum_(15, N)))
    
if __name__ == "__main__":
    main()


# In[ ]:




