# Take the hour of the day (0–23) and print “Good Morning”, “Good Afternoon”, “Good Evening”, or “Good Night”.

Time = int(input("Enter the time in 24-hour format (HHMM): "))

if Time >= 0 and Time < 1200:
    print("Good Morning!")
elif Time >= 1200 and Time < 1700:
    print("Good Afternoon!")
else:
    print("Good Evening!")