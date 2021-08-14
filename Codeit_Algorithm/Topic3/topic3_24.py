def fib_memo(n, cache):
    # base case
    if n < 3:
        return 1

    if n not in cache:
        cache[n] = fib_memo(n-2, cache) + fib_memo(n-1, cache)

    return cache[n]


def fib(n):
    # n번째 피보나치 수를 담는 사전
    fib_cache = {}
    return fib_memo(n, fib_cache)


# 테스트
print(fib(10))
print(fib(50))
print(fib(100))