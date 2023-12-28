#take something return somenthing
def add(a,b):
    sum=a+b
    return sum
"""a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
s=add(a,b)
print("Sum of two number:",s)"""
#Area of circle 
def Area(r):
    area=3.14*r**2
    return area
a=Area(7)
print("Area of circle is:",a)
#Average of three numbers
def Avg(a,b,c):
    Average=(a+b+c)/3
    return Average
Average=Avg(1,2,3)
print("Average of three number is:",Average)
#Volume of cuboid
def Volume(l,b,h):
    volume=l*b*h
    return volume
V=Volume(1,2,3)
print("Volume of cuboid is:",V)
#Check even or odd
def evenodd(x):
    if(x%2==0):
        print("Even")
    else:
        print("odd")
evenodd(4)
#Greater among three numbers
def Greater(x,y,z):
    if(x>y & x>z):
        print("Greater number is x:",x)
    elif(y>x & y>z):
        print("Greatest number is y:",y)
    else:
        print("Greatest number is z:",z)
Greater(4,8,1)
#Factorial of a number
def factorial(x):
    fact=1
    for i in range(1,x+1):
        fact=fact*i
    print("Factorial of number is",fact)
factorial(5)
#print("Factorial of number is given :",f)


    
