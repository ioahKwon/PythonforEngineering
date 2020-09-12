'''
Date : 2019. 10. 06.
Subject : If & While Output
Student ID : 2015312904
Name : 권준우 (Kwon Joon Woo)

'''

# exercise_01

a=input("Where is the capital of Switzerland? ")
if a=="Bern":
    print("Your answer is right")
else:
    print("Your answer is wrong")



# exercise_02
H = int(input("Input your height : "))
W = int(input("Input your weight : "))
S = H*H/10000
O = int(W/S)

if O>=35:
    print("Obese class III")
elif O<35 and O>=30:
    print("Obese class ll")
elif 0<30 and O>=25:
    print("Obese class l")
elif O<25 and O>=23:
    print("Overweight")
elif O >= 18.5:
    print("Normal weight")
else:
    print("Underweight")




# exercise_03
W= str(input("Enter a word: "))
B = W.upper()

if 'A' in B and 'E' in B and 'I' in B and 'O' in B and 'U' in B:
    print(B, "is vowel word.")
else:
    print(B, "is not vowel word.")
    



# exercise_04
wage = float(input("Enter hourly wage: "))
hours = float(input("Enter number of hours worked: "))
pay = 0

if hours < 40:
    pay = hours * wage
    print("Gross pay for week is $"+"%.2f."% pay)
else:
    pay = (40 * wage) + (1.5 *wage*(hours-40))
    print("Gross pay for week is $"+"%.2f."% pay)





# exercise_05
a = int(input("Input number: "))
cnt = 0
i= 2

while(i<=(a//2)):
    if(a % i ==0):
        cnt = cnt + 1
        break
    i = i+1

if (cnt ==0 and a != 1):
    print("yes")
else:
    print("no")

    
