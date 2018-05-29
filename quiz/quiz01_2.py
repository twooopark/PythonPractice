'''
Q2
리스트의 인덱스, 슬라이스, 치환에 관한 퀴즈입니다.
파일명은 quiz01_2.py로 저장합니다
다음과 같이 리스트가 선언되어 있습니다.
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
리스트 내부의 순서를 일부 뒤집어 다음과 같은 결과를 만들고자 합니다.
[1, 2, 3, 7, 6, 5, 4, 8, 9, 10]

Instruction:

리스트로부터 [4, 5, 6, 7]을 추출하여 slice 에 담아 봅시다.
slice의 순서를 뒤집어 봅시다.
lst의 적절한 부분에 slice를 끼워 넣어 봅시다.
'''

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
i, j = 3, 6
while True:
    if i == j:
        break
    slice = lst.pop(j)
    lst.insert(i, slice)
    i += 1

print(lst)