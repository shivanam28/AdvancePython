# 10. Check whether a number is a perfect square (without using the square root function).


num = int(input("Enter a number to check: "))

if num < 0:
    print("Negative numbers do not have a real square root.")
elif num < 2:
    print(f"{num} is the square root of {num}.")
else:
    start, end, ans = 1, num // 2, 0

    while start <= end:
        mid = (start + end) // 2

        if mid * mid == num:
            ans = mid
            break
        elif mid * mid < num:
            ans = mid
            start = mid + 1
        else:
            end = mid - 1

    if ans * ans == num:
        print(f"{ans} is the exact square root of {num} (Perfect Square).")
    else:
        print(f"{num} is not a perfect square. Floor square root is {ans}.")