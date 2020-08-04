import unittest
import solution


class TestSolution(unittest.TestCase):
    """Tests as specified in the README"""
    def test1(self):
        self.assertEqual(solution.solution('vmxibkgrlm'), 'encryption')

    def test2(self):
        self.assertEqual(solution.solution(
            'wrw blf hvv ozhg mrtsg\'h vkrhlwv?'),
            'did you see last night\'s episode?')

    def test3(self):
        self.assertEqual(solution.solution(
            'Yvzs! I xzm\'g yvorvev Lzmxv olhg srh qly zg gsv xlolmb!!'),
            'Yeah! I can\'t believe Lance lost his job at the colony!!')

    def test4(self):
        self.assertEqual(solution.solution('a'), 'z')

    def test5(self):
        self.assertEqual(solution.solution('b'), 'y')

    def test6(self):
        self.assertEqual(solution.solution('c'), 'x')

    # my tests

    def test7(self):
        self.assertEqual(solution.solution('z'), 'a')

    def test8(self):
        self.assertEqual(solution.solution('m'), 'n')

    def test9(self):
        self.assertEqual(solution.solution('ABCZYX'), 'ABCZYX')

    def test810(self):
        self.assertEqual(solution.solution('.;?=&%'), '.;?=&%')


if __name__ == '__main__':
    unittest.main()
