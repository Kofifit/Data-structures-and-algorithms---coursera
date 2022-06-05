# Uses python3
import sys

def get_majority_element_linear(a, left, right):
    major = a[0]
    counter = 0
    for num in a:
        if counter == 0:
            major = num
        if num == major:
            counter += 1
        else:
            counter -= 1
    counter = 0
    for num in a:
        if num == major:
            counter += 1
    if counter > len(a)/2:
        return 1
#     else:
#         return 0



def get_majority_element_divide_conquer(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]

    left_m = get_majority_element_divide_conquer(a, left, (left + right - 1)//2 + 1)
    right_m = get_majority_element_divide_conquer(a, (left + right - 1)//2 + 1, right)
    left_count = 0
    for i in range(left, right):
        if a[i] == left_m:
            left_count += 1
    if left_count > (right-left)//2:
        return left_m

    right_count = 0
    for i in range(left, right):
        if a[i] == right_m:
            right_count += 1
    if right_count > (right-left)//2:
        return right_m

    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    print("n=" + str(n))
    if get_majority_element_divide_conquer(a, 0, len(a)) != -1:
        print(1)
    else:
        print(0)


