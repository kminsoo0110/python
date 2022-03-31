# sentence = '나는 소년입니다.'
# print(sentence)

# sentence2 = "파이썬은 쉬워요."
# print(sentence2)

# sentence3 = '''나는 소년이고요,
# 파이썬은 쉬워요.''' #줄 바꾸면서까지 출력함
# print(sentence3)

#문자열 슬라이싱
# jumin = "990110-1234567"
# print("성별 : " + jumin[7]) #문자열리스트 7번째 위치만 출력
# print("연 : " + jumin[0:2]) #문자열리스터 0~1번째 위치 출력
# print("월 : " + jumin[2:4])
# print("일 : " + jumin[4:6])
# print("생년월일 : " + jumin[:6]) #처음부터 6번째직전까지 출력
# print("주민등록 뒤 7번째 자리 : " + jumin[7:]) #7부터 끝까지
# print("뒤 7자리 (뒤에부터)" + jumin[-7:]) #맨 뒤에서 7번째부터 끝까지

#문자열 처리함수
# python = "Python is Amazing"
# print(python.lower()) #모두 소문자로 출력
# print(python.upper()) #모두 대문자로 출력
# print(python[0].isupper()) #특정 문자가 대문자인지 판별
# print(len(python)) #문자열 길이 측정
# print(python.replace("Python", "Java")) #문자열 내에 특정 문자를 찾아서 교체함

# index  = python.index("n") #특정문자의 위치값 출력
# print(index) 
# index = python.index("n", index + 1) #처음 위치를 제외한 다음 발견위치 출력
# print(index)

# print(python.find("Java")) #원하는 문자열 못찾는 경우 -1뜸
# # print(python.index("Java")) #원하는 문자열 못팢는 경우 에러뜸

# print(python.count("n")) #특정 문자 발견횟수 출력

#문자열 포멧
# print("나는 %d살입니다." %20)
# print("나는 %s을 좋아합니다." %"파이썬")
# print("Apple은 %c로 시작하요." %"A")
# print("나는 %s색과 %s색을 좋아해요" %("빨간", "초록"))
# print("나는 {}을 좋아합니다".format("게임"))
# print("나는 {}{}입니다.".format("섹시","가이"))

# print("나는 {}살이며 {}색을 좋아합니다".format(20, "빨간"))

# age = 20
# color = "초록"
# print(f"나는 {age}살이며, {color}색을 좋아합니다.")

# escape 함수 정리
# print("백문이 불여일건\n백견이 불여일타") #\n : 줄바꿈
# print("저는 \"케인\"입니다")
# print("저는 \'케인\'입니다")

# \\ : 문장내에서 \ 쓰임
# print("D:\\Users")

# \r : 커서를 맨 앞으로 이동
# print("Red apple\rPine")

# \b : 백스페이스 (한 글자 삭제)
# print("Redd\bapple")

# \t : 탭(8칸 이동)
# print("Red\tapple")