'''
Date : 2019. 11. 24.
Subject : Processing Data 2
Student ID : 2015312904
Name : 권준우 (Kwon Joon Woo)

'''

# assignment_01

a=(input("Enter the first set in CSV format: "))
b=(input("Enter the second set in CSV format: "))

a=set(a.split(","))
b=set(b.split(","))

print('First set:', a)
print('Second set:', b)
print('Intersection:', a.intersection(b))


# assignment_02

def countAllLetters(a):
    a = a.lower()
    counts ={}
    for num in a:
        if num.isalpha():
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1
    return counts


a = input('Enter the string: ')
print(countAllLetters(a))


# assignment_03

f_s=int(input("Enter the start index of the first interval: "))
f_e=int(input("Enter the end index of the first interval: "))
s_s=int(input("Enter the start index of the second interval: "))
s_e=int(input("Enter the end index of the second interval: "))
print("First Interval:",[f_s,f_e])
print("Second Interval:",[s_s,s_e])
set1=set(range(f_s,f_e+1))
set2=set(range(s_s,s_e+1))
i=set1.intersection(set2)
u=set1.union(set2)
y=list(i)
t=list(u)
answer=round(len(y)/len(t),5)
print("Intersection of Union(IoU):",answer)


# assignment_04

import string
import random

num_of_ids=int(input("Enter the number of IDs: "))

alphabet_digit_list = string.ascii_letters + string.digits

ids = list()

def genrateRandomList(maxLimit):
    rList =[]
    for i in range(0,11):
        rList.append(random.randint(0,maxLimit-1))
    return rList

while len(ids) < num_of_ids:
    id = ""
    randomList=genrateRandomList(len(alphabet_digit_list))
    for b in randomList:
        id += alphabet_digit_list[b]
    if id not in ids:
        ids.append(id)
for id in ids:
    print(id)


# assignment_05

import random

a = int(input("Enter the number of times of tossing a coin: "))
b = int(input("Enter the number of consecutive outcomes to find: "))

result = ""
for i in range(a):
    if random.randint(0,1) == 0:
        result += "H"
    else:
        result += "T"

print("Outcomes:", result)

heads = 0
tails = 0

while len(result) >= b:
    if result[:b] == "T"*b or result[:b] == "H"*b:
        if result[:b] == "T" * b:
            tails += 1
        else:
            heads += 1
        result = result[b:]
    else:
        result = result[1:]

print("The number of", b, "consecutive heads:", heads)
print("The number of", b, "consecutive tails:", tails)
