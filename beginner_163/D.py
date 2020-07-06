#!/usr/bin/env python
# coding: utf-8

# In[14]:


mod = 1000000007

def sum_(a, b):
    return int((a+b)*(b-a+1)/2)

def main():
    args = input().rstrip().split(' ')
    N, K = int(args[0]), int(args[1])
    
    Ans = 0
    for i in range(K, N+2):
        sum_b = sum_(0, i-1)
        sum_u = sum_(N-i+1, N)
        Ans += (sum_u-sum_b)+1
        Ans = Ans % mod
    print(Ans)
    
if __name__ == "__main__":
    main()


# In[ ]:




