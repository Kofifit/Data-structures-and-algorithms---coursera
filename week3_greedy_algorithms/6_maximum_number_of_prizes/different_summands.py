# Uses python3
import sys

def optimal_summands(n):

    summands = []
    prize = 1
    while n > 0:
        if n - prize > prize:
            n -= prize
            summands.append(prize)
            prize += 1
        else:
            summands.append(n)
            return summands


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')

