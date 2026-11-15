"""This is the Main file from where execution begins.
To run the program just run the main.py file
The project is build around 7 Total Files (4 python files, 2 csv files, 1 txt file):
->	main.py : The Program Execution starts from here.
->	customer_codes.py : This file contains all the functions related to customer portal such as customer menu, searching bookings, finding room, checking availability.
->	staff_codes.py : contain all the codes and functions related to staff (staff menu, changing booking/room)
->	dataplay.py : contains functions related to data visualization charts and Analysis.
->	room_booking.csv : csv file that contains the booking records
->	room_types.csv : csv file that contains the room type records (room no., min guest, max guest and cost per night)
->	staff_authentication.txt : text file that has the usernames and passwords of the staff member. It is only through this that the staff members can access the staff portal/menu.

Program Flow:-
-Main Menu:
    ->Login as Staff : (All operational and booking management options)
        After being Authentication through ID and Password
        ->Search Booking Record : searches the booking records (room_booking.csv) through desired column
        ->Change Booking : Edit/Delete the Booking of entered booking_id try example: 908368298 and see the record change
        ->Edit Room: Edits the room_types.csv (Room records)
        ->Data Analysis/Visualization : Shows charts and Data Analysis done on the booking records
        ->Exit: go back the previous menu
    ->Customer Portal
        ->Create Booking : add a booking in the room_bookings.csv
        ->Search your Booking : Searches the booking records through booking_id column only (customer's confidentiality)
        ->Exit: go back the previous menu
    ->Exit: Closes the program

"""

import staff_codes
import customer_codes
import dataplay

def welcome():#displays welcome message 
    print("\nWelcome to the hotel TAJ MAHAL")
    print("We are happy to have you as our guest")
    print("Always at your Service...")
    
def login():#Main Menu to choose staff or Customer
    print()
    print("1. Login as Staff")#if a staff member is logging IN
    print("2. Customer Portal")#for everyone
    print("3. Exit Program")  
    try:
        login=int(input("Please choose one option: "))
        if login not in (1,2,3):#If the entered option is not from 1,2 or 3.
            raise ValueError
    except ValueError:#Handeling the Error
        print("Incorrect Input..")
        print("Enter a number only from the given options")
        return None
    return login#Returns the Main Menu choosen option

def exit():#display exit message
    print("\nThank You for Visiting TAJ MAHAL...")
    print("Have a wonderful journey ahead...")




#Main code starts from here
welcome()#function called to display welcome message
while True:#infinite loop
    log=login()#calling main menu
    if log==1:#If user chooses staff
        staff_login_check=staff_codes.staff_check()#to authenticate staff members
        if staff_login_check:#Either True or False
            staff_choice=0#setting initial choice as 0 so that no NameErroe occurs
            while staff_choice!=7:#Loop that runs untill staff choice is exit
                staff_choice=staff_codes.staff_menu()

                if staff_choice==1:
                    customer_codes.search(code="staff@look")#If staff chooses searching from booking records
                elif staff_choice==2:
                    staff_codes.change_booking()#if staff chooses to edit a booking
                elif staff_choice==3:
                    staff_codes.change_room()#if choice is the edit room record
                elif staff_choice==4:
                    dataplay.datascience_menu()#if choice is data analysis
                elif staff_choice==5:
                    dataplay.charts_menu()#if choice is to see charts
                elif staff_choice==6:
                    staff_codes.see_records()#If staff chooses to see the records
    
    elif log==2:#for customer
        cust_choice=0
        while cust_choice!=3:
            cust_choice=customer_codes.cust_menu()#calling customer menu from suctomer_codes module
            if cust_choice==1:
                customer_codes.valid_input_check()#To add a booking
            elif cust_choice==2:
                customer_codes.search()#to search a booking at customer's end
            
        else:
            exit()

    elif(log==3):#get out of the infinite loop if choosen exit
        break
    

exit()
print()
print("Ending Program....GoodBye.....")
print()



