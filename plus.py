print("\t\t\t\t\t\tcoded by @081user\n")

import time #importing time

timestamp = time.strftime('%H:%M:%S')
t = timestamp #import full time
timestamp = time.strftime('%H')
h = int(timestamp) #import hour
timestamp = time.strftime('%M')
m = int(timestamp) #import minutes
timestamp = time.strftime('%S')
s = int(timestamp) #import seconds

show = "Current Time"
print(show.center(56),'\n',t.center(53),'\n')

# defining a fuction for enter name and greeting user
def greet(name):
    if len(name) < 3 :
        print("Name should be greater than 3 words.")
        while len(name) < 3 :
            name = input("Your Name : ")
    if len(name) > 16 :
        print('Name should be smaller than 16 words.')
        while len(name) > 16:
            name = input("Your Name : ")  
    print("Welcome,",name.title())

    if h>=6 and h<=11:
        if m>=00 or m<59:
            if s>=00 or s<59:
                print("Good Morning,",name)
    elif h>=12 and h<=16:
        if m>=00 or m<59:
            if s>=00 or s<59:
                print("Good Afternoon,",name)
    elif h>=17 and h<=21:
        if m>=00 or m<59:
            if s>=00 or s<59:
                print("Good Evening,",name)
    elif h>=22 and h<=23:
        if m>=00 or m<59:
            if s>=00 or s<59:
                print("Good Night,",name)
    elif h>=00 and h<=5:
        if m>=00 or m<59:
            if s>=00 or s<59:
                print("Good Night,",name)
    else:
        print("Resfresh or Retry Again..")()

greet(input("Your Name : ").title())

print("\n","calculator".upper().center(56))

a = int(input("\nEnter first number : "))#First number  
b = int(input("Enter second number : "))#Secind Number
print("\n","Arithmetic Operations".center(56))
sum = a+b #Addition
print("\nSum of",a, "and", b, ":", sum) 
sub = a-b #Subtractiin
print("\nSubtraction of",a, "and", b, ":", sub) 
mltp = a*b #Multiplication0
print("\nMultiplication of",a, "and", b, ":", mltp)
div = a/b#Division
print("\nDivion of", a, "and",b,":",div) 
sqra=a**2 #square
print("\nSquare of", a, ":",sqra) 
sqrb=b**2
print("\nSquare of", b, ":",sqrb) 
mdl = a%b #module
print("\nRemainder of", a, "and",b,":",mdl) 
#print("\n\t\t...  :)"):