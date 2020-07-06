#!/usr/bin/env python
# coding: utf-8

# In[11]:




def main():
    args = input().rstrip().split(' ')
    A, B, C, D = int(args[0]),int(args[1]),int(args[2]),                  int(args[3])
    chance = A / D
    if(chance.is_integer() == False):
        chance = int(chance) + 1
    
    if(C <= B*chance):
        print('Yes')
    else:
        print('No')
    
if __name__ == "__main__":
    main()


# In[ ]:




