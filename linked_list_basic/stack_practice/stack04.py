from linked_list_basic import LinkedListBasic
class ListStack:
    """배열 리스트로 구현한 스택 클래스"""
    def __init__(self):
        self.__stack = []
    
    def push(self, x):
        self.__stack.append(x)
    
    def pop(self):
        return self.__stack.pop()
    
    def top(self):
        if self.isEmpty():
            return None
        else:
            return self.__stack[-1]
    
    def isEmpty(self) -> bool:
        return not bool(self.__stack)   # bool 함수가 False를 반환하는 경우
                                        # 1. 객체가 비어 있는 경우
                                        # 2. 객체가 False인 경우
                                        # 3. 객체의 값이 0인 경우
                                        # 4. 객체가 None인 경우
    
    def popAll(self):
        self.__stack.clear()
    
    def printStack(self):
        print("Stack from top:", end = ' ')
        for i in range(len(self.__stack)-1, -1, -1):
            print(self.__stack[i], end = ' ')
        print()
    
    def size(self):
        return len(self.__stack)

    
    def get(self, index):
        return self.__stack[index]

    def set_by_index(self, index, x):
        self.__stack[index] = x