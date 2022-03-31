# cabinet = {3 : "유재석", 100 : "조세호"}
# # print(cabinet[3])
# print(cabinet[100])

# print(cabinet.get(3))
# # print(cabinet[5]) #에러뜸
# print(cabinet.get(5)) #None 출력하고 계속 이어나감
# print(cabinet.get(5, "사용 가능")) 

# print(3 in cabinet) #True
# print(5 in cabinet) #False

# 새 손님
cabinet = {"A-3" : "유재석", "B-100" : "조세호"}
print(cabinet)
cabinet["A-3"] = "김성근" #value 값 업데이트
cabinet["C-20"] = "케인인님"
print(cabinet)

# 간 손님
del cabinet["A-3"]
print(cabinet)

# key만 출력
print(cabinet.keys())

# value만 출력
print(cabinet.values())

# 쌍으로 출력
print(cabinet.items())

# 사전 삭제
cabinet.clear()
print(cabinet)