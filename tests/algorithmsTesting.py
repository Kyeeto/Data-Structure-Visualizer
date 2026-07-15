"""
Unit tests for all sorting algorithms (Python's built-in unittest framework).

Each sort takes a list and RETURNS a list of "steps" (it does not sort in place).
We verify:
  - correctness   : the final step's "array" matches sorted()
  - immutability  : the caller's list is never mutated
  - step schema   : every step is { "array": list, "highlight": list,
                                     "action": str, "pointers": dict }
  - permutation   : every snapshot holds the same multiset as the input

Run:  py -m unittest tests.algorithmsTesting        (from the project root)
  or: py tests/algorithmsTesting.py
"""

import unittest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from algorithms.bubbleSort import bubbleSort
from algorithms.insertionSort import insertionSort
from algorithms.selectionSort import selectionSort
from algorithms.mergeSort import mergeSort
from algorithms.quickSort import quickSort

ALGORITHMS = {
    "bubble": bubbleSort,
    "insertion": insertionSort,
    "selection": selectionSort,
    "merge": mergeSort,
    "quick": quickSort,
}

VALID_ACTIONS = {"compare", "swap", "overwrite"}

TEST_INPUTS = [
    [],
    [1],
    [2, 1],
    [1, 2, 3, 4, 5],
    [5, 4, 3, 2, 1],
    [3, 1, 4, 1, 5, 9, 2, 6],
    [7, 7, 7, 7],
    [42, -3, 0, 17, -8, 5],
]


class TestSortingAlgorithms(unittest.TestCase):

    def test_sorts_correctly(self):
        """The final step's array must equal Python's sorted()."""
        for name, func in ALGORITHMS.items():
            for data in TEST_INPUTS:
                with self.subTest(algorithm=name, data=data):
                    steps = func(data[:])
                    if len(data) >= 2:
                        self.assertTrue(len(steps) > 0,
                                        "expected at least one step for a 2+ element list")
                        self.assertEqual(steps[-1]["array"], sorted(data),
                                         "final step should show the fully sorted array")

    def test_does_not_mutate_input(self):
        """A sort must operate on an internal copy, leaving the caller's list intact."""
        for name, func in ALGORITHMS.items():
            for data in TEST_INPUTS:
                with self.subTest(algorithm=name, data=data):
                    work = data[:]
                    func(work)
                    self.assertEqual(work, data,
                                     "sort mutated the caller's list")

    def test_step_schema(self):
        """Every step must match the agreed schema shape and types."""
        for name, func in ALGORITHMS.items():
            for data in TEST_INPUTS:
                steps = func(data[:])
                for idx, step in enumerate(steps):
                    with self.subTest(algorithm=name, data=data, step=idx):
                        self.assertIsInstance(step, dict)
                        self.assertIn("array", step)
                        self.assertIn("highlight", step)
                        self.assertIn("action", step)
                        self.assertIn("pointers", step)
                        self.assertIsInstance(step["array"], list)
                        self.assertIsInstance(step["highlight"], list)
                        self.assertIn(step["action"], VALID_ACTIONS)
                        self.assertIsInstance(step["pointers"], dict)

    def test_highlight_indices_in_range(self):
        """Highlighted indices must be valid positions in the array snapshot."""
        for name, func in ALGORITHMS.items():
            for data in TEST_INPUTS:
                steps = func(data[:])
                for idx, step in enumerate(steps):
                    with self.subTest(algorithm=name, data=data, step=idx):
                        n = len(step["array"])
                        for h in step["highlight"]:
                            self.assertTrue(0 <= h < n,
                                            f"highlight index {h} out of range for size {n}")

    def test_snapshots_are_permutations(self):
        """Every snapshot must contain exactly the same values as the input."""
        for name, func in ALGORITHMS.items():
            for data in TEST_INPUTS:
                steps = func(data[:])
                for idx, step in enumerate(steps):
                    with self.subTest(algorithm=name, data=data, step=idx):
                        self.assertEqual(sorted(step["array"]), sorted(data),
                                         "a snapshot lost or duplicated a value")


if __name__ == "__main__":
    unittest.main(verbosity=2)
