def is_palindrome(word):
    word = list(word)
    for i in range(len(word)):
        if word[i] != word[-i-1]:
            return False
        else:
            continue
    return True


# 테스트
print(is_palindrome("racecar"))
print(is_palindrome("stars"))
print(is_palindrome("토마토"))
print(is_palindrome("kayak"))
print(is_palindrome("hello"))