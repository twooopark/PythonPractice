# 문장에 총 몇 개의 알파벳 글자가 사용되었는지 판별해 봅시다.
'''
Instruction:

이 문자열 내의 글자를 모두 소문자로 변경합니다.
이 문자열 내의 공백과 ,를 제거합니다.
이 문자열을 list로 형변환한 후 lst 변수에 담아 봅니다.
lst를 set로 형변환하여 chars 변수에 담아 봅시다.
chars를 화면에 출력해 봅시다.
chars를 다시 list로 형변환하여 lst에 담아 봅시다.
lst를 알파벳 순으로 정렬하고, 길이를 출력해 봅시다.
'''

str = "Life is too short, You need Python"

str = str.lower()
print(str) 

str = str.strip().replace(" ","")
print(str) # 양 끝 공백 제거, 중간 공백 제거

lst = list(str.lower().strip().replace(" ","").replace(",","")) 
print(lst)

chars = set(lst)
print(chars)

lst = list(chars)
print(lst)

lst.sort()
print(lst)
print("Size: ", len(lst))


