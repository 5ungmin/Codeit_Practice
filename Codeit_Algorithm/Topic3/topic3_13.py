# 제목: 합병 정렬 구현하기
def merge(list1, list2):
    merged_list = []

    # merge
    i, j = 0, 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1

    # 남아있는 것 추가
    if i == len(list1):
        merged_list += list2[j:]
    elif j == len(list2):
        merged_list += list1[i:]

    return merged_list


# 합병 정렬
def merge_sort(my_list):
    # 원소 1개짜리 리스트인 경우
    if len(my_list) == 1:
        return my_list

    mid = len(my_list) // 2

    # my_list를 두 리스트로 나눈다.
    left_list = merge_sort(my_list[:mid])
    right_list = merge_sort(my_list[mid:])

    my_list = merge(left_list, right_list)

    return my_list

# 테스트
print(merge_sort([1, 3, 5, 7, 9, 11, 13, 11]))
print(merge_sort([28, 13, 9, 30, 1, 48, 5, 7, 15]))
print(merge_sort([2, 5, 6, 7, 1, 2, 4, 7, 10, 11, 4, 15, 13, 1, 6, 4]))
