

```
# This is formatted as code
```

**RAPTOR TO PYTHON**

n =int(input("Enter a number to find Factorial:"))
f=1
while n>0:
  f=f*n
  n=n-1
print("The Factorial is :",f)  


print("Program to find the GCD of two numbers:")
a=int(input("Enter 1st Number:"))
b=int(input("Enter 2nd Number:"))
if a<b:
  a,b=b,a
for i in range(b,0,-1):
  if a % i==0 and b % i==0 :
    break
print("The GCD is :",i)

print("Program to Print first n  Odd numbers:")
n =int(input("Enter the value of N:"))
for i in range(1,n*2,2):
  print(i," ")

print("Program to find the value of x^n")
x =int(input("Enter the value of X:"))
n=int(input("Enter the value of n:"))
a=1
while(n>0):
  a=a*x
  n=n-1
print("The value of X^n=",a)

import math
print("Program to check whether the givem number is Armstrong or not :")
a=int(input("Enter the Number:"))
b=a
c=0
s=0
while(a>0):
  a=a//10
  c=c+1
a=b
while(a>0):
  r=a%10
  s=s+math.pow(r,c)
  a=a//10
if(b==s):
  print("The Number is Armstrong")
else :
  print("The Number is not Armstrong")


print("Program to check whether the givem number is Palindrome or not :")
a=int(input("Enter the Number:"))
b=a
s=0
while(a>0):
  r=a%10
  s=s*10+r
  a=a//10
if(b==s):
  print("The Number is Palindrome")
else :
  print("The Number is not Palindrome")


n=int(input("Enter a number:"))
f=2
c=0
while f<=n/2 :
  if n % f ==0 :
    c=c+1
    break
  f=f+1
if(c==0):
  print("The Number is Prime.")
else:
     print("The Number is not Prime.")


print("Program to find the sum of Factors of a number:")
n=int(input("Enter a number:"))
i=1
s=0
while(i<=n):
  if(n%i==0):
    s=s+i
  i=i+1
print("Sum of factors:",s)


print("Program to print sum of n natural numbers:")
n=int(input("Enter the number:"))
s,i=0,0
while(i<=n):
  s=s+i
  i=i+1
print("The sum =",s)

print("Program to Print the reverse of a number:")
a=int(input("Enter the Number:"))
b=a
s=0
while(a>0):
  r=a%10
  s=s*10+r
  a=a//10
print("The Number after reversing=",s)


print("Program to print the nature of Quadratic equations:")
a=int(input("Enter the value of a: "))
b=int(input("Enter the value of b: "))
c=int(input("Enter the value of c  "))
d=(b*b)-4*(a*c)
if(d==0):
  print("The roots are real and equal")
else:
  if(d>0):
    print("The roots are real and unequal")
  else:
      print("The roots are imaginary and Unequal")
  

print("Program to check whether a number is a multiple of another:")
a=int(input("Enter the first number:"))
b=int(input("Enter the Second number:"))
if(a>b):
  if(a%b==0):
    print("It is a multiple")
  else:
    print("It is not a multiple")
else:
  if(b%a==0):
    print("It is multiple")
  else:
    print("It is not a multiple")

print("Program to check whether the accepted number is +ve -ve or 0")
n=int(input("Enter a number:"))
if(n>=0):
  if(n==0):
   print("The number is zero")
  else:
    print("The number is +ve")
else:
  print("The number is -ve")

print("Program to check whether the given number is 2 digit or not:")
n=int(input("Enter a number:"))
if(n>9 and n<100):
  print("It is a 2 digit number")
else:
  print("It is not a 2 digit number")

import math
print("Program to find the distance between 2 points:")
x1=int(input("Enter the value of x1:"))
y1=int(input("Enter the value of y1:"))
x2=int(input("Enter the value of x2:"))
y2=int(input("Enter the value of y2:"))
d=math.sqrt(math.pow(x2-x1,2)+math.pow(y2-y1,2))
print("The distance=",d)

print("Program to find the smallest of 3 numbers:")
a=int(input("Enter the first number :"))
b=int(input("Enter the second number:"))
c=int(input("Enter the third number:"))
s=a;
if(a>b):
  if(b<c):
    s=b
  else:
    s=c
elif(b>a):
  if(a<c):
    s=a
  else:
    s=c
print("The Smallest number is:",s)

print("Program to find the largest of 2 numbers:")
a=int(input("Enter 1st number:"))
b=int(input("Enter 2nd number:"))
if(a>b):
  print(a,"is greater")
else:
  print(b,"is greater")

print("Program to print quotient and remainder:")
n =int(input("Enter a number:"))
a=int(input("Enter a number to divide it with:"))
d=n//a
r=n%a
print(d,"is the quotient",r,"is the remainder")