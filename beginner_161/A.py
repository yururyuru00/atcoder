#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def main():
    args = input().rstrip().split(' ')
    a, b, c = int(args[0]), int(args[1]), int(args[2])
    print('{} {} {}'.format(c, a, b))
    
if __name__ == "__main__":
    main()

