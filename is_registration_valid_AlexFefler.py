username = input("Enter email: ")
if (username.find('@') != -1) and (username.find('.') != -1):
    password = input("Enter password: ")
    if (password.find('#') != -1) and len(password) > 7:
        print("Yay")
    else:
        print("Invalid password")
else:
    print("Invalid username")