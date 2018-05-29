# format_ex.py
# 문자열 서식

# 서식 문자
'''
%s 문자열 (string)
%c 문자 1개 (character)
%d 정수 (integer)
%f 부동 소수 (floating point)
%o 8진수
%x 16진수
%% Literal %
'''

formay = "I have %d apples"
print(format % 10)

print("Interest Rate is %.2f%%" % 1.24)

# 두 개 이상의 값을 넣고 싶을 때 
format = "total : %d개, get: %d 개"
print(format % (10, 3))

# formmat과 값의 형식이 일치하지 않으면 TypeError 발생


#고급 문자열 포매팅
format_str = "I have {} apples, and I ate {} apples."
print(format_str.format(5,3))


#서식에 설정된 공간의 개수보다 실제 값의 개수가 적으면 IndexError 발생
print(format_str.format(10,3,1))
#print(format_str.format(10)) # Tuple IndexError

# 이름 기반의 포맷
format_str = "I have {total} apples, and I ate {num} apples."
print(format_str.format( total = 5, num = 3))
# print(format_str.format( total = 5)) # keyError

# dict 객체를 이용한 포맷
print(format_str.format_map("total":5, "num":2))