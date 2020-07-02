#!/usr/bin/env python
# coding: utf-8

# In[12]:



def main():
    args = input().rstrip().split(' ')
    A, B = int(args[0]), int(args[1])
    p_A = [A * 12.5, (A+1.) * 12.5]
    p_B = [B * 10., (B+1.) * 10.]
    if(p_A[0].is_integer() == False):
        p_A[0] = int(p_A[0])+1
    else:
        p_A[0] = int(p_A[0])
    if(p_B[0].is_integer() == False):
        p_B[0] = int(p_B[0])+1
    else:
        p_B[0] = int(p_B[0])
    if(p_A[1].is_integer == False):
        p_A[1] = int(p_A[1])
    else:
        p_A[1] = int(p_A[1]) -1
    if(p_B[1].is_integer() == False):
        p_B[1] = int(p_B[0])
    else:
        p_B[1] = int(p_B[1]) -1
        
        
    if(p_A[1] <= p_B[0] or p_B[1] <= p_A[0]):
        print('-1')
    else:
        print(int(max(p_A[0], p_B[0])))
    
if __name__ == "__main__":
    main()


# In[ ]:




