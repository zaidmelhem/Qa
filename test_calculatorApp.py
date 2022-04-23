import unittest
from unittest import mock
from unittest.mock import patch
from calculatorApp import *
import calculatorApp


class TestCalculate(unittest.TestCase):
    def setUp(self):
        print("Setup .. ")
        self.patcher1 = patch('calculatorApp.add', return_value = 5)
        self.MockClass1 = self.patcher1.start()
        self.addCleanup(self.patcher1.stop)
        self.patcher2 = patch('calculatorApp.subtract', return_value = 1)
        self.MockClass2 = self.patcher2.start()
        self.addCleanup(self.patcher2.stop)

    def test_AddPass(self):
        self.assertEqual(add(6,3), 9)# will execute the add
        self.assertEqual(calculate('1',2,3), 5) # will call the mock

    def test_AddInvalid(self):
        self.assertNotEqual(calculate('1',9,3), 9)

    def test_DividByZerror(self):
        with self.assertRaises(ValueError):
             calculate('4','0','w')
 

    def test_DividByZerrorRegex(self):
        with self.assertRaisesRegex(ValueError, "input is not a number!"):
             calculate('4','3','w')

    
    def test_AddPassWithMockEx1(self):
        with mock.patch('calculatorApp.add', return_value = 6):
            result = calculate('1',2,4)
        self.assertEqual(result, 6)

    def test_subtract(self):
        self.assertEqual(subtract(20,10), 10)
        self.assertNotEqual(subtract(25,10), 10)
        self.assertEqual(calculate('2',2,1), 1)
        self.assertEqual(subtract(-4,2), -6)
        self.assertEqual(subtract(-7,10), -17)

    @mock.patch('calculatorApp.subtract', return_value = -5)
    def test_SubtractPassWithMockEx(self, mock_check):
        result = calculate('2',-2,-3)
        self.assertEqual(result, -5)    
    
    @mock.patch('calculatorApp.multiply', return_value =2)
    def test_MultiplyPass(self, mock_check):
        result = calculate('3',2,2)
        excepted_result = 2, "*", 2, "=",2
        self.assertEqual(result,excepted_result) 
        self.assertEqual(multiply(2,-4),-8)
        self.assertEqual(multiply(3,4), 12)
        self.assertEqual(multiply(2,-2), -4)

    @mock.patch('calculatorApp.multiply', return_value =4)
    def test_MultiplyInvalid(self, mock_check):
        result = calculate('3',2,2)
        excepted_result = 2, "*", 2, "=",8
        self.assertNotEqual(result,excepted_result) 
        self.assertNotEqual(multiply(2,-4),-4)

    @mock.patch('calculatorApp.divide', return_value =4)
    def test_dividePass(self, mock_check):
        result = calculate('4',16,4)
        excepted_result = 16, "/", 4, "=",4
        self.assertEqual(result,excepted_result) 
        self.assertEqual(divide(0,2), 0)
        self.assertEqual(divide(7,2), 3.5)
        self.assertEqual(divide(30,2), 15)
       

    @mock.patch('calculatorApp.divide', return_value =5)
    def test_divideInvalid(self,mock_check): 
        self.assertNotEqual(divide(30,2), 14)
        self.assertNotEqual(divide(7,2), 3)
        self.assertNotEqual(divide(0,5),5)
        with self.assertRaisesRegex(ValueError, "input is not a number!"):
                 calculate('4','15','mm') 

    def test_DividByZerror(self):   
            with self.assertRaises(ZeroDivisionError):
                calculatorApp.divide(5,0)    
     
    def testcheck_user_input(self):
       self.assertEqual(check_user_input(4),4)
       self.assertAlmostEqual(check_user_input('6.12'), 6.12)
       with self.assertRaises(ValueError):
           calculatorApp.check_user_input("")
       with self.assertRaises(ValueError):
            calculatorApp.check_user_input("a")        

    def test_isexit(self):
        self.assertTrue(isExit("no"))
        self.assertFalse(isExit("yes"))
        with self.assertRaises(ValueError):
            calculatorApp.isExit("aa")


    def tearDown(self):
        print("tearDown .. ")
        #self.patcher1.stop()#or add this and remove self.addCleanup(self.patcher1.stop) in startup but this is not recommened!



if __name__ == '__main__':
	unittest.main()
