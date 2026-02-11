from stack import Stack
from myqueue import Queue
from singlyLinkedList import SinglyLinkedList

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


def main():
    # stackLogicTest()
    # queueLogicTest()
    singlyLinkedListTest()
    
if __name__ == "__main__":
    main()
