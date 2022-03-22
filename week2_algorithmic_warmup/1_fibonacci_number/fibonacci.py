# Uses python3
def naiveFib(n):

    if (n <= 1):
        return n

    return naiveFib(n - 1) + naiveFib(n - 2)

def fastFib(n):

    if (n <= 1):
        return n

    fibList = []
    for num in range(0,n+1):
        if len(fibList) < 2:
            fibList.append(num)
        else:
            new = fibList[num-1] + fibList[num-2]
            fibList.append(new)

    return fibList[n]


n = int(input())
print(fastFib(n))
# for n in range(0,46):
    # print(naiveFib(n))
    # print(fastFib(n))

