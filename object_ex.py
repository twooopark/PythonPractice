# object_ex.py

print("0: id a: ",id(3))


# 변수에 3을 담는다.
# 3 객체를 만들고,
# 변수에 3 객체의 ID를 연결 심볼 테이블에 저장.

a = 3
print("1: id a: ", id(3))

b = 3
print("2: id b: ", id(b))

b = 4
print("3: id b: ", id(b))
print("4: a = {}, b = {}".format(a, b))
# 0, 1, 2는 같은 결과, 3은 다른 결과를 출력한다.


# 객체 심볼 테이블

g_a = 2018
g_b = "symbol"

# 글로벌 영역

def f():
    l_a = "local" 
    l_b = 5
    print(locals())

print("---------: Locals")
f()

print("---------: Globals")
print(globals())



print("f" in globals().keys())


print("---------: Object")

x = [1,2,3]

y=x
print(x==y)
print(hex(id(x)), hex(id(y)))

x[1]=4
print(y[1])

y=x[:]

print("x" , x)
print("y" , y)

x[1]=0
print(y[1])

print("---------: copy 함수 이용")
import copy

y=copy.copy(x)
print(x is y) # ==

print("x" , x)
print("y" , y)

x[1]=100

print("x" , x)
print("y" , y)

# a->b->x 같은 복합객체를 재귀적으로 생성하여 복사
print("---------: deepcopy 함수 이용")
a = [1,2,3]
b = [4,5,a]
x = [a,b,100]

print("a: " , a)
print("b: " , b)
print("x: " , x)

# y=copy.copy(x)  # a, b, x, y가 가리키던 모든 a[1]이 변경됨
y=copy.deepcopy(x)  #  독립적인 y 객체에 복사 (y의 a[1] 위치(자리(?))는 변경 안됨)
a[1] = 0


print("a: " , a)
print("b: " , b)
print("x: " , x)
print("y: " , y)
