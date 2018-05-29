# paint.py
from point import Point # point 모듈에서 Point 객체 불러오기

p1 = Point(10, 10)
p2 = Point(20, 20)

print(p1)   # <point.Point object at 0x0321D6B0> 
print(p2)   #--> __str__ 오버라이딩
            #--> Point x = 10, y = 10
print("repr: ", repr(p1))
print("repr: ", repr(p2))

print("Instance Count: ", Point.Instance_count)
print("Instance Count: ", Point.Instance_count)

# repr의 용도(str과의 차이점: eval을 통한 객체 생성)
p2_copy = eval(repr(p2)) #eval(p2) --> #TypeError: eval() arg 1 must be a string, bytes or code object
print("p2_copy :", p2_copy)

