from queue03 import *

def copy(aa:LinkedQueue,bb:LinkedQueue):
    for i in range(aa.size()):
        bb.enqueue(aa.get(i))


a = LinkedQueue()
b = LinkedQueue()
a.enqueue("H")
a.enqueue("E")
a.enqueue("L")
a.enqueue("L")
a.enqueue("O")



copy(a,b)

a.printQueue()
b.printQueue()

