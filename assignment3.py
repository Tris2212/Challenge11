import re

email = input('Enter an email address: ')
match = re.search(r"^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$", email, re.IGNORECASE)
if match:
    print("You have a valid email address: " + match.group())
else:
    print("Your email address is not valid.")