import random
import string
print("""
+------------------+
|PASSWORD GENERATOR|
+------------------+
""")
length = int(input("Enter the length of the password: "))
if length>7:
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''
    for i in range(length):
        password += random.choice(characters)
    print("Your Password is:", password)
else:
    print("Password length cannot be less than 8 characters.")