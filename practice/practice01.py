
def q1():
    num = input("수를 입력하세요: ")
    try:
        num = int(num)
        if num % 3 == 0 :
            print("3의 배수 입니다.")
        else:
            print("3의 배수가 아닙니다.")
    except Exception as e:
        print("정수가 아닙니다.")
    exit(0)
# q1()

def q2():
    num = input("수를 입력하세요: ")
    try:
        num = int(num)
        if num % 2 == 0 :
            print("짝수입니다.")
        else:
            print("홀수입니다.")
    except Exception as e:
        print("정수가 아닙니다.")
    exit(0)
# q2()

def q3():
    s = '/usr/local/bin/pyhon'
    splits = s.strip("/").split("/")
    print(splits)

    splits = s.rsplit("/", 1)
    print(splits)
# q3()

def q4():
    lst = [1, 5, 4, 8, 6, 11, 12, 18, 54, 24, 36, 7, 17]
    cnt, sum = 0, 0
    for i in lst:
        if i % 3 == 0:
            cnt += 1
            sum += i
    print("주어진 리스트에서 3의 배수의 개수=> ", cnt)
    print("주어진 리스트에서 3의 배수의 합=> ", sum)
# q4()

def q5():
    lst = [50000, 10000, 5000, 1000, 500, 100, 50, 10, 5, 1]
    coin = input("금액")
    coin = int(coin)
    l = []
    for i in range(0, len(lst)):
        l.append(0)
    while coin > 0 :
        for i in range(0, len(lst)):
            while coin - lst[i] > -1 :
                coin -= lst[i]
                if l[i] == 0:
                    l[i] = 1
                else:
                    l[i] += 1   
    
    for i in range(0, len(lst)):
        print("{}원: {}개".format(lst[i],l[i]))
# q5()

def q6():
    l = []
    for i in range(0,5):
        s = input()
        l.append(int(s))
    print(sum(l)/len(l))       
# q6()

def q7():
    s = input("입력>")
    print("".join(reversed(s)))
# q7()

def q8():
    m = input('메뉴: ')
    menu = {}
    menu['오뎅'] = {"price":300}
    menu['순대'] = {"price":400}
    menu['만두'] = {"price":500} 

    print('가격: {}'.format(menu[m]["price"]))
# q8()

def q9():
    def sum(*args):
        result = 0
        for i in args:
            result += i
        return result
    print(sum(1, 2, 3, 4, 5))
    print(sum(1, 3, 5, 7, 9, 11))
    print(sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
# q9()

def q10():
    s = ""
    for i in range(1,100):
        cnt = 0
        if i < 10 and i % 3 == 0: 
            cnt += 1
        if i >= 10 and int(i/10)%3==0 and (i-int(i/10)*10)!=0:
            cnt += 1
        if i >= 10 and i%10%3 == 0:
            cnt += 1
        if cnt > 0:
           print("\n",i," ",end="")
           for i in range(0,cnt):
               print("짝", end="")
# q10()

def q11():
    num = input("숫자를 입력하세요: ")
    sum = 0
    for i in range(1,int(num)+1):
        if i%2 == int(num)%2:
            sum += i
    print("결과 값 : ",sum)
q11()

