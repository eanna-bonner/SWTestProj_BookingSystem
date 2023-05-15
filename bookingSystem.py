import pandas as pd
from datetime import datetime, timedelta
whitelistdf = pd.read_csv("whitelist.csv")
bookingsdf = pd.read_csv("bookings.csv")


'''
CONSTRAINTS
-----------
- ID Must be in whitelist
- Must book 3 days in advance
- Can't book on weekend
- Can't exceed room capacity
- West and South wing bookings must have at least 10 people
'''
# Variables
roomCapacityDict = {"West Wing":30, "South Wing":30, "Forest":12, "Meeting Room":10, "TA Lounge":3, "AWS Lounge":8}

def refreshCSV():
    global bookingsdf
    bookingsdf = pd.read_csv("bookings.csv")

def checkIDinCSV(input: int):
    x = whitelistdf['ID'].eq(input).any()
    return x

def getName(userID: int):
    x = whitelistdf[whitelistdf['ID']==userID].index.tolist()
    name = whitelistdf.iloc[x[0],whitelistdf.columns.get_loc("Name")]
    return name 

def getAvailableSlots(room, date):
    availableSlots = [1,2,3,4,5,6,7]
    filtered_df = bookingsdf[(bookingsdf['Room'] == room) & (bookingsdf['Date'] == date)]
    timeslots = filtered_df['Timeslot'].tolist()
    for i in range(len(timeslots)):
        availableSlots.remove(timeslots[i])
    return availableSlots

def makeBooking(ID, Name, Room, Date, Timeslot, NumPeople, filename):
    data = {'ID': [ID], 'Name': [Name], 'Room': [Room], 'Date': [Date], 'Timeslot': [Timeslot], 'NumPeople': [NumPeople]}
    df = pd.DataFrame(data)
    df.to_csv(filename, encoding='utf-8', mode='a', header=False, index=False)

def checkValidDate(date_string):
    date_format = "%d/%m/%Y"
    date = datetime.strptime(date_string, date_format).date()
    today = datetime.today().date() + timedelta(days=2)
    
    if date <= today:
        return True
    else:
        return False

def checkWeekend(date_string):
    date_format = "%d/%m/%Y"
    date = datetime.strptime(date_string, date_format).date()

    if date.weekday() >= 5:
        return True
    else:
        return False

def checkCapacity(room, numPeople):
    if room == "West Wing" or room == "South Wing":
        if numPeople < 10:
            return True
    
    if numPeople > roomCapacityDict[room]:
        return True
    else:
        return False