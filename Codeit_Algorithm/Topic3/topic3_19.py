# 제목: 퀵 정렬 더 멋있게 구현하기
# 두 요소의 위치를 바꿔주는 helper function
def swap_elements(my_list, index1, index2):
    my_list[index1], my_list[index2] = my_list[index2], my_list[index1]


# 퀵 정렬에서 사용되는 partition 함수
def partition(my_list, start, end):
    # 리스트의 마지막 원소를 pivot으로 한다.
    p = end
    b = start
    i = start

    while i < p:
        # pivot보다 크다면 그대로 둔다.
        if my_list[i] < my_list[p]:
            swap_elements(my_list, i, b)
            b += 1
        i += 1

    # b가 가리키고있는 값과 pivot을 바꾼다.
    swap_elements(my_list, b, p)
    p = b

    return p


# 퀵 정렬
def quicksort(my_list, start=0, end=None):
    # 처음 quicksort를 호출한 경우 end 설정
    if end == None:
        end = len(my_list) - 1

    # base case
    if start >= end:
        return my_list

    # 처음 partition
    pivot_index = partition(my_list, start, end)

    # 왼쪽을 quicksort
    quicksort(my_list, start, pivot_index-1)
    # 오른쪽을 quicksort
    quicksort(my_list, pivot_index+1, end)


# 테스트 1
list1 = [1, 3, 5, 7, 9, 11, 13, 11]
quicksort(list1) # start, end 파라미터 없이 호출
print(list1)

# 테스트 2
list2 = [28, 13, 9, 30, 1, 48, 5, 7, 15]
quicksort(list2) # start, end 파라미터 없이 호출
print(list2)

# 테스트 3
list3 = [2, 5, 6, 7, 1, 2, 4, 7, 10, 11, 4, 15, 13, 1, 6, 4]
quicksort(list3) # start, end 파라미터 없이 호출
print(list3)