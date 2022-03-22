#Uses python3

import sys
import numpy as np

def max_dot_product(a, b):
    res = 0
    new_a = []
    new_b = []

    while a and b:
        max_a = 0
        max_b = 0
        for i in range(1, len(a)):
            if a[max_a] < a[i]:
                max_a = i
            if b[max_b] < b[i]:
                max_b = i
        new_a.append(a[max_a])
        new_b.append(b[max_b])
        del a[max_a]
        del b[max_b]

    for i in range(len(new_a)):
        res += new_a[i] * new_b[i]
    return res


def max_dot_product_test(a, b):
    a = sorted(a)
    b = sorted(b)
    res = 0
    for i in range(0, len(a)):
        res += a[i] * b[i]
    return res


# if __name__ == '__main__':
#     input = sys.stdin.read()
#     data = list(map(int, input.split()))
#     n = data[0]
#     a = data[1:(n + 1)]
#     b = data[(n + 1):]
#     print(max_dot_product(a, b))


for _ in range(0, 1000):
    n = np.random.randint(1, 1000)
    a = list(np.random.randint(-100000, 100000, size=n))
    b = list(np.random.randint(-100000, 100000, size=n))
    mdp = max_dot_product(a.copy(), b.copy())
    mdpt = max_dot_product_test(a.copy(), b.copy())
    if mdp == mdpt:
        print("Correct")
    else:
        print(a)
        print(b)
        print("ERROR")
        print(mdp)
        print(mdpt)
        break


