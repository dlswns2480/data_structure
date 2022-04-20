from stack04 import *

def copy(a:ListStack, b:ListStack):
    for i in range(a.size()):
        b.push(a.get(i))


stack_a = ListStack()
stack_b = ListStack()

stack_a.push("O")
stack_a.push("L")
stack_a.push("L")
stack_a.push("E")
stack_a.push("H")

copy(stack_a, stack_b)

stack_b.printStack()

# 같은 레퍼런스를 가지는지 확인하기 위한 테스트 출력
stack_b.set_by_index(3, "O")

print("stack_a:")
stack_a.printStack()

print("stack_b:")
stack_b.printStack()