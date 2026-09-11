total_sum, count, active = 0, 0, True
while active:
    val = int(input("Enter a number (0 to stop): "))
    if val == 0:
        active = False
    elif val > 0:
        total_sum = total_sum + val
        count += 1

if count > 0:
    average = total_sum / count
    print(f"The average of your numbers is: {average}")
else:
    print("No positive numbers were entered.")