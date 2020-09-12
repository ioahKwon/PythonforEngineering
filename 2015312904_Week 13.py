'''
Date : 2019. 12. 01.
Subject : Recursion, Turtle
Student ID : 2015312904
Name : 권준우 (Kwon Joon Woo)

'''

# assignment_01

dan=int(input("Enter number: "))

def gugudan(n,t=1):
    if t<=10:
        print(n,"x",t,"=",n*t)
        gugudan(n,t+1)
gugudan(dan)

# assignment_02

N=int(input("Enter N: "))
R=int(input("Enter R: "))

def C(n,r):
    def P(k):
        a=1
        for i in range(1,k+1):
            a=a*i
        return a
    c=int(P(n)/(P(r)*P(n-r)))
    if r==0 or r==n:
        c=1
    return c

print(C(N,R))

# assignment_03

import turtle as a
a.shape("turtle")
a.fillcolor('yellow')
a.pencolor('red')
a.begin_fill()
for k in range(5):
    a.forward(280)
    a.left(144)
a.end_fill()

# assignment_04

import turtle as t
b=t.Turtle()
r=t.Turtle()
b.fillcolor('blue')
b.pencolor('white')
b.forward(100)
b.begin_fill()
for a in range(5):
    b.forward(80)
    b.right(144)
b.end_fill()
b.goto(0,-100)
b.begin_fill()
for k in range(2):
    b.forward(280)
    b.right(90)
    b.forward(200)
    b.right(90)
b.end_fill()

r.fillcolor('red')
r.pencolor('white')
r.goto(280,100)
r.begin_fill()
for p in range(2):
    r.forward(280)
    r.right(90)
    r.forward(200)
    r.right(90)
r.end_fill()
r.left(90)
r.backward(300)
r.right(90)
r.forward(100)
r.begin_fill()
for w in range(5):
    r.forward(80)
    r.right(144)
r.end_fill()

b.hideturtle()
r.hideturtle()


