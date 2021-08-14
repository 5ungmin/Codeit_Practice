def fib_tab(n):
    fib_table = [1, 1]

    for i in range(2, n):
        fib_table.append(fib_table[i-2] + fib_table[i-1])

    return fib_table[n-1]


# 테스트
print(fib_tab(10))
print(fib_tab(56))
print(fib_tab(132))