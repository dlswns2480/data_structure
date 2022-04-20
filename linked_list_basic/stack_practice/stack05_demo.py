from stack05 import *


def parenBalance(string:str) -> bool:
    """주어진 문자열 인풋의 모든 괄호가 짝이 있는지 확인해주는 메소드"""

    print(f"테스트하는 문자열: {string}")
    stack = ListStack() # 사용할 스택 정의
    balance = True      # 괄호 짝이 맞으면 True, 아니면 False

    # (를 찾을 때마다 스택에 위치를 저장한다.
    # )를 찾을 때마다 마지막 (를 지운다.
    # 만약 )를 찾았는데 (가 없다면 스택에 )의 위치를 저장한다.
    # 스택에 남은 것이 (라면
    for i in range(len(string)):
        if string[i] == "(":
            stack.push(i)    
        elif string[i] == ")":
            if stack.size() > 0:
                stack.pop()
            else:
                print("문자열 {} 번째 위치에 있는 닫는 괄호에 맞는 열리는 괄호가 없습니다".format(i))
                balance = False
        else:
            pass

    if stack.size() != 0:
        for j in range(stack.size()):
            print("문자열 {} 번째 위치에 있는 괄호가 닫히지 않았습니다".format(stack.pop()))
        balance = False
    
    return balance

case1 = "(1+2)*(3+5)"
case2 = "((3*12)/(41-31))"
case3 = "((1+4)-(3*12)/3"
case4 = "(12-3)*(56/3))"
case5 = ")1+14)/3"
case6 = "(3+15(*3"

print(parenBalance(case1))
print(parenBalance(case2))
print(parenBalance(case3))
print(parenBalance(case4))
print(parenBalance(case5))
print(parenBalance(case6))