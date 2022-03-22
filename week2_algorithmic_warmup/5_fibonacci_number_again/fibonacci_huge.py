# Uses python3
import sys

def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m


def get_fibonacci_huge_fast(n, m):

    if n <= 1:
        return n

    fibList = [0, 1]

    for i in range(n - 1):
        
        num = fibList[i] + fibList[i+1]
        fibList.append(num % m)
        listLen = len(fibList)

        if listLen % 2 == 0:
            if fibList[0:int(listLen/2)] == fibList[int(listLen/2):]:
                fibList = fibList[0:int(listLen/2)]
                break

    index = n % len(fibList)

    return fibList[index]




if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(get_fibonacci_huge_fast(n, m))
