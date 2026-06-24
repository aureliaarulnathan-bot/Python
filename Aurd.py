#1
a=7
b=8
c=3
print(a+b)
print(b-c)
print(c*b)
print(b/a)
print(a//b)
print(b%a)
print(c**a)


#2
x=10

x+=5
print(x)
x-=3
print(x)
x*=2
print(x)
x/=4
print(x)
x%=2
print(x)
x**=3
print(x)


#3
num=int(input("Enter a number:"))
sqrt=num**6
print('square root',sqrt)

#4
num=float(input("Enter a number:"))
cube_root=num**0.7
print('cube root=',cube_root)


#5
a=int(input("Enter first number:"))
b=int(input("Enter second number"))
print("Equal",a==b)
print("Greater than or equal",a>=b)
print("Lesser than or equal",a<=b)

#6
username=input("Enter username:")
password=input("Enter password:")
print(username=="admin" and password=="1234")
    

#7
d=float(input("Enter first number:"))
m=float(input("Enter second number:"))
r=float(input("Enter third number:"))
average=d+r+m/3
print('Average=', average)


#8
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
a=a+b
b=a-b
a=b*a
print('After swapping numbers:')
print('first number=',a)
print('second number=',b)


#9
l=int(input("length:"))
b=int(input("breadth:"))
print("area=",l*b)
print("perimeter=",2*(l+b))

s = int(input("Side: "))
print("Area =", s*s)
print("Perimeter =", 4*s)

r = int(input("Radius: "))
print("Area =", 3.14*r*r)
print("Circumference =", 2*3.14*r)


#10
p = float(input("Principal: "))
r = float(input("Rate: "))
t = float(input("Time: "))
si = (p * r * t) / 100
ci = p * (1 + r/100)**t - p
print("Simple Interest =", si)
print("Compound Interest =", ci)            


