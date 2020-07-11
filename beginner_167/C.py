#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np

global N, M, X, A, C

def check(l, m_l):
    global M, X, A, C
    sum_ = np.zeros(M)
    for i in range(1, len(l)-1):
        sum_ += A[l[i]-1]
    flag = True
    for i in range(M):
        if(sum_[i] < X):
            flag = False
            break
    if(flag == True):
        money = 0
        for i in range(1, len(l)-1):
            money += C[l[i]-1]
        m_l.append(money)

def dfs(l, m_l):
    global N, M, X, A, C
    check(l, m_l)
    tail = l[len(l)-1]
    for i in range(tail+1, N+1):
        l.append(i)
        dfs(l, m_l)
        l.pop()

def main():
    global N, M, X, A, C, money_l
    args = input().rstrip().split(' ')
    N, M, X = int(args[0]), int(args[1]), int(args[2])
    A = np.zeros((N, M))
    C = np.zeros(N)
    for i in range(N):
        args = input().rstrip().split(' ')
        C[i] = int(args[0])
        for j in range(1, 1+M):
            A[i][j-1] = int(args[j])
    money_l = []
    dfs([0], money_l)
    
    print(money_l)
    
    
if __name__ == "__main__":
    main()


# In[ ]:




