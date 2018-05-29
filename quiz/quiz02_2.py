'''
Q2
파일명은 quiz02_2.py로 합니다.
다음과 같이 리스트가 선언되어 있다고 가정합니다.
lst = [1, 3.14, 'python', 7, 89.1, 3]
해당 리스트에서 정수형, 실수형 데이터만 추출하여 
lst_cleaned 라는 이름의 리스트에 담아 봅시다.
'''
lst = [1, 3.14, 'python', 7, 89.1, 3]
lst_cleaned = []

for item in lst:
    # if isinstance(item, lst) or isinstance(item, float) 
    #   lst_cleaned.append(item)
    if isinstance(item, (int, float)): # 축소형
        lst_cleaned.append(item)

# for i in len(lst):
#     if type(lst[i]) == int:
#         lst_cleaned.append(lst[i])
#     elif type(lst[i]) == float:
#         lst_cleaned.append(lst[i])

print(lst_cleaned)