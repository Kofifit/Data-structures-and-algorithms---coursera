# Uses python3
import sys

def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a*b


def lcm_fast(a,b):

    if a == b:
        return a

    maximal = max(a,b)
    minimal = min(a,b)
    l = max(a,b)

    if l % minimal == 0:
        return l

    while l % minimal != 0:

        l += maximal

        if l % minimal == 0:
            return l

    


if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm_fast(a, b))

