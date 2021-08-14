grades = {}

# key-value 데이터 삽입
grades["aaa"] = 80
grades["bbb"] = 60
grades["ccc"] = 90
grades["ddd"] = 70
grades["eee"] = 96

print(grades)
print()

# 한 key에 여러 value 저장 시도
grades["aaa"] = 100

print(grades)
print()

# key를 이용한 value 탐색
print(grades["aaa"])
print(grades["ccc"])
print()

# key를 이용한 삭제
grades.pop("aaa")
grades.pop("eee")

print(grades)
print()













