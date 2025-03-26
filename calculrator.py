kind = int(input("1. 입력한 수식 계산 2. 두 수 사이의 합계 : "))
if kind==1:
    mathematical_expression = input("*** 수식을 입력하세요 : ")
    print(mathematical_expression,"결과는",eval(mathematical_expression),"입니다.")
elif kind ==2:
    start = int(input("*** 첫 번째 숫자를 입력하세요 : "))
    end = int(input("*** 두 번째 숫자를 입력하세요 : "))
    print(start,"+...+",end,"는",(start+end)*abs((end-start+1))//2,"입니다.")