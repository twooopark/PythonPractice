# # exception_ex.py

# def try_f1():
#     try:
#         lst = [1, 3 ,5, 7, 9]
#         lst[5] # IndexError
#     except:
#         print("Error")

# try_f1()

# def try_f2():
#     try :
#         Value = int("10a")  
#     except Exception as e:
#         print("Exception e:", e)
#         print("type e:", type(e))
# # try_f2()

# def try_f3():
#     # result = 4 / 0 # ZeroDevisionError

def example():
    num1 = input("첫번째 숫자를 입력하시오.")
    num2 = input("두번째 숫자를 입력하시오.")

    try: # Do Something
        num1 = int(num1)
        num2 = int(num2) #(int)num2
        result = num1/num2
    except ValueError as e: # Do Something when {발생오류} occurred
        print("정수형이 아니다")
    except ZeroDivisionError as e:
        print("0으로는 나눌 수 없다")
    except Exception as e:
        print("e:",e)
    else:   # 예외가 발생하지 않은 경우 실행
        print("{} / {} = {}".format(num1, num2, result))
    finally:    # 예외 발생 여부와 상관 없이 마지막에 항상 수행
        print("예외처리 예제")

# example()

# 특정 경우에는 일부러 예외를 발생시키기도 한다.
def beware_dog(animal):
    if animal == "dog" :
        raise RuntimeError("멍멍") # 예외 발생
    else:
        print("어서오세요")

try:
    beware_dog("cow")
    beware_dog("cat")
    beware_dog("dog")
except RuntimeError as e:
    print(e)
    print(type(e))


