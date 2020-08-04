import unittest
import solution


class TestSolution(unittest.TestCase):
    """Tests as specified in the README"""
    def test1(self):
        self.assertEqual(solution.solution('code'), '100100101010100110100010')

    def test2(self):
        self.assertEqual(solution.solution('Braille'),
                         '000001110000111010100000010100111000111000100010')

    def test3(self):
        self.assertEqual(solution.solution('The quick brown fox jumps over the lazy dog'),
                         '00000101111011001010001000000011111010100101010010010010100000'
                         '00001100001110101010100101111011100000001101001010101011010000'
                         '00010110101001101100111100011100000000101010111001100010111010'
                         '00000001111011001010001000000011100010000010101110111100000010'
                         '0110101010110110')


if __name__ == '__main__':
    unittest.main()
