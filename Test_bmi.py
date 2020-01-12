import unittest
import bmi

## bmi function
class TestBMI(unittest.TestCase):
    def testBMInum(self):
            self.assertEqual(BMInum(180,80),None) 

if __name__ == '__main__':
    unittest.main()
    
    