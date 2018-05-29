# func_ex.py

# function
def dummy():
    pass

def print_hello():
    print("Hello World")

def times(a, b):
    return a * b

def do_nothing():
    return

t = times
print(t(100, 100))
print(t, times, sep = ",")


# 함수의 인자 전달
print("---------: args")

def func1(t):
    t[0] *=2

a = [1,2,3]
func1(a)
print("a: ", a)


# imutable 을 넘겼을 때는 오류가 발생할 것
# func1( (1,2,3) ) #Type Error


# 함수의 계산
print("---------: 함수의 계산")
def func2(t):
    if isinstance(t, list):
        t[0] *= 2
        return True
    else:   
        return False

result = func2(a)
print(result, a)

result = func2((1,2,3))
print(result)
    

# 함수 인수는 필요한 개수만큼 만들 수 있다

# 기본값을 따로 미리 선언할 수 있다
print("---------: 함수의 기본값 인자")
def incr(a, step=1):
    return a + step
a = 10
print(incr(a))
print(incr(a,3))


# 가변 인수
# 정해지지 않은 개수의 인수값을 받아 사용할 때: *
print("---------: 함수의 가변 인자")
def get_total(*args):
    sum = 0
    for num in args :
        sum += num
    return sum

print(get_total(1,2,3,4,5))
print(get_total(1,3,5,7,9,11,13,2,4,6,8))


# 사전 키워드 전달: **
print("---------: 함수의 사전 키워드 전달")
def f(a, b, *args, **kwd):
    print(a, b)
    print(args)
    print(kwd)

print(": f(10,20)\n", f(10,20))
print(": f(10,20,30,40)\n", f(10,20,30,40))
print(": f(10,20,30,40,option1=1,option2=2)\n", f(10,20,30,40,option1=1,option2=2)) # option1,2는 키워드 변수

# 함수도 객체다
print("---------: 함수도 객체")
def plus(a,b):
    return a+b

def minus(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    return a/b

print(plus(10,20))
print(minus(10,40))

print(type(minus))


print("---------: 함수 인자")
def apply(a, b, *funcs):
    for func in funcs:
        #if is instance(func, function)
        print(func.__name__, func(a, b))
apply(1,2,plus,minus)

# 익명 함수(lambda)
print("---------: 익명 함수(Lambda)")
def apply2(a,b,func=plus):
    return func(a, b)

print(apply(2, 3))  # func = plus
print(apply(2, 3, multiply)) # func = multiply

print(apply(2, 3, lambda a, b: a+b)) 
print(apply(2, 3, lambda a, b: 2*a+b))

# 람다를 이용한 정렬
# 리스트 등 시퀀스 자료형 정렬할 때 key
print("---------: 익명 함수(Lambda)를 이용한 정렬")
strings = ["Hello", "World", "Python", "Java"]
strings.sort()
print(strings)
strings.sort(key = lambda x : len(x))
print("길이와 "strings)

