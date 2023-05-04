import pandas as pd

bookingdf = pd.read_csv("bookings.csv")

def checkIDinCSV(input: int):
    x = bookingdf['ID'].eq(input).any()
    return x

def getName(userID: int):
    x = bookingdf[bookingdf['ID']==userID].index.tolist()
    name = bookingdf.iloc[x[0],bookingdf.columns.get_loc("Name")]
    return name

print(checkIDinCSV(22359435))

inputID = int(input("Please enter your ID: "))
inputInvalid = True
while inputInvalid:
    inputInvalid = False
    if checkIDinCSV(inputID)==True:
        currentID = inputID
        name = getName(currentID)
        print("Welcome "+name)
    else:
        inputInvalid = True
        inputID = int(input("Invalid ID, please enter a valid ID: "))


