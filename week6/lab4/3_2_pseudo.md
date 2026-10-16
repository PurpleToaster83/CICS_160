# 3.2 Password Checker Pseudocode
function header stuff to return a string - takes in string type paramters for username and password

if !password.equalTo(username) || password.length() < 8
    return "Not valid password"

bool valid = defualt to false
create variable i at 1, less than lenght password, increment by 1
    if password.substring(i-1, i).equalTo("!"), valid = True

if !valid
    return "Not valid password"
return "Valid password"