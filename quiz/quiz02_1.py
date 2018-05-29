'''
Q1
파일명은 quiz02_1.py로 저장합니다.
키보드로 정수를 입력 받습니다.
만일 입력받은 값이 정수 형태가 아니면 "정수가 아닙니다"를 출력하고 다시 입력을 받습니다.
만일 입력받은 값이 정수라면 1부터 해당 입력값까지의 정수 중에서 3의 배수만 합산하여 출력합니다.
(결과)

수를 입력하세요:abc
정수가 아닙니다. 다시 입력하세요
수를 입력하세요:100
1부터 100까지 3의 배수의 합 = 1683
'''

while True:
    num = input("수를 입력하시오:")

    if num.isdigit():
        break
    print("정수가 아닙니다. 다시 입력하세요")

total = 0
to = int(num) # 정수화
for i in range(1, to+1): # 1부터 num까지
    if i%3 == 0:
        total += i

print("1부터 {}까지 3의 배수의 합 = {}".format(to, total))