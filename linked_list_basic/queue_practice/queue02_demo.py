from queue02 import *

class SentenceChecker:
    def __init__(self):
        self.__queue = LinkedQueue()
    
    def sentence_find(self, string):
        index = string.find("$")
        for i in range(index):
            self.__queue.enqueue(string[i])
            
        
        for i in range(index+1, len(string)): # abc$abc
            prev = self.__queue.dequeue()   # 아까 enqueue한 abc가 prev 입력
            #앞에 문자열을 넣은 상태에서 FIFO로 dequeue
            curr = string[i]    # $의 오른쪽에 있는 abc가 curr에 입력
            #$뒤에 문자열
            if prev != curr:
                return False

        return self.__queue.isEmpty()


if __name__ == "__main__":
    checker = SentenceChecker()
    rv = checker.sentence_find("abc$abc")
    if rv == True :
        print("is included")
    else :
        print("is not included")