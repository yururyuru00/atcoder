import numpy as np

def count(ary, val):
    c, sum_ = 0, 0
    for i, v in enumerate(ary[::-1]):
        if(v==1):
            c += 1
            sum_ += val[i]

    return c, sum_

def vert(ary, idx):
    if(ary[idx] == 1):
        ary[idx] = 0
    else:
        ary[idx] = 1

def main():
    with open('../in.csv', 'r') as r:
        args = list(r.readlines())
    N = int(args[0].rstrip())
    ary = [int(i) for i in str(args[1].rstrip())]
    val = np.array([2**i for i in range(N)])
    
    for i in range(N):
        vert(ary, i)
        c, v = count(ary)
        v = v % c
        vert(ary, i)

    
if __name__ == "__main__":
    main()