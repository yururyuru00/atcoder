#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np

def main():
    args = input().rstrip().split(' ')
    N = int(args[0])
    item_list = {}
    for i in range(N):
        item = input().rstrip()
        if(item in item_list):
            item_list[item] = 0
        else:
            item_list[item] += 1
    print(item_list)
    
if __name__ == "__main__":
    main()


# In[ ]:


|

