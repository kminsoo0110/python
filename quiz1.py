# (Quiz) 변수를 이용하여 다음 문장을 출력하시오

# 변수명
#     : station
    
# 변수값
#     : "사당", "신도림", "인천공항" 순서대로 입력
    
# 출력문장 
#  : XX 행 열차가 들어오고 있습니다.

# 풀이1
station = ["사당", "신도림", "인천공항"]

# i = 0

# while i<3 :
#     print(station[i] + "행 열차가 들어오고 있습니다.")
#     i += 1
    
# 풀이2

i = 0
for i in range(0,3,1) :
    print("{} 행 열차가 들어오고 있습니다.".format(station[i]))