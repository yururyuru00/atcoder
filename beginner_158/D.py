#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from collections import deque

def swap(d, query):
    if(query[0] == 1):
        d.reverse()
    else:
        if(query[1] == 1):
            d.appendleft(query[2])
        else:
            d.append(query[2])

def main():
    S = [c for c in input().rstrip()]
    Q = int(input().rstrip())
    d = deque(S)
    
    count = 0
    for i in range(Q):
        q = input().rstrip().split(' ')
        if(q[0] == '1'):
            count += 1
        else:
            if(count % 2 == 1):
                swap(d, (1, -1, -1))
            count = 0
            swap(d, q)
    if(count % 2 == 1):
        swap(d, (1, -1, -1))
    
    for c in d:
        print(c, end='')
    
if __name__ == "__main__":
    main()


# # 
