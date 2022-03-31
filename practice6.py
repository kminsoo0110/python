# if문
# weather = input("오늘 날씨 어때요? : ")
# if weather == "비" or weather == "눈":
#     print("우산 챙기세요")
# elif weather == "미세먼지" :
#     print("마스크 챙기세요")
# else :
#     print("준비물 필요없음")

# temp = int(input("기온을 어때요? "))
# if temp >= 30 :
#     print("나가지 마세요 덥습니다")
# elif temp >= 10 and temp < 30 :
#     print("나가도 됩니다")
# elif temp >= 0 and temp < 10 :
#     print("패딩 챙기세요")
# else :
#     print("나가지 마세요 춥습니다.")

# 반복문 for문
# for waitng_no in range(1, 6) : # 1,2,3,4,5
#     print("대기번호 : {}".format(waitng_no))

# starbucks = ["아이언맨", "토르", "그루트"]
# for customer in starbucks :
#     print("{}님, 커피가 준비되었습니다.".format(customer))

# 반복문 while문
# customer = "토르"
# index = 5

# while index >= 1 :
#     print("{}, 커피가 준비되었습니다 {}번 남았어요.".format(customer, index))
#     index -= 1
#     if index == 0 :
#         print("커피는 폐기처분되었습니다.")

# customer = "아이언맨"
# index = 1
# while True :
#     print("{}, 커피가 준비되었습니다 호출 {}회.".format(customer, index))
#     index += 1

# customer = "토르"
# person = "Unknown"

# while person != customer :
#     print("{}, 커피가 준비되었습니다.".format(customer))
#     person = input("어떻게 되나요 : ")

# print("맛있게 드세요~")

# continue, break 명령어
# absent = [2,5] # 결석학생
# no_book = [7] # 책을 깜박함
# for student in range(1,11,1) : # (1 ~ 10)
#     if student in absent :
#         continue # 다음 반복 진행
#     elif student in no_book :
#         print("오늘 수업 여기까지, {}는 교무실로 따라와".format(student))
#         break # 반복문 강제 종료
#     print("{}, 책을 읽어봐".format(student))

# for문 한 문장으로 써보기
# students = range(1,6)
# students = list(students)

# students = [i+100 for i in students]
# print(students)

# 학생 이름을 길이로 변환
# students = ["Iron Man", "Thor", "I am groot"]
# students = [len(i) for i in students]
# print(students)

# 학생 이름을 대문자로 변환
# students = ["Iron Man", "Thor", "I am groot"]
# students = [i.upper() for i in students]
# print(students)