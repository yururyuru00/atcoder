#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def main():
    args = input().rstrip()
    S = args
    T = input().rstrip()
    
    flag = True
    for i in range(len(S)):
        if(S[i] != T[i]):
            flag = False
            break
    
    if(flag == True):
        print('Yes')
    else:
        print('No')
    
    
if __name__ == "__main__":
    main()

