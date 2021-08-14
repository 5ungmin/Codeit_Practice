# 투자 귀재 규식이 I
# Brute Force 이용
def sublist_max(profits):
    max_profit = profits[0]

    for current in range(len(profits)):
        for walk in range(current+1, len(profits)):
            if sum(profits[current:walk+1]) > max_profit:
                max_profit = sum(profits[current:walk+1])

    return max_profit


# 테스트
print(sublist_max([4, 3, 8, -2, -5, -3, -5, -3]))
print(sublist_max([2, 3, 1, -1, -2, 5, -1, -1]))
print(sublist_max([7, -3, 14, -8, -5, 6, 8, -5, -4, 10, -1, 8]))

# 모범 답안
# def sublist_max(profits):
#     max_profit = profits[0]  # 최대 수익
#
#     for i in range(len(profits)):
#         # 인덱스 i부터 j까지 수익의 합을 보관하는 변수
#         total = 0
#
#         for j in range(i, len(profits)):
#             # i부터 j까지 수익의 합을 계산
#             total += profits[j]
#
#             # i부터 j까지 수익의 합이 최대 수익이라면, max_profit 업데이트
#             max_profit = max(max_profit, total)
#
#     return max_profit
#
#
# # 테스트
# print(sublist_max([4, 3, 8, -2, -5, -3, -5, -3]))
# print(sublist_max([2, 3, 1, -1, -2, 5, -1, -1]))
# print(sublist_max([7, -3, 14, -8, -5, 6, 8, -5, -4, 10, -1, 8]))
