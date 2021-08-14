class User:
    def __init__(self, name, email, pw):
        self.name = name
        self.email = email
        self.pw = pw

    def say_hello(self):
        print("안녕하세요! 저는 {}입니다.".format(self.name))

    def __str__(self):
        return "사용자: {}, 이메일: {}, 비밀번호: ******".format(self.name, self.email)


user1 = User("Young", "young@codeit.kr", "123456")
user2 = User("Yoonsoo", "yoonsoo@codeit.kr", "abcdef")

print(user1)
print(user2)
