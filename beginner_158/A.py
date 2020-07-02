#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def main():
    args = input().rstrip().split(' ')
    S = [c for c in args[0]]
    if(S[0]==S[1] and S[0]==S[2] and S[1]==S[2]):
        print('No')
    else:
        print('Yes')
    
if __name__ == "__main__":
    main()

