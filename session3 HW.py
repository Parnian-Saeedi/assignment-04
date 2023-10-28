import math

op =input("enter op(+,-,*,/,cos,sin,tan,cot,factorial,sqrt): ")
if op =="+":
    a=int(input("enter the first number:"))
    b=int(input("enter the second number:"))
    r=a+b
if op=="-":
    a=int(input("enter the first number:"))
    b=int(input("enter the second number:"))
    r=a-b
if op=="*":
    a=int(input("enter the first number:"))
    b=int(input("enter the second number:"))
    r=a*b
if op=="/":
    a=int(input("enter the first number:"))
    b=int(input("enter the second number:"))
    if b==0:
        r="error"
    else:
        r=a/b
if op=="sin":
    a=int(input("enter sin:"))
    r=(math.sin(math.radians(a)))
if op=="cos":
    a=int(input("enter cos:"))
    r=(math.cos(math.radians(a)))
if op=="tan":
    a=int(input("enter tan:"))
    r=(math.tan(math.radians(a)))
if op=="cot":
    a=int(input("enter cot:"))
    r=1/(math.tan(math.radians(a)))
if op=="factorial":
    a=int(input("enter the number:"))
    r=(math.factorial(a))
if op=="sqrt":
    a=int(input("enter the number:"))
    if a<0:
        print("run again, error")
    else:
        r=(math.sqrt(a))

print(r)



