import unittest
import bmi


# test on bmi function
class TestBMI(unittest.TestCase):
    def testBMInum(self):
        # weight stubs
        ws1 = 100
        ws2 = 87
        ws3 = 90
        ws4 = 54
        ws5 = 93
        ws6 = 120

        # height stubs 
        hs1 = 0
        hs2 = 1.8
        hs3 = 1.9
        hs4 = 2
        hs5 = 1.65
        hs6 = 1

        # action
        result1 = bmi.BMInum(ws1, hs1)
        result2 = bmi.BMInum(ws2, hs3)
        result3 = bmi.BMInum(ws3, hs4)
        result4 = bmi.BMInum(ws4, hs5)
        result5 = bmi.BMInum(ws5, hs2)
        result6 = bmi.BMInum(ws6, hs2)
        result7 = bmi.BMInum(ws5, hs3)
        result8 = bmi.BMInum(ws4, hs5)

        # tests
        self.assertEqual(result1, 'ZeroDivisionError')
        self.assertEqual(result2, 24.099722991689752)
        self.assertEqual(result3, 22.50)
        self.assertEqual(result4, 19.834710743801654)
        self.assertEqual(result5, 28.703703703703702)
        self.assertEqual(result6, 37.03703703703704)
        self.assertEqual(result7, 25.761772853185597)
        self.assertEqual(result8, 19.834710743801654)


class TestBMIsol(unittest.TestCase):
    def testBMIsol(self):
        # bmi number stubs
        stub1 = 13
        stub2 = 15
        stub3 = 18
        stub4 = 20
        stub5 = 25
        stub6 = 30
        stub7 = 36
        stub8 = 41
        stub9 = 48
        stub10 = 52
        stub11 = 60
        stub12 = 62

        # excpected result

        exp1 = "Very severely underweight"
        exp2 = "severely underweight"
        exp3 = "Underweight"
        exp4 = "Normal (healthy weight)"
        exp5 = "Overweight"
        exp6 = "Obese Class I (Moderately obese)"
        exp7 = "Obese Class II (Severely obese)"
        exp8 = "Obese Class III (Very severely obese)"
        exp9 = "Obese Class IV (Morbidly obese)"
        exp10 = "Obese Class V (Super obese)"
        exp11 = "Obese Class VI (Hyper obese)"

        # action

        result1 = bmi.BMIsolution(stub1)
        result2 = bmi.BMIsolution(stub2)
        result3 = bmi.BMIsolution(stub3)
        result4 = bmi.BMIsolution(stub4)
        result5 = bmi.BMIsolution(stub5)
        result6 = bmi.BMIsolution(stub6)
        result7 = bmi.BMIsolution(stub7)
        result8 = bmi.BMIsolution(stub8)
        result9 = bmi.BMIsolution(stub9)
        result10 = bmi.BMIsolution(stub10)
        result11 = bmi.BMIsolution(stub11)
        result12 = bmi.BMIsolution(stub12)

        # test
        self.assertEqual(exp1, result1)
        self.assertEqual(exp2, result2)
        self.assertEqual(exp3, result3)
        self.assertEqual(exp4, result4)
        self.assertEqual(exp5, result5)
        self.assertEqual(exp6, result6)
        self.assertEqual(exp7, result7)
        self.assertEqual(exp8, result8)
        self.assertEqual(exp9, result9)
        self.assertEqual(exp10, result10)
        self.assertEqual(exp11, result11)
        self.assertEqual(exp11, result12)


if __name__ == '__main__':
    unittest.main()
