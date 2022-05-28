# python3
import sys


def compute_min_refills(distance, tank, stops):

    # Check if no stop is needed
    if tank >= distance:
        return 0

    # Check if possible to get to the distance
    test_array = stops
    test_array.insert(0, 0)
    test_array.insert(len(test_array), distance)
    for i in range(1, len(test_array)):
        if test_array[i] - test_array[i-1] > tank:
            return -1

    min_stops = 0
    current_point = 0
    while current_point < distance:
        index = 0
        for stop in stops:
            if stop <= current_point + tank:
                next_stop = stop
                index += 1
            else:
                break
        min_stops += 1
        current_point = next_stop
        if current_point + tank >= distance:
            return min_stops
        elif index < len(stops):
            stops = stops[index:]




if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))

