# pickle_ex.py

# Pickle 모듈은 객체를 파일에 썼다가 나중에 복원할 수 있도록 객체를 바이트 스트림으로 직렬화
# 원하는 객체를 형태 변환 없이 쉽게 쓰고 읽을 수 있다
import pickle 

def pwrite01():
    f = open("./sample/players.bin", "wb")
    data = { "baseball": 9 }
    pickle.dump(data, f)    # file에 객체를 저장하고자 할 때에는 dump 메서드를 이용한다
    f.close()

# pwrite01()

def pread01():
    f = open("./sample/players.bin", "rb")
    data = pickle.load(f)   # file에 객체로부터 객체를 불러올 때에는 load 메서드를 이용한다
    f.close()
    print(data, type(data))

# pread01()


def pwrite02():
    # 복수의 객체 저장
    with open("./sample/players.bin", "wb") as f:
        pickle.dump({"baseball": 9}, f, 1)   # dump 메서드에 프로토콜 버전을 정의해 줄 수 있다
        pickle.dump({"basketball": 5}, f, 3)   
        pickle.dump({"soccer": 11}, f, pickle.HIGHEST_PROTOCOL)   # 최신 프로토콜 버전을 확인하려면 pickle.HIGHEST_PROTOCOL로 확인
    

# pwrite02()


def pread02():
    # 복수의 객체 복원
    with open("./sample/players.bin", "rb") as f:
        print(pickle.load(f))
        print(pickle.load(f))
        print(pickle.load(f))

# pread02()



def pread03():
    # 복수의 객체 복원
    with open("./sample/players.bin", "rb") as f:
        data_list = []
        while True:
            try:
                data = pickle.load(f)
            except EOFError:
                break
            else:
                data_list.append(data)
        
        print(data_list)

pread03()

