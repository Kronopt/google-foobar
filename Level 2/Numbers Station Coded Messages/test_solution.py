import unittest
import solution


class TestSolution(unittest.TestCase):
    """Tests as specified in the README"""
    def test1(self):
        self.assertEqual(solution.solution([4, 3, 5, 7, 8], 12), [0, 2])

    def test2(self):
        self.assertEqual(solution.solution([1, 2, 3, 4], 15), [-1, -1])

    def test3(self):
        self.assertEqual(solution.solution([4, 3, 10, 2, 8], 12), [2, 3])

    # my tests

    def test4(self):
        self.assertEqual(solution.solution([1], 1), [0, 0])

    def test5(self):
        self.assertEqual(solution.solution([1, 2, 3, 4, 5, 100], 100), [5, 5])


if __name__ == '__main__':
    unittest.main()
