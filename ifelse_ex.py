# ifelse_ex.py

n = -2

if n>0:
    print("양수")
elif n<0:
    print("음수")
else:
    print("0")


# if는 중첩사용 가능하다
# 조건이 여러개일 경우, and, or 등 논리연산자를 이용하여 조건을 조합할 수 있다.

# 조건 표현식
# Java, C의 3항 연산과 비슷

money = 12000
print("by taxi" if money > 10000 else "by bus")


money = 0
print("by taxi" if money > 10000 else "by foot" if money == 0 else "by bus")


# in / not in: 포함 관계를 나타내는 연산
# 리스트 내포도 같이 해 봅시다.
source = [x for x in range(1,100,2)] #리스트 내포
print(source)
if 2 in source :
    print("2를 포함하고 있다.")
else :
    print("2를 포함하고 있지 않다.")


