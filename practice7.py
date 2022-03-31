# 함수 정의
def open_account() : 
    print("새로운 계좌가 생성되었습니다.")
    
def deposit(balance, money) : # 입금
    print("입금이 완료되었습니다. 잔액은 {0}원 입니다".format(balance + money)) 
    return balance + money # 총금액 반환

def withdraw(balance, money) : # 출금
    if (balance > money) :
        print("출금이 완료되었습니다. 잔액은 {}원 입니다".format(balance - money))
        return balance - money
    else :
        print("출금이 완료되지 않았습니다. 잔액은 {}원 입니다.".format(balance))
        return balance

def withdraw_night(balance, money) : # 저녁에 출금하려는 경우
    commission = 100 # 수수료 100원
    return commission, balance - money - commission
    
# 함수 호출
# open_account()
balance = 0
balance = deposit(0, 1000)

# balance = withdraw(balance, 2000)
# balance = withdraw(balance, 500)

commission, balance = withdraw_night(balance, 500)
print("수수료 : {}원, 잔액 : {}원".format(commission, balance))