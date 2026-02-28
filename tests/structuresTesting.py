from structures.stack import Stack
from structures.myqueue import Queue
from structures.singlyLinkedList import SinglyLinkedList
from structures.doublyLinkedList import DoublyLinkedList

def stackLogicTest():
    s = Stack()

    print(s.is_empty())

    s.push(10)
    s.push(20)
    s.push(30)
    print(s)

    print(s.peek())

    print(s.pop())
    print(s.pop())
    print(s)

    print(s.size())
    print(s.is_empty())

    s.clear()
    print(s)
    print(s.is_empty())
def queueLogicTest():
    q = Queue(3)
    
    print(q.is_empty())

    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print(q)

    print(q.enqueue(4))

    print(q.front())

    print(q.dequeue())
    print(q.dequeue())
    print(q)

    print(q.qsize())
    print(q.is_empty())
    print(q.is_full())

    q.clear()
    print(q)
    print(q.is_empty())
def singlyLinkedListTest():
    lst = SinglyLinkedList()

    print("is_empty:", lst.is_empty())
    print("size:", lst.size())
    print("pop:", lst.pop())
    print("remove(10):", lst.remove(10))

    lst.append(10)
    lst.append(20)
    lst.append(30)
    print("size after appends:", lst.size())
    print("get(0):", lst.get(0))
    print("get(2):", lst.get(2))

    lst.prepend(5)
    lst.prepend(1)
    print("get(0):", lst.get(0))
    print("get(1):", lst.get(1))
    print("size:", lst.size())

    print("find(1):", lst.find(1))
    print("find(20):", lst.find(20))
    print("find(99):", lst.find(99))

    print("remove head (1):", lst.remove(1))
    print("remove middle (20):", lst.remove(20))
    print("remove tail (30):", lst.remove(30))
    print("remove missing (100):", lst.remove(100))

    print("size:", lst.size())
    print("get(0):", lst.get(0))
    print("get(1):", lst.get(1))

    print("pop:", lst.pop())
    print("pop:", lst.pop())
    print("pop on empty:", lst.pop())
    print("size:", lst.size())

    lst.append(99)
    lst.append(100)
    print("size before clear:", lst.size())
    lst.clear()
    print("size after clear:", lst.size())
    print("is_empty:", lst.is_empty())
def doublyLinkedListTest():
     lst = DoublyLinkedList()
     
     print(lst.is_empty())       # 0
     print(lst.size())           # 0

     lst.append(10)
     lst.append(20)
                #10 20
     print(lst.get(0))           # 10
     print(lst.get(1))           # 20
     print(lst.size())           # 2

     lst.prepend(5)
     lst.prepend(2)
                #2 5 10 20
     print(lst.get(0))           # 2
     print(lst.get(1))           # 5
     print(lst.size())           # 4

     lst.insert(0, 1)
                #1 2 5 10 20
     print(lst.get(0))           #1
     lst.insert(5, 40)
                #1 2 5 10 20 40
     print(lst.get(5))           #40
     lst.insert(4, 15)
                #1 2 5 10 15 20 40
     print(lst.get(4))           #15

     print(lst.pop())            #40
                #1 2 5 10 15 20
     print(lst.pop_first())      #1
                #2 5 10 15 20
     lst.remove(2)
     lst.remove(10)
     lst.remove(20)
                #5 15
     print(lst.get(0))           #5
     print(lst.get(1))           #15

     lst.append(30)
     lst.append(50)
                #5 15 30 50
     lst.remove_at(0)
     lst.remove_at(2)
                #15 30
     print(lst.get(0))          #15
     print(lst.get(1))          #30

     print(lst.find(30))        #1
     lst.set(0, 20)
                 #20 30
     print(lst.get(0))
     lst.clear()
     print(lst.get(0))          #0

def main():
    """stackLogicTest()
    queueLogicTest()
    singlyLinkedListTest()
    doublyLinkedListTest()
    """
    
if __name__ == "__main__":
    main()
