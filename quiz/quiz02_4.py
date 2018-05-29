'''
Q4
파일명은 quiz02_4.py로 합니다.
다음과 같이 문자열이 설정되어 있습니다.
s = """We encourage everyone to contribute to Python. 
If you still have questions after reviewing the material
in this guide, then the Python Mentors 
group is available to help guide new contributors through the process."""
문자열에서 ',', '.', '\n'을 제거하고 모두 대문자로 변경합니다.
변경된 소스를 기반으로 단어의 빈도수를 체크해 봅시다.

'''
s = """We encourage everyone to contribute to Python. 
If you still have questions after reviewing the material
in this guide, then the Python Mentors 
group is available to help guide new contributors through the process."""

s = s.replace(",","").replace(".","").replace("\n","").upper()
print(s)


temp = {}
splits = s.split()
print(splits)

for split in splits:
    if split in temp.keys():
        temp[split] += 1
    else:
        temp[split] = 1

for key, value in temp.items():
    print("{}: {}".format(key, value))



