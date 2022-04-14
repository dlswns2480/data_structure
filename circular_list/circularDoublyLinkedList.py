class BidirectNode:
    def __init__(self,x,prevNode : 'BidirectNode', nextNode:'BidirectNode'):
        self.item = x
        self.prev = prevNode
        self.next = nextNode
from bidirectNode import BidirectNode

class CircularDoublyLinkedList:
    """원형 더블리 링크드 리스트"""
    def __init__(self):
        """더미 헤드가 있는 버전의 원형 더블리 링크드 리스트"""
        self.__head = BidirectNode("dummy", None, None)
        self.__head.prev = self.__head
        self.__head.next = self.__head
        self.__numItems = 0
    
    def insert(self, i:int, newItem) -> None:
        """i번째에 새로운 데이터를 삽입하는 메소드"""
        if 0 == i :
            prev = self.getNode(i-1)
            newNode = BidirectNode(newItem, prev, prev.next)
            newNode.next.prev = newNode
            prev.next = newNode
            self.__numItems += 1
        else:
            print("index", i, ": out of bound in insert()") # 필요 시 에러 처리
    
    def append(self, newItem) -> None:
        """리스트 맨 뒤에 원소를 삽입하는 메소드"""
        prev = self.__head.prev
        newNode = BidirectNode(newItem, prev, self.__head)
        prev.next = newNode
        self.__head.prev = newNode
        self.__numItems += 1
    
    def pop(self, *args):
        """i 번째 원소를 삭제하는 메소드"""
        # 가변 파라미터. 인자가 없거나 -1이면 마지막 원소로 처리하기 위함. 파이썬 리스트 규칙 만족
        if self.isEmpty():
            return None
        # 인덱스 i 결정
        if len(args) != 0:  # pop(k)과 같이 인자가 있으면 i = k 할당
            i = args[0]
        if len(args) == 0 or i == -1:   # pop()에 인자가 없거나 pop(-1)이면 i에 맨 끝 인덱스 할당
            i = self.__numItems - 1
        # i번 원소 삭제
        if (0 <= i <= self.__numItems - 1):
            curr = self.getNode(i)
            retItem = curr.item
            curr.prev.next = curr.next
            curr.next.prev = curr.prev
            self.__numItems -= 1
            return retItem
        else:
            return None
    
    def remove(self, x):
        """원소 x를 삭제하는 메소드"""
        curr = self.__findNode(x)
        if curr != None:
            curr.prev.next = curr.next
            curr.next.prev = curr.prev
            self.__numItems -= 1
            return x
        else:
            return None
    
    def get(self, *args):
        """i번째 원소를 가져오는 메소드"""
        # 가변 파라미터. 인자가 없거나 -1이면 마지막 원소로 처리하기 위함. 파이썬 리스트 규칙 만족.
        if self.isEmpty():
            return None
        # 인덱스 i 결정
        if len(args) != 0:
            i = args[0]
        if len(args) == 0 or i == -1:   # pop()에 인자가 없거나 pop(-1)이면 i에 맨 끝 인덱스 할당
            i = self.__numItems - 1
        # i번 원소 리턴
        if (0 <= i <= self.__numItems - 1):
            return self.getNode(i).item
        else:
            return None
    
    def index(self, x) -> int:
        """원소 x의 인덱스를 리턴해주는 메소드"""
        cnt = 0
        for element in self:
            if element == x:
                return cnt
            cnt += 1
        return -12345
    
    def isEmpty(self) -> bool:
        """리스트가 비어있는지 알려주는 메소드 (비어 있으면 True, 비어 있지 않으면 False)"""
        return self.__numItems == 0

    def size(self) -> int:
        """리스트의 길이를 리턴해주는 메소드"""
        return self.__numItems
    
    def clear(self):
        """리스트를 초기화 해주는 메소드"""
        self.__head = BidirectNode("dummy", None, None)
        self.__head.prev = self.__head
        self.__head.next = self.__head
        self.__numItems = 0
    
    def count(self, x) -> int:
        """원소 x의 개수를 리턴해주는 메소드"""
        cnt = 0
        for element in self:
            if element == x:
                cnt += 1
        return cnt

    def extend(self, a):    # a는 순회 가능한 모든 객체
        """현재 리스트에 다른 객체를 더하여 확장시키는 메소드"""
        for element in a:
            self.append(element)
    
    def copy(self) -> 'CircularDoublyLinkedList':
        """다른 객체에 현재 리스트를 추가하는 메소드"""
        a = CircularDoublyLinkedList()
        for element in self:
            a.append(element)
        return a
    
    # 중요!!
    def reverse(self) -> None:
        """리스트를 거꾸로 뒤집는 메소드"""
        prev = self.__head
        curr = prev.next
        next = curr.next

        self.__head.next = prev.prev
        self.__head.prev = curr

        for _ in range(self.__numItems):
            curr.next = prev
            curr.prev = next
            prev = curr
            curr = next
            next = next.next
    
    def sort(self) -> None:
        """리스트를 정렬해주는 메소드"""
        a = []
        for element in self:
            a.append(element)
        a.sort()    # 파이썬 내장 함수 sort() 이용
        self.clear()
        for element in a:
            self.append(element)
        
    def __findNode(self, x) -> BidirectNode:
        """x와 데이터가 일치하는 노드를 찾는 메소드"""
        curr = self.__head.next     # 0번 노드
        
        # 0번 노드에서 다시 헤드로 돌아올 때까지 탐색
        while curr != self.__head:
            if curr.item == x:
                return curr
            else:
                curr = curr.next
        return None
    
    def getNode(self, i:int) -> BidirectNode:
        """i번째 노드를 가져오는 메소드"""
        curr = self.__head  # 더미 헤드, index: -1
        for _ in range(i+1):
            curr = curr.next
        return curr
    
    def printList(self) -> None:
        """리스트를 출력해주는 메소드"""
        for element in self:
            print(element, end = ' ')
        print()
            
    def __str__(self) -> None:
        """리스트를 출력해주는 메소드"""
        for element in self:
            print(element, end = ' ')
        print()
    
    def __iter__(self):     # generating iterator and return
        """이터레이터 메소드"""
        return CircularDoublyLinkedListIterator(self)

class CircularDoublyLinkedListIterator:
    """이터레이터 클래스"""
    def __init__(self, alist):
        self.__head = alist.getNode(-1)         # 더미 헤드
        self.iterPosition = self.__head.next    # 0번 노드

    def __next__(self):
        if self.iterPosition == self.__head:    # 순환 끝
            raise StopIteration
        
        else:                                   # 현재 원소를 리턴하면서 다음 원소로 이동
            item = self.iterPosition.item
            self.iterPosition = self.iterPosition.next
            return item


