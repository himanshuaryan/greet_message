# greet_message
#According your system time, greeting message.
import time

timestamp = time.strftime('%H:%M:%S')
t = timestamp
timestamp = time.strftime('%H')
h = int(timestamp)
timestamp = time.strftime('%M')
m = int(timestamp)
timestamp = time.strftime('%S')
s = int(timestamp)

show = "Current Time"
print(show.center(56),'\n',t.center(53),'\n')
name = input("Your Full Name : ").title()

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
    print("Resfresh or Retry Again..")