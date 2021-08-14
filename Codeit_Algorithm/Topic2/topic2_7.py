# 제목: 이진 탐색 재귀로 구현해보기
def binary_search(element, some_list, start_index=0, end_index=None):
    # end_index가 따로 주어지지 않은 경우에는 리스트의 마지막 인덱스 (초기 설정)
    if end_index == None:
        end_index = len(some_list) - 1

    # 이진 탐색
    if start_index > end_index:
        return None

    current = (start_index + end_index) // 2

    if some_list[current] == element:
        return current
    elif some_list[current] > element:
        return binary_search(element, some_list, start_index, current-1)
    else:
        return binary_search(element, some_list, current+1, end_index)


print(binary_search(2, [2, 3, 5, 7, 11]))
print(binary_search(0, [2, 3, 5, 7, 11]))
print(binary_search(5, [2, 3, 5, 7, 11]))
print(binary_search(3, [2, 3, 5, 7, 11]))
print(binary_search(11, [2, 3, 5, 7, 11]))