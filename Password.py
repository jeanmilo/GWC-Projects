from hashlib import *

inventory = { }
print ("Type 'sign in' or 'sign up' to access your account.")
decision = input()
if decision == "sign in":
      username = input ("Username: ")
      userpass = input ("Password: ")
      hashpass = sha256 (userpass.encode( 'utf-8') ) .hexdigest ()
     # if username and password is found in inventory, open access.

  
elif decision == "sign up":
            input("Username: ") = newuser
            if newuser = inventory:
                  print("")
            input("Password: ") = newpass


username = input ("Username: ")
userpass = input ("Password: ")

hashpass = sha256 (userpass.encode( 'utf-8') ) .hexdigest () 


def hash(password):
      password = userpass

inventory ( username : userpass )


print(inventory)
