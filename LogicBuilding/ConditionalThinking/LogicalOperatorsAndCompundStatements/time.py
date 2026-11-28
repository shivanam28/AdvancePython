# 4. Take 24-hour time (hours and minutes) and print whether it is AM or PM.

time = int(input("Enter time in HHMM (24 hour format) - "))

if 0000 <= time <= 1100: 
    print("Its AM")
elif 1200 <= time <= 2300: 
    print("Its PM")
else: 
    print("Error!!!")

# hours = int(input("Enter hours: "))
# minutes = int(input("Enter minutes: "))

# if not (0 <= hours <= 23 and 0 <= minutes <= 59):
#     print("Invalid time") 
#     period = "AM" if hours < 12 else "PM"
#     print(period)