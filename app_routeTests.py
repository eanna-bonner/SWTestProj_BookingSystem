import unittest
from urllib.parse import urlparse

from flask import url_for
from app_baseTest import BaseTestCase

class RouteTests(BaseTestCase):

    def testHome(self):
        response = self.client.get('/')
        self.assert_template_used('index.html')

    def testLoginButtonClicked(self):
        response = self.client.get('/button-clicked')
        expected_path = '/login'
        parsed_url = urlparse(response.location)
        actual_path = parsed_url.path
        self.assertEqual(actual_path, expected_path)

    def testLoginGetRequest(self):
        response = self.client.get('/login')
        self.assert_template_used('login.html')  

    def testLoginValidID(self):
        response = self.client.post('/login', data={'id': '22359435'})
        expected_path = '/bookingForm'
        parsed_url = urlparse(response.location)
        actual_path = parsed_url.path
        self.assertEqual(actual_path, expected_path)

    def testLoginInvalidID(self):
        response = self.client.post('/login', data={'id': '12345678'})
        self.assert_template_used('error.html')
        self.assert_context('error_message', 'Invalid ID')

    def testBookingForm(self):
        response = self.client.get('/bookingForm')
        self.assert_template_used('bookingForm.html')  

    def testFormInvalidDate(self):
        response = self.client.post('/roomPicked', data={'date': '01/01/2001'})
        self.assert_template_used('error.html')
        self.assert_context('error_message', 'The selected date was invalid. PLease select a date at least 3 days from today.')
    
    def testFormWeekendDate(self):
        response = self.client.post('/roomPicked', data={'date': '11/11/2028'})
        self.assert_template_used('error.html')
        self.assert_context('error_message', 'Bookings cannot be made on weekends. PLease select a valid date.')

    def testFormInvalidCapacity(self):
        response = self.client.post('/roomPicked', data={'room': 'Forest','date': '09/11/2023',"numPeople": 15})
        self.assert_template_used('error.html')
        self.assert_context('error_message', 'Invalid party size for the selected room. Please select a different room or change your group size.')

    def testRoomPicked(self):
        response = self.client.post('/roomPicked', data={'room': 'Forest', 'date': '09/11/2023', 'numPeople': 7})
        self.assert_template_used('selectTimeslot.html')  

    def testReviewBooking(self):
        response = self.client.get('/reviewBooking', data={'timeslot': 4})
        self.assert_template_used('reviewBooking.html')  

    def testSubmitBooking(self):
        response = self.client.get('/submitBooking')
        expected_path = '/login'
        parsed_url = urlparse(response.location)
        actual_path = parsed_url.path
        self.assertEqual(actual_path, expected_path)

if __name__ == '__main__':
    unittest.main()