# age = int(input("Enter your age : "))

# if (age < 0):
#     print("Enter your number is Negative.")
# elif (age >= 18):
#     print("You are Eligible to vote.")

# else:
#     print("You are not Eligible to vote. Go watch POGO")


import time

# start = time.strftime('%H')
start = 3
print(start)

if int(start) >= 21 or int(start) <= 6 :
    print(f"Good Night", start)
elif int(start) >= 7 or int(start) <= 12:
    print(f"Good Morning",start)
elif int(start) >= 13 or int(start) <= 16:
    print(f"Good Afternoon", start)
else:
    print("Good Evening")
