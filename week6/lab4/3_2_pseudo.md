# 3.2 Password Checker Pseudocode
function header stuff to return a string - takes in string type paramters for username and password<br><br>

if !password.equalTo(username) || password.length() < 8<br>
    return "Not valid password"<br><br>

bool valid = defualt to false<br>
create variable i at 1, less than lenght password, increment by 1<br>
    if password.substring(i-1, i).equalTo("!"), valid = True<br><br>

if !valid<br>
    return "Not valid password"<br>
return "Valid password"
