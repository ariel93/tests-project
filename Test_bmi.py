import unittest
import bmi

##test on bmi function
class TestBMI(unittest.TestCase):
    def testBMInum(self):
            self.assertEqual(BMInum(80,180),5) 

class TestBMIsol(unittest.TestCase):
    def testBMIsol(self):
            self.assertEqual(BMIsolution(8),None)             

if __name__ == '__main__':
    unittest.main()
    
    