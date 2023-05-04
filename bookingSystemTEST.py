import unittest
from bookingSystem import *

def idValidation(idNum):

    if not idNum.isnumeric():
        raise ValueError()
    if checkIDinCSV(idNum) == True:
        return True
    elif checkIDinCSV(idNum) == False:
        return False
 

class idValidationTest(unittest.TestCase):

    def test_idValidation(self):
        self.assertTrue(idValidation(22359435))
        self.assertFalse(idValidation(12345678))
        with self.assertRaises(ValueError):
            idValidation("1235gd4")

class getNameTest(unittest.TestCase):

    def test_getName(self):
        self.assertEqual(getName(22359435),"Éanna Bonner")
        self.assertEqual(getName(20230504), "May Burke")