'''
Date : 2019. 10. 20.
Subject : List and Tuple, for
Student ID : 2015312904
Name : 권준우 (Kwon Joon Woo)

'''

# exercise_01

num=int(input("Input number: "))
for i in range(2,num):
    if num%i==0:
        print("no")
        break
    else:
        print("yes")
        break

# exercise_02

list1 = [[1,2], [3,4,5], [5,6], [7,8], [1,2], [345,44], [58,64,102], [70,898],
         [11,200], [30,47],[105,26,34,80],[97,78],[100,200]]

sum_val = 0
for i in range(len(list1)):
    for e in list1[i]:
        sum_val += e
print(sum_val)


# exercise_03

Num_List = []
i = 0

while 1:
    Num = int(input("Input a number : "))
    if Num != 0:
        Num_List.append(Num)
    else:
        break

print("Your inputs are")
while i < len(Num_List):
    print(Num_List[i])
    i +=1
print("The largest:", max(Num_List))
print("The smallest:", min(Num_List))
Avg = sum(Num_List)/len(Num_List)
print("Average:" + " %.2d"% Avg)


# exercise_04

num = int(input("Enter a number: "))
fact = num

for i in range (1,num):
    fact = fact * i
    i += 1

print(num, " factorial is ", fact)

# exercise_05

num = int(input("Type the number: "))
List = []
sum = 0

for i in  range (1,num):
    if num%i == 0:
        List.append(i)
    i +=1

for i in List:
    sum = sum + i

if sum != num:
    print(num, "is not the perfect number")
else:
    print(num, "is the perfect number")


