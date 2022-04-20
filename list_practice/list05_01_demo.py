from traceback import print_list
from list05_01 import *

list = LinkedListBasic()
list.append(30)
list.insert(0, 20)

a = LinkedListBasic()
a.append(4)
a.append(3)
a.append(3)
a.append(2)
a.append(1)

list.extend(a)
list.reverse()
list.pop(0)

list.printList()
