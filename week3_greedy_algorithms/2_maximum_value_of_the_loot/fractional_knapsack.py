# Uses python3
import sys
import numpy as np


def get_optimal_value(capacity, weights, values):
    value = 0.
    value_per_unit = []

    for i in range(0, len(weights)):
        value_per_unit.append(values[i]/weights[i])

    while capacity > 0:
        max_value = max(value_per_unit)
        max_index = value_per_unit.index(max_value)

        if weights[max_index] >= capacity:
            value += value_per_unit[max_index] * capacity
            return value
        else:
            value += values[max_index]
            capacity -= weights[max_index]
            del value_per_unit[max_index], weights[max_index], values[max_index]

        if not values:
            return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
