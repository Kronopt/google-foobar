import unittest
import solution


class TestSolution(unittest.TestCase):
    """Tests as specified in the README"""
    def test1(self):
        self.assertEqual(solution.solution("4", "7"), "4")

    def test2(self):
        self.assertEqual(solution.solution("2", "1"), "1")

    def test3(self):
        self.assertEqual(solution.solution("2", "4"), "impossible")

    # my tests

    def test4(self):
        self.assertEqual(solution.solution("1", "1"), "0")

    def test5(self):
        self.assertEqual(solution.solution("11", "15"), "6")

    def test6(self):
        self.assertEqual(solution.solution("15", "11"), "6")

    def test7(self):
        self.assertEqual(solution.solution("20", "1"), "19")

    def test8(self):
        self.assertEqual(solution.solution("200", "1"), "199")

    def test9(self):
        self.assertEqual(solution.solution("999999", "999999"), "impossible")


if __name__ == '__main__':
    unittest.main()
