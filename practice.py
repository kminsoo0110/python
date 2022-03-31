# # 애완동물을 소개해주세요
# animal = "고양이" #string
# name = "연탄이"
# age = 2 #integer
# hobby = "낮잠"
# is_adult = age >= 3 #boolean

# 문자열 간단다루기
# print("우리집 " + animal + "의 이름은 " + name +"에요")
# # print(name + "는 "+ str(age) + "살이며, " + hobby + "을 아주 좋아해요") #함수써야함
# print(name, "는 ", age, "살이며, ", hobby, "을 아주 좋아해요") #함수 안써도됨
# print(name +"는 어른일까요? " + str(is_adult))

# print(1+1)
# print(3>5)
# print((3>0) or (1<0))

# 숫자처리함수
# print(abs(-5)) #abs함수는 절대값함수 absolute
# print(pow(4,2)) #제곱함수 16 power
# print(max(5,12)) #2개 숫자중 하나가 큰거 출력
# print(min(5,12)) #2게 숫자중 하나가 작은거 출력
# print(round(3.14)) #소수점 1의자리를 계산하여 반올림해서 정수로 변환

# from math import *
# print(floor(4.99)) #4, 내림함수
# print(ceil(3.14)) #4, 올림함수
# print(sqrt(16)) #4, 제곱근함수, 셋다 math 라이브러리를 import한다.

# 랜덤함수
from random import *

# print(random()) # random() 0.0 ~ 1.0 미만의 임의의 숫자를 출력
# print(random() * 10) #0.0 ~ 10.0미만의 임의의 숫자를 출력
print(int(random() * 10)) #0 ~ 10미만의 임의의 숫자를 출력
print(int(random() * 10) + 1) #1 ~ 10미만의 임의의 숫자를 출력

print(randrange(1, 46)) #1 ~ 46미만의 임의의 숫자를 출력
print(randint(1, 45)) #1 ~ 45이하의 임의의 숫자를 출력


