"""
This file contains all of the cutomer Menu related functions
"""
import numpy as np
import pandas as pd
from datetime import datetime
import random
"""
Here we first make a DataFrame of both of the csv records and then convert the date columns from string to a proper datetime datatype.
The datetime library helps us acheive the conversion of date from String to Datetime.
The reason we are converting the dates is so that we can later perform operations on the dates and check if the entered checkout date
is after the checkin day and to make sure the check in date is after today's date.

"""
bookings=pd.read_csv('room_bookings.csv')#Making a DataFrame out of bookings csv
room_type=pd.read_csv('room_types.csv')#Making a DataFrame out of room type csv
today=datetime.today()#to store todays date, later used so that the user does not enter a check In date that is before today's date
bookings['check_in_date'] = pd.to_datetime(bookings['check_in_date'],format='%Y-%m-%d')#to convert the dates taken from csv as string to datetime to perform calculations on the date such as finding the greater date
bookings['check_out_date'] = pd.to_datetime(bookings['check_out_date'],format='%Y-%m-%d')#same reason as line just above

"""
As we want every booking to have some unique column through which every booking can be identified:
we are using random number generator so that it generates a random number that that is not already 
present in the booking_id of the room_bookings.csv records.
"""
def random_generator():#to generate a unique random booking ID for each booking
    while True:
        val=random.randint(100,1000000000)
        if val not in list(bookings["booking_id"]):
            return val

"""
Everytime the roomtype/Bookings DataFrames are updated these function is called
so that the updation takes place in the csv files too.
Notice that in the DataFrame there our indexed rows,
as we did not want the index of rows in the csv file, we have used index=False
"""
def save_room():#to save the updated room type DataFrame to csv
    room_type.to_csv("room_types.csv",index=False)

def save_booking():#to save the updated Bookings DataFrame to csv
    bookings.to_csv("room_bookings.csv",index=False)

"""
This function updates the bookings DataFrame whenever there is a booking added
"""
def book_room(room_no,n_guest,checkindate,checkoutdate,n_days,cost_per_night,name):#updates the Bookings DataFrame
    last_index=len(bookings.index)
    bookings.loc[last_index,"room_no"]=int(room_no)
    bookings.loc[last_index,"check_in_date"]=checkindate
    bookings.loc[last_index,"check_out_date"]=checkoutdate
    bookings.loc[last_index,"cost"]=(n_days+1)*cost_per_night
    bookings.loc[last_index,"booking_id"]=int(random_generator())
    bookings.loc[last_index,"name"]=name
    save_booking()

"""
After a room is found, we need to confirm if the user is willing to make the booking
That is why we ask for the confirmation, Else the booking is not done
"""
def confirm_booking(room_no,n_guest,checkindate,checkoutdate,n_days,cost_per_night):#To confirm the room with the User before finally Booking
    print("We have found a room",room_no,"for you")
    choice=input("Do you want to go ahead and confirm the booking? (y/n): ")
    if choice=='y':
        name=input("Enter your Name: ")
        book_room(room_no,n_guest,checkindate,checkoutdate,n_days,cost_per_night,name)
        return True
    elif choice=='n':
        print("Redirecting back to Customer Menu....")
        return False
    else:
        print("Invalid Input Redirecting back to Customer Menu....")
        return False

"""
This is a little critical part, We need to find a room for the entered no. of guest(n_guest), checkindate(lets call it IN_Date, checkoutdate(lets call it OUT_Date))
First we check the room_type DataFrame for the room that can accomodate the entered n_guest, and store the room_no
Then we check if the room_no is present in the bookings DataFrame. If not that means there is no booking for that room
and dirrectly go ahead and book the room.
If a booking is already present for that room with dates= lets say..bookedIN, bookedOUT, then we check if the Stay date overlap or not: The logic is:
if IN_Date > bookOUT or OUT_Date < bookedIN, this shall be TRUE for all of the booking for that room_no, 
ONLY THEN we book the room, esle we shift to the next room_no for the n_guest and repeat the process untill we find a suitable room_no.
"""
def find_room(n_guest,checkindate,checkoutdate,n_days):#To search for an available room that is not already occupiad for any date from checkin to checkout for anyother record
    print("Searching Available Space.....")
    confirm=False#Flag -to indicate that room is not present by default
    for i in room_type.index:
        if room_type['min_guest'][i]<=n_guest<=room_type["max_guest"][i]:#to look only for those rooms from the room_type DataFrame that can have the entered no. of guests
            room_no=room_type['room_no'][i]
            cost_per_night=room_type['cost_per_night'][i]
            if room_no not in list(bookings['room_no']):
                confirm=True#if the found room no has no record for any booking then the room can directly be booked without checking the dates
                break
            else:#if there is a booking already present for that room
                n=0#counts the number of bookings that do not coincide with the entered users checkin-out date
                count=0#counts the total number of bookings for the room room_no
                for j in bookings.index:
                    if bookings["room_no"][j]==room_no:
                        count+=1#every booking found that has the room as room_no
                        booked_in_date=bookings.loc[j,"check_in_date"]
                        booked_out_date=bookings.loc[j,"check_out_date"]
                        if checkindate>booked_out_date or checkoutdate<booked_in_date :#logic that finds if the date coincide or not
                            n+=1
                            confirm=True
                    if n!=count:#if any dates coincides(with user checkin-out date) then the total no. of records of the same room_no variable shall be the same a n(room_no bookings with no coincident dates)
                        confirm=False
                        break                                             
    if confirm==True and confirm_booking(room_no,n_guest,checkindate,checkoutdate,n_days,cost_per_night):
        print("Room Booked")
        print("We are happy to have you as our esteemed Guest")
        print("Have a great Stay")
        return True
                
    elif confirm==False:              
        print("Couldn't find a room, Please Try with some other Date")
        return False        
                    

'''
Once the user selects to book a room, we then check if the entered details such as no. of guest (n_guest), check in dat (IN_Date), check out date (OUT_Date)
are logically correct. 
-> n_guest shall not be negative.It shall be greater than zero 
-> In_Date shall always be greater Today's date (today variable set at the top ,line 17.) 
-> In_Date shall always be less than the OUT_Date.
Hence we find the difference of Out_Date-IN_Date=n_days (no. of days the user stays) 
Hence we check if n_days>0, and move forward only if its True. Later n_day is used to calculate the cost of the room too.
'''

def valid_input_check():# To check if the user enters correct values to add a booking
    attempt=5#Five attempts given to book else he'll have to retry
    check=False
    while attempt>0:
        print()
        n=input("Enter the Total number of Guests joining (1-15): ")
        try:
            if n.isdigit()==False:
                raise ValueError
        except ValueError:
            attempt-=1 
            print("Enter a Valid Value for No. of Guest")
            print("You have",attempt,'attempt(s) left')
            
        else:
            n=int(n)
            if n>0 and n<16:#Checks if the number of guests is greater than 0(No negative no. of guests)
                try:
                    date1=input("Enter the CheckIn Date in YYYY-MM-DD format: ")
                    d1=datetime.strptime(date1, "%Y-%m-%d")#converts the entered string(date1) to date time
                    date2=input("Enter the CheckOut Date in YYYY-MM-DD format: ")
                    d2=datetime.strptime(date2, "%Y-%m-%d")#converts the entered string(date1) to date time
                except Exception:
                    print("Date Must Be only in YYYY-MM-DD format")
                    attempt-=1
                    print("You have",attempt,'attempt(s) left')
                    continue
                n_days=(d2.date()-d1.date()).days#finding difference between the entered dates
                if d1.date()>=today.date() and n_days>=0:#checks if the check In date is after check Out (Logically wrong) and if the checkin date is not before today's date
                    check=True
                    break
                else:
                    attempt-=1
                    print("Incorrect Input Type:")
                    print("You have",attempt,'attempt(s) left')
            else:
                attempt-=1
                print("Incorrect Input Type:")
                print("You have",attempt,'attempt(s) left')
             
    if check:
        room_found=find_room(n,d1,d2,n_days)


"""
This Displays the Customer Menu, takes the input from the user, checks if the input is either 1 or 2 or 3 
and returns the chosen menu option.
"""    
def cust_menu():
    print()
    print("How may we be of your Service today?")
    print("1. Book a room at the TAJ MAHAL Hotel")
    print("2. See your Booking Information")
    print("3. Exit")
    try:
        menu_choice=int(input("Choose an option to move forward with: "))
        if menu_choice not in (1,2,3):
            raise ValueError
    except ValueError:
        print("Incorrect Input..Enter number only from the given options")
        return None
    
    return menu_choice


"""
This is the function to Search any booking record.
It has 2 parts, the first part 
1. (if code=="cust") is when function is called from customer portal for the customers so that is the customer is searching for a booking, he/she can
only search through booking_id and nothing else due to confidentially of information. Only one rresult is printed
2. (elif code=="staff@look") is when this function is called from the staff portal, the staff can check the 
booking record based on any column (room_no,booking_id,check_in_date,check_out_date,cost,name)
provided that the exact column name is used. First the staff is prompt to enter the field name (column name) to search according to
then staff is asked to enter the exact value in that column. Example search form field: <room_no> and value in field as <103>
And the function prints the booking record for all bookings that have room_no as 103. Multiple results can be printed based on how many rows have the same 
value in that field entered.
Why do a staff search be in this function? --so that there is no need to creat one more function.
"""
def search(code="cust"):
    print()
    print("Searching Menu....")
    print("")
    if code=="cust":
        print("Due to confidentiality of information\nCustomers can search is only through their booking id")
        try:
            searchid=float(input("Enter your booking ID:"))
        except ValueError:
            print("Booking ID can only be a number")
        else:
            if searchid in list(bookings["booking_id"]):
                print("ID match found. Fetching Booking Details....")
                for i in bookings.index:
                    if bookings.loc[i,'booking_id']==searchid:#Displaying the Details of the Booking
                        print()
                        print("Name: ",bookings.loc[i,"name"])
                        print("Booking ID:",bookings.loc[i,"booking_id"])
                        print("Room No.",bookings.loc[i,"room_no"]//1)
                        print("Check In Date: ",bookings.loc[i,"check_in_date"])
                        print('Check Out Date: ',bookings.loc[i,"check_out_date"])
                        print("Total Cost: $",bookings.loc[i,"cost"])
                        break
            else:
                print("The Booking ID",searchid,"does not match our Records")
    elif code=="staff@look":
        field=input("Enter the Column Name you want to search: ")
        if field in ['room_no','booking_id','cost']:#float columns
            val=float(input("Enter the value in that Column: "))
        elif field in ['check_in_date','check_out_date']:#date columns
            try:
                val=input("Enter the value in that Column: ")
                val=datetime.strptime(val, "%Y-%m-%d")#converting the input date string to date
            except Exception:
                print("Enter a Valid Date in YYYY-MM-DD format Only")
                return None
        elif field in ['name']:#string column
            val=input("Enter the value in that Column: ")
        if field in bookings.columns:
            if val in list(bookings[field]):#checking if the val is in that column(field)
                for i in bookings.index:
                    if bookings.loc[i,field]==val:
                        print()
                        print("Name: ",bookings.loc[i,"name"])
                        print("Booking ID:",bookings.loc[i,"booking_id"])
                        print("Room No.",bookings.loc[i,"room_no"]//1)
                        print("Check In Date: ",bookings.loc[i,"check_in_date"])
                        print('Check Out Date: ',bookings.loc[i,"check_out_date"])
                        print("Total Cost: $",bookings.loc[i,"cost"])
            else:
                print("The Value",val,"is not present in the Column",field)
        else:
            print("Field entered is NOT present in the booking record")

                    
    


