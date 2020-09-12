'''
Date : 2019. 09. 22.
Subject : String & Output
Student ID : 2015312904
Name : 권준우 (Kwon Joon Woo)

'''

# exercise_01

a=input("Enter a string: ")
b= a[-1]+a[1:len(a)-1]+a[0]
print("New string: ", b)


# exercise_02
n = 0
a=input("Enter a nonempty string: ")
while n<len(a)-1:
    n=int(input("Enter a index number: "))
    b=a.replace(a[n],"")
    print("New string: ",b)


# exercise_03

a=str(input("Enter a string: "))
b=a.upper()
c=b.count("A")+b.count("E")+b.count("I")+b.count("O")+b.count("U")
print("The number of vowel is: ", c)


# exercise_04
a=input("Enter three characters: ")
aup=a.upper()
for i in aup:
    new = ord(i)
    new += 3
    if new <= 64:
        new += 26
    elif new >= 91:
        new -= 26
    print(chr(new), end = "")


# exercise_05

a=str(input("Enter the name of a student: "))
b=float(input("Enter the score of Python Programming(PP): "))
c=float(input("Enter the score of Creative Writing(CW): "))
d=float(input("Enter the score of English Writing(EW): "))
e=round((b+c+d)/3,2)
print("\n")

print("{0:^10s}|{1:^8s}|{2:^8s}|{3:^8s}|{4:^10s}"
      .format("Student","PP","CW","EW","Average"))

print("{0:^10s}|{1:^8.2f}|{2:^8.2f}|{3:^8.2f}|{4:^8.2f}".format(a,b,c,d,e))




