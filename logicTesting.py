from stack import Stack
from myqueue import Queue

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

def main():
    # stackLogicTest()
    queueLogicTest()
    
if __name__ == "__main__":
    main()
