#!/usr/bin/env python
# coding: utf-8

# In[13]:




def relu(a, b):
    if(a <= b):
        return 0
    else:
        return a - b

def main():
    args = input().rstrip().split(' ')
    A, B, C, K = int(args[0]),int(args[1]),int(args[2]),int(args[3])
    
    if(A >= K):
        print(K)
    else:
        print(A - relu(K, A+B))
    
if __name__ == "__main__":
    main()


# In[ ]:




