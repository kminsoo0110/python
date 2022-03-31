# Quiz 3) 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오

# ex) http://naver.com

# 규칙1 : http:// 부분은 제외 => naver.com
# 규칙2 : 처음 만나는 점(.) 이후 부분 제외 => naver
# 규칙3 : 남은 글자중 처음 세자리 + 글자 개수 + 글자 내 'e' 개수 + "!"로 구성

# ex) 생성된 비밀번호 : nav51!

# pwd = "http://naver.com"
# pwd = pwd[7:] 
# pwd = pwd[:5]

# cou3 = pwd[0:3]
# len_naver = len(pwd)
# count_e = pwd.count("e")

# pwd = cou3 + str(len_naver) + str(count_e) + "!"

# print(pwd)

# 나도코딩 풀이
url = "http://naver.com"
my_str = url.replace("http://", "")
my_str = my_str[:my_str.index(".")]
password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"

print(password)