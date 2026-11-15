'''class Car:
    color='Black'
    engine='V8'
    def __init__(self):
        print(self)
c1=Car()
print(c1.color)
print(c1.engine)
print(c1)
#self and object created are the same thing
#self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class'''

'''
Create a student class that takes name and makrs of 3 subjects as arguments in constructor. Then creat a method to print the average
'''

class Student():
    def __init__(self,name,m1,m2,m3):
        self.name=name
        self.m1=m1
        self.m2=m2
        self.m3=m3
    def avg(self):
        average=(self.m1+self.m2+self.m3)/3
        print("Hii",self.name,"Your score is:",average)
s1=Student('Krishu',10,10,10)
s1.name="Ajla"

class Account():
    def __init__(self,bal,acc):
        self.balance=bal
        self.account=acc
    def debit(self,amount):
        self.balance-=amount
    def credit(self,amount):
        self.balance+=amount

acc1=Account(10000,432)
acc1.debit(1000)
print(acc1.balance)
acc1.credit(5000)
print(acc1.balance)

class Circle():
    def __init__(self,r):
        self.radius=r
        self.circum()

    def circum(self):
        self.circumference=3.14*self.radius**2

c1=Circle(10)
print(c1,c1.radius,c1.circumference)
c1.radius=14
print(c1,c1.radius,c1.circumference)


