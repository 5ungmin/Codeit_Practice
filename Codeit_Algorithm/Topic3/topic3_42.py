# 수강 신청
def course_selection(course_list):
    # 빨리 끝나는 수업이 먼저 오도록 정렬
    sorted_list = sorted(course_list, key=lambda x: x[1])
    # 가장 먼저 끝나는 수업을 듣는다.
    my_selection = [sorted_list[0]]
    # 안 겹치는 수업 중 가장 먼저 끝나는 수업을 듣는다.
    for course in sorted_list:
        if course[0] > my_selection[-1][1]:
            my_selection.append(course)

    return my_selection


# 테스트
print(course_selection([(6, 10), (2, 3), (4, 5), (1, 7), (6, 8), (9, 10)]))
print(course_selection([(1, 2), (3, 4), (0, 6), (5, 7), (8, 9), (5, 9)]))
print(course_selection([(4, 7), (2, 5), (1, 3), (8, 10), (5, 9), (2, 5), (13, 16), (9, 11), (1, 8)]))
