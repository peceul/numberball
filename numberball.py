# Python 스크립트 파일로 만든 숫자야구 게임

import random as rd
import sys

total_list = []
number = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

chance = 35 # 입력 기회 설정
count = 0 # 입력 소모 횟수 체크
sc = 0 # 스트라이크 카운트
bc = 0 # 볼 카운트

# 컴퓨터가 뽑은 숫자 변수 초기화
cn1 = "0"
cn2 = "0"
cn3 = "0"
cn4 = "0"
cn5 = "0"
select_num = "0"

def reg_list(ch, in_number, rs) :
    total_list.append([ch, in_number, rs])

def show_list() :
    for c in total_list :
        print(c[0], "회 : ", c[1], " / 결과 : ", c[2], sep="")

while True :
    try :
        if count >= chance : # 입력 횟수 35회 체크
            print("입력 제한 횟수 35회를 모두 사용하여 새 게임이 시작 됩니다.")
            count = 0
            sc = 0
            bc = 0
            number = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
            continue
        print("맞춰볼 숫자 5자리를 입력해주세요. (10234 ~ 98765) (남은 기회 : ", (chance - count), ")", sep="")
        input_num = input()
        if input_num.isdecimal() == False : # 숫자인지 검증
            raise ValueError
        if int(input_num) < 10234 or int(input_num) > 98765 : #숫자범위 체크
            raise ValueError
        # 각 자리수 별로 숫자 추출
        in1 = input_num[0]
        in2 = input_num[1]
        in3 = input_num[2]
        in4 = input_num[3]
        in5 = input_num[4]
        # 중복 숫자 입력 여부 확인
        if (in1 == in2 or in1 == in3 or in1 == in4 or in1 == in5 or
            in2 == in3 or in2 == in4 or in2 == in5 or
            in3 == in4 or in3 == in5 or in4 == in5) :
            print("-" * 100)
            show_list()
            print("-" * 100)
            print("자릿수 중에 중복된 숫자가 입력되었습니다. 입력하신 숫자 : " + input_num, sep = "")
            print("=" * 100)
            continue
        # 컴퓨터가 조건에 맞는 랜덤 숫자를 뽑는다.
        if count == 0 : # 처음시작 할 때 한번만 컴퓨터 숫자를 뽑음
            cn1 = number.pop(rd.randint(1, 9))
            cn2 = number.pop(rd.randint(0, 8))
            cn3 = number.pop(rd.randint(0, 7))
            cn4 = number.pop(rd.randint(0, 6))
            cn5 = number.pop(rd.randint(0, 5))
            select_num = cn1 + cn2 + cn3 + cn4 + cn5
        # print(select_num) # 컴퓨터 번호 체크
        # 입력한 번호와 컴퓨터의 번호를 숫자 마다 1:1로 체크한다.
        # 스트라이크 카운트
        if in1 == cn1 : sc += 1
        if in2 == cn2 : sc += 1
        if in3 == cn3 : sc += 1
        if in4 == cn4 : sc += 1
        if in5 == cn5 : sc += 1
        # 볼카운트
        if in1 == cn2 or in1 == cn3 or in1 == cn4 or in1 == cn5 : bc += 1
        if in2 == cn1 or in2 == cn3 or in2 == cn4 or in2 == cn5 : bc += 1
        if in3 == cn1 or in3 == cn2 or in3 == cn4 or in3 == cn5 : bc += 1
        if in4 == cn1 or in4 == cn2 or in4 == cn3 or in4 == cn5 : bc += 1
        if in5 == cn1 or in5 == cn2 or in5 == cn3 or in5 == cn4 : bc += 1
        count += 1 # 시도 횟수 1 증가
        if input_num == select_num : # 번호를 맞춘 경우
            print("축하합니다. 번호를 맞추셨습니다.\n최종 시도 횟수 : ", count, "회", sep="")
            print("번호 :", select_num)
            print("=" * 100)
            retry = input("새 게임을 진행하시려면 Y 또는 y를 입력해주시고, 그만 하시려면 아무키나 입력해주세요. ")
            if retry == "Y" or retry == "y" :
                count = 0
                sc = 0
                bc = 0
                number = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
                total_list = []
                continue
            else :
                print("프로그램을 종료합니다.")
                sys.exit(0)
        elif sc == 0 and bc == 0 : # 번호를 맞추지 못한 경우
            print("-" * 100)
            show_list()
            print("-" * 100)            
            print(count, "회 / 입력한 숫자 : ", input_num, " / 결과 : 아웃")
            print("=" * 100)
            reg_list(count, input_num, "아웃")
            sc = 0
            bc = 0
        else : # 번호를 맞추지 못한 경우
            print("-" * 100)
            show_list()
            print("-" * 100)
            print(count, "회 / 입력한 숫자 : ", input_num, " / 결과 : ", sc, "스트라이크 ", bc, "볼", sep="")
            print("=" * 100)
            reg_list(count, input_num, str(sc) + "스트라이크 " + str(bc) + "볼")
            sc = 0
            bc = 0
    except ValueError as e:
        print("-" * 100)
        show_list()
        print("-" * 100)  
        print("잘못된 숫자나 값을 입력하였습니다.")
        print("=" * 100)
