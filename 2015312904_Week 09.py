'''
Date : 2019. 11. 3.
Subject : Functions
Student ID : 2015312904
Name : 권준우 (Kwon Joon Woo)

'''

# assignment_01

def evenprint(num):
    list = []
    tem = 0
    while tem < num-2:
        tem +=2
        list.append(tem)
    return list

print(evenprint(100))



# assignment_02

def fac(number):
    i = 1
    total = 1
    while i < number+1:
       total = total * i
       i += 1
    return total

list = []
i = 0
number =5

while i < number:
    i += 1
    list.append(i)
    
print("%d *%d *%d *%d *%d = %d"
      %(list[0],list[1],list[2],list[3],list[4],fac(5)))



# assignment_03

def mulOrAdd(mode,a,b):
    total = 0
    new_mode = 0
    
    if mode == 1:
        total = a *b
    elif mode == 2:
        total = a +b
    else:
        while 1:
            
            new_mode = int(input("!!only add or mul please 1,2: "))
            if new_mode == 1:
                total = a*b
                break
            elif new_mode == 2:
                total = a+b
                break
            else:
                continue
            
    return total
        
        
    
mode = int(input("If you want to mul then 1, add 2: "))
first = int(input("first number: "))
second = int(input("second number: "))
print(mulOrAdd(mode,first,second))



# assignment_04 (문제에 맞춰서)

def voweldetector(strings):
    final = ""
    for i in strings:
        if i in "aeiou":
            final += i.upper()
        else:
            final += i
    return final
            
print(voweldetector("aeiou Why So SeRiouS"))

# assignment_04 (결과에 맞춰서)

def voweldetector(strings):
    final = ""
    for i in strings:
        final += i.swapcase()
    return final

print(voweldetector("aeiou Why So SeRiouS"))

# assignment_05

def better_salary(day):
    if day <= 1:
        return False
    else:
        option1 = day * 100
        option2 = 2
        for i in range(2, day+1):
            option2 = option2 + (option2 *2)

        if option1 > option2:
            return 1
        elif option1 == option2:
            return 0
        else:
            return 2

print(better_salary(6))
print(better_salary(10))
