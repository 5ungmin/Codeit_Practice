def fib_optimized(n):
    previous = 1
    current = 1

    for i in range(3, n+1):
        previous, current = current, previous + current

    return current


# 테스트
print(fib_optimized(16))
print(fib_optimized(53))
print(fib_optimized(213))
