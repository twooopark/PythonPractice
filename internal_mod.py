# internal_mod.py

# sys module
# python interpreter's info * func
# argv


import sys

def argv_f():
    print(sys.argv)
    args = sys.argv[1:]
    print("args:",args)
# argv_f()

def env_f():
    print(sys.platform)
    print(sys.version)
    print(sys.path)
# env_f()



# random module

import random

print(random.random()) # 0 ~ 1사이 실수 난수
print(random.randint(1,6)) # 1 ~ 6 범위 지정 정수 난수

# 랜덤 유틸리티 함수
seq = ["짬뽕", "짜장면", "짬짜면"]
# seq = range(1,15,3) #TypeError: 'range' object does not support item assignment
# 이 리스트를 섞어 봅시다: shuffle
random.shuffle(seq)
print(seq)

# 순차형에서 임의의 한개 객체 반환
print(random.choice(seq))

# Sampling
print(random.sample(range(1,46),6))
