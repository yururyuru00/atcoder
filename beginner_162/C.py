#!/usr/bin/env python
# coding: utf-8

# In[13]:


def gcd(a, b):
    c = a % b
    if(c==0):
        return b
    else:
        return gcd(b, c)

def main():
    args = input().rstrip().split(' ')
    K = int(args[0])
    sum_ = 0
    for a in range(1, K+1):
        for b in range(a+1, K+1):
            for c in range(b+1, K+1):
                sum_ += gcd(gcd(a, b), c)
    for i in range(1, K+1):
        
    print('{} {}'.format(sum_, (K+1)*K/2))
    
if __name__ == "__main__":
    main()


# In[ ]:




