def write01():
    # 텍스트 파일 쓰기
    f = open('./sample/test.txt', 'w', encoding="utf-8")
    size = f.write("Life is too short, you need Python") # 내용을 쓰고 길이를 반환
    print("write size: {}".format(size))
    f.close() # 열었으면 꼭 닫아야 한다.

# write01()


def read01():
    # 텍스트 파일 읽기
    f = open("./sample/test.txt", 'r', encoding="utf-8")
    text = f.read()
    print(text)
    f.close()

# read01()

def write02():
    # 여러줄 만들어 봅시다
    f = open('./sample/multilines.txt', 'w', encoding="utf-8")
    for i in range(1,10):
        f.write("Line %d\n" %i)
    f.close() # 열었으면 꼭 닫아야 한다.

# write02()

def read02():
    # 여러줄 읽기
    f = open('./sample/multilines.txt', 'r', encoding="utf-8")
    lines = f.readlines()
    print(lines)

    line = lines[5]
    print(line)

    f.close()

# read02()


'''
샘플 디렉토리 안에 sanbuk.csv 파일을 열고
각 줄을 dict으로 만들고 리스트(members)에 저장해 봅시다.
'''


def slamdunk():
    f = open("./sample/sangbuk.csv", 'r', encoding="utf-8")
    members = [] # 리스트 생성
    while True:
        line = f.readline()
        if not line:
            break
        line = line.strip().replace(" ", "") # 양 끝의 공백, 중간의 공백 제거
        info = line.split(",") # 각 줄을 컴마로 구분하여 자름
        member = {"name":info[0], "number":info[1], "height":info[2], "position":info[3]}
        members.append(member)
    print(members) 
    f.close()

# slamdunk()

# 바이너리 파일 다루기 모드: b
def binfile():
    f = open("./sample/rose-flower.jpeg", 'rb')
    data = f.read()
    f.close()
    
    f = open("./sample/rose-flower-copy.jpeg", 'wb')
    f.write(data)
    f.close()

# binfile()    


def safe_file():
    # 파일은 open 하면 반드시 닫아줘야 하는데
    # with ~ as 를 이용하면 파이썬이 사용 후 닫아준다
    with open('./sample/multilines.txt', 'r') as f:
        for line in f.readlines():
            print(line, end="")
        
    # f가 닫혀있는지 확인
    print(f.closed)

safe_file()
