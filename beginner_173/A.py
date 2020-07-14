import math
def main():
    with open('in.csv', 'r') as r:
        args = list(r.readlines())
    N = int(args[0])
    use = math.ceil(N/1000)
    print(1000*use - N)
    
if __name__ == "__main__":
    main()
