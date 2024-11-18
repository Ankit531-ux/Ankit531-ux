
def add (x,y):
     return x+y
def subtract (x,y):
    return x-y
def multiply (x,y):
    return x*y
def divide (x,y):
    return x/y
def square (x,y):
    return x*y
def cube (x,y):
    return x*num1*y
def power4(x,y):
    return x*num1*num1*y
def power5 (x,y):
    return x*num1*num1*num1*y
print("select operation")
print("2.subtract")
print("3.multiply")
print("4.divide")
print("5.square")
print("6.cube")
print("7.power4")
print("8.power5")
choice = input("enter choice(1/2/3/4/5/6/7/8);")
num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))
if choice  == '1':
    print(num1,'+',num2,"=",
    add(num1,num2))
elif choice  == '2':
    print(num1,'-',num2,"=",
    subtract(num1,num2)) 
elif choice  == '3':
    print(num1,'*',num2,"=",
    multiply(num1,num2))
elif choice  == '4':
    print(num1,'/',num2,"=",
    divide(num1,num2))
elif choice  == '5':
    print(num1,'*',num2,"=",
    square(num1,num2))
elif choice  == '6':
    print(num1,'**',num2,"=",
    cube(num1,num2))
elif choice  == '7':
    print(num1,'****',num2,"=",
    power4(num1,num2))
elif choice  == '8':
    print(num1,'*****',num2,"=",
    power5(num1,num2))      
else:
     print("invalid input")