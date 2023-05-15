# SWTestProj_BookingSystem

ISE CS4442 Software Testing Project: Room Booking System 

Simple Flask Web Application for booking rooms in the ISE building

CONSTRAINTS
-----------
- ID Must be in whitelist
- Must book 3 days in advance
- Can't book on weekend
- Can't exceed room capacity
- West and South wing bookings must have at least 10 people

Logic functions in bookingSystem.py with parameterised unit tests in bookingSystem_test.py

Flask App in app.py with app route unit tests in app_routeTests.py

HOW TO RUN APP
--------------
run app.py to use the web application to make bookings by: 
- first inputting a valid ID (Can be found in whitelist.csv)
- inputting a valid date in the provided format
- selecting a room from the dropdown options
- inputting a valid group size

- selecting an available timeslot from the dropdown
- confirming booking details and submitting to the csv using the provided button

- then you will be redirected back to login if you want to make another booking

HOW TO RUN TESTS
----------------
run bookingSystem_test.py to run parameterized unit tests for each function in bookingSystem.py
these tests use a fake csv for the bookings called bookings_test.csv to ensure the tests still apply for the values given even if someone makes a booking, altering the bookings.csv file.
these tests also freeze the system time to avoid test failure due to the tests being run at a later date.

run app_routeTests.py to run unit tests for each app.route in the flask app

DECLARATION OF WORK
-------------------
Solo project. No declaration of work needed.




