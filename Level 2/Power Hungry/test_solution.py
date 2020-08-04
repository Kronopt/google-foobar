import unittest
import solution


class TestSolution(unittest.TestCase):
    """Tests as specified in the README"""
    def test1(self):
        self.assertEqual(solution.solution([2, -3, 1, 0, -5]), "30")

    def test2(self):
        self.assertEqual(solution.solution([2, 0, 2, 2, 0]), "8")

    def test3(self):
        self.assertEqual(solution.solution([-2, -3, 4, -5]), "60")

    # my tests

    def test4(self):
        self.assertEqual(solution.solution([1]), "1")

    def test5(self):
        self.assertEqual(solution.solution([13]), "13")

    def test6(self):
        self.assertEqual(solution.solution([-1]), "-1")

    def test7(self):
        self.assertEqual(solution.solution([-13]), "-13")

    def test8(self):
        self.assertEqual(solution.solution([5, -5]), "5")

    def test9(self):
        self.assertEqual(solution.solution([1, 1, 1, 1, 1, 1, 1, 1, 1]), "1")

    def test10(self):
        self.assertEqual(solution.solution([1, 1, 1, 1, 1, 1, 1, 1, 1, -1]), "1")

    def test11(self):
        self.assertEqual(solution.solution([1, 1, 1, 1, 1, 1, 1, 1, 1, -1, -1]), "1")

    def test12(self):
        self.assertEqual(solution.solution([1000] * 50), "1" + "0" * 150)

    def test13(self):
        self.assertEqual(solution.solution([-1000] * 50), "1" + "0" * 150)

    def test14(self):
        self.assertEqual(solution.solution([-1000] * 49), "-1" + "0" * 147)

    def test15(self):
        self.assertEqual(solution.solution([-13, 0]), "0")


if __name__ == '__main__':
    unittest.main()
