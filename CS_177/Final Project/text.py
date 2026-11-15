import numpy as np#External library for arrays
import pandas as pd#External Library for DataFrames
import dataplay
import matplotlib.pyplot as plt#Library for charts
from datetime import datetime#library to save dates
from scipy import stats#library to perform linear Regreassion and other statistical calculation
bookings=pd.read_csv('room_bookings.csv')
room_type=pd.read_csv('room_types.csv')
today=datetime.today()
bookings['check_in_date'] = pd.to_datetime(bookings['check_in_date'],format='%Y-%m-%d')
bookings['check_out_date'] = pd.to_datetime(bookings['check_out_date'],format='%Y-%m-%d')

date1=input("Enter the CheckIn Date in YYYY-MM-DD format: ")
d1=datetime.strptime(date1, "%Y-%m-%d")#converts the entered string(date1) to date time
today=datetime.today()
print(d1.date)

print((today.date())<=(d1.date()))
print("Wiht . date=", (d1.date()-today.date()).days)
print((d1-today).days)