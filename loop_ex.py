# loop_ex.py

# for문 : for ... in (객체)
for i in range(1, 10 ,2 ):
    print(i, end= ",")
else : # 루프가 종료 없이 끝났을 때
    print()

# 시퀀스 객체를 이용한 for문
animals = ['dog','cat','cow','tiger']

for animal in animals : 
    print(animal, end =',')

else:
    print()


# enumerate를 이용한 루프
for index, value in enumerate(animals):
    print(index, value)



# while문
sum, i = 0, 1

while i <= 1000:
    sum += i
    i += 1

print("sum: ", sum)












