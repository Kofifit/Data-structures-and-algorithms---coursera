#Uses python3

import sys
import numpy as np

def max_dot_product(a, b):
    res = 0

    while a:
        max_a = max(a)
        max_b = max(b)
        max_a_index = a.index(max_a)
        max_b_index = b.index(max_b)
        res += max_a * max_b
        del a[max_a_index]
        del b[max_b_index]

    return res


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    a = data[1:(n + 1)]
    b = data[(n + 1):]
    print(max_dot_product(a, b))

