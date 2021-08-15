import random


# n개의 랜덤한 숫자를 뽑아 리스트로 리턴하는 함수
def generate_numbers(n):
    num_list = random.sample(range(1, 45), n)
    return num_list


# 당첨 번호 6개와 보너스 번호 1개를 리스트로 리턴하는 함수
def draw_winning_numbers():
    winning_numbers = generate_numbers(7)
    return sorted(winning_numbers[:6]) + winning_numbers[6:]


# 두 리스트 간에 겹치는 번호가 몇 개인지 리턴하는 함수
def count_matching_numbers(list_1, list_2):
    overlapping_set = set(list_1) & set(list_2)
    return len(overlapping_set)


# 주최즉 번호 리스트, 참가자 번호 리스트를 받아 당첨 금액을 리턴하는 함수
# 주최즉 번호는 6+1개, 참가자 번호는 6개
def check(numbers, winning_numbers):
    # 보너스 번호 빼고 몇 개가 겹치는지 확인
    match = count_matching_numbers(numbers, winning_numbers[:6])
    bonus_count = count_matching_numbers(numbers, winning_numbers[6:])

    if match == 6:
        return 100000000
    elif match == 5 and bonus_count == 1:
        return 50000000
    elif match == 5:
        return 1000000
    elif match == 4:
        return 50000
    elif match == 3:
        return 5000
    else:
        return 0
