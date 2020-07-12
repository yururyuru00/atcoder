import numpy as np

def eval(x, y, z):
    if(x==y and y==z):
        return 1
    if(x==y):
        return 3
    if(y==z):
        return 3
    return 6


def main():
    with open('../in.csv', 'r') as r:
        args = list(r.readlines())
    N = int(args[0].rstrip())
    ans = np.zeros(N, dtype=np.int64)

    for x in range(1, 143):
        for y in range(x, 143):
            for z in range(y, 143):
                val = (x+y)**2 + (x+z)**2 + (y+z)**2
                if(val <= 2*N and val%2==0):
                    ans[int(val/2)-1] += eval(x, y, z)

    print(ans)

if __name__ == "__main__":
    main()
