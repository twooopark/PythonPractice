# module_test.py

import math
import mymod

# 모듈명을 앞에 붙이고 객체 사용 가능
print(math.pi)
print(mymod.divide(6,3))


r = 10

print(math.pi * r ** 2)
print(mymod.Pi * r ** 2)

# 어떤 모듈이 현재 로드되어 있는가
import sys
# 현재 로드된 모듈의 목록을 출력
# print(sys.modules)

# 모듈의 목록에 mymod가 있는가 ?
modules = sys.modules.keys()
print( "yes" if "mymod" in modules else "no")