import unittest
from bookingSystem import checkIDinCSV, getName

# def idValidation(idNum):

#     if not idNum.isnumeric():
#         raise ValueError()
#     if checkIDinCSV(idNum) == True:
#         return True
#     elif checkIDinCSV(idNum) == False:
#         return False
 

class bookingSystemFunctionTests(unittest.TestCase):

    def test_checkIDinCSV(self):
        self.assertTrue(checkIDinCSV(22359435))
        self.assertFalse(checkIDinCSV(12345678))
        

    def test_getName(self):
        self.assertEqual(getName(22359435),"Éanna Bonner")
        self.assertEqual(getName(20230504), "May Burke")

if __name__ == '__main__':
    unittest.main()