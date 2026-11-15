"""
This file contains all of the data related functions: Data Visualization and Data Analysis
"""


import numpy as np#External library for arrays
import pandas as pd#External Library for DataFrames
import matplotlib.pyplot as plt#Library for charts
from datetime import datetime#library to save dates
from scipy import stats#library to perform linear Regreassion and other statistical calculation
bookings=pd.read_csv('room_bookings.csv')
room_type=pd.read_csv('room_types.csv')
today=datetime.today()
bookings['check_in_date'] = pd.to_datetime(bookings['check_in_date'],format='%Y-%m-%d')
bookings['check_out_date'] = pd.to_datetime(bookings['check_out_date'],format='%Y-%m-%d')

"""
This function returns two lists in which one list is Contains the room numbers and the 
other list contains the Number of rooms Booked for those room number respectively. 
This function's returned values are being used by other chart functions.
"""

def list_of_room_and_bookings_size():#funtion that returns rooms and their respective number of bookings
    result=bookings.groupby(bookings['room_no'])['booking_id'].count().reset_index()
    label=list(result['room_no'])
    size=list(result['booking_id'])
    return label,size
    
"""
As the earlier function. This function also returns two lists, 
but one list contains the number of years 
and the other list contains the number of bookings for rescpective years
These functions used groupby to group and the calculate the sum of the records for that year.
"""
def list_of_year_and_booking_size():#function that returns the list of year and the respective number of bookings
    result=bookings.groupby(bookings['check_in_date'].dt.year)['room_no'].count().reset_index()
    label=list(result['check_in_date'])
    size=list(result['room_no'])
    return label,size

"""
The function below gives a pie charts for the no. of bookings done for a room. 
This can help the Hotel executives know what rooms help generate more bookings 
so that they can expand those hotels.
"""
def piechart():#creates a pei chart
    label,size=list_of_room_and_bookings_size()
    plt.pie(size,labels=label,autopct="%1.2f%%",pctdistance=0.8,wedgeprops={'edgecolor':"#F9F8F8",'linewidth':5})
    plt.title("No. of Bookings for each Rooms")
    plt.show()
    plt.close()

'''
This line chart shows the trend of revenue generated year on year. This information can help the 
hotel executive team know if their business is expanding or decreasing. And by what rate.
'''
def linechart():#creates a line chart for revenue earned by year
    result = bookings.groupby(bookings['check_in_date'].dt.year)['cost'].sum().reset_index()
    x,y=(list(result["check_in_date"]),list(result["cost"]))
    plt.plot(x,y,color="#F34E12",linestyle="--",marker="o")
    plt.title("Yearly Revenue Generated")
    plt.xlabel("Years")
    plt.ylabel("Revenue Generate ($)")
    plt.show()
    plt.close()

'''
This data analysis function calculates and returns the statistical terms (such as slope, intercept, R value, p-value and atandard Deviation)
between year and no. of bookings so that these can be used to check the relation between both variables (year and no. of bookings),
Estimate the booking for a future year and check its accuracy. It uses the linear regression command from the Scipy.stats Module.
'''
def data_analysis():#returns the statistical terms such as slope, intercept, R value etc, between year and respective no. of bookings
    l,s=list_of_year_and_booking_size()
    label=np.array(l)
    size=np.array(s)
    slope,intercept,r,p,std_err=stats.linregress(label,size)
    return slope,intercept,r,p,std_err

'''
This function plots a scatter plot for the years and respective no. of bookings along with a line chart 
of the line of best fit found uding the data_analysis() function.
'''
def scatterplot_bestfit():#Scatter cum line chart that shows the booking size for each year(scatter) and the line of best fit that linearly represents that data by using the data_analysis() function
    l,s=list_of_year_and_booking_size()
    label=np.array(l)
    slope,intercept,r,p,std_err=data_analysis()
    fx=slope*label+intercept
    plt.scatter(l,s,color="#EE802C",s=90)
    plt.plot(label,fx,color="#1125D9",linewidth=3)
    plt.title("Yearly Bookings")
    plt.xlabel("Years")
    plt.ylabel("No. of Bookings")
    plt.show()
    
'''
This function displays the Chart Menu option to choose what chart to display...
'''     
def charts_menu():#displaying the charts menu option to choose from
    print("Charts Menu...")
    print("1. Pie Chart showing the Category of rooms booked")
    print("2. Line Chart showing the trend in Revenue")
    print("3. Scatter plot between year and bookings in that year with line of best fit")
    print("4. Exit")
    #implementing try/except to handel error susceptible values
    try: 
        ch=int(input("Enter the option to go forward with: "))
        if ch not in (1,2,3,4):
            raise ValueError
    except ValueError:
        print("Enter a Valid Input!!!")
        return None
    else:
        if ch==1:
            piechart()
        elif ch==2:
            linechart()
        elif ch==3:
            scatterplot_bestfit()

'''
This function displays the Data Analysis Menu.
'''
def datascience_menu():#displaying datascience Menu
    print("Data Science Menu")
    print("1. Number of Bookings for each year ")
    print("2. Revenue Earned for each Year")
    print("3. Data Analysis on year and Bookings")
    print("4. Exit")
    try:
        ch=int(input("Enter the option to go forward with: "))
        if ch not in (1,2,3,4):
            raise ValueError
    except ValueError:
        print("Enter a Valid Input!!!")
        return None
    else:
        if ch==1:
            no_of_booking()
        elif ch==2:
            df=revenue_per_year()
            print(df)
            print("Total Revenue: ",sum(list(df["revenue"])))
        elif ch==3:
            data_analysis_study()

'''
If the staff member wants to see the option 1 from data science menu, this function is called.
This function calls the list_of_year_and_booking_size() function to get the list of Year and Bookings. Then these list are 
used to form a DataFrame.
'''
def no_of_booking():#Displays a DataFrame of year and the no. of bookings for that year
    x,y=list_of_year_and_booking_size()
    df=pd.DataFrame({"Year":x,"Bookings":y})
    print(df)
    print("The Total Number of Bookings: ",sum(y))


'''
If the staff member chooses to see the option no. 2 from data science menu, this function is called.
This function gets the list of Year and Revenue made every year. Then these list are 
used to form a DataFrame again so that the Column names can be changed.
'''
def revenue_per_year():#returns a DataFrame of Years and the revenue earned for that year
    result = bookings.groupby(bookings['check_in_date'].dt.year)['cost'].sum().reset_index()
    result=result.rename(columns={"check_in_date":'year','cost':'revenue'})
    return result


'''
This Function is a booking forcaster. It first finds the value of mean median and mode of the no. of bookings year on year
then it calls the data_analysis() function (or the linear Regression function) to get all of the statistical terms.
After which our forecast starts. The staff is asked to enter the year (greater than th year going on right now) and it calculates the estimated 
no. of bookings for that year. Along with this is also give the acuuracy based on the p-value and Corelation Coefficient.
This information can help the hotel know how many bookings to expect in a future year so that they can prepare and expand
operation accordingly.

'''
def data_analysis_study():#Displays the Statistical terms and relation between the year and no. of bookings and estimate the future bookings using that relationship
    l,s=list_of_year_and_booking_size()
    size=np.array(s)
    mean=np.mean(size)
    median=np.median(size)
    mode,count=stats.mode(size)
    print()
    slope,intercept,r,p,std_err=data_analysis()
    print("Mean of Bookings is:",mean)
    print("Median of Bookings is:",median)
    print("Mode is",mode,"and occurs",count,"times")
    print("Slope: ",slope)
    print("Intercept: ",intercept)
    print("Correlation coefficient(R): ",r)
    print("p-value: ",p)
    print("Standard Error: ",std_err)
    print("\nLets predict a booking for the future")
    predict=int(input("Enter the Year to find the Estimated booking: "))
    try:
        if predict <= datetime.today().year:
            raise ValueError
    except Exception:
        print("The year to predict shall only be a number greater than 2026")
    else:
        estimated_booking=slope*predict+intercept
        print("Booking for the year",predict,"could be:",estimated_booking//1)
    print("Following Information will help your evaluate the Accuracy of the prediction\n")
    #following conditional statements check the accuracy of our predicted value.
    if abs(r)>0.7:
        print("The Corelation Coefficient is a Strong Predictor")
    elif 0.7<=abs(r)<=0.3:
        print("The Corelation Coefficient is a Moderate Predictor")
    else:
        print("The Corelation Coefficient is a Weak Predictor")

    if p<=0.05:
        print("The P Value shows very strong evidence that the result is Statistically Significant")
    else:
        print("The P Value is High. Hence the result could easily happen by random luck.")

    