#!/usr/bin/env python
# coding: utf-8

# In[9]:


def comb(val):
    if(val > 0):
        return int(val*(val-1) / 2)
    else:
        return 0
    
def make_map(balls):
    balls_map = {}
    for ball in balls:
        if(ball in balls_map):
            balls_map[ball] += 1
        else:
            balls_map[ball] = 1
    return balls_map

def main():
    args = input().rstrip().split(' ')
    N = int(args[0])
    balls = [val for val in input().rstrip().split(' ')]
    balls_map = make_map(balls)
    
    sum_ = 0
    for val in balls_map.values():
        sum_ += comb(val)
    for ball in balls:
        print(sum_ - (balls_map[ball]-1))
    
if __name__ == "__main__":
    main()


# In[ ]:




