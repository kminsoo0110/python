# 표준입출력
# print("Python", "Java", "Javascript", sep = ",", end ="?")
# print("무엇이 더 재밌을까요?")

# import sys 
# print("Python", "Java", file = sys.stdout) # 표준 출력
# print("Python", "Java", file = sys.stderr) # 표준 에러 처리해줄수 있다

# 자리 정렬
# scores = {"수학" : 0, "영어" : 50, "코딩" : 100}
# for subject, score in scores.items() : # 쌍으로 받음
#     # print(subject, score)
#     print(subject.ljust(8), str(score).rjust(4), sep = ":") # 8개 공간 만들고 왼쪽으로 정렬

# 은행 대기순번표
# 001, 002, 003
# for num in range(1,21,1) :
    # print("대기번호 : " + str(num).zfill(3)) # 3만큼 크기에 값이 없는 부분을 0으로 채워줌    
    
# 표준 입력
answer = input("아무 값이나 입력하세요 : ")
print(type(answer))
# print("입력하신 값은 {}입니다".format(answer))