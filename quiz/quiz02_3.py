'''
Q3
파일명은 quiz02_3.py로 합니다.
메서드를 하나 만들고, 임의의 개수의 인수를 받아서 해당 인수의 합, 최대값, 최소값, 평균값을 한꺼번에 반환하는 함수를 만들어 봅시다.
(함수 사용 예)
total, maxval, minval, avg = summary(80, 75, 90, 95, 85)
print(total, maxval, minval, avg)

(결과)
425 95 75 85.0
'''

def summary(*args):
    data = []
    total = 0
    for argv in args:
        if isinstance(argv, (int,float)):
            data.append(argv)
            total += argv
    return total, max(data), min(data), total/len(args)
    
# print(summary(80, 75, 90, 95, 85))
total, maxval, minval, avg = summary(80, 75, 90, 95, 85)
print(total, maxval, minval, avg)