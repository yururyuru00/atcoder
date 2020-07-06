#!/usr/bin/env python
# coding: utf-8

# In[8]:




def main():
    args = input().rstrip().split(' ')
    N = [val for val in args[0]]
    flag = False
    for val in N:
        if(val == '7'):
            flag = True
            break
    if(flag):
        print('Yes')
    else:
        print('No')
    
if __name__ == "__main__":
    main()


# In[ ]:




