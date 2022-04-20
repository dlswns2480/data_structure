from stack03 import *

def reverse_find(string):
    linkedStack = LinkedStack()
    index = 0
    reversed_str = ""
    front_str = ""

    while string[index] != "$":
        linkedStack.push(string[index])
        index += 1
    
    for i in range(index+1, len(string)):
        reversed_str += string[i]
    linkedStack.printStack()
    
    for i in range(index):
        front_str += linkedStack.pop()
    

    if front_str == reversed_str:
        return True
    else:
        return False
    

print(reverse_find("abc$cba"))