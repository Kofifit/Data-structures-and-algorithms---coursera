def binary_search(keys, query):
    low = 0
    high = len(keys) - 1

    if len(keys) == 1 and keys[0] == query:
        return 0

    while low <= high:
        mid = int(low + (high-low)/2)
        if (keys[mid - 1] < query or mid == 0) and keys[mid] == query:
            return mid
        elif query > keys[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return -1


if __name__ == '__main__':
    num_keys = int(input())
    input_keys = list(map(int, input().split()))
    assert len(input_keys) == num_keys

    num_queries = int(input())
    input_queries = list(map(int, input().split()))
    assert len(input_queries) == num_queries

    for q in input_queries:
        print(binary_search(input_keys, q), end=' ')


