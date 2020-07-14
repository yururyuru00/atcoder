import math
def main():
    judge_l = {'AC':0, 'WA':0, 'TLE':0, 'RE':0}
    with open('in.csv', 'r') as r:
        r.readline()
        for line in r.readlines():
            judge = line.rstrip()
            judge_l[judge] += 1
    
    str = ''
    for key in judge_l.keys():
        str += '{} × {}\n'.format(key, judge_l[key])
    print(str.rstrip('\n'))
    
if __name__ == "__main__":
    main()
