# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    if capacity == 0 or not weights:
        return 0
    value = 0.
    value_per_unit = []

    for i, w in enumerate(weights):
        v = values[i]
        value_per_unit.append(v/w)

    while capacity > 0:

        max_value = max(value_per_unit)
        max_index = value_per_unit.index(max_value)
        amount = min(capacity, weights[max_index])
        value += amount * max_value
        capacity -= amount
        del value_per_unit[max_index], weights[max_index], values[max_index]

        if not values:
            return value

    return value



if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))



