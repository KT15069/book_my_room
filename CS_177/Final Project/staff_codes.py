"""
This Module contains all of the functions related staff portal
"""

import customer_codes
import pandas as pd
import numpy as np
from datetime import datetime
today=datetime.today().date()
"""
In the staff_authentication.txt file are the usernames,passowrds stored. One line has one Username, Password for one staff member in the format example: cs177,project@cs177
here cs177 is the username and project@cs177 is the password
Here we are reading the staff_authentication txt file (File I/O) so that only the actual staff members can login to the staff portal
We first open the text file in 'file' and read line by line into it (for i in file) then strip the excape characters (\n,\t) from the ends of line using i.strip()
Then we create a list of the username and password using .split(',') and comma as the seperator. Then we add the username in the dictionary auth{} as key and password as the value.
"""
file=open("staff_authentication.txt",'r')#contains staff memeber username and password for authentication
auth={}#To store username as keys and value as passwords
for i in file:
    d=i.strip()#Removes \n and \t from the string
    j=d.split(',')#Create a list of userid and password.
    auth.update({j[0]:j[1]})#to join this dictionary in auth{}
file.close()

"""
This function displays the staff portal menu options to choose from
"""
def staff_menu():
    print()
    print("Choose your Options")
    print("1. Search a booking")
    print("2. Change a Booking")
    print("3. Remove/Add a Room")
    print("4. Do Data Analysis on Records")
    print("5. Data Visualization on Records")
    print("6. See Booking Records")
    print("7. Exit")
    try:
        menu_choice=int(input("Choose an option to move forward with: "))
        if menu_choice not in (1,2,3,4,5,6,7):
            raise ValueError
    except ValueError:
        print("Incorrect Input..Enter number only from the given options")
        return None
    else:
        return menu_choice
    
"""
This function is used to authenticate if the person trying to access the staff portal is Truly a staff.
"""

def staff_auth(uid,pwd):
    f=0
    for i in auth.keys():
        if uid==i:
            if pwd==auth[i]:
                f=1
                break
    if f==1:
        return True
    else:
        return False

"""
This function asks from the user to enter his/her staff userid and password. Then the above staff_auth(uid,pwd) funtion is called to checkif  the id and pwd match 
from the auth dictionary.
"""
def staff_check():
    check=False
    attempt=3#3 attempts given in total to verify username and password
    while attempt>0:
        print()
        print("Hello STAFF")
        uid=input("Please enter your UserName: ") 
        pwd=input("Please enter your Password: ")
        check=staff_auth(uid,pwd)#to check staff member authenticity and verify
        if check:
            return True
        else:
            attempt-=1
            print()
            print("UserName and Password do not match our Records. :<")
            print("You have",attempt,"Attempt(s) Left")
    return False

"""
This function is used to edit/delete the booking details from the booking (customer_codes.bookings) DataFrame.
First the booking ID of the booking to edit is entered and then asked if edit or del is needed. 
If Edit is typed then the booking is edited by entering the check in date, out date, room no. 
Again we check if the date entered is correct or not, same as valid_input_check funtion in the customer_codes.py module.
And then the Booking ID is generated, along with asking the new name. Then the new booking is saved place of the old booking.
IF del is chosen then the booking with the enetered boking ID is droped f rom the DataFrame, and hence from the csv.
"""
def change_booking():
    try:
        booking_id=int(input("Enter the Booking ID to Change:"))
    except ValueError:
        print("Booking ID should only be an Integer")
        return None
    if booking_id in list(customer_codes.bookings["booking_id"]):#looks if the booking id is present in the records
        print("ID match found. Fetching Booking Details....")
        for i in customer_codes.bookings.index:#going through each row
            if customer_codes.bookings.loc[i,'booking_id']==booking_id:#to display the current booking in the record
                print()
                print("Name: ",customer_codes.bookings.loc[i,"name"])
                print("Booking ID:",customer_codes.bookings.loc[i,"booking_id"])
                print("Room No.",customer_codes.bookings.loc[i,"room_no"]//1)
                print("Check In Date: ",customer_codes.bookings.loc[i,"check_in_date"])
                print('Check Out Date: ',customer_codes.bookings.loc[i,"check_out_date"])
                print("Total Cost: $",customer_codes.bookings.loc[i,"cost"])
                break
   
        choice=input("Do you want to Edit or Delete the Booking? (edit/del): ")
        if choice=='edit':
            
            try:
                date1=input("Enter the CheckIn Date in YYYY-MM-DD format: ")
                d1=datetime.strptime(date1, "%Y-%m-%d")#converts the entered string(date1) to date time
                date2=input("Enter the CheckOut Date in YYYY-MM-DD format: ")
                d2=datetime.strptime(date2, "%Y-%m-%d")#converts the entered string(date2) to date time
                n_days=(d2.date()-d1.date()).days#finding difference between the entered dates
                if n_days<0:#checks if the check In date is after check Out (Logically wrong)
                    raise ZeroDivisionError  #hence raised an error 
            except ZeroDivisionError:
                print("CheckIn Date Shall be before CheckOut date")
                return None   
            except Exception:#If any other error occurs
                print("Invalid Input.\nThe Date shall be in YYYY-MM-DD format only.\nWhere YYYY= year, MM=month, DD=day all in integer\nExample: ",today)
                return None
            else:#Updating the bookings DataFrame
                try:
                    room=int(input("Enter new room no.: "))
                except ValueError:
                    print("Room No. shall be an Integer")
                else:
                    if room in list(customer_codes.room_type["room_no"]):
                        name=input("Enter new Name: ")
                        customer_codes.bookings.loc[i,"name"]=name
                        customer_codes.bookings.loc[i,"room_no"]=room
                        customer_codes.bookings.loc[i,"check_in_date"]=d1
                        customer_codes.bookings.loc[i,"check_out_date"]=d2
                        customer_codes.bookings.loc[i,"booking_id"]=int(customer_codes.random_generator())
                        for j in customer_codes.room_type.index:
                            if customer_codes.room_type.loc[j,'room_no']==room:
                                cost=customer_codes.room_type.loc[j,'cost_per_night']
                                break
                        customer_codes.bookings.loc[i,"cost"]=(n_days+1)*cost
                        customer_codes.save_booking()#called to save the updated DataFrame to csv
                        print()
                        print("Records Updated")
                    else:
                        print("Room is not present in the Room_type.csv records!!!")
                
        elif choice=='del':
            customer_codes.bookings.drop(index=i,inplace=True)#to delete the record from DataFrame
            customer_codes.save_booking()#to update the csv
            print("Booking Deleted")
            
        else:
            print("Invalid Input. Redirecting...")
    else:
        print("Booking ID",booking_id,"Not found in the records")

"""
This function is used to update the room_types.csv records, in which every room is unique.
First it is asked whether to add or remove a room
If chosen to ADD: Then staff member is asked the new room no. After it is checked that the enetered room no. of is not present already
only then the it is asked to enter the min and max guest.
If chosen to Remove: It is prompted to enter the room no. After checking the room no. exists only then the room no. is dropped from the DataFrame, and hence the csv
"""
    
def change_room():#to edit the room_type records and update the csv
    print("Change Room Records")
    print("1. Add a Room")
    print("2. Remove a Room")
    print("3. Exit")
    try:
        todo=int(input("Choose your Desired option: "))
        if todo not in (1,2,3):
            raise ValueError
    except TypeError:
        print("Incorrect Value Enterred.")
        return None
    except ValueError:
        print(todo,"is not in the Change Room Records Options")
        return None
    else:
        if todo==1:
            try:
                room_no=int(input("Enter the new room number: "))
                if room_no in list(customer_codes.room_type["room_no"]):
                    raise ValueError
            except ValueError:
                print("Room Number",room_no,"Already Present in the Record.\nDuplicate Room numbers not allowed.")
                print("Delete the existing room first then Add a new one")
                return None
            else:
                last_index=len(customer_codes.room_type.index)#edning index of the booking DataFram
                customer_codes.room_type.loc[last_index,"room_no"]=room_no
                customer_codes.room_type.loc[last_index,"min_guest"]=int(input("Enter the minimum number of guest: "))
                customer_codes.room_type.loc[last_index,"max_guest"]=int(input("Enter the maximum number of guest: "))
                customer_codes.room_type.loc[last_index,"cost_per_night"]=float(input("Enter the cost per night for the room: "))
                customer_codes.save_room()#calling function to update the csv
                print("New Room",room_no,"added to the Records")
        elif todo==2:#when the room is to be deleted
            try:
                room_no=int(input("Enter the room number to remove: "))
                if room_no not in list(customer_codes.room_type["room_no"]):
                    raise ValueError
            except ValueError:
                print("Room number",room_no,"not found in the Room Records")
                return None
            else:
                for i in customer_codes.room_type.index:
                    if customer_codes.room_type.loc[i,"room_no"]==room_no:
                        customer_codes.room_type.drop(index=i,inplace=True)#dropping the row with the entered room_no from the DataFrame
                        break
                
                customer_codes.save_room()#calling function to update the csv
                print("Room number",room_no,"removed from the Records")

"""
This funtion is used only to see the bookings and room_type DataFrame or records.
"""
                
def see_records():
    print("Following is the booking Record")
    print(customer_codes.bookings)
    print("------------------------")
    print("Following is the room Record")
    print(customer_codes.room_type)