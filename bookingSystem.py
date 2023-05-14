import pandas as pd
from datetime import datetime, timedelta
whitelistdf = pd.read_csv("whitelist.csv")
bookingsdf = pd.read_csv("bookings.csv")
roomSlotsdf = pd.read_csv("roomSlots.csv")


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
















def main():
    inputID = int(input("Please enter your ID: "))
    inputInvalid = True
    while inputInvalid:
        inputInvalid = False
        if checkIDinCSV(inputID)==True:
            currentID = inputID
            name = getName(currentID)
            print("\nWelcome "+name)
        else:
            inputInvalid = True
            inputID = int(input("Invalid ID, please enter a valid ID: "))
     
    # Create a dictionary to store available time slots for each room
    roomSlotsDict = {}

    # Loop through each column (starting at the second column)
    for col in roomSlotsdf.columns[1:]:
        # Create an empty list to store slot numbers with 0s for the current column (room)
        roomSlots = []
        # Loop through each row in the DataFrame
        for index, row in roomSlotsdf.iterrows():
            # Check if the value in the current cell is 0
            if row[col] == 0:
                # If it is, append the slot number to the roomSlots list
                roomSlots.append(row['Slot'])
        # Add the list of slot numbers with 0s for the current column to the dictionary
        roomSlotsDict[col] = roomSlots

    timeSlotsDict = {1:"09:00 -> 09:55", 2:"10:00 -> 10:55", 3:"11:00 -> 11:55", 4:"12:00 -> 12:55", 5:"14:00 -> 14:55", 6:"15:00 -> 15:55", 7:"16:00 -> 16:55" }
    print("\nHere is a guide to the time slots:")
    print("\nSlot\t Time")
    for i in range(len(timeSlotsDict)):
        print(i+1,"\t", timeSlotsDict[i+1])

    print("\nHere is a list of rooms and the available time slots for each room:")
    print("\nRoom\t\t   Slots Available")
    print("South Wing\t",roomSlotsDict["South Wing"])
    print("West Wing\t",roomSlotsDict["West Wing"])
    print("Forest\t\t",roomSlotsDict["Forest"])
    print("Meeting Room\t",roomSlotsDict["Meeting Room"])
    print("TA Lounge\t",roomSlotsDict["TA Lounge"])
    print("AWS Lounge\t",roomSlotsDict["AWS Lounge"])




