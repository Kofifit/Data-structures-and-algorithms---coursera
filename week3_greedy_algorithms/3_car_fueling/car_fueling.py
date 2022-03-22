# python3
import sys


def compute_min_refills(distance, tank, stops):
    minStops = 0
    maxDistance = tank
    while maxDistance < distance:
        index = 0
        for stop in stops:
            if stop <= maxDistance:
                nextstop = stop
                index += 1
            else:
                break

        if index < len(stops):
            stops = stops[index:]
        elif nextstop + tank < distance:
            return -1
        maxDistance = nextstop + tank
        minStops += 1
    return minStops

# if __name__ == '__main__':
#     d, m, _, *stops = map(int, sys.stdin.read().split())
#     print(compute_min_refills(d, m, stops))


d = 700
t = 200
s = [100, 200, 300, 400]
print(compute_min_refills(d, t, s))
