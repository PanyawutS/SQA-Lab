import unittest
import os, sys
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(CURRENT_DIR))
from source.CountClump import CountClump


class TestCountClump(unittest.TestCase):
    def test_case_1(self):
        """nums is None"""
        self.assertEqual(CountClump.count_clumps(None), 0)

    def test_case_2(self):
        """nums is an empty list"""
        self.assertEqual(CountClump.count_clumps([]), 0)

    def test_case_3(self):
        """nums = [1, 1, 2, 3, 3, 3]"""
        self.assertEqual(CountClump.count_clumps([1, 1, 2, 3, 3]), 2)

    def test_case_4(self):
        """nums = [1, 2]"""
        self.assertEqual(CountClump.count_clumps([1, 2]), 0)

    def test_case_5(self):
        """nums = [1, 2, 2, 3, 4, 4, 4]"""
        self.assertEqual(CountClump.count_clumps([1, 2, 2, 3, 4, 4]), 2)

    def make_suite(self):
        suite = unittest.TestSuite()
        suite.addTest(TestCountClump("test_case_1"))
        suite.addTest(TestCountClump("test_case_2"))
        suite.addTest(TestCountClump("test_case_3"))
        suite.addTest(TestCountClump("test_case_4"))
        suite.addTest(TestCountClump("test_case_5"))
        return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    test_suite = TestCountClump().make_suite()
    runner.run(test_suite)
