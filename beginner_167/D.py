#!/usr/bin/env python
# coding: utf-8

# In[ ]:




def main():
    args = input().rstrip().split(' ')
    N, K = int(args[0]), int(args[1])
    d = {}
    args = input().rstrip().split(' ')
    for i in range(len(args)):
        d[i+1] = int(args[i])
    
    spot = 1
    for i in range(K):
        print(spot)
        spot = d[spot]
        
    
if __name__ == "__main__":
    main()


# In[ ]:




