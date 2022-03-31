# Quiz) 표준 체중을 구하는 프로그램을 작성하시오.vars

# * 표준 체중 : 각 개인의 키에 적당한 체중

# (성별에 따른 공식)
# 남자 : 키(m) * 키(m) * 22
# 여자 : 키(m) * 키(m) * 21

# 조건 1 : 표준 체중은 별도의 함수 내에서 계산
#     * 함수명 : std_weight
#     * 전달값 : 키(height), 성별(gender)
# 조건 2 : 표준 체중은 소수점 둘째자리까지 표시

# (출력 예제)
# 키 175cm 남자의 표준 체중은 67.38kg 입니다.


# def std_weight(height, gender) :
#     if (gender == "남자") :
#         weight = ((height * height)/10000) * 22
#         return weight
#     else :
#         weight = ((height * height)/10000) * 22
#         return weight

# height = 175
# gender = "남자"
# weight = std_weight(height, gender)

# print("키 %dcm %s의 표준 체중은 %.2f입니다."%(height, gender, weight))

# 나도 코딩 풀이
def std_weight(height, gender) : # 키 m 단위(실수), 성별 "남자", "여자"
    if gender == "남자" :
        return height * height * 22
    else :
        return height * height * 21
    
height = 175 # cm 단위
gender = "남자"
weight = round(std_weight(height / 100, gender), 2) # 소수점 둘째짜리까지 출력하게 도와줌
print("키 {}cm {}의 표준 체중은 {}kg 입니다.".format(height, gender, weight))