'''
Date : 2019. 12. 08.
Subject : Class & Total of Python
Student ID : 2015312904
Name : 권준우 (Kwon Joon Woo)

'''

# assignment_01

class grade:
    def __init__(self):
        self.math = 0
        self.korean = 0
        self.english = 0

    def set_grade(self,math,korean,english):
        self.math= math
        self.korean = korean
        self.english = english

    def show_grade(self):
        print("\n*** Your Scores ***")
        print("Math : {}".format(self.math))
        print("Korean : {}".format(self.korean))
        print("English : {}".format(self.english))
        

print("Input Score Info")
student1 = grade()
math = int(input("Math: "))
korean = int(input("Korean: "))
english = int(input("English: "))
student1.set_grade(math,korean,english)
student1.show_grade()

# assignment_02

class rectangle:
    def __init__(self):
        self.width = 0
        self.height = 0

    def set_rect(self,width,height):
        self.width = width
        self.height = height

    def area_rect(self):
        self.area = self.width * self.height
        return self.area

    def print_rect(self):
        print("The rectangle's area is : {}".format(self.area_rect()))

rect1 = rectangle()
print("Input Rectangle's width and height")
width = int(input("Width: "))
height = int(input("Height: "))
rect1.set_rect(width,height)
rect1.print_rect()

# assignment_03

class patient:
    def __int__(self):
        self.name = 0
        self.age = 0
        self.waiting_time = 0

    def set_patient(self,name,age,waiting_time):
        self.name = name
        self.age = age
        self.waiting_time = waiting_time

    def show_patient(self):
        print("\n*** patient info ***")
        print("name : {}".format(self.name))
        print("age : {}".format(self.age))
        print("waitings : {}".format(self.waiting_time))
        print("{} Please Wait more".format(self.name))
        print("Waiting....")

patient1 = patient()
print("Input patient info")
name = str(input("Name: "))
age = int(input("Age: "))
waiting_time = int(input("waitings: "))
patient1.set_patient(name,age,waiting_time)
patient1.show_patient()

# assignment_04

class account:
    def __init__(self):
        self.name = 0
        self.balance = 0
        self.sendingmoney = 0

    def send(self):
        self.balance = self.balance - self.sendingmoney

    def printBalance(self):
        print('Now your balance is ', self.balance)

accnt1 = account()
accnt1.name = str(input("Please input your name: "))
accnt1.balance = int(input("Input initial balance: "))
accnt1.sendingmoney = int(input("Input how much you will send: "))
print('\nGlad to see you Mr.',accnt1.name)
print('Initial Balance : ',accnt1.balance)
print('Sending Money : ', accnt1.sendingmoney)
accnt1.send()
accnt1.printBalance()

# assignment_05

class Person():
    def __init__(self):
        self.name = 0
        self.height = 0
        self.weight = 0

    def printinfos(self):
        print('Name is {}'.format(self.name))
        print('Height is {}'.format(self.height))
        print('Weight is {}'.format(self.weight))

    def cal_BMI(self):
        height_modified=self.height/100

        return self.weight/(height_modified**2)

    def weightStatus(self):
        bmi = int(self.cal_BMI())
        if bmi < 19:
            print('Your BMI is {} You are Underweight '.format(bmi))
        elif bmi < 25:
            print('Your BMI is {} You are Healthy '.format(bmi))
        elif bmi < 30:
            print('Your BMI is {} You are Overweight '.format(bmi))
        else:
            print('Your BMI is {} You are Obese'.format(bmi))
            
person1 = Person()
print('BMI Checker, enter your Name, Height, Weight')
person1.name=str(input('Name :'))
person1.height=int(input('Height :'))
person1.weight=int(input('weight :'))

print()
person1.printinfos()
person1.weightStatus()

