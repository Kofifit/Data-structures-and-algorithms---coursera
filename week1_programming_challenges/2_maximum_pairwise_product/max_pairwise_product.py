def max_pairwise_product(numbers):

    max_index1 = 0
    max_index2 = 0
    for idx, num in enumerate(numbers):
        if num >= numbers[max_index1] or idx == 0:
            max_index1 = idx
    for idx, num in enumerate(numbers):
        if num >= numbers[max_index2] and idx != max_index1 or max_index1 == max_index2:
            max_index2 = idx

    max_product = numbers[max_index1] * numbers[max_index2]

    return max_product


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
