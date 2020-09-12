'''
Date : 2019. 11. 17.
Subject : File I/O
Student ID : 2015312904
Name : 권준우 (Kwon Joon Woo)

'''

# assignment_01

f=open('input2.txt','w')
x = 30
while x>0 and x<=30:
    if x%2==0:
        f.write(str(x)+'\n')
    x -= 1
f.close()


# assignment_02

with open('input for assignment 2.txt','r') as f:
    integer=f.readlines()
    A=[]
    t=0
    for k in integer:
        n=k.rstrip('\n')
        A.append(n)
    for a in A:
        t=t+int(a)
    
    print("result is",t)


# assignment_03

with open("class.txt",'w') as f:
    f.write("Name\tEnglish\tMath\tScience\n")
    k=1
    T=1
    while T:
        name=str(input("\nInput the name of {}th student : ".format(k)))
        math=str(input("Input the math score of {}th student : ".format(k)))
        eng=str(input("Input the english score of {}th student : ".format(k)))
        sci=str(input("Input the science score of {}th student : ".format(k)))
        f.write("{0}\t{1}\t{2}\t{3}\n".format(name,eng,math,sci))
        a=str(input("\nKeep moving? (y/n): "))
        
        if a=='n':
            break
        elif a=='y':
            k += 1
            continue
        else:
            while T:
                b=str(input("\nKeep moving? (y/n): "))
                if b=='n':
                    T=0
                    break
                elif b == 'y':
                    k += 1
                    break
                else:
                    continue
            continue


# assignment_04

with open("Thunder.txt","r") as f:
    a=f.readlines()
    Line=[]
    P=[]
    for i in a:
        q=i.strip('\n').split(" ")
        Line.append(q)
    for b in Line:
        for c in b:
            d=c.replace(','," ")
            P.append(d)
    l=len(a)
    n=len(P)
    print('number of lines are {0} number of words are {1}'.format(l,n))


# assignment_05

list_tem = list(open("input for assignment 5.txt"))
list_tem.reverse()

for i in list_tem:
    print(" ".join(i.rstrip().split()[::-1]))


