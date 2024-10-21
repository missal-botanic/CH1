class Person:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

    def display(self):
        print(f"이름: {self.name}, 성별: {self.gender}")
        print(f"나이: {self.age}")

# 사용자 입력 받기
name = input("이름을 입력하세요: ")
gender = input("성별을 입력하세요 (male 또는 female): ")
age = int(input("나이를 입력하세요: "))

person = Person(name, gender, age) # Person 객체 생성

person.display() # 정보 출력