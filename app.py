from flask import Flask, jsonify, request, render_template, redirect, url_for
from bookingSystem import *

app = Flask(__name__)


recordID = str
recordName = str
recordRoom = str
recordDate = str
recordTimeslot = int
recordNumPeople = int

@app.route("/") 
def index():
    return render_template("index.html")

@app.route("/button-clicked")
def button_clicked():
    return redirect(url_for("login"))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        userID = request.form.get('id')
        userID = int(userID)
        # Check inputted ID
        if checkIDinCSV(userID)==True:
            global recordID
            recordID = userID
            global recordName  
            recordName = getName(recordID)
            return redirect(url_for("bookingForm"))
        else:
            error_message = "Invalid ID"
            return render_template("error.html", error_message=error_message)

    return render_template('login.html')

@app.route('/bookingForm', methods = ['GET', 'POST'])
def bookingForm():
    return render_template('bookingForm.html', name=recordName)

@app.route("/roomPicked", methods=['GET','POST'])
def roomPicked():
    refreshCSV()
    if request.method == 'POST':
        global recordRoom
        global recordDate
        global recordNumPeople 
        recordRoom = request.form.get('room')
        recordDate = request.form.get('date')

        if checkValidDate(recordDate):
            error_message = "The selected date was invalid. PLease select a date at least 3 days from today."
            return render_template("error.html", error_message=error_message)

        if checkWeekend(recordDate):
            error_message = "Bookings cannot be made on weekends. PLease select a valid date."
            return render_template("error.html", error_message=error_message)
        
        recordNumPeople = request.form.get('numPeople')

        if checkCapacity(recordRoom,int(recordNumPeople)):
            error_message = "Invalid party size for the selected room. Please select a different room or change your group size."
            return render_template("error.html", error_message=error_message)

        availableSlots = getAvailableSlots(recordRoom,recordDate)

    return render_template('selectTimeslot.html', room_name =  recordRoom, timeslots = availableSlots)  

@app.route('/reviewBooking', methods = ['GET','POST'])
def reviewBooking():
    global recordTimeslot
    recordTimeslot = request.form.get('timeslot')
    return render_template('reviewBooking.html', room=recordRoom, date=recordDate, timeslot=recordTimeslot, num_people=recordNumPeople)

@app.route('/submitBooking')
def submitBooking():
    makeBooking(recordID, recordName, recordRoom, recordDate, recordTimeslot, recordNumPeople, 'bookings.csv')
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run()

