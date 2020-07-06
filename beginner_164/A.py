#!/usr/bin/env python
# coding: utf-8

# In[3]:




def main():
    args = input().rstrip().split(' ')
    S, W = int(args[0]), int(args[1])
    
    if(S <= W):
        print('unsafe')
    else:
        print('safe')
    
    
if __name__ == "__main__":
    main()


# In[ ]:




