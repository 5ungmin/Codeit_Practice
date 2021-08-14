# 이진 탐색하는 함수(있으면 index, 없으면 None을 리턴)
def binary_search(element, some_list):
    right = len(some_list) - 1
    left = 0

    while left <= right:
        mid = (left + right) // 2
        if some_list[mid] == element:
            return mid
        elif some_list[mid] > element:
            right = mid - 1
        else:
            left = mid + 1
    return None


print(binary_search(2, [2, 3, 5, 7, 11]))
print(binary_search(0, [2, 3, 5, 7, 11]))
print(binary_search(5, [2, 3, 5, 7, 11]))
print(binary_search(3, [2, 3, 5, 7, 11]))
print(binary_search(11, [2, 3, 5, 7, 11]))