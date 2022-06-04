# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):

    if len(segments) == 1:
        return segments[0].start

    points = []

    while segments:
        end = segments[0].end
        index = 0


        for idx, s in enumerate(segments):
            if s.end <= end:
                end = s.end
                index = idx
        points.append(end)
        del segments[index]

        index_delete = []
        for idx, s in enumerate(segments):
            if s.start <= end:
                index_delete.append(idx)

        for i in sorted(index_delete, reverse=True):
            del segments[i]


    return points

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    print(*points)

