import random

def num_guess():
    # 1과 10 사이의 랜덤 숫자를 생성
    num = random.randint(1, 10)
    attempts = 0  # 시도 횟수를 저장할 변수
    print("1과 10 중에 골라.")
    
    while True:
        try:
            # 사용자로부터 숫자 입력 받기
            guessed_num = int(input("게스 왓?: "))
            attempts += 1  # 시도 횟수 증가

            # 3번 이상 시도 시 메시지와 정답 출력
            if attempts > 3:
                print(f"넌 로또하지 마라. 정답은 {num}였어.")
                break

            # 1번에 성공했을 경우 메시지 출력
            if attempts == 1 and guessed_num == num:
                print("오~ 1번에 성공! 로또하러 달려가즈아!")
                break

            # 입력된 숫자가 유효한 범위인지 확인
            if guessed_num < 1 or guessed_num > 10:
                print("한글 몰라?")
            elif guessed_num < num:
                print("UP!")
            elif guessed_num > num:
                print("DOWN.")
            else:
                print("오~")  # 정답을 맞춘 경우
                break  
        except ValueError as e:
            # 숫자가 아닌 값을 입력했을 때의 처리
            print(f"{e}??????? 숫자 몰라?.")
            
# 게임 시작
num_guess()

while True:  # 게임 재시작 여부 확인
    restart = input("찐막리겜? (y/n): ").strip().lower()
    if restart == 'y':  # 게임 재시작
        num_guess()
    elif restart == 'n':  # 게임 종료
        print("잘 가시고")
        break 
    else:
        continue  # 유효하지 않은 입력 시 다시 확인
