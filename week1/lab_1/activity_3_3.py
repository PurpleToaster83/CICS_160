import string

password = input("Enter a password:")

good = True
if not(len(password) >= 8) and (password[0] != password[1]) and (password[0] in string.ascii_uppercase) and (password[1] in string.ascii_uppercase):
    good = False

sum = 0
for i in range(len(password)):
        if not(password[i] in (string.ascii_letters + string.digits)):
            good = False
        if password[i] in string.digits:
            sum += password[i]

if not(sum % 2):
     good = False

if good:
     print("Password is good")
else:
     print("Password is bad")
