import numpy as np


def main():
    with open('../in.csv', 'r') as r:
        args = list(r.readlines())
    N = int(args[0].rstrip())
    a = np.array([int(i) for i in args[1].rstrip().split(' ')])

    c = 0
    for i, val in enumerate(a):
        if((i+1)%2 == 1 and val%2 == 1):
            c += 1
    print(c)

if __name__ == "__main__":
    main()
