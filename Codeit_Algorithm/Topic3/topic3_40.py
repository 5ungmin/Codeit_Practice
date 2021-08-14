# 지각 벌금 적게 내기
def min_fee(pages_to_print):
    fee_list = []
    fee = 0

    for page in sorted(pages_to_print):
        fee += page
        fee_list.append(fee)

    sum = 0
    for fee in fee_list:
        sum += fee

    return sum


# 테스트
print(min_fee([6, 11, 4, 1]))
print(min_fee([3, 2, 1]))
print(min_fee([3, 1, 4, 3, 2]))
print(min_fee([8, 4, 2, 3, 9, 23, 6, 8]))

# 모범 답안
# # 지각 벌금 적게 내기
# def min_fee(pages_to_print):
#     sorted_list = sorted(pages_to_print)
#     total_fee = 0
#
#     for i in range(len(sorted_list)):
#         total_fee += sorted_list[i] * (len(sorted_list) - i)
#
#     return total_fee
#
#
# # 테스트
# print(min_fee([6, 11, 4, 1]))
# print(min_fee([3, 2, 1]))
# print(min_fee([3, 1, 4, 3, 2]))
# print(min_fee([8, 4, 2, 3, 9, 23, 6, 8]))
