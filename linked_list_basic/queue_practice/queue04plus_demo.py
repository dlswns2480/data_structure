from  linked_stack import *

class TwoStack:
    def __init__(self):
        self.__firststack = LinkedStack()
        self.__secondstack = LinkedStack()

    
    def enqueue(self,x):
        if self.__firststack.isEmpty():
            self.__firststack.push(x)
        else :
            while not self.__firststack.isEmpty():
                self.__secondstack.push(self.__firststack.pop())
            self.__firststack.push(x)

            while not self.__secondstack.isEmpty():
                self.__firststack.push(self.__secondstack.pop())
    def dequeue(self):
        return self.__firststack.pop()


if __name__ == "__main__":
    qu = TwoStack()
    qu.enqueue(1)
    qu.enqueue(2)
    qu.enqueue(3)

    print(qu.dequeue())
    print(qu.dequeue())
    print(qu.dequeue())