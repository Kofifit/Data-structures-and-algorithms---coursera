# Uses python3
import sys
import numpy as np


def get_optimal_value(capacity, weights, values):
    value = 0.
    valuePerUnit = []

    for i in range(0, len(weights)):
        valuePerUnit.append(values[i]/weights[i])

    while capacity > 0:

        maxIndex = 0
        for i in range(1, len(weights)):
            if valuePerUnit[i-1] < valuePerUnit[i]:
                maxIndex = i

        if weights[maxIndex] >= capacity:
            value += valuePerUnit[maxIndex] * capacity
            return value
        else:
            value += valuePerUnit[maxIndex] * weights[maxIndex]
            capacity -= weights[maxIndex]

        del valuePerUnit[maxIndex], weights[maxIndex]


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
