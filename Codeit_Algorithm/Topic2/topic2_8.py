# 제목: 하노이의 탑
def move_disk(disk_num, start_peg, end_peg):
    print("%d번 원판을 %d번 기둥에서 %d번 기둥으로 이동" % (disk_num, start_peg, end_peg))

# 하노이의 탑 게임의 해답을 알려주는 함수
# num_disks개의 원판이 start_peg에 있고, 이를 end_peg까지 옮김
def hanoi(num_disks, start_peg, end_peg):
    if num_disks == 1:
        move_disk(num_disks, start_peg, end_peg)

    else:
        by_peg = 6 - start_peg - end_peg

        hanoi(num_disks - 1, start_peg, by_peg)
        move_disk(num_disks, start_peg, end_peg)
        hanoi(num_disks - 1, by_peg, end_peg)


# 테스트 코드 (포함하여 제출해주세요)
hanoi(3, 1, 3)
