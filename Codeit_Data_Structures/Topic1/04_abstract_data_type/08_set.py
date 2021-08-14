finished_classes = set()

# 데이터 저장
finished_classes.add("Data Structures")
finished_classes.add("Algorithm")
finished_classes.add("Programming Basics")
finished_classes.add("Interactive Web")
finished_classes.add("Data Science")

print(finished_classes)
print()

# 중복 데이터 저장 시도
finished_classes.add("Data Structures")
finished_classes.add("Algorithm")

print(finished_classes)
print()

# 데이터 탐색
print("Digital Circuits" in finished_classes)
print("Data Structures" in finished_classes)
print()

# 데이터 삭제
finished_classes.remove("Data Structures")
finished_classes.remove("Algorithm")
print(finished_classes)







