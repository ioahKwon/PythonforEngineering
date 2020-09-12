'''
Date : 2019. 11. 10.
Subject : Functions (2)
Student ID : 2015312904
Name : 권준우 (Kwon Joon Woo)

'''

# assignment_01

def sub(num1,num2=0):
    if num2 == 0:
        return num1-2
    else:
        return num1-num2
    


num = int(input("Input a number:"))
print(sub(num))
print(sub(num,3))
print(sub(num,5))


# assignment_02

def f(component):
    return component+2

list1 = [1,2,3,4,5]
list2 = [f(i) for i in list1]
list3 = [i+3 for i in list1]
list4 = [i+4 for i in list(range(1,6))]

print("list1:",list1)
print("list2:",list2)
print("list3:",list3)
print("list4:",list4)


# assignment_03

func=lambda num1, num2 : num1 * num2

num=int(input("Input a number: "))

for i in range(1,10):
    print(num,"*",i,"=",func(num,i))


# assignment_04

def sumCha(list):
    sum = 0
    for i in list:
        sum = sum + ord(i)
    return sum

list1 = ['apple','dearandbeer','banana','face','class',
         'freedom','treasure','Android']

list1.sort(key = sumCha)

for i in list1:
    print(i,":",sumCha(i))
print(list1)


# assignment_05
    
percent_sale = lambda price,percent : price * (100-percent)/100
discount_sale = lambda price,discount : price - discount
best_option = lambda price1, price2 : min(price1, price2)

price = int(input("How much is it? "))
percent = int(input("What percent discount is it? "))
discount = int(input("How much is the discount? "))

pri_per = percent_sale(price,percent)
pri_dis = discount_sale(price,discount)

print("percentage: "+str(pri_per)+","+" discount :"+ str(pri_dis))

if best_option(pri_per,pri_dis) == pri_per:
    print("best option is percentage sale")
else:
    print("best option is discount")


