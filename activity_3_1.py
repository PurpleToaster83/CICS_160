while True:
    try:
        name_1 = input('input name: ')
        if name_1:
            break
        else:
            print('Please type your name')
            continue
    except:
        continue


while True:
    try:
        age_1 = int(input('input age (as integer): '))
    except:
        print('Please enter the age as an integer')
        continue
    break

while True:
    try:
        name_2 = input('input name: ')
        if name_2:
            break
        else:
            print('Please type your name')
            continue
    except:
        continue


while True:
    try:
        age_2 = int(input('input age (as integer): '))
    except:
        print('Please enter the age as an integer')
        continue
    break

if age_1 > age_2:
    print(f"{name_1} is {age_1 - age_2} years older than {name_2}")
else:
    print(f"{name_2} is {age_2 - age_1} years older than {name_1}")

