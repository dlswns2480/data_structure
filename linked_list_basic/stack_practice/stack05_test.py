from stack05 import *

def parenBalance(string:str):
    stack = ListStack()
    balance = True
    for i in range(len(string)):
        if string[i] == "(":
            stack.push(string[i])
        elif string[i] == ")":
            if stack.size() > 0:
                stack.pop()
            else :
                print("괄호 ) 에 맞는 열리는 괄호가 없습니다.")
                balance = False
    if stack.size() != 0:
        print("괄호 (에 맞는 닫는 괄호가 없습니다.")
        balance = False
    return balance

print(parenBalance("(1+3)("))