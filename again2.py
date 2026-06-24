#1
num=int(input("Enter a number:"))
if num%2==0:
    print("Even")
else:
    print("Odd")


#2
num=int(input("Enter a number:"))
if num%2==0 and num%3 ==0:
    print("Divisible by both")
else:
    print("Not divisible by both")


#3
num=int(input("Enter a number:"))
if num%5==0:
    print("Multiple of 5")
else:
    print("Not a multiple of 5")


#4
mark=int(input("Enter mark:"))
if mark>=90:
    print("Grade A")
elif mark>=80:
    print("Grade B")
elif mark>=70:
    print("Grade C")
elif mark>=60:
    print("Grade D")
else:
    print("Fail")


#5
num=int(input("Enter a number:"))
if num>=0:
    print("Positive")
elif num<=0:
    print("Negative")
else:
    print("Zero")


#6
ticket=input("Haveticket(yes/no):")
age=int(input("Enter age:"))
if ticket=="yes":
    if age>=18:
        print("Entry Allowed")
    else:
        print("Under the age")
else:
    print("Bring your ticket")



#7
username=input("Enter username:")
password=input("Enter password:")
if username=="darsh" and password=="1234":
    print("Login success")
else:
    print("Login failed")


#8
a=int(input("A:"))
b=int(input("B:"))
c=int(input("C:"))
print("Maximum=", max(a,b,c))
print("Minimum=", min(a,b,c))


#9


    
 
