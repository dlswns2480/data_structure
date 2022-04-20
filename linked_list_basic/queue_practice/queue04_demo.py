from queue04 import *

class TwoQueue:
    def __init__(self):
        self.__firstqueue = LinkedQueue()
        self.__secondqueue = LinkedQueue()

    def push(self, x):
        if self.__firstqueue.isEmpty():
            self.__firstqueue.enqueue(x)
        else :
            while not self.__firstqueue.isEmpty():
                self.__secondqueue.enqueue(self.__firstqueue.dequeue())
                
            self.__firstqueue.enqueue(x)

            while not self.__secondqueue.isEmpty():
                self.__firstqueue.enqueue(self.__secondqueue.dequeue())
        

    def pop(self):
        return self.__firstqueue.dequeue()





if __name__ == "__main__":
    st = TwoQueue()
    st.push(1)
    st.push(2)
    st.push(3)

    print(st.pop())
    print(st.pop())
    print(st.pop())