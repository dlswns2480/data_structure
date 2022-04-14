from stack03 import *

def check_func():
    w = input()
    check_sum = 0
    check_w = ListStack()
    for i in w:
        check_w.push(i)
    for k in range(len(w) - 1, -1, -1):
        if w[k] == check_w.pop():
            check_sum += 1
    if check_sum == len(w):
        print("True")
    else:
        print("False")
check_func()