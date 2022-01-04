import random

count = 0
win = 0
lose = 0
while True:
    num = random.randint(1, 3)  # 1부터 3 사이의 숫자 중 랜덤한 숫자를 뽑음
    user_num = int(input("입력 (1: 가위), (2: 바위), (3: 보) >>"))
    if num == user_num:
        print("비겼습니다. 다시 입력하세요.")
    elif num == 1 and user_num == 2:
        print("You Win!")
        count += 1
        win += 1
    elif num == 1 and user_num == 3:
        print("You Lose..")
        count += 1
        lose += 1
    elif num == 2 and user_num == 1:
        print("You Lose..")
        count += 1
        lose += 1
    elif num == 2 and user_num == 3:
        print("You Win!")
        count += 1
        win += 1
    elif num == 3 and user_num == 1:
        print("You Win!")
        count += 1
        win += 1
    elif num == 3 and user_num == 2:
        print("You Lose..")
        count += 1
        lose += 1
    if count == 10:
        print("전적 : 10전 {}승 {}패".format(win, lose))
        print("승률 : {} %".format(win*10))
        break