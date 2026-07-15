"""
Unit tests for all data structures (Python's built-in unittest framework).

Tests assert CORRECT behavior, so real bugs surface as failures/errors. Method
names match the current code (BST/hashmap still use camelCase inOrder/isEmpty/
findMin/findMax; if you later rename them to snake_case, update these calls).

Run:  py -m unittest tests.structuresTesting          (from the project root)
  or: py tests/structuresTesting.py
"""

import unittest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from structures.array import MyArray
from structures.stack import Stack
from structures.myqueue import Queue
from structures.singlyLinkedList import SinglyLinkedList
from structures.doublyLinkedList import DoublyLinkedList
from structures.bst import BinarySearchTree
from structures.hashmap import Hashmap


class TestMyArray(unittest.TestCase):
    def setUp(self):
        self.a = MyArray()

    def test_new_is_empty(self):
        self.assertTrue(self.a.is_empty())
        self.assertEqual(self.a.size(), 0)

    def test_append_and_get(self):
        self.a.append(10)
        self.a.append(20)
        self.assertEqual(self.a.get(0), 10)
        self.assertEqual(self.a.get(1), 20)
        self.assertEqual(self.a.size(), 2)
        self.assertFalse(self.a.is_empty())

    def test_set(self):
        self.a.append(1)
        self.a.set(0, 99)
        self.assertEqual(self.a.get(0), 99)

    def test_find_and_contains(self):
        self.a.append(5)
        self.a.append(15)
        self.assertEqual(self.a.find(15), 1)
        self.assertIsNone(self.a.find(999))
        self.assertTrue(self.a.contains(5))
        self.assertFalse(self.a.contains(999))

    def test_insert_shifts_right(self):
        for v in (1, 2, 3):
            self.a.append(v)
        self.a.insert(1, 99)
        self.assertEqual(self.a.get(1), 99)
        self.assertEqual(self.a.get(2), 2)
        self.assertEqual(self.a.size(), 4)

    def test_append_past_capacity(self):
        for i in range(10):
            self.a.append(i)
        self.assertEqual(self.a.append(11), "Array is full")

    def test_clear(self):
        self.a.append(1)
        self.a.clear()
        self.assertTrue(self.a.is_empty())
        self.assertEqual(self.a.size(), 0)


class TestStack(unittest.TestCase):
    def setUp(self):
        self.s = Stack()

    def test_new_is_empty(self):
        self.assertTrue(self.s.is_empty())
        self.assertIsNone(self.s.pop())
        self.assertIsNone(self.s.peek())

    def test_push_pop_lifo(self):
        self.s.push(1)
        self.s.push(2)
        self.s.push(3)
        self.assertEqual(self.s.size(), 3)
        self.assertEqual(self.s.pop(), 3)
        self.assertEqual(self.s.pop(), 2)
        self.assertEqual(self.s.size(), 1)

    def test_peek_does_not_remove(self):
        self.s.push(7)
        self.assertEqual(self.s.peek(), 7)
        self.assertEqual(self.s.size(), 1)

    def test_clear(self):
        self.s.push(1)
        self.s.clear()
        self.assertTrue(self.s.is_empty())


class TestQueue(unittest.TestCase):
    def setUp(self):
        self.q = Queue(3)

    def test_new_is_empty(self):
        self.assertTrue(self.q.is_empty())
        self.assertIsNone(self.q.dequeue())
        self.assertIsNone(self.q.front())

    def test_fifo_order(self):
        self.q.enqueue("a")
        self.q.enqueue("b")
        self.assertEqual(self.q.front(), "a")
        self.assertEqual(self.q.dequeue(), "a")
        self.assertEqual(self.q.dequeue(), "b")

    def test_full_behavior(self):
        self.q.enqueue(1)
        self.q.enqueue(2)
        self.q.enqueue(3)
        self.assertTrue(self.q.is_full())
        self.assertEqual(self.q.enqueue(4), "Queue is Full")

    def test_qsize(self):
        self.q.enqueue(1)
        self.q.enqueue(2)
        self.assertEqual(self.q.qsize(), 2)

    def test_clear(self):
        self.q.enqueue(1)
        self.q.clear()
        self.assertTrue(self.q.is_empty())


class TestSinglyLinkedList(unittest.TestCase):
    def setUp(self):
        self.sll = SinglyLinkedList()

    def test_new_is_empty(self):
        self.assertTrue(self.sll.is_empty())
        self.assertEqual(self.sll.size(), 0)

    def test_append_and_get(self):
        self.sll.append(1)
        self.sll.append(2)
        self.sll.append(3)
        self.assertEqual(self.sll.get(0), 1)
        self.assertEqual(self.sll.get(2), 3)
        self.assertEqual(self.sll.size(), 3)

    def test_prepend(self):
        self.sll.append(2)
        self.sll.prepend(1)
        self.assertEqual(self.sll.get(0), 1)
        self.assertEqual(self.sll.get(1), 2)

    def test_find(self):
        self.sll.append(10)
        self.sll.append(20)
        self.assertEqual(self.sll.find(20), 1)
        self.assertIsNone(self.sll.find(999))

    def test_pop_returns_tail(self):
        self.sll.append(1)
        self.sll.append(2)
        self.assertEqual(self.sll.pop(), 2)
        self.assertEqual(self.sll.size(), 1)

    def test_remove(self):
        self.sll.append(1)
        self.sll.append(2)
        self.assertEqual(self.sll.remove(1), 1)
        self.assertIsNone(self.sll.remove(999))

    def test_insert_middle(self):
        for v in (1, 2, 3):
            self.sll.append(v)
        self.sll.insert(1, 99)
        self.assertEqual(self.sll.get(1), 99)
        self.assertEqual(self.sll.get(2), 2)

    def test_clear(self):
        self.sll.append(1)
        self.sll.clear()
        self.assertTrue(self.sll.is_empty())


class TestDoublyLinkedList(unittest.TestCase):
    def setUp(self):
        self.dll = DoublyLinkedList()

    def test_new_is_empty(self):
        self.assertTrue(self.dll.is_empty())
        self.assertEqual(self.dll.size(), 0)

    def test_append_and_get(self):
        self.dll.append(1)
        self.dll.append(2)
        self.dll.append(3)
        self.assertEqual(self.dll.get(0), 1)
        self.assertEqual(self.dll.get(2), 3)

    def test_prepend(self):
        self.dll.append(2)
        self.dll.prepend(1)
        self.assertEqual(self.dll.get(0), 1)

    def test_pop_and_pop_first(self):
        for v in (1, 2, 3):
            self.dll.append(v)
        self.assertEqual(self.dll.pop(), 3)
        self.assertEqual(self.dll.pop_first(), 1)
        self.assertEqual(self.dll.size(), 1)

    def test_find(self):
        self.dll.append(10)
        self.dll.append(20)
        self.assertEqual(self.dll.find(20), 1)
        self.assertIsNone(self.dll.find(999))

    def test_set(self):
        self.dll.append(1)
        self.dll.set(0, 77)
        self.assertEqual(self.dll.get(0), 77)

    def test_insert_middle(self):
        for v in (1, 2, 3):
            self.dll.append(v)
        self.dll.insert(1, 99)
        self.assertEqual(self.dll.get(1), 99)
        self.assertEqual(self.dll.get(2), 2)

    def test_clear(self):
        self.dll.append(1)
        self.dll.clear()
        self.assertTrue(self.dll.is_empty())


class TestBinarySearchTree(unittest.TestCase):
    def setUp(self):
        self.bst = BinarySearchTree()

    def test_new_is_empty(self):
        self.assertTrue(self.bst.isEmpty())
        self.assertEqual(self.bst.size(), 0)
        self.assertIsNone(self.bst.findMin())
        self.assertIsNone(self.bst.findMax())

    def test_inorder_is_sorted(self):
        for v in (5, 3, 7, 2, 4, 6, 8):
            self.bst.insert(v)
        self.assertEqual(self.bst.inOrder(), [2, 3, 4, 5, 6, 7, 8])
        self.assertEqual(self.bst.size(), 7)

    def test_find_min_max(self):
        for v in (5, 3, 7, 2, 8):
            self.bst.insert(v)
        self.assertEqual(self.bst.findMin(), 2)
        self.assertEqual(self.bst.findMax(), 8)

    def test_search(self):
        for v in (5, 3, 7):
            self.bst.insert(v)
        node = self.bst.search(3)
        self.assertIsNotNone(node)
        self.assertEqual(node.val, 3)
        self.assertIsNone(self.bst.search(999))

    def test_duplicates_ignored(self):
        self.bst.insert(5)
        self.bst.insert(5)
        self.assertEqual(self.bst.size(), 1)

    def test_delete_leaf(self):
        for v in (5, 3, 7):
            self.bst.insert(v)
        self.bst.delete(3)
        self.assertEqual(self.bst.inOrder(), [5, 7])

    def test_delete_node_with_two_children(self):
        for v in (5, 3, 7, 6, 8):
            self.bst.insert(v)
        self.bst.delete(7)
        self.assertEqual(self.bst.inOrder(), [3, 5, 6, 8])

    def test_clear(self):
        self.bst.insert(1)
        self.bst.clear()
        self.assertTrue(self.bst.isEmpty())
        self.assertEqual(self.bst.size(), 0)


class TestHashmap(unittest.TestCase):
    def setUp(self):
        self.hm = Hashmap()

    def test_new_is_empty(self):
        self.assertTrue(self.hm.isEmpty())
        self.assertEqual(self.hm.size(), 0)
        self.assertIsNone(self.hm.get("missing"))
        self.assertFalse(self.hm.contains("missing"))

    def test_insert_and_get(self):
        self.hm.insert("name", "kyle")
        self.hm.insert("lang", "python")
        self.assertEqual(self.hm.get("name"), "kyle")
        self.assertEqual(self.hm.size(), 2)
        self.assertTrue(self.hm.contains("lang"))

    def test_update_existing_key(self):
        self.hm.insert("name", "kyle")
        self.hm.insert("name", "kyler")
        self.assertEqual(self.hm.get("name"), "kyler")
        self.assertEqual(self.hm.size(), 1)  # update must not grow the map

    def test_delete(self):
        self.hm.insert("a", 1)
        self.hm.insert("b", 2)
        self.hm.delete("a")
        self.assertFalse(self.hm.contains("a"))
        self.assertEqual(self.hm.size(), 1)
        self.assertIsNone(self.hm.delete("missing"))

    def test_collision_chaining(self):
        # force two different keys into behavior that exercises chaining, then
        # confirm both are independently retrievable
        self.hm.insert("abc", 1)
        self.hm.insert("cba", 2)
        self.assertEqual(self.hm.get("abc"), 1)
        self.assertEqual(self.hm.get("cba"), 2)

    def test_clear(self):
        self.hm.insert("a", 1)
        self.hm.clear()
        self.assertTrue(self.hm.isEmpty())
        self.assertEqual(self.hm.size(), 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
