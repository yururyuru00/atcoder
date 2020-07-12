def main():
    with open('../in.csv', 'r') as r:
        args = list(r.readlines())
    L, R, d = map(int, args[0].rstrip().split(' '))

    c = 0
    for i in range(L, R+1):
        if(i % d == 0):
            c += 1
    print(c)
    
if __name__ == "__main__":
    main()