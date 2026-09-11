def averageAbove(threshold):
    # Initialize list which stores the numbers
    list = []

  # Repeatedly ask for numbers until interrupted by <0 number
    while True:
    # Account for bad input
        try:
            number = int(input("Number?"))
            if int(number) < 0:
                break
        except ValueError: # if user did not enter number
            print("Enter a number!")
        # add number
        list.append(number)
    listAbove = [item for item in list if item > threshold]  # iterate to make numbers greater than
    return int(sum(listAbove)/len(listAbove))
