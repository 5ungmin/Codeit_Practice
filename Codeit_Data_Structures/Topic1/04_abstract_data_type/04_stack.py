from collections import deque

stack = deque()

# 스택 맨 위에 데이터 추가
stack.append("A")
stack.append("B")
stack.append("C")
stack.append("D")
stack.append("E")

print(stack)
print()

# 스택 맨 위 데이터 접근
print(stack[-1])
print()

# 스택 맨 위 데이터 삭제
print(stack.pop())
print(stack.pop())
print(stack.pop())

print(stack)
print()















