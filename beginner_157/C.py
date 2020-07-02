#!/usr/bin/env python
# coding: utf-8

# In[6]:


import numpy as np

def main():
    rule = {1:[0, 10], 2:[10, 100], 3:[100, 1000]}
    args = input().rstrip().split(' ')
    N, M = int(args[0]), int(args[1])
    query = []
    for i in range(M):
        args = input().rstrip().split(' ')
        query.append([int(args[0]), int(args[1])])
        
    global_flag = False
    for i in range(rule[N][0], rule[N][1]):
        if(N==1):
            val = np.array([i, -1,-1, -1, -1])
        elif(N==2):
            val = np.array([int(i/10), i%10, -1, -1, -1])
        else:
            val = np.array([int(i/100), int(i%100/10), i%10, -1, -1])
        
        flag = True
        for q in query:
            if(val[q[0]-1] != q[1]):
                flag = False
                break
        if(flag == True):
            print(i)
            global_flag = True
            break
    if(global_flag == False):
        print('-1')
    
if __name__ == "__main__":
    main()


# ### 
