# 출근하는 방법 I
def staircase(n):
    if n < 2:
        return 1

    previous = 1
    current = 1
    for i in range(n):
        previous, current = current, previous + current

    return previous


# 테스트
print(staircase(0))
print(staircase(6))
print(staircase(15))
print(staircase(25))
print(staircase(41))
