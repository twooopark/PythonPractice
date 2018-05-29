# 클래스 만들기
class Point:
    Instance_count = 0 # 0으로 define 해야함
    # 생성자
    def __init__(self, x = 0, y = 0):
        self.x, self.y = x, y
        Point.Instance_count += 1 # 클래스 영역의 접근
    # 소멸자
    def __del__(self):
        Point.Instance_count -= 1 
    # __str__
    def __str__(self):
        return "Point x = {}, y = {}".format(self.x, self.y)
    # __repr__
    def __repr__(self):
        return "Point ({}, {})".format(self.x, self.y)
        
    # 인스턴스 메서드
    def setX(self, x):
        self.x = x
    def getX(self):
        return self.x
    def setY(self, y):
        self.y = y
    def getY(self):
        return self.y


def bound_method():
    p = Point()
    p.setX(10)
    p.setY(10)

    print(p.getX(), p.getY(), sep = ", ")
    print(p.getX, p.getY)
# <bound method Point.getX of <__main__.Point object at 0x02F1D6F0>> <bound method Point.getY of<__main__.Point object at 0x02F1D6F0>>


def unbound_method():
    p = Point()
    Point.setX(p, 10)
    Point.setY(p, 10)
    print(Point.getX(p), Point.getY(p), sep=", ")
    print(Point.getX, Point.getY)
# <function Point.getX at 0x031880C0> <function Point.getY at 0x03188150>
 
if __name__ == "__main__": # point.py에서 실행될 때
    bound_method()
    unbound_method()

    