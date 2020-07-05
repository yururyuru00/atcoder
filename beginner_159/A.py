#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def comb(val):
    if(val > 0):
        return int(val*(val-1) / 2)
    else:
        return 0

def main():
    args = input().rstrip().split(' ')
    N, M = int(args[0]), int(args[1])
    print(comb(N) + comb(M))
    
if __name__ == "__main__":
    main()

