# 7. Check if an amount can be evenly divided into 2000, 500, and 100 currency notes.

amount = int(input("Enter amount: "))

if amount % 100 == 0 and amount > 0:
    notes_2000 = amount // 2000
    amount = amount % 2000
    notes_500 = amount // 500
    amount = amount % 500
    notes_100 = amount // 100
    print(f"Yes! This amount is evenly distributed in 2000 X {notes_2000} Notes, 500 X {notes_500} notes, 100 X {notes_100} notes.")
else:
    print("Not evenly ditributed using 2000, 500, 100 currency notes.")

    