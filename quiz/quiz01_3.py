'''
Q3
리스트와 사전을 다루는 퀴즈입니다.
다음과 같이 사전을 포함한 리스트가 선언되어 있습니다.
두 학생의 kor, eng, math 합계 점수와 평균을 
사전 데이터에 "total", "average" 키값으로 넣어 봅시다.
'''
students = [
    {   
        "name": "Kim",
        "kor": 80,
        "eng": 90,
        "math": 80
    },
    {   
        "name": "Lee",
        "kor": 90,
        "eng": 85,
        "math": 85
    }
]

for student in students:
    total = student.get("kor") + student.get("eng") + student.get("math")
    average = total / 3
    student["total"] = total
    student["average"] = average

print(students)