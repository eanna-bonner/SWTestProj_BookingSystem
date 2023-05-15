import unittest
from bookingSystem import *
from freezegun import freeze_time

class bookingSystemFunctionTests(unittest.TestCase):

    global bookingsdf
    bookingsdf = pd.read_csv("bookings_test.csv")
    
    def test_checkIDinCSV(self):
        test_cases = [
            (22359435, True),
            (12345678, False),
            (20221225, True),
        ]

        for input_value, expected in test_cases:
            with self.subTest(input=input_value, expected=expected):
                result = checkIDinCSV(input_value)
                self.assertEqual(result, expected, f"Input: {input_value}, Expected: {expected}")
        

    def test_getName(self):
        test_cases = [
            (22359435, "Eanna Bonner"),
            (20230504, "May Burke"),
            (20221225, "Nick Snow"),
        ]

        for input_value, expected in test_cases:
            with self.subTest(input=input_value, expected=expected):
                result = getName(input_value)
                self.assertEqual(result, expected, f"Input: {input_value}, Expected: {expected}")

    def test_getAvailableSlots(self):
        test_cases = [
            (("AWS Lounge", "19/05/2023"), [4]),
            (("West Wing", "23/05/2023"), [2,3,5,6])
        ]

        for input_values, expected in test_cases:
            with self.subTest(input=input_values, expected=expected):
                result = getAvailableSlots(*input_values)
                self.assertEqual(result, expected, f"Input: {input_values}, Expected: {expected}")
    
    def test_make_booking(self):
        test_cases = [
            {'ID': 1, 'Name': 'John', 'Room': 'Forest', 'Date': '2023-06-01', 'Timeslot': '09:00 - 10:00', 'NumPeople': 5},
            {'ID': 2, 'Name': 'Jane', 'Room': 'Beach', 'Date': '2023-06-02', 'Timeslot': '13:00 - 14:00', 'NumPeople': 3},
            # Add more test cases here if needed
        ]

        filename = 'bookings_test.csv'

        for case in test_cases:
            ID = case['ID']
            Name = case['Name']
            Room = case['Room']
            Date = case['Date']
            Timeslot = case['Timeslot']
            NumPeople = case['NumPeople']

            makeBooking(ID, Name, Room, Date, Timeslot, NumPeople, filename)

            df = pd.read_csv(filename)
            last_row = df.iloc[-1]

            self.assertEqual(last_row['ID'], ID)
            self.assertEqual(last_row['Name'], Name)
            self.assertEqual(last_row['Room'], Room)
            self.assertEqual(last_row['Date'], Date)
            self.assertEqual(last_row['Timeslot'], Timeslot)
            self.assertEqual(last_row['NumPeople'], NumPeople)

    @freeze_time("2023-05-15")
    def test_checkValidDate(self):
       
        test_cases = [
            ("15/05/2023", True),
            ("01/01/2001", True),
            ("17/05/2023", True),

            ("24/05/2023", False),
            ("02/06/2023", False),
            ("14/06/2023", False)
        ]

        for input_value, expected in test_cases:
            with self.subTest(input=input_value, expected=expected):
                result = checkValidDate(input_value)
                self.assertEqual(result, expected, f"Input: {input_value}, Expected: {expected}")

    def test_checkWeekend(self):
        test_cases = [
            ("20/05/2023", True),
            ("11/06/2023", True),
            ("18/05/2023", False),
            ("06/06/2023", False)
        ]

        for input_value, expected in test_cases:
            with self.subTest(input=input_value, expected=expected):
                result = checkWeekend(input_value)
                self.assertEqual(result, expected, f"Input: {input_value}, Expected: {expected}")

    def test_checkCapacity(self): 
        test_cases = [
            (("West Wing",5),True),
            (("West Wing",40),True),
            (("South Wing",9),True),
            (("South Wing",31),True),
            (("Forest",13),True),
            (("Meeting Room",20),True),
            (("TA Lounge",5),True),
            (("AWS Lounge",15),True),
            
            (("West Wing",17),False),
            (("South Wing",30),False),
            (("Forest",8),False),
            (("Meeting Room",6),False),
            (("TA Lounge",2),False),
            (("AWS Lounge",8),False)
        ]

        for input_values, expected in test_cases:
            with self.subTest(input=input_values, expected=expected):
                result = checkCapacity(*input_values)
                self.assertEqual(result, expected, f"Input: {input_values}, Expected: {expected}")

        
        


if __name__ == '__main__':
    unittest.main()