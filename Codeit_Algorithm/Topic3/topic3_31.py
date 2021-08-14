def max_profit_memo(price_list, count, cache):
    # base case: 0개 혹은 1개인 경우
    if count < 2:
        cache[count] = price_list[count]
        return price_list[count]

    # 이미 계산했으면 cache에 있는 값을 리턴한다
    if count in cache:
        return cache[count]

    # 일단 count개로 팔았을 때를 profit으로 정한다.
    # 정해진 값이 없다면 0으로 한다.
    if count < len(price_list):
        profit = price_list[count]
    else:
        profit = 0

    # count개를 팔 수 있는 조합들을 비교
    # 기존 profit과 비교해 최댓값을 저장
    for i in range(1, count // 2 + 1):
        profit = max(profit,
                     max_profit_memo(price_list, i, cache) + max_profit_memo(price_list, count - i, cache))

    # 최대 수익을 cache에 저장
    cache[count] = profit

    return profit


def max_profit(price_list, count):
    max_profit_cache = {}

    return max_profit_memo(price_list, count, max_profit_cache)


# 테스트
print(max_profit([0, 100, 400, 800, 900, 1000], 5))
print(max_profit([0, 100, 400, 800, 900, 1000], 10))
print(max_profit([0, 100, 400, 800, 900, 1000, 1400, 1600, 2100, 2200], 9))
