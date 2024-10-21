class Person:
    def __init__(self, name, gender, age):
        self.name = name
        self.age = age
        self.gender = self.validate_gender(gender)  # 성별 유효성 검사 추가

    def validate_gender(self, gender):
        if gender.lower() in ["male", "female"]:
            return gender.lower()
        else:
            raise ValueError("'male' 오아 'female'")  # 유효하지 않은 성별 입력에 대한 예외 처리

    def display(self):
        gender_display = "남성" if self.gender == "male" else "여성"
        print(f"이름: {self.name}, 성별: {gender_display}")
        print(f"나이: {self.age}")

    def greet(self):
        if self.age < 18:
            print("알림장 썻니?")
        elif self.age < 36:
            print("요~맨~")
        else:
            print("안녕하세요, 어르신!")

# 사용자 입력 받기
name = input("이름을 입력하세요: ")
gender = input("성별을 입력하세요 (male 또는 female): ")
age = int(input("나이를 입력하세요: "))

try:
    person = Person(name, gender, age)  # Person 객체 생성
    person.display()  # 정보 출력
    person.greet()  # 나이에 맞는 인사 메시지 출력
except ValueError as e:
    print(e)
