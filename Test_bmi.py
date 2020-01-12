import unittest
import bmi


class TestBMI(unittest.TestCase):
    def testBMInum(self):
            self.assertEqual(BMInum(180,80),None) 

if __name__ == '__main__':
    unittest.main()
    